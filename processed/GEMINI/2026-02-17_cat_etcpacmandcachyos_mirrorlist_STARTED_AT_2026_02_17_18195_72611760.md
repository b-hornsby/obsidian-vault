---
id: 799420
source: GEMINI
date: 2026-02-17
tags: ['mirrorlist', 'rate-mirrors', 'cachyos', 'pacman-mirrors', 'speed-test']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was reviewing the rated mirrorlist output to understand which CachyOS mirrors were selected and their speeds.
---
# ❯ cat /etc/pacman.d/cachyos-mirrorlist
# STARTED AT: 2026-02-17 18:19:57.787037801 -05:00
# VERSION: 0.27.0
# ARGS: rate-mirrors --save /tmp/tmp.31finWLu7Z cachyos
# MIRRORS LEFT AFTER FILTERING: 22
# JUMP #1
# EXPLORING US
# VISITED US
# BLANK ITERATION
# COUNTRY JUMPING YIELDED TOO FEW MIRRORS (0), ADDING OTHERS TO UNLABELED
#  

# TESTING UNLABELED MIRRORS
# FAILED TO CONNECT TO https://mirror.meowsmp.net/cachyOS/repo/x86_64/cachyos/cachyos.files
# SpeedTestResult { speed: 27.4 MB/s; elapsed: 212ms; connection_time: 319ms }
# SpeedTestResult { speed: 17.3 MB/s; elapsed: 336ms; connection_time: 200ms }
# SpeedTestResult { speed: 17.0 MB/s; elapsed: 343ms; connection_time: 191ms }
# SpeedTestResult { speed: 14.7 MB/s; elapsed: 395ms; connection_time: 250ms }
# SpeedTestResult { speed: 14.2 MB/s; elapsed: 411ms; connection_time: 367ms }
# SpeedTestResult { speed: 11.6 MB/s; elapsed: 500ms; connection_time: 292ms }
# SpeedTestResult { speed: 6.9 MB/s; elapsed: 846ms; connection_time: 322ms }
# SpeedTestResult { speed: 1.5 MB/s; elapsed: 994ms; connection_time: 212ms }
# SpeedTestResult { speed: 6.5 MB/s; elapsed: 894ms; connection_time: 535ms }
# SpeedTestResult { speed: 6.5 MB/s; elapsed: 901ms; connection_time: 539ms }
# SpeedTestResult { speed: 7.0 MB/s; elapsed: 831ms; connection_time: 641ms }
# SpeedTestResult { speed: 1.7 MB/s; elapsed: 930ms; connection_time: 565ms }
# SpeedTestResult { speed: 6.2 MB/s; elapsed: 938ms; connection_time: 653ms }
# SpeedTestResult { speed: 786.1 KB/s; elapsed: 956ms; connection_time: 628ms }
# SpeedTestResult { speed: 6.7 MB/s; elapsed: 870ms; connection_time: 763ms }
# SpeedTestResult { speed: 3.8 MB/s; elapsed: 966ms; connection_time: 663ms }
# SpeedTestResult { speed: 4.7 MB/s; elapsed: 916ms; connection_time: 1.06s }
# SpeedTestResult { speed: 1.9 MB/s; elapsed: 996ms; connection_time: 1.08s }
# SpeedTestResult { speed: 438.7 KB/s; elapsed: 858ms; connection_time: 1.24s }
# SpeedTestResult { speed: 322.8 KB/s; elapsed: 811ms; connection_time: 1.86s }
# SpeedTestResult { speed: 360.7 KB/s; elapsed: 998ms; connection_time: 2.66s }
#  

