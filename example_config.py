backup_path = "~/.backups"
verbose_mode = True
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
user_configs = [".vimrc",
                ".zshrc",
                ".zprofile",
                ".gitconfig",
               ]
system_configs = ["/etc/pulse/default.pa",
                  "/etc/makepkg.conf",
                  "/etc/modprobe.d/alsa-base.conf",
                 ]
other_paths = [
              ]
