#!/usr/bin/env python3
"""
enrich_semantic_v3_retry.py — Retry enrichment for files that had write errors in v3.
Processes files individually (not batched) for reliability.
"""
import os, re, json, time, urllib.request, urllib.error

VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "enrichment-log-v3-retry.md")

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODEL = "openrouter/owl-alpha"

def _load_api_key():
    try:
        with open('/home/toastedmel0n/.hermes/auth.json') as f:
            auth = json.load(f)
        for cred in auth.get('credential_pool', {}).get('openrouter', []):
            if cred.get('auth_type') == 'api_key':
                return cred['access_token']
    except Exception:
        pass
    return os.environ.get('OPENROUTER_API_KEY', '')

OPENROUTER_API_KEY = _load_api_key()

CATEGORIES = ["ai-tools", "crypto-web3", "coding", "career", "homelab", "streaming", "general"]
SENTIMENTS = ["curious", "frustrated", "exploratory", "building", "stuck", "executing"]
RESOLUTIONS = ["resolved", "unresolved", "partial", "abandoned"]
PROJECTS = [
    "operation-immortal-agent", "homelab-stack", "private-ai-consulting",
    "second-brain-vault", "streaming-rig", "it-certification", "flappy-meme-bird",
]

USER_LABELS = {"CLAUDE": "### HUMAN", "GEMINI": "### USER", "GPT": "### USER", "GROK": "### USER"}
ALT_USER_LABELS = {"GPT": ["### HUMAN"], "GROK": ["### HUMAN"]}

def extract_frontmatter(content):
    if not content.startswith("---"):
        return {}, 0
    end = content.find("---", 3)
    if end == -1:
        return {}, 0
    fm_text = content[3:end].strip()
    fm = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            if not inner:
                fm[key] = []
            else:
                items = re.findall(r"'([^']*)'|\"([^\"]*)\"|([^,]+)", inner)
                fm[key] = [a or b or c.strip() for a, b, c in items if (a or b or c.strip())]
        else:
            fm[key] = val
    return fm, end + 3

def build_frontmatter(fm):
    lines = ["---"]
    for key in ["id", "source", "date"]:
        if key in fm:
            lines.append(f"{key}: {fm[key]}")
    for key in ["tags", "category", "sentiment", "resolution", "linked_projects", "linked_nodes", "summary"]:
        if key in fm:
            val = fm[key]
            if isinstance(val, list):
                if val:
                    items = ", ".join(f"'{v}'" for v in val)
                    lines.append(f"{key}: [{items}]")
                else:
                    lines.append(f"{key}: []")
            else:
                lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines) + "\n"

def extract_user_turns(content, provider):
    user_label = USER_LABELS.get(provider, "### USER")
    alt_labels = ALT_USER_LABELS.get(provider, [])
    body_start = content.find("---", 3)
    if body_start == -1:
        return ""
    body = content[body_start + 3:]
    turns = []
    lines = body.split("\n")
    in_user = False
    current_turn = []
    for line in lines:
        stripped = line.strip()
        is_user_header = stripped == user_label
        is_alt_header = stripped in alt_labels
        is_any_header = stripped.startswith("### ")
        if is_user_header or is_alt_header:
            if current_turn:
                turns.append("\n".join(current_turn).strip())
            in_user = True
            current_turn = []
        elif is_any_header and in_user:
            if current_turn:
                turns.append("\n".join(current_turn).strip())
            in_user = False
            current_turn = []
        elif in_user:
            current_turn.append(line)
    if current_turn and in_user:
        turns.append("\n".join(current_turn).strip())
    return "\n\n".join(turns)

