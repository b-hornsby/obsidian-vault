---
id: 560354
source: GEMINI
date: 2026-01-31
tags: ['cachyos', 'paru', 'polychromatic', 'aur', 'razer-peripherals']
category: homelab
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is installing Polychromatic for Razer peripheral management on CachyOS using paru.
---
# paru  -S polychromatic

:: Resolving dependencies...
:: There are 2 providers available for polychromatic:
:: Repository AUR:
    1) polychromatic  2) polychromatic-git  
Enter a number (default=1): 1
:: Calculating conflicts...
:: Calculating inner conflicts...

Repo (21)                                   Old Version  New Version       Make Only
cachyos-extra-v3/blas                                    3.12.1-2.1        No
cachyos-extra-v3/cblas                                   3.12.1-2.1        No
cachyos-extra-v3/lapack                                  3.12.1-2.1        No
cachyos-extra-v3/ninja                                   1.13.2-2.1        Yes
cachyos-extra-v3/python-charset-normalizer               3.4.4-2.1         No
cachyos-extra-v3/python-numpy                            2.4.1-1.1         No
cachyos-extra-v3/python-pyqt6-sip                        13.11.0-1.1       No
cachyos-extra-v3/qt6-positioning                         6.10.2-1.1        No
cachyos-extra-v3/qt6-webchannel                          6.10.2-1.1        No
cachyos-extra-v3/re2                                     2:2025.11.05-1.1  No
extra/libappindicator                                    12.10.1-1         No
extra/meson                                              1.10.1-1          Yes
extra/python-colorama                                    0.4.6-6           No
extra/python-colour                                      0.1.5-16          No
extra/python-idna                                        3.11-2            No
extra/python-openrazer                                   3.11.0-3          No
extra/python-pyqt6                                       6.10.2-3          No
extra/python-pyqt6-webengine                             6.10.0-2          No
extra/python-requests                                    2.32.5-3          No
extra/python-tqdm                                        4.67.1-5          Yes
extra/qt6-webengine                                      6.10.2-1          No

Aur (1)                                     Old Version  New Version       Make Only
aur/polychromatic                                        0.9.6-1           No

:: Proceed to review? [Y/n]: y

:: Downloading PKGBUILDs...
 (1/1) polychromatic-0.9.6-1                         [
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
--]
Paging with less. Press 'q' to quit or 'h' for help.

