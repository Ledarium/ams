from pathlib import Path
from os import path
from subprocess import call
from datetime import datetime
import config as userconfig
from logging import debug


def expanded_path(string):  # It's pretty shitty, I know.
    return Path(path.expandvars(path.expanduser(string)))


def date(formatstring="%d-%m-%y.%H:%M:%S"):
    return datetime.now().strftime(formatstring)


config = userconfig  # TODO make default config values


def launch(args):
    exec_string = ' '.join(args)
    debug('Executing '+exec_string)
    call(exec_string, shell=True)
