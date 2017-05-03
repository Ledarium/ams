backup_path = "~/.backups"
package_utility = "yaourt"
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
system_configs = {
    'name': "system configs",  # specifies name displayed in log
    'prefix': "sudo",  # specifies how to prefix rsync command
    'folder': "system",  # subfolder for this category inside your backup_path
    'args': "-v",  # specifies additional rsync flag to this category
    'files': ["/etc/pulse/default.pa",
              "/etc/makepkg.conf",
              "/etc/modprobe.d/alsa-base.conf",
              "/etc/systemd/system/suspend@.service"]
                 }
user_configs = {
    'name': "user configs",
    'folder': "user",
    'relative_to': "$HOME",  # shell variables and specials are supported
    'files': [".vimrc",
              ".zshrc",
              ".zprofile"]
                }
backup = [user_configs, system_configs]

remove_orphans = {'flags': "-Qdt"}
full_update = {'flags': "-Syuu"}
update = [remove_orphans, full_update]
