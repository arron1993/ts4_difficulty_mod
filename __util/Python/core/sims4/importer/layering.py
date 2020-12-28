# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: T:\InGame\Gameplay\Scripts\Core\sims4\importer\layering.py
# Compiled at: 2013-11-06 00:41:02
# Size of source mod 2**32: 1616 bytes
import caches, paths, sims4.log
logger = sims4.log.Logger('Layering')

@caches.cached
def _get_file_layer(filename):
    if paths.LAYERS is not None:
        for i, v in enumerate(paths.LAYERS):
            if filename.startswith(v):
                return i


def check_import(initiating_file, target_file):
    if initiating_file is None or target_file is None or paths.IS_ARCHIVE:
        return
    initiating_layer = _get_file_layer(initiating_file)
    target_layer = _get_file_layer(target_file)
    if initiating_layer is None or target_layer is None:
        return
    if target_layer > initiating_layer:
        logger.error('LAYERING VIOLATION:\n  {}\nimports\n  {}\n\nThings in\n  {}\\*\nshould not import from\n  {}\\*', initiating_file, target_file, paths.LAYERS[initiating_layer], paths.LAYERS[target_layer])