def call_llm(prompt, max_tokens=1000):
    payload = json.dumps({
        "model": OPENROUTER_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
        "max_tokens": max_tokens,
    }).encode()
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"}
    for attempt in range(5):
        try:
            req = urllib.request.Request(f"{OPENROUTER_BASE_URL}/chat/completions", data=payload, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode())
                return data["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            body = e.read().decode() if e.fp else ""
            print(f"  HTTP {e.code}: {body[:100]}")
            if e.code == 429:
                wait = min(3 * (2 ** attempt) * 2, 60)
                print(f"  Rate limited, waiting {wait:.0f}s...")
                time.sleep(wait)
            elif e.code == 402:
                print(f"  Insufficient credits")
                return None
            elif e.code >= 500:
                wait = min(3 * (2 ** attempt), 60)
                time.sleep(wait)
            else:
                return None
        except Exception as e:
            print(f"  Error: {e}")
            if attempt < 4:
                time.sleep(3)
            else:
                return None
    return None

def enrich_file(filepath, provider):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"  Cannot read {filepath}: {e}")
        return False

    fm, body_start = extract_frontmatter(content)
    if not fm:
        print(f"  No frontmatter in {filepath}")
        return False

    user_turns = extract_user_turns(content, provider)
    if not user_turns:
        print(f"  No user turns in {filepath}")
        return False

    if len(user_turns) > 3000:
        user_turns = user_turns[:3000] + "\n... [truncated]"

    # Get title
    body = content[body_start:] if body_start > 0 else content
    title = ""
    for line in body.split("\n"):
        ls = line.strip()
        if ls.startswith("# ") and not ls.startswith("## "):
            title = ls[2:].strip()
            break

    prompt = f"""Analyze this conversation from Bryan's second-brain vault.

Return a JSON object with these exact fields:
{{
  "tags": ["3-5 specific topic tags"],
  "category": "one of: ai-tools, crypto-web3, coding, career, homelab, streaming, general",
  "sentiment": "one of: curious, frustrated, exploratory, building, stuck, executing",
  "resolution": "one of: resolved, unresolved, partial, abandoned",
  "linked_projects": ["project names actually discussed: operation-immortal-agent, homelab-stack, private-ai-consulting, second-brain-vault, streaming-rig, it-certification, flappy-meme-bird"],
  "summary": "1 sentence summarizing what Bryan was trying to accomplish"
}}

Title: {title}
User turns:
{user_turns}

Return ONLY the JSON object, no other text."""

    response = call_llm(prompt, max_tokens=500)
    if not response:
        return False

    # Parse JSON
    match = re.search(r'\{.*\}', response, re.DOTALL)
    if not match:
        print(f"  Could not parse response: {response[:100]}")
        return False
    try:
        result = json.loads(match.group())
    except json.JSONDecodeError:
        print(f"  JSON parse error: {match.group()[:100]}")
        return False

    # Update frontmatter
    if result.get("tags"):
        fm["tags"] = result["tags"]
    if result.get("category") and result["category"] in CATEGORIES:
        fm["category"] = result["category"]
    if result.get("sentiment") and result["sentiment"] in SENTIMENTS:
        fm["sentiment"] = result["sentiment"]
    if result.get("resolution") and result["resolution"] in RESOLUTIONS:
        fm["resolution"] = result["resolution"]
    if result.get("linked_projects"):
        fm["linked_projects"] = result["linked_projects"]
    if result.get("summary"):
        fm["summary"] = result["summary"]

    new_fm = build_frontmatter(fm)
    body = content[body_start:] if body_start > 0 else content
    if body.startswith("\n"):
        body = body[1:]

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_fm + body)
        return True
    except Exception as e:
        print(f"  Write error: {e}")
        return False

