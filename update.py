from subprocess import call
import config


def update():
    for action in config.update:
        call(' '.join([config.package_utility,
                       action['flags']]),
             shell=True)
