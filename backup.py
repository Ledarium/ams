from logging import debug, info
from utility import expanded_path, launch


def file_backup(backup_location, rsync_args, tasklist):
    debug("Backup_location is set to " + str(backup_location))
    if not backup_location.is_dir():
        backup_location.mkdir()
    info("Current backup will be saved in " + str(backup_location))

    def backup_files(task):
        debug("Backing up task " + task['name'])
        parent = task.get('relative_to', None)
        task_location = backup_location / expanded_path(task['folder'])
        task_location.mkdir()
        if parent:  # expanded_path is relative
            parent = expanded_path(parent)

        for source in task['paths']:
            if parent:
                location = task_location \
                    / expanded_path(source).parent
                source = parent / expanded_path(source)
            else:
                source = expanded_path(source)
                location = task_location \
                    / expanded_path(source).parent.relative_to('/')
                location.mkdir(parents=True, exist_ok=True)
            debug("source {0} goes to {1}".format(source, location))
            launch([task.get('prefix', ''),
                    'rsync',
                    task.get('args', rsync_args),
                    str(source),
                    str(location)])
        info("Sucessfully backed up task " + task['name'])

    for task in tasklist:
        backup_files(task)


def pkglist_backup(backup_location, utility):
    debug("Starting packagelist backup")
    location = backup_location / "pkglist.txt"
    backup_location.mkdir()
    debug("Pkglist goes to " + str(location))
    launch([utility,
            '-Qqe >',
            str(location)])
    info("Package list backed up")