# RE-TESTING TOP MIRRORS
# SpeedTestResult { speed: 39.5 MB/s; elapsed: 147ms; connection_time: 78ms }
# SpeedTestResult { speed: 22.4 MB/s; elapsed: 260ms; connection_time: 144ms }
# SpeedTestResult { speed: 14.2 MB/s; elapsed: 409ms; connection_time: 101ms }
# SpeedTestResult { speed: 19.5 MB/s; elapsed: 299ms; connection_time: 167ms }
# SpeedTestResult { speed: 16.7 MB/s; elapsed: 349ms; connection_time: 173ms }
# ==== RESULTS (top re-tested) ====
#   1. SpeedTestResult { speed: 39.5 MB/s; elapsed: 147ms; connection_time: 78ms } -> https://us-mnz.soulharsh007.dev/cachyos/repo/
#   2. SpeedTestResult { speed: 22.4 MB/s; elapsed: 260ms; connection_time: 144ms } -> https://cdn77.cachyos.org/repo/
#   3. SpeedTestResult { speed: 19.5 MB/s; elapsed: 299ms; connection_time: 167ms } -> https://mirror.allthingslinux.org/cachyos/repo/
#   4. SpeedTestResult { speed: 16.7 MB/s; elapsed: 349ms; connection_time: 173ms } -> https://ca.mirror.cx/cachyos/repo/
#   5. SpeedTestResult { speed: 14.2 MB/s; elapsed: 409ms; connection_time: 101ms } -> https://us.cachyos.org/repo/
#   6. SpeedTestResult { speed: 11.6 MB/s; elapsed: 500ms; connection_time: 292ms } -> https://cdn.lansing2600.org/cachyos/repo/
#   7. SpeedTestResult { speed: 7.0 MB/s; elapsed: 831ms; connection_time: 641ms } -> https://mirror.cachyos.org/repo/
#   8. SpeedTestResult { speed: 6.9 MB/s; elapsed: 846ms; connection_time: 322ms } -> https://cachyos.doridian.net/repo/
#   9. SpeedTestResult { speed: 6.7 MB/s; elapsed: 870ms; connection_time: 763ms } -> https://nl.mirror.cx/cachyos/repo/
#  10. SpeedTestResult { speed: 6.5 MB/s; elapsed: 894ms; connection_time: 535ms } -> https://cdn.cachyos.org/repo/
#  11. SpeedTestResult { speed: 6.5 MB/s; elapsed: 901ms; connection_time: 539ms } -> https://no.mirror.cx/cachyos/repo/
#  12. SpeedTestResult { speed: 6.2 MB/s; elapsed: 938ms; connection_time: 653ms } -> https://de-nue.soulharsh007.dev/cachyos/repo/
#  13. SpeedTestResult { speed: 4.7 MB/s; elapsed: 916ms; connection_time: 1.06s } -> https://mirror.hb9hil.org/cachyos/repo/
#  14. SpeedTestResult { speed: 3.8 MB/s; elapsed: 966ms; connection_time: 663ms } -> https://at.cachyos.org/repo/
#  15. SpeedTestResult { speed: 1.9 MB/s; elapsed: 996ms; connection_time: 1.08s } -> https://cachyos.next-works.it/repo/
#  16. SpeedTestResult { speed: 1.7 MB/s; elapsed: 930ms; connection_time: 565ms } -> https://mirror.lesviallon.fr/cachy/repo/
#  17. SpeedTestResult { speed: 1.5 MB/s; elapsed: 994ms; connection_time: 212ms } -> https://mirrors.lansing2600.org/cachyos/repo/
#  18. SpeedTestResult { speed: 786.1 KB/s; elapsed: 956ms; connection_time: 628ms } -> https://archlinux.gay/cachy/repo/
#  19. SpeedTestResult { speed: 438.7 KB/s; elapsed: 858ms; connection_time: 1.24s } -> https://mirror.limda.net/cachy/repo/
#  20. SpeedTestResult { speed: 360.7 KB/s; elapsed: 998ms; connection_time: 2.66s } -> https://mirrors.ustc.edu.cn/cachyos/repo/
#  21. SpeedTestResult { speed: 322.8 KB/s; elapsed: 811ms; connection_time: 1.86s } -> https://mirror.nju.edu.cn/cachyos/repo/
# FINISHED AT: 2026-02-17 18:20:04.068086072 -05:00
Server = https://us-mnz.soulharsh007.dev/cachyos/repo/$arch/$repo
Server = https://cdn77.cachyos.org/repo/$arch/$repo
Server = https://mirror.allthingslinux.org/cachyos/repo/$arch/$repo
Server = https://ca.mirror.cx/cachyos/repo/$arch/$repo
Server = https://us.cachyos.org/repo/$arch/$repo
Server = https://cdn.lansing2600.org/cachyos/repo/$arch/$repo
Server = https://mirror.cachyos.org/repo/$arch/$repo
Server = https://cachyos.doridian.net/repo/$arch/$repo
Server = https://nl.mirror.cx/cachyos/repo/$arch/$repo
Server = https://cdn.cachyos.org/repo/$arch/$repo
Server = https://no.mirror.cx/cachyos/repo/$arch/$repo
Server = https://de-nue.soulharsh007.dev/cachyos/repo/$arch/$repo
Server = https://mirror.hb9hil.org/cachyos/repo/$arch/$repo
Server = https://at.cachyos.org/repo/$arch/$repo
Server = https://cachyos.next-works.it/repo/$arch/$repo
Server = https://mirror.lesviallon.fr/cachy/repo/$arch/$repo
Server = https://mirrors.lansing2600.org/cachyos/repo/$arch/$repo
Server = https://archlinux.gay/cachy/repo/$arch/$repo
Server = https://mirror.limda.net/cachy/repo/$arch/$repo
Server = https://mirrors.ustc.edu.cn/cachyos/repo/$arch/$repo
Server = https://mirror.nju.edu.cn/cachyos/repo/$arch/$repo

