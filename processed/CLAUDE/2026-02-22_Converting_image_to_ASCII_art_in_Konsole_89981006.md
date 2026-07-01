---
id: 733353
source: CLAUDE
date: 2026-02-22
tags: ['ascii-art', 'konsole', 'cachyos', 'ascii-image-converter', 'fish-shell', 'terminal-customization']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan wanted to convert a Dark Souls Solaire image to colorful ASCII art and set it as his Konsole terminal display in CachyOS, troubleshooting installation and color vibrancy issues.
---
# Converting image to ASCII art in Konsole

### HUMAN
looking to change the ascii in my konsole in cachyos and im not sure how to do that? i have an image in mind but i havent turned it into ascii either

### ASSISTANT
Cool aesthetic! To change the ASCII art in your KDE Konsole on CachyOS, here's the process:

**First, convert your image to ASCII**

The easiest tool for this is `ascii-image-converter`:

```bash
yay -S ascii-image-converter
```

Then convert your image:

```bash
ascii-image-converter /path/to/image.png -C -W 60
```

`-C` keeps color, `-W` sets the width in characters. Play with the width to get it looking right.

**Then, where to put it**

That ASCII art likely runs on terminal startup via your shell's config file. Check which shell you're using:

```bash
echo $SHELL
```

Then add the command to the appropriate config file:

- **bash** → `~/.bashrc`
- **zsh** → `~/.zshrc`
- **fish** → `~/.config/fish/config.fish`

You'd add something like this at the top or bottom:

```bash
ascii-image-converter ~/pictures/myimage.png -C -W 60
```

Or if you want to save the output statically (faster startup):

```bash
ascii-image-converter ~/pictures/myimage.png -C -W 60 > ~/.config/my-ascii.txt
```

Then in your shell config:

```bash
cat ~/.config/my-ascii.txt
```

**Tip:** That green color you have looks like it might be set via `lolcat` or just the terminal color theme. If you want your ASCII to match, you can pipe through `lolcat`:

```bash
ascii-image-converter ~/pictures/myimage.png -W 60 | lolcat -p 1000 -S 200
```

What image are you thinking of using?

### HUMAN
❯ yay -S ascii-image-converter fish: Unknown command: yay ~ ❯

### ASSISTANT
Looks like you're using **fish** shell and don't have `yay` installed. On CachyOS you might have `paru` instead, or you can install it:

**Check what AUR helper you have:**
```fish
which paru
which yay
```

**If you have paru:**
```fish
paru -S ascii-image-converter
```

