# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\interactions\utils\__init__.py
# Compiled at: 2018-10-22 23:23:09
# Size of source mod 2**32: 636 bytes
import enum

class LootType(enum.Int, export=False):
    SITUATION = 1
    RELATIONSHIP = 2
    SKILL = 3
    SIMOLEONS = 4
    GENERIC = 6
    RELATIONSHIP_BIT = 7
    TEAM_SCORE = 8
    GAME_OVER = 9
    GAME_SETUP = 10
    PARTY_AFFINITY = 11
    LIFE_EXTENSION = 12
    TAKE_TURN = 13
    ACTIONS = 14
    GAME_RESET = 15
    DISCOVER_CLUE = 16
    NEW_CRIME = 17
    SCHEDULED_DELIVERY = 18