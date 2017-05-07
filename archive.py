from os import chdir
from utility import launch


def archive(path, date, tar_args):
    archive_name = '"./'+date+'.tar.xz"'
    chdir(path)
    launch([ 'tar',
            tar_args,
            archive_name,
            "*"])
