from subprocess import call
from os import chdir
from logging import debug, info
import config


def archive(path):
    chdir(path)
    exec_string = ' '.join([
        'tar',
        config.tar_args,
        "backup.tar.xz",
        "*"])
    debug(exec_string)
    call(exec_string, shell=True)