**If neither is installed, install yay:**
```fish
sudo pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

**Alternatively**, `ascii-image-converter` might be in the CachyOS repos directly:
```fish
sudo pacman -S ascii-image-converter
```

Try that pacman one first — CachyOS has a lot of extra packages in their repos so it may just work without needing an AUR helper at all.

### HUMAN
❯ sudo pacman -S ascii-image-converter [sudo] password for toastedmel0n:  Sorry, try again. [sudo] password for toastedmel0n:  error: target not found: ascii-image-converter ~ 9s ❯

### ASSISTANT
Not in the main repos. Let's check what AUR helper you have:

```fish
which paru; which yay
```

If neither exists, we can install `paru` (the recommended AUR helper on CachyOS):

```fish
sudo pacman -S paru
```

CachyOS actually includes paru in their repos so that should work directly. Then once you have it:

```fish
paru -S ascii-image-converter
```

### HUMAN
installed  via paru. now what?

### ASSISTANT
Now convert your image! First, what's the path to the image you want to use? You can find it by running:

```fish
ls ~/Pictures
```

Or if it's somewhere else, let me know where you saved it. Once we know the path we can run the converter and preview it before adding it to your shell config.

### HUMAN
its in downloads

### ASSISTANT
Run this to preview it:

```fish
ascii-image-converter ~/Downloads/yourfilename.png -C -W 60
```

Replace `yourfilename.png` with the actual filename. If you're not sure of the exact name:

```fish
ls ~/Downloads
```

### HUMAN
its this one .rw-r--r-- 203k toastedmel0n 10 Feb 17:43  png-clipart-dark-souls-solaire-of-astora-drawing-knight-bloodborne-dark-souls

### ASSISTANT
Run:

```fish
ascii-image-converter ~/Downloads/png-clipart-dark-souls-solaire-of-astora-drawing-knight-bloodborne-dark-souls -C -W 60
```

That'll preview it in the terminal. Try adjusting `-W` (width) up or down to get it looking how you want — something like `-W 80` or `-W 40`. Let me know how it looks!

### HUMAN
❯ ascii-image-converter ~/Downloads/png-clipart-dark-souls-solaire-of-astora-drawing-knight-bloodborne-dark-souls -C -W 60 Error: unable to open file: open /home/toastedmel0n/Downloads/png-clipart-dark-souls-solaire-of-astora-drawing-knight-bloodborne-dark-souls: no such file or directory ~ ❯

### ASSISTANT
The filename probably has an extension. Try tab completion to get the exact name:

```fish
ascii-image-converter ~/Downloads/png-clipart<TAB>
```

Press Tab after typing the first few characters and fish will autocomplete the full filename for you.

### HUMAN
okay that worked but its not in color? the command is: ❯ ascii-image-converter __~/Downloads/png-clipart-dark-souls-solaire-of-astora-drawing-knight-bloodborne-dark-souls-dark-souls-solaire-of-astora-thumbnail-3302336950.png__

### ASSISTANT
Add the `-C` flag for color:

```fish
ascii-image-converter ~/Downloads/png-clipart-dark-souls-solaire-of-astora-drawing-knight-bloodborne-dark-souls-dark-souls-solaire-of-astora-thumbnail-3302336950.png -C -W 60
```

### HUMAN
better but the color isnt as vibrant as id like

### ASSISTANT
Try adding the `-b` flag which uses braille characters and tends to look more detailed/vibrant, or you can pipe through `lolcat` for more intense color:

**More detailed rendering:**
```fish
ascii-image-converter ~/Downloads/png-clipart...thumbnail-3302336950.png -C -b -W 60
```

**Or pipe through lolcat for vivid color:**
```fish
ascii-image-converter ~/Downloads/png-clipart...thumbnail-3302336950.png -W 60 | lolcat
```

(install lolcat first if needed: `paru -S lolcat`)

You can also try `-c` (lowercase) instead of `-C` which uses a different color method — sometimes it's more vibrant depending on the image.

### HUMAN
lowercase c just gets rid of the color?

### ASSISTANT
Yeah, `-c` is for custom color input, not what we want. Stick with `-C`.

For more vibrant color, try the `-color-bg` flag which also colors the background:

```fish
ascii-image-converter ~/Downloads/png-clipart...thumbnail-3302336950.png -C --color-bg -W 60
```

Or if you want to try lolcat for that vivid green look like your current ASCII:

```fish
paru -S lolcat
ascii-image-converter ~/Downloads/png-clipart...thumbnail-3302336950.png -W 60 | lolcat -p 10000
```

The high `-p` value on lolcat keeps it from rainbow-ing too much and stays closer to one color.

### HUMAN
this is the image im trying to change it to but as you can see its not super vibrant? i just need the colors to stand out ever so slightly so its not as muted looking

### ASSISTANT
That looks pretty good actually! To get slightly more vibrant colors, try the `--color-bg` flag combined with `-C`:

```fish
ascii-image-converter ~/Downloads/png-clipart...thumbnail-3302336950.png -C --color-bg -W 60
```

If that's too much, another option is to just boost your terminal's color saturation in Konsole's profile settings — since the ASCII colors are pulled from the image, the terminal color profile has a big effect on how vivid they appear. Go to **Konsole → Settings → Edit Current Profile → Appearance** and try a higher contrast color scheme.

### HUMAN
okay ill try the konsole profile setting once we change the ascii image. so now that we have the ascii image converter and i have my image in ascii, now what?

### ASSISTANT
Now we save it and add it to your fish config so it shows on every terminal startup.

**1. Save the ASCII output to a file:**
```fish
ascii-image-converter ~/Downloads/png-clipart...thumbnail-3302336950.png -C -W 60 > ~/.config/fish/ascii-art.txt
```

**2. Add it to your fish config:**
```fish
nano ~/.config/fish/config.fish
```

Then add this line at the top or bottom:
```fish
cat ~/.config/fish/ascii-art.txt
```

Save with `Ctrl+X` → `Y` → `Enter`

**3. Test it:**
```fish
source ~/.config/fish/config.fish
```

It should display your Solaire ASCII art every time you open a new terminal!

### HUMAN
the one i need to save the output of is this ❯ ascii-image-converter __~/Downloads/png-clipart-dark-souls-solaire-of-astora-drawing-knight-bloodborne-dark-souls-dark-souls-solaire-of-astora-thumbnail-3302336950.png__ -C -W 60

### ASSISTANT
Run this to save it:

```fish
ascii-image-converter ~/Downloads/png-clipart-dark-souls-solaire-of-astora-drawing-knight-bloodborne-dark-souls-dark-souls-solaire-of-astora-thumbnail-3302336950.png -C -W 60 > ~/.config/fish/ascii-art.txt
```

Then follow the next steps to add it to your fish config!

### HUMAN
this is whats in that fish config

### ASSISTANT
I can see your config. Notice the commented out section about `fish_greeting` and `fastfetch` — CachyOS uses **fastfetch** for the startup display (that's what's showing your current ASCII). 

The cleanest way to add your art is to use the `fish_greeting` function. Click at the end of the `#end` line and add a new line below everything:

