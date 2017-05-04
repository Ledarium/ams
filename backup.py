from subprocess import call
from pathlib import Path
from os import path
from datetime import datetime
from logging import debug, info
import config


def expanded_path(string):  # It's pretty shitty, I know.
    return Path(path.expandvars(path.expanduser(string)))


def backup():
    # preparations
    date = datetime.now().strftime("%d-%m-%y.%H:%M:%S")
    backup_path = expanded_path(config.backup_path)
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
        parent = category.get('relative_to', None)
        category_location = backup_location / expanded_path(category['folder'])
        category_location.mkdir()
        if parent:  # path is relative
            parent = expanded_path(parent)

        for source in category['paths']:
            if parent:
                location = category_location \
                    / expanded_path(source).parent
                source = parent / expanded_path(source)
            else:
                source = expanded_path(source)
                location = category_location \
                    / expanded_path(source).parent.relative_to('/')
                location.mkdir(parents=True, exist_ok=True)
            debug("source {0} goes to {1}".format(source, location))
            exec_string = ' '.join([
                category.get('prefix', ''),
                'rsync',
                category.get('args', global_args),
                str(source),
                str(location)])
            debug(exec_string)
            call(exec_string, shell=True)
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
    return(backup_location)