# Files that need retry (from the v3 run)
MISSING_FILES = [
    "processed/CLAUDE/2025-11-30_Flappy_bird_game_with_meme_collection_and_leaderboard_78218227.md",
    "processed/GEMINI/2025-05-04_Can_you_use_moonlight_to_stream_from_your_pc_to_your_phone_r_87250893.md",
    "processed/GEMINI/2025-05-16_Its_been_an_ongoing_thing_88406682.md",
    "processed/GEMINI/2025-06-24_right_now_its_building_cuda_object_and_it_let_me_go_through__62233021.md",
    "processed/GEMINI/2025-06-25_i_ran_step_2_and_it_says_Preparing_transaction_done_Executin_24082978.md",
    "processed/GEMINI/2025-06-25_to_ensure_its_the_right_one_i_deleted_the_old_one_from_my_de_19142373.md",
    "processed/GEMINI/2025-07-03_there_wasnt_any_errors_during_the_pip_install_whats_next_64393363.md",
    "processed/GEMINI/2025-07-05_base_bryan_DESKTOP_NG2I0P2text_generation_webui_cd_text_gene_75120291.md",
    "processed/GEMINI/2025-07-05_what_about_tinyen_75925441.md",
    "processed/GEMINI/2025-08-10_Why_would_the_Q4_version_have_a_memory_warning_92297758.md",
    "processed/GEMINI/2025-09-07_well_to_clarify_all_ive_done_is_make_those_foldersfiles_and__87587020.md",
    "processed/GEMINI/2025-09-15_Can_the_two_be_used_together_in_a_multi_agent_workflow_30282445.md",
    "processed/GEMINI/2025-10-31_What_are_the_latest_things_that_are_happening_in_AI_right_no_80456718.md",
    "processed/GEMINI/2025-12-09_so_in_one_prompt_how_can_i_implement_this_keep_is_concise_an_53439816.md",
    "processed/GEMINI/2026-01-01_I_want_to_know_about_vitamin_browser_specifically_80876684.md",
    "processed/GEMINI/2026-01-20_Yeah_that_part_worked_in_desktop_and_I_let_it_run_for_a_litt_26087974.md",
    "processed/GEMINI/2026-01-23_What_does_this_mean_for_nvidiavibe_coders_Is_this_a_good_thi_17117851.md",
    "processed/GEMINI/2026-02-01_Is_there_a_way_to_make_a_server_of_some_kind_to_sync_save_da_52274102.md",
    "processed/GEMINI/2026-02-01_bash_paru_S_appimagelauncher_usrbinparu_usrbinparu_cannot_ex_52507633.md",
    "processed/GEMINI/2026-02-02_how_to_blur_background_obs_camera_cachyos_94388671.md",
    "processed/GEMINI/2026-02-02_systemctl_list_units_typeservice_grep_E_tlplaptop_modepower__57072575.md",
    "processed/GEMINI/2026-02-07_its_currenttly_finishing_compiling_42062373.md",
    "processed/GEMINI/2026-02-19_What_type_of_oil_is_best_for_beards_Specifically_for_softnes_88536171.md",
    "processed/GEMINI/2026-02-24_It_doesnt_HAVE_to_be_bitcoin_im_just_saying_something_less_v_49908706.md",
    "processed/GEMINI/2026-02-26_planmd_is_updated_to_v22_Heres_what_changed_Kamino_Multiply__58495465.md",
    "processed/GEMINI/2026-03-06_i_just_want_to_know_how_to_get_rid_of_the_old_project_in_my__12190771.md",
    "processed/GEMINI/2026-03-10_this_is_what_i_have_up_to_my_usernamesecrets_for_obv_reasons_25081177.md",
    "processed/GEMINI/2026-03-15_if_i_go_the_torrent_route_do_i_keep_these_all_selected_80012813.md",
    "processed/GEMINI/2026-03-15_rootCachyOS_ls_boot6cd86a12288e4089802591bd1a9a39celinux_cac_69430171.md",
    "processed/GEMINI/2026-03-16_sudo_micro_etcdefaultgrub_sudo_password_for_toastedmel0n_1m__56859485.md",
    "processed/GEMINI/2026-03-16_sudo_sbctl_create_keys_sudo_sbctl_enroll_keys_m_sudo_password_for_t_68003030.md",
    "processed/GEMINI/2026-03-16_sudo_sbctl_sign_s_bootEFIBOOTsyslinuxefi_sudo_password_for_t_80284759.md",
    "processed/GEMINI/2026-03-19_So_the_current_model_Im_using_is_the_most_efficient_given_my_58289048.md",
    "processed/GEMINI/2026-03-23_Okay_so_to_sum_up_i_now_have_my_defendants_answer_which_afte_26045474.md",
    "processed/GEMINI/2026-03-23_The_lady_there_said_they_didnt_have_a_notary_there_and_appar_62451745.md",
    "processed/GEMINI/2026-04-05_To_be_more_specific_transunion_is_532_equinox_is_518_accordi_48678654.md",
    "processed/GEMINI/2026-04-06_so_i_did_steps_1_and_2_but_now_i_cant_hear_my_music_in_brave_23145426.md",
    "processed/GEMINI/2026-04-06_so_to_clairfy_give_me_a_checklist_of_what_to_check_to_ensure_50809578.md",
    "processed/GEMINI/2026-04-06_the_thing_is_though_tiktok_studio_asks_for_two_separate_sour_67749212.md",
    "processed/GEMINI/2026-04-07_And_docker_is_a_better_solution_here_than_a_vm_Why_do_people_13819428.md",
    "processed/GPT/2024-01-31_Warehouse_Experience_in_IT_45188402.md",
    "processed/GPT/2024-03-13_Arhaus_Job_Application_Follow_up_27989535.md",
    "processed/GPT/2025-01-10_Ohio_Salary_Take-home_Estimate_11878800.md",
    "processed/GPT/2025-04-19_Web3_Python_Projects_61854887.md",
    "processed/GPT/2025-05-23_Strain_Choice_Advice_87317373.md",
    "processed/GPT/2025-06-02_OXFUN_App_Features_25010821.md",
    "processed/GPT/2025-07-06_Mac_Studio_vs_GPU_Setup_54795572.md",
    "processed/GPT/2025-07-07_MCP_Servers_in_LLMs_66876385.md",
    "processed/GPT/2025-07-08_Vibe_Coding_for_Beginners_59989595.md",
    "processed/GPT/2025-07-25_Safe_mode_entry_methods_97513247.md",
    "processed/GPT/2025-08-09_LLM_deployment_skills_83845935.md",
    "processed/GPT/2025-08-21_Brutal_self_analysis_and_feedback_85485402.md",
    "processed/GPT/2025-08-31_Crypto_chat_name_ideas_53793918.md",
    "processed/GPT/2025-10-12_Death_counter_for_stream_16734482.md",
    "processed/GROK/2026-01-26_Open_Source_LLMs_Prompt_Injection_Resistance_59600766.md",
]

