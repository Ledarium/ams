#!/usr/bin/env python3
from subprocess import call
from pathlib import Path
from datetime import datetime
from logging import debug, info
import config


def backup():
    # preparations
    date = datetime.now().strftime("%d-%m-%y.%H:%M:%S")
    backup_path = Path(config.backup_path).expanduser()
    debug("Backup_path is set to " + str(backup_path))
    if not backup_path.is_dir():
        backup_path.mkdir()
    backup_location = backup_path / date
    backup_location.mkdir()
    debug("Current backup will be saved in " + str(backup_location))
    if config.rsync_args:
        global_args = config.rsync_args
    else:
        global_args == "--progress"

    def backup_files(category):
        debug("Backing up category " + category['name'])
        location = backup_location / category['folder']
        location.mkdir(exist_ok=True)
        location = str(location)
        for path in category['paths']:
            call(' '.join([
                category.get('prefix', ''),
                'rsync',
                category.get('args', global_args),
                path,
                location]),
                shell=True)
        info("Sucessfully backed up category " + category['name'])

    for category in config.backup:
        backup_files(category)

    def backup_packages():
        debug("Starting packagelist backup")
        location = backup_location / "pkglist.txt"
        debug("Pkglist goes to " + str(location))
        call(' '.join([
            config.package_utility,
            '-Qqe >',
            str(location)]),
            shell=True)
        info("Package list backed up")

    backup_packages()
