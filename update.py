from subprocess import call
import config


def update():
    for action in config.update:
         call(' '.join([action['command'], action['flags']]),
             shell=True)
