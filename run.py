#!/usr/bin/env python3
from backup import backup
from update import update
from archive import archive
from argparse import ArgumentParser
from logging import DEBUG, INFO, basicConfig, debug, info

parser = ArgumentParser(
    description="ams - utility to backup and maintain your Arch"
)
parser.add_argument("-v", "--verbose",
                    help="show verbose output",
                    action="store_true")
parser.add_argument("-b", "--backup",
                    help="do not perform backup",
                    action="store_true")
parser.add_argument("-u", "--update",
                    help="do not perdorm update",
                    action="store_true")
parser.add_argument("-a", "--archive",
                    help="do not perform archiving",
                    action="store_true")
parser.add_argument("-s", "--silent",
                    help="NOT IMPLEMENTED be silent (use with carefulness)",
                    action="store_true")
args = parser.parse_args()

# setting logging
if args.verbose:
    basicConfig(level=DEBUG)
else:
    basicConfig(level=INFO,
                format="%(message)s")

if not args.backup:
    info("Launching backup")
    path = backup()
else:
    info("Skipping backup...")
if not args.archive:
    info("Launching archiving")
    archive(path)
else:
    info("Skipping archiving...")

if not args.update:
    info("Launching update")
    update()
else:
    info("Skipping update...")
info("We are done, thank you.")