```fish
function fish_greeting
    cat ~/.config/fish/ascii-art.txt
end
```

Then save with `Ctrl+X` → `Y` → `Enter`. This overrides the default greeting with your Solaire art!

### HUMAN
perfect but now all my system info is gone?

### ASSISTANT
That's because fastfetch was handling the system info display. Just add it after the cat command:

```fish
function fish_greeting
    cat ~/.config/fish/ascii-art.txt
    fastfetch
end
```

Open the config again with `nano ~/.config/fish/config.fish`, update the function, save and then test with `source ~/.config/fish/config.fish`.

### HUMAN
when i run ❯ source __~/.config/fish/____config.fish__ ~ ❯ i get nothing and when i open my terminal it now shows the new ascii image and then the old one with all system info?

### ASSISTANT
The old ASCII is coming from fastfetch's own config. You need to disable it there. Run:

```fish
nano ~/.config/fastfetch/config.jsonc
```

Look for a logo or ASCII art section and remove it, or just run fastfetch without the logo:

```fish
function fish_greeting
    cat ~/.config/fish/ascii-art.txt
    fastfetch --logo none
end
```

That should show your Solaire art and then just the system info text underneath without the duplicate ASCII.

### HUMAN
i want the new ascii art to be right next to the system info. i literally want to change the cachyos logo with my new custom ascii

### ASSISTANT
In that case, fastfetch supports custom ASCII logos directly! You can point it to your saved ascii-art.txt file:

```fish
fastfetch --logo ~/.config/fish/ascii-art.txt
```

If that looks right, then update your fish config to just use that instead:

```fish
function fish_greeting
    fastfetch --logo ~/.config/fish/ascii-art.txt
end
```

But there's a catch — fastfetch may not render the colors from the file correctly since it has its own logo color system. If the colors look off, we can set the logo type explicitly:

```fish
fastfetch --logo ~/.config/fish/ascii-art.txt --logo-type file
```

Give those a try and see how it looks!

### HUMAN
it looks good but now i want to mess with konsole profile settings

### ASSISTANT
Sure! Go to **Konsole → Settings → Edit Current Profile → Appearance** and you can tweak:

- **Color scheme** — try different schemes or edit the current one to boost saturation/contrast
- **Background** — adjust opacity/blur
- **Font** — size and font can affect how your ASCII art looks

What specifically are you looking to change?