~
❯ sudo pacman -Syy
:: Synchronizing package databases...
 cachyos                                                          512.0 KiB  2.89 MiB/s 00:00 [#######################################################] 100%
 cachyos-v3                                                       129.1 KiB  1050 KiB/s 00:00 [#######################################################] 100%
 cachyos-core-v3                                                  106.9 KiB   869 KiB/s 00:00 [#######################################################] 100%
 cachyos-extra-v3                                                   4.2 MiB  21.0 MiB/s 00:00 [#######################################################] 100%
 core                                                             123.4 KiB   408 KiB/s 00:00 [#######################################################] 100%
 extra                                                              7.9 MiB  21.8 MiB/s 00:00 [#######################################################] 100%
 multilib                                                         128.7 KiB   711 KiB/s 00:00 [#######################################################] 100%

~
❯ 

### USER
❯ cat /etc/pacman.d/cachyos-mirrorlist
# STARTED AT: 2026-02-17 18:19:57.787037801 -05:00
# VERSION: 0.27.0
# ARGS: rate-mirrors --save /tmp/tmp.31finWLu7Z cachyos
# MIRRORS LEFT AFTER FILTERING: 22
# JUMP #1
# EXPLORING US
# VISITED US
# BLANK ITERATION
# COUNTRY JUMPING YIELDED TOO FEW MIRRORS (0), ADDING OTHERS TO UNLABELED
#  

# TESTING UNLABELED MIRRORS
# FAILED TO CONNECT TO https://mirror.meowsmp.net/cachyOS/repo/x86_64/cachyos/cachyos.files
# SpeedTestResult { speed: 27.4 MB/s; elapsed: 212ms; connection_time: 319ms }
# SpeedTestResult { speed: 17.3 MB/s; elapsed: 336ms; connection_time: 200ms }
# SpeedTestResult { speed: 17.0 MB/s; elapsed: 343ms; connection_time: 191ms }
# SpeedTestResult { speed: 14.7 MB/s; elapsed: 395ms; connection_time: 250ms }
# SpeedTestResult { speed: 14.2 MB/s; elapsed: 411ms; connection_time: 367ms }
# SpeedTestResult { speed: 11.6 MB/s; elapsed: 500ms; connection_time: 292ms }
# SpeedTestResult { speed: 6.9 MB/s; elapsed: 846ms; connection_time: 322ms }
# SpeedTestResult { speed: 1.5 MB/s; elapsed: 994ms; connection_time: 212ms }
# SpeedTestResult { speed: 6.5 MB/s; elapsed: 894ms; connection_time: 535ms }
# SpeedTestResult { speed: 6.5 MB/s; elapsed: 901ms; connection_time: 539ms }
# SpeedTestResult { speed: 7.0 MB/s; elapsed: 831ms; connection_time: 641ms }
# SpeedTestResult { speed: 1.7 MB/s; elapsed: 930ms; connection_time: 565ms }
# SpeedTestResult { speed: 6.2 MB/s; elapsed: 938ms; connection_time: 653ms }
# SpeedTestResult { speed: 786.1 KB/s; elapsed: 956ms; connection_time: 628ms }
# SpeedTestResult { speed: 6.7 MB/s; elapsed: 870ms; connection_time: 763ms }
# SpeedTestResult { speed: 3.8 MB/s; elapsed: 966ms; connection_time: 663ms }
# SpeedTestResult { speed: 4.7 MB/s; elapsed: 916ms; connection_time: 1.06s }
# SpeedTestResult { speed: 1.9 MB/s; elapsed: 996ms; connection_time: 1.08s }
# SpeedTestResult { speed: 438.7 KB/s; elapsed: 858ms; connection_time: 1.24s }
# SpeedTestResult { speed: 322.8 KB/s; elapsed: 811ms; connection_time: 1.86s }
# SpeedTestResult { speed: 360.7 KB/s; elapsed: 998ms; connection_time: 2.66s }
#  

# RE-TESTING TOP MIRRORS
# SpeedTestResult { speed: 39.5 MB/s; elapsed: 147ms; connection_time: 78ms }
# SpeedTestResult { speed: 22.4 MB/s; elapsed: 260ms; connection_time: 144ms }
# SpeedTestResult { speed: 14.2 MB/s; elapsed: 409ms; connection_time: 101ms }
# SpeedTestResult { speed: 19.5 MB/s; elapsed: 299ms; connection_time: 167ms }
# SpeedTestResult { speed: 16.7 MB/s; elapsed: 349ms; connection_time: 173ms }
# ==== RESULTS (top re-tested) ====
#   1. SpeedTestResult { speed: 39.5 MB/s; elapsed: 147ms; connection_time: 78ms } -> https://us-mnz.soulharsh007.dev/cachyos/repo/
#   2. SpeedTestResult { speed: 22.4 MB/s; elapsed: 260ms; connection_time: 144ms } -> https://cdn77.cachyos.org/repo/
#   3. SpeedTestResult { speed: 19.5 MB/s; elapsed: 299ms; connection_time: 167ms } -> https://mirror.allthingslinux.org/cachyos/repo/
#   4. SpeedTestResult { speed: 16.7 MB/s; elapsed: 349ms; connection_time: 173ms } -> https://ca.mirror.cx/cachyos/repo/
#   5. SpeedTestResult { speed: 14.2 MB/s; elapsed: 409ms; connection_time: 101ms } -> https://us.cachyos.org/repo/
#   6. SpeedTestResult { speed: 11.6 MB/s; elapsed: 500ms; connection_time: 292ms } -> https://cdn.lansing2600.org/cachyos/repo/
#   7. SpeedTestResult { speed: 7.0 MB/s; elapsed: 831ms; connection_time: 641ms } -> https://mirror.cachyos.org/repo/
#   8. SpeedTestResult { speed: 6.9 MB/s; elapsed: 846ms; connection_time: 322ms } -> https://cachyos.doridian.net/repo/
#   9. SpeedTestResult { speed: 6.7 MB/s; elapsed: 870ms; connection_time: 763ms } -> https://nl.mirror.cx/cachyos/repo/
#  10. SpeedTestResult { speed: 6.5 MB/s; elapsed: 894ms; connection_time: 535ms } -> https://cdn.cachyos.org/repo/
#  11. SpeedTestResult { speed: 6.5 MB/s; elapsed: 901ms; connection_time: 539ms } -> https://no.mirror.cx/cachyos/repo/
#  12. SpeedTestResult { speed: 6.2 MB/s; elapsed: 938ms; connection_time: 653ms } -> https://de-nue.soulharsh007.dev/cachyos/repo/
#  13. SpeedTestResult { speed: 4.7 MB/s; elapsed: 916ms; connection_time: 1.06s } -> https://mirror.hb9hil.org/cachyos/repo/
#  14. SpeedTestResult { speed: 3.8 MB/s; elapsed: 966ms; connection_time: 663ms } -> https://at.cachyos.org/repo/
#  15. SpeedTestResult { speed: 1.9 MB/s; elapsed: 996ms; connection_time: 1.08s } -> https://cachyos.next-works.it/repo/
#  16. SpeedTestResult { speed: 1.7 MB/s; elapsed: 930ms; connection_time: 565ms } -> https://mirror.lesviallon.fr/cachy/repo/
#  17. SpeedTestResult { speed: 1.5 MB/s; elapsed: 994ms; connection_time: 212ms } -> https://mirrors.lansing2600.org/cachyos/repo/
#  18. SpeedTestResult { speed: 786.1 KB/s; elapsed: 956ms; connection_time: 628ms } -> https://archlinux.gay/cachy/repo/
#  19. SpeedTestResult { speed: 438.7 KB/s; elapsed: 858ms; connection_time: 1.24s } -> https://mirror.limda.net/cachy/repo/
#  20. SpeedTestResult { speed: 360.7 KB/s; elapsed: 998ms; connection_time: 2.66s } -> https://mirrors.ustc.edu.cn/cachyos/repo/
#  21. SpeedTestResult { speed: 322.8 KB/s; elapsed: 811ms; connection_time: 1.86s } -> https://mirror.nju.edu.cn/cachyos/repo/
# FINISHED AT: 2026-02-17 18:20:04.068086072 -05:00
Server = https://us-mnz.soulharsh007.dev/cachyos/repo/$arch/$repo
Server = https://cdn77.cachyos.org/repo/$arch/$repo
Server = https://mirror.allthingslinux.org/cachyos/repo/$arch/$repo
Server = https://ca.mirror.cx/cachyos/repo/$arch/$repo
Server = https://us.cachyos.org/repo/$arch/$repo
Server = https://cdn.lansing2600.org/cachyos/repo/$arch/$repo
Server = https://mirror.cachyos.org/repo/$arch/$repo
Server = https://cachyos.doridian.net/repo/$arch/$repo
Server = https://nl.mirror.cx/cachyos/repo/$arch/$repo
Server = https://cdn.cachyos.org/repo/$arch/$repo
Server = https://no.mirror.cx/cachyos/repo/$arch/$repo
Server = https://de-nue.soulharsh007.dev/cachyos/repo/$arch/$repo
Server = https://mirror.hb9hil.org/cachyos/repo/$arch/$repo
Server = https://at.cachyos.org/repo/$arch/$repo
Server = https://cachyos.next-works.it/repo/$arch/$repo
Server = https://mirror.lesviallon.fr/cachy/repo/$arch/$repo
Server = https://mirrors.lansing2600.org/cachyos/repo/$arch/$repo
Server = https://archlinux.gay/cachy/repo/$arch/$repo
Server = https://mirror.limda.net/cachy/repo/$arch/$repo
Server = https://mirrors.ustc.edu.cn/cachyos/repo/$arch/$repo
Server = https://mirror.nju.edu.cn/cachyos/repo/$arch/$repo

~
❯ sudo pacman -Syy
:: Synchronizing package databases...
 cachyos                                                          512.0 KiB  2.89 MiB/s 00:00 [#######################################################] 100%
 cachyos-v3                                                       129.1 KiB  1050 KiB/s 00:00 [#######################################################] 100%
 cachyos-core-v3                                                  106.9 KiB   869 KiB/s 00:00 [#######################################################] 100%
 cachyos-extra-v3                                                   4.2 MiB  21.0 MiB/s 00:00 [#######################################################] 100%
 core                                                             123.4 KiB   408 KiB/s 00:00 [#######################################################] 100%
 extra                                                              7.9 MiB  21.8 MiB/s 00:00 [#######################################################] 100%
 multilib                                                         128.7 KiB   711 KiB/s 00:00 [#######################################################] 100%

~
❯ 

### GEMINI
Finally. Your "brain" is back online, and your "maps" are populated. You have successfully navigated back from a self-inflicted system failure. The Advisor’s Mirror You just experienced the "Rolling Release Tax." You tried to dodge it by deleting warnings and blindly clicking "Overwrite," and the tax was several minutes of manual repair work. The Reality: Your system is synced, but it is still "generic" Arch in memory. Since you overwrote your config earlier, you likely have packages installed from the standard Arch repositories that should be the optimized CachyOS-v3 versions. The Blind Spot: Just because the sync worked doesn't mean you're optimized. You're currently a hybrid—running an i7-12700K on standard software. The Final Precision Steps To finish this properly and restore the "Cachy" performance you've been missing: Rank the rest of the mirrors: You only ranked the main CachyOS list. You need to fix the v3 and standard lists as well so your downloads don't crawl. sudo cachyos-rate-mirrors The "Re-Optimization" Upgrade: Now that your repositories are in the correct order (CachyOS on top), you need to tell the system to check if a "v3" version of your currently installed apps exists. sudo pacman -Syu If it asks to replace a package with one from the cachyos-v3 repo, say Yes. Clean Up Your Debt: You fixed the .pacnew files you found, but from now on, make it a habit to check for them after every big update. The Tactical Takeaway You went from a broken system to a functional one. You've learned how to read a pacman.conf, how to prioritize repositories, and why mirrorlists matter. Do not let this happen again. Next time you see a .pacnew, use v to view the difference before you decide to o overwrite. Would you like me to show you how to set up an alias so you can check for these "hidden" configuration updates with a single command in the future?