:: polychromatic:
  PKGBUILD:
    # Maintainer: Luke Horwell <code (at) horwell (dot) me>
    # Contributor: Luca Weiss <luca (at) z3ntu (dot) xyz>
    
    pkgname=polychromatic
    pkgver=0.9.6
    pkgrel=1
    pkgdesc='RGB lighting management front-end application for OpenRazer'
    arch=('any')
    url='https://github.com/polychromatic/polychromatic'
    license=('GPL-3.0-or-later')
    depends=(
      libappindicator
      python
      python-colorama
      python-colour
      python-gobject
      python-openrazer
      python-pyqt6
      python-pyqt6-webengine
      python-requests
      python-setproctitle
      qt6-svg
    )
    makedepends=(
      meson
      ninja
    )
    source=("$pkgname-v$pkgver.tar.gz::https://github.com/polychromatic/polychromatic/archive/v$pkgver.tar.gz")
    sha512sums=('7bd364a803e9c29af8a9db1b573a89bd05615d6ced051d8244e5780390d67bc4024c351d6b96447fba68444b04e35239d2370dabfbd7beb99d5095>
    
    build() {
      arch-meson $pkgname-$pkgver build
:
Paging with less. Press 'q' to quit or 'h' for help.

:: polychromatic:
  PKGBUILD:
    # Maintainer: Luke Horwell <code (at) horwell (dot) me>
    # Contributor: Luca Weiss <luca (at) z3ntu (dot) xyz>
    
    pkgname=polychromatic
    pkgver=0.9.6
    pkgrel=1
    pkgdesc='RGB lighting management front-end application for OpenRazer'
    arch=('any')
    url='https://github.com/polychromatic/polychromatic'
    license=('GPL-3.0-or-later')
    depends=(
      libappindicator
      python
      python-colorama
      python-colour
      python-gobject
      python-openrazer
      python-pyqt6
      python-pyqt6-webengine
      python-requests
      python-setproctitle
      qt6-svg
    )
    makedepends=(
      meson
      ninja
    )
    source=("$pkgname-v$pkgver.tar.gz::https://github.com/polychromatic/polychromatic/archive/v$pkgver.tar.gz")
    sha512sums=('7bd364a803e9c29af8a9db1b573a89bd05615d6ced051d8244e5780390d67bc4024c351d6b96447fba68444b04e35239d2370dabfbd7beb99d5095>
    
    build() {
      arch-meson $pkgname-$pkgver build
:⏎                                                                                                                                      
~ 50s
]

### USER
paru  -S polychromatic

:: Resolving dependencies...
:: There are 2 providers available for polychromatic:
:: Repository AUR:
    1) polychromatic  2) polychromatic-git  
Enter a number (default=1): 1
:: Calculating conflicts...
:: Calculating inner conflicts...

Repo (21)                                   Old Version  New Version       Make Only
cachyos-extra-v3/blas                                    3.12.1-2.1        No
cachyos-extra-v3/cblas                                   3.12.1-2.1        No
cachyos-extra-v3/lapack                                  3.12.1-2.1        No
cachyos-extra-v3/ninja                                   1.13.2-2.1        Yes
cachyos-extra-v3/python-charset-normalizer               3.4.4-2.1         No
cachyos-extra-v3/python-numpy                            2.4.1-1.1         No
cachyos-extra-v3/python-pyqt6-sip                        13.11.0-1.1       No
cachyos-extra-v3/qt6-positioning                         6.10.2-1.1        No
cachyos-extra-v3/qt6-webchannel                          6.10.2-1.1        No
cachyos-extra-v3/re2                                     2:2025.11.05-1.1  No
extra/libappindicator                                    12.10.1-1         No
extra/meson                                              1.10.1-1          Yes
extra/python-colorama                                    0.4.6-6           No
extra/python-colour                                      0.1.5-16          No
extra/python-idna                                        3.11-2            No
extra/python-openrazer                                   3.11.0-3          No
extra/python-pyqt6                                       6.10.2-3          No
extra/python-pyqt6-webengine                             6.10.0-2          No
extra/python-requests                                    2.32.5-3          No
extra/python-tqdm                                        4.67.1-5          Yes
extra/qt6-webengine                                      6.10.2-1          No

Aur (1)                                     Old Version  New Version       Make Only
aur/polychromatic                                        0.9.6-1           No

:: Proceed to review? [Y/n]: y

:: Downloading PKGBUILDs...
 (1/1) polychromatic-0.9.6-1                         [
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
--]
Paging with less. Press 'q' to quit or 'h' for help.

:: polychromatic:
  PKGBUILD:
    # Maintainer: Luke Horwell <code (at) horwell (dot) me>
    # Contributor: Luca Weiss <luca (at) z3ntu (dot) xyz>
    
    pkgname=polychromatic
    pkgver=0.9.6
    pkgrel=1
    pkgdesc='RGB lighting management front-end application for OpenRazer'
    arch=('any')
    url='https://github.com/polychromatic/polychromatic'
    license=('GPL-3.0-or-later')
    depends=(
      libappindicator
      python
      python-colorama
      python-colour
      python-gobject
      python-openrazer
      python-pyqt6
      python-pyqt6-webengine
      python-requests
      python-setproctitle
      qt6-svg
    )
    makedepends=(
      meson
      ninja
    )
    source=("$pkgname-v$pkgver.tar.gz::https://github.com/polychromatic/polychromatic/archive/v$pkgver.tar.gz")
    sha512sums=('7bd364a803e9c29af8a9db1b573a89bd05615d6ced051d8244e5780390d67bc4024c351d6b96447fba68444b04e35239d2370dabfbd7beb99d5095>
    
    build() {
      arch-meson $pkgname-$pkgver build
:
Paging with less. Press 'q' to quit or 'h' for help.

:: polychromatic:
  PKGBUILD:
    # Maintainer: Luke Horwell <code (at) horwell (dot) me>
    # Contributor: Luca Weiss <luca (at) z3ntu (dot) xyz>
    
    pkgname=polychromatic
    pkgver=0.9.6
    pkgrel=1
    pkgdesc='RGB lighting management front-end application for OpenRazer'
    arch=('any')
    url='https://github.com/polychromatic/polychromatic'
    license=('GPL-3.0-or-later')
    depends=(
      libappindicator
      python
      python-colorama
      python-colour
      python-gobject
      python-openrazer
      python-pyqt6
      python-pyqt6-webengine
      python-requests
      python-setproctitle
      qt6-svg
    )
    makedepends=(
      meson
      ninja
    )
    source=("$pkgname-v$pkgver.tar.gz::https://github.com/polychromatic/polychromatic/archive/v$pkgver.tar.gz")
    sha512sums=('7bd364a803e9c29af8a9db1b573a89bd05615d6ced051d8244e5780390d67bc4024c351d6b96447fba68444b04e35239d2370dabfbd7beb99d5095>
    
    build() {
      arch-meson $pkgname-$pkgver build
:⏎                                                                                                                                      
~ 50s
]

### GEMINI
You are currently stuck in the PKGBUILD review phase. Paru is doing exactly what it is designed to do: forcing you to audit the script before it executes on your system. If you just sit there staring at the screen, nothing will happen. The Immediate Fix Press q: This will quit the pager (less) and move you to the next step of the installation. Confirm the build: After you press q, it will likely ask if you want to proceed with the installation. Type y or press Enter. Why You’re Stuck You’re treating the terminal like a loading screen. It's not. It's a conversation. Paru is showing you the "source code" of how it’s going to build polychromatic to ensure you aren't installing something malicious. The "Advisor" Reality Check You are encountering "the wall" because you haven't learned the basic controls of the tools you're using. The Pager: less is the standard Linux tool for viewing text. q to quit, j/k to scroll. Learn it. Automation vs. Safety: If you hate reviewing these files and trust the AUR blindly (which is a risk), you can skip this in the future by using paru -S --noconfirm [package], but don't come crying when a broken PKGBUILD borks your path. Critical Blind Spot Look at your dependency list. You are about to install 21 packages just for RGB control. Opportunity Cost: You are bloating your system with python-numpy, blas, and lapack (heavy math libraries) just to make your keyboard change colors. Risk: polychromatic is just a front-end. It requires openrazer to actually function. If your user isn't in the plugdev group after this, it won't work anyway. Next Step: Press q now. Once the install finishes, do you want the command to add your user to the necessary group so the software actually detects your hardware?
