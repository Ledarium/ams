#!/usr/bin/env python3
from subprocess import call, Popen, PIPE
import shlex
from pathlib import Path
from datetime import datetime
import config


def backup():
    # preparations
    date = datetime.now().strftime("%d-%m-%y.%H:%M:%S")
    backup_path = Path(config.backup_path).expanduser()
    if config.verbose_mode:
        print("Backup_path is set to", backup_path)
    if not backup_path.is_dir():
        backup_path.mkdir()
    backup_location = backup_path / date
    backup_location.mkdir()
    if config.verbose_mode:
        print("Current backup will be saved in", backup_location)
    if config.rsync_args:
        global_args = config.rsync_args
    else:
        global_args == "--progress"

    def backup_category(category):
        print("Backing up", category['name'])
        location = backup_location / category['folder']
        location.mkdir(exist_ok=True)
        location = str(location)
        for path in category['files']:
            call(' '.join([
                 category.get('prefix', ''), # prefix rsync command (for example with sudo)
                 'rsync',
                 category.get('args', global_args), # args passed to rsync
                 path,
                 location]), shell = True)

    for category in config.categories:
        backup_category(category)


if __name__ == "__main__":
    backup()
