#!/usr/bin/env python3
from subprocess import call, Popen, PIPE
from shlex import split
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
    rsync_args = config.rsync_args;
    if not rsync_args:
        rsync_args == "--progress"
    if config.verbose_mode:
        print("Current backup will be saved in", backup_location)

    print("Backing up user configs")
    for path in config.user_configs:
        path = Path.home() / path
        args = rsync_args.split()
        call(['rsync',
              *args,
              str(path),
              str(backup_location)])

    print("Backing up system configs")
    for path in config.system_configs:
        args = rsync_args.split()
        call(['sudo', 'rsync',
              *args,
              str(path),
              str(backup_location)])

    print("Backing up other paths")
    for path in config.system_configs:
        args = rsync_args.split()
        call(['rsync',
              *args,
              str(path),
              str(backup_location)])

if __name__ == "__main__":
    backup()
