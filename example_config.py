system = {
    'utility': 'yaourt'
}
archive = {
    'tar_args': "-cJvf",
}
'''
Enabled options for tar are:
    -c: create archive
    -J: compress with xz
    -v: show progress
    -f: specifies output filename (you will not need to remove it, seriously)
'''

backup = {
    'path': "~/.backups",
    'rsync_args': "-pogbr -hhh --progress",
    'backup_pkglist': True,
    'tasklist': [
        {
            'name': "user configs",
            'folder': "user",
            'relative_to': "$HOME",
            'paths': [
                ".vimrc",
                ".zshrc",
                ".i3",
                ".config/conkyrc",
                ".config/cmus",
                ".config/beets"
            ]
        },
        {
            'name': "system configs",
            'prefix': "sudo",
            'folder': "system",
            'paths': [
                "/etc/pulse/default.pa",
                "/etc/makepkg.conf",
                "/etc/default/grub",
                "/etc/modprobe.d/alsa-base.conf"
            ]
        },
        {
            'name': "my_apps",
            'folder': "apps",
            'relative_to': "$HOME/Apps",
            'paths': ["*"]
        },
        {
            'name': "music",
            'folder': "music",
            'relative_to': "$HOME/Music",
            'paths': ["*"]
        },
        {
            'name': "docs",
            'folder': "documents",
            'relative_to': "$HOME/Documents",
            'paths': ["*"]
        }
    ]
}
'''
Enabled options for rsync are:
    -p: preserves permissions.
    -o: preserves owner.
    -g: preserves group
    -b: makes backup instead of overwriting
    -r: recurse directories.
    -hhh: outputs numbers in units of 1024 (K, M, G, T).
    --progress: show progress
'''

update = {
    'tasklist': [
        {
            'name': "Removing orphans",
            'flags': "-Qdt",
        },
        {
            'name': "Full system update",
            'flags': "-Syuua",
        }
    ]
}
