#!/usr/bin/env python3
from backup import file_backup, pkglist_backup
from archive import archive
from argparse import ArgumentParser
from logging import DEBUG, INFO, basicConfig, debug, info
from utility import config, date, expanded_path

parser = ArgumentParser(
    description="lbs - utility to easily backup your files"
)
parser.add_argument("-v", "--verbose",
                    help="show verbose output",
                    action="store_true")
parser.add_argument("-b", "--nobackup",
                    help="do not perform backup",
                    action="store_true")
parser.add_argument("-u", "--noupdate",
                    help="do not perform update",
                    action="store_true")
parser.add_argument("-p", "--nopkglist",
                    help="do not backup pkglist",
                    action="store_true")
parser.add_argument("-a", "--noarchive",
                    help="do not perform archiving",
                    action="store_true")
'''
parser.add_argument("-s", "--silent",
                    help="NOT IMPLEMENTED be silent (use with carefulness)",
                    action="store_true")
'''
args = parser.parse_args()

# setting logging
if args.verbose:
    basicConfig(level=DEBUG)
else:
    basicConfig(level=INFO,
                format="%(message)s")

debug(args)
current_date = date()
debug(config.backup['path'])
debug(current_date)
path = expanded_path(config.backup['path']) / current_date

if config.backup and not args.nobackup:
    info("Launching backup")
    file_backup(path,
                config.backup['rsync_args'],
                config.backup['tasklist'])
else:
    info("Skipping backup...")

if config.backup['backup_pkglist'] and not args.nopkglist:
    info("Backing up package list")
    pkglist_backup(path, config.system['utility'])
else:
    info("Skipping package list backup...")

if config.archive and not args.noarchive:
    info("Launching archiving")
    archive(path, current_date, config.archive['tar_args'])
else:
    info("Skipping archiving...")

info("We are done, thank you.")
