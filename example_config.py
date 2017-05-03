backup_path = "~/.backups"
rsync_args = "-pogbr -hhh --progress"
'''
Enabled options for rsync are:
    -p: preserves permissions.
    -o: preserves owner.
    -g: preserves group.
    -b: makes backup instead of overwriting
    -r: recurse directories.
    -hhh: outputs numbers in human-readable format, in units of 1024 (K, M, G, T).
    --progress: show progress
'''
user_configs = {'name': "user configs",
                'folder': "user",
                'files':   ["$HOME/.vimrc",
                            "$HOME/.zshrc",
                            "$HOME/.zprofile"]
                }
system_configs = {'name': "system configs", # specifies name displayed in log
                  'prefix': "sudo", # specifies how to prefix rsync command
                  'folder': "system", # subfolder for this category inside your backup_path
                  'args': "-v", # specifies additional flag to this category
                  'files': ["/etc/pulse/default.pa", # shell variables and specials are supported
                            "/etc/makepkg.conf",
                            "/etc/modprobe.d/alsa-base.conf",
                            "/etc/systemd/system/suspend@.service"]
                 }
backup = [user_configs, system_configs]

''' not implemented
remove_orphans = {'name': "yaourt",
                  'flags': "-Qdt",
                  }
full_update = {'name': "yaourt",
               'flags': "-Syuu",
               }
update = [remove_orphans, full_update]
'''
