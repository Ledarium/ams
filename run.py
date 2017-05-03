#!/usr/bin/env python3
from backup import backup
from update import update
from argparse import ArgumentParser
from logging import DEBUG, basicConfig, debug

parser = ArgumentParser(
    description="ams - utility to backup and maintain your Arch"
)
parser.add_argument("-v", "--verbose", help="show verbose output",
                    action="store_true")
parser.add_argument("-b", "--backup", help="perform backup",
                    action="store_true")
parser.add_argument("-s", "--silent", help="be silent",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    basicConfig(level=DEBUG)

backup()
