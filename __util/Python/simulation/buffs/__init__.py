# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\buffs\__init__.py
# Compiled at: 2015-12-09 22:13:40
# Size of source mod 2**32: 729 bytes
import enum

class BuffPolarity(enum.Int):
    NEUTRAL = 0
    NEGATIVE = 1
    POSITIVE = 2


class Appropriateness(enum.Int, export=False):
    DONT_CARE = (0, )
    NOT_ALLOWED = (1, )
    ALLOWED = (2, )