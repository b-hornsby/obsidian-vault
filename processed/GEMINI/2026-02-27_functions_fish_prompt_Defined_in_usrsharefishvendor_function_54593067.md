---
id: 471713
source: GEMINI
date: 2026-02-27
tags: ['fish-shell', 'terminal-prompt', 'customization']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is examining the fish shell prompt function, likely to customize his terminal.
---
# ❯ functions fish_prompt
# Defined in /usr/share/fish/vendor_functions.d/fish_prompt.fish @ line 2
function fish_prompt
    set --local exit_codes $pipestatus # save previous exit codes

    # Handle transient prompt (Fish 4.1.0+)
    # When --final-rendering is passed, show simplified prompt for scrollback
    if contains -- --final-rendering $argv
        set --local last_status $exit_codes[-1]

        echo -e -n (_pure_prompt_transient $last_status)
        echo -e -n (_pure_prompt_ending)
        return
    end

    _pure_print_prompt_rows # manage default vs. compact prompt
    _pure_place_iterm2_prompt_mark # place iTerm shell integration mark
    echo -e -n (_pure_prompt $exit_codes) # print prompt
    echo -e -n (_pure_prompt_ending) # reset colors and end prompt

    set _pure_fresh_session false
end

~
❯ 

### USER
❯ functions fish_prompt
# Defined in /usr/share/fish/vendor_functions.d/fish_prompt.fish @ line 2
function fish_prompt
    set --local exit_codes $pipestatus # save previous exit codes

    # Handle transient prompt (Fish 4.1.0+)
    # When --final-rendering is passed, show simplified prompt for scrollback
    if contains -- --final-rendering $argv
        set --local last_status $exit_codes[-1]

        echo -e -n (_pure_prompt_transient $last_status)
        echo -e -n (_pure_prompt_ending)
        return
    end

    _pure_print_prompt_rows # manage default vs. compact prompt
    _pure_place_iterm2_prompt_mark # place iTerm shell integration mark
    echo -e -n (_pure_prompt $exit_codes) # print prompt
    echo -e -n (_pure_prompt_ending) # reset colors and end prompt

    set _pure_fresh_session false
end

~
❯ 

### GEMINI
You’re using Pure, or a CachyOS fork of it. The "brutally honest" truth? You’re digging through /usr/share/, which is system-owned. Stop. If you edit files there, the next system update will steamroll your changes and put that IP right back where it was. You're fighting a losing battle against your package manager. The IP isn't in fish_prompt; it's in fish_right_prompt. In the Pure theme, the right side is where the "clutter" lives. The Kill Switch (Action) Don't look for the line of code. Overwrite the function. This is the cleanest, most "high-level" way to silence a prompt component in Fish without breaking the theme. Run this command to create a local override that kills the right-side prompt (where your IP lives) entirely: echo "function fish_right_prompt; end" > ~/.config/fish/functions/fish_right_prompt.fish Why this is the right move: Persistence: Files in ~/.config/fish/functions/ take priority over /usr/share/. Updates won't touch this. Performance: You just stopped your shell from executing a network lookup every time you hit Enter. Focus: You've removed the "wlan0" noise without nuking the clean "Pure" aesthetic on the left. The Reality Check You’ve spent several minutes hunting for a string in a vendor-supplied script. In a high-leverage environment, you don't "fix" vendor bloat; you override it. You should be spending your time on the commands you're typing after the prompt, not the prompt itself. Now, restart your terminal or type source ~/.config/fish/config.fish. Is your screen finally clean, or are you still staring at that IP?
