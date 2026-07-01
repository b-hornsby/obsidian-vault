#!/usr/bin/env python3
import os, re, json
from pathlib import Path
from collections import defaultdict

VAULT = Path("/vault")

def run_corrected_audit():
    print("="*60)
    print("CORRECTED VAULT AUDIT")
    print("="*60)

    # Build file index: check both exact relative path and stem matches
    vault_files = {}
    vault_stems = {}
    for f in VAULT.rglob("*.md"):
        if '.obsidian' in str(f):
            continue
        rel = str(f.relative_to(VAULT))
        vault_files[rel] = f
        vault_stems[f.stem] = f

    print(f"\n1. FILE INDEX")
    print(f"   Total .md files in vault (excl .obsidian): {len(vault_files)}")

    # Scan all wikilinks
    all_links = defaultdict(list)
    link_targets = set()
    for fpath, f in vault_files.items():
        content = f.read_text(encoding="utf-8", errors="ignore")
        for match in re.findall(r'\[\[([^\]|#]+)', content):
            # Clean up the target
            target = match.strip().lstrip('/')
            all_links[target].append(fpath)
            link_targets.add(target)

    print(f"\n2. WIKILINK ANALYSIS")
    print(f"   Total unique link targets: {len(link_targets)}")
    print(f"   Total link instances: {sum(len(v) for v in all_links.values())}")

    # Check which targets exist
    broken = []
    valid = []
    for target in link_targets:
        # Try exact relative path
        if target in vault_files:
            valid.append(target)
            continue
        # Try with .md appended
        if target + '.md' in vault_files:
            valid.append(target)
            continue
        # Try stem match (for targets without path)
        if target in vault_stems:
            valid.append(target)
            continue
        # Try directory + .md (for folder links like nodes/topics/coding.md)
        parts = target.split('/')
        if len(parts) > 1:
            # Check if it's a directory that exists
            check_path = VAULT / target
            if check_path.exists():
                valid.append(target)
                continue
            check_md = VAULT / (target + '.md')
            if check_md.exists():
                valid.append(target)
                continue
        broken.append(target)

    print(f"   Valid targets: {len(valid)}")
    print(f"   Broken/orphan targets: {len(broken)}")
    if broken:
        # Filter out short/common false positives
        real_broken = [b for b in broken if len(b) > 3 and not b.startswith(('nodes/', 'processed/', 'goals/', 'insights/'))]
        print(f"   Suspicious broken (non-path targets): {len(real_broken)}")
        for b in real_broken[:20]:
            sources = all_links[b][:3]
            print(f"      '{b}' — appears in: {sources}")

    print("\n3. TOPIC HUB BACKLINK STRENGTH")
    for topic_file in sorted((VAULT / "nodes" / "topics").glob("*.md")):
        name = topic_file.stem
        # Count how many other files link to this topic
        backlink_count = 0
        for target, sources in all_links.items():
            # Does this target resolve to this topic?
            if target.endswith(f"/topics/{name}.md") or target == name or target.endswith(f"/{name}"):
                backlink_count += len(sources)
        print(f"   {name}: ~{backlink_count} backlinks")

    print("\n4. PROCESSED FILE INBOUND LINKS")
    processed_files = list((VAULT / "processed").rglob("*.md"))
    linked_count = 0
    for pf in processed_files:
        rel = str(pf.relative_to(VAULT))
        stem = pf.stem
        found = False
        for target in link_targets:
            if target == rel or target == rel.replace('.md', '') or target == stem:
                found = True
                break
        if found:
            linked_count += 1
    print(f"   Processed files with inbound links: {linked_count}/{len(processed_files)}")
    print(f"   Coverage: {linked_count/len(processed_files)*100:.1f}%")

    print("\n5. NODE DIRECTORY SIZES")
    for subdir in ["topics", "projects", "people"]:
        files = list((VAULT / "nodes" / subdir).glob("*.md"))
        total_size = sum(f.stat().st_size for f in files)
        print(f"   nodes/{subdir}/: {len(files)} files, {total_size//1024}KB total")

    print("\n6. PROCESSED FILE SIZE WARNINGS")
    huge = []
    for f in processed_files:
        size = f.stat().st_size
        if size > 500_000:
            huge.append((str(f.relative_to(VAULT)), size))
    if huge:
        for path, size in huge:
            print(f"   WARN: {path} = {size//1024}KB")
    else:
        print("   No oversized processed files")

    print("\n" + "="*60)
    print("AUDIT COMPLETE")
    print("="*60)

if __name__ == "__main__":
    run_corrected_audit()