def main():
    print("=" * 60)
    print("Enrichment v3 Retry — Individual file processing")
    print("=" * 60)

    total = len(MISSING_FILES)
    success = 0
    failed = 0
    errors_list = []

    for i, rel_path in enumerate(MISSING_FILES):
        filepath = os.path.join(VAULT_PATH, rel_path)
        provider = rel_path.split("/")[1]  # e.g. "GEMINI"

        print(f"[{i+1}/{total}] {rel_path}...", end=" ", flush=True)

        if not os.path.exists(filepath):
            print("NOT FOUND")
            failed += 1
            errors_list.append(f"{rel_path}: file not found")
            continue

        result = enrich_file(filepath, provider)
        if result:
            print("OK")
            success += 1
        else:
            print("FAILED")
            failed += 1
            errors_list.append(f"{rel_path}: enrichment failed")

        time.sleep(1.5)  # Rate limit delay

    # Write log
    log_lines = [
        "# Enrichment Log v3 Retry — Individual File Processing",
        "",
        f"**Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Total files attempted:** {total}",
        f"**Successful:** {success}",
        f"**Failed:** {failed}",
        "",
    ]
    if errors_list:
        log_lines.append("## Errors")
        for e in errors_list:
            log_lines.append(f"- {e}")
    log_lines.append("")

    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines))

    print(f"\nDone! {success}/{total} enriched, {failed} failed")
    print(f"Log: {LOG_PATH}")

if __name__ == "__main__":
    main()
