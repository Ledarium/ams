from utility import launch
from logging import info


def update(actions, util):
    for action in actions:
        info('Performing '+action['name'])
        launch([util, action['flags']])
