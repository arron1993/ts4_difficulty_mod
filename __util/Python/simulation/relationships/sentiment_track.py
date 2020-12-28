# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\relationships\sentiment_track.py
# Compiled at: 2020-07-31 21:50:05
# Size of source mod 2**32: 3718 bytes
from interactions.utils.loot import LootActions
from relationships.relationship_track import RelationshipTrack
from relationships.relationship_enums import SentimentDurationType
from relationships.relationship_enums import SentimentSignType
from relationships.relationship_enums import RelationshipTrackType
from relationships.tunable import SentimentRelationshipTrackData
from sims4.localization import TunableLocalizedString
from sims4.tuning.instances import lock_instance_tunables
from sims4.tuning.tunable import TunableList, TunableEnumEntry
from sims4.tuning.tunable_base import GroupNames
from sims4.utils import classproperty
from tunable_multiplier import TunableMultiplier

class SentimentTrack(RelationshipTrack):
    INSTANCE_TUNABLES = {'duration':TunableEnumEntry(description='\n            The duration of this sentiment. Must be either long or short type.  \n            ',
       tunable_type=SentimentDurationType,
       default=SentimentDurationType.INVALID,
       invalid_enums=(
      SentimentDurationType.INVALID,)), 
     'sign':TunableEnumEntry(description='\n            The sign of this sentiment. Must be either positive or negative \n            type.  \n            ',
       tunable_type=SentimentSignType,
       default=SentimentSignType.INVALID,
       invalid_enums=(
      SentimentDurationType.INVALID,)), 
     'archetype_name':TunableLocalizedString(description='\n            The localized archetype name for this sentiment.\n            Eg: hurt/ecstatic/glad  \n            '), 
     'loot_on_proximity':TunableList(description='\n            A list of loot actions that will be applied to the subject Sim if \n            the subject sim comes in proximity of the target sim, and the \n            subject sim is not in a cooldown period for the target sim.\n            Resolver Participants:\n            actor - sim owning the sentiment\n            target - target of the sentiment\n            ',
       tunable=LootActions.TunableReference(description='\n                A loot action applied to the subject Sim.\n                ',
       tuning_group=(GroupNames.SENTIMENT_LOOT))), 
     'proximity_loot_chance_weight':TunableMultiplier.TunableFactory(description='\n            The random weight for this loot to be applied when in proximity of \n            a sim that this sim has a sentiment towards.\n            Resolver Participants:\n            actor - sim owning the sentiment\n            target - target of the sentiment\n            ',
       tuning_group=GroupNames.SENTIMENT_LOOT)}

    @classproperty
    def track_type(cls):
        return RelationshipTrackType.SENTIMENT

    def build_single_relationship_track_proto(self, relationship_track_update):
        super().build_single_relationship_track_proto(relationship_track_update)
        relationship_track_update.track_type = RelationshipTrackType.SENTIMENT
        relationship_track_update.sign_type = self.sign
        relationship_track_update.duration_type = self.duration
        relationship_track_update.archetype_name = self.archetype_name


lock_instance_tunables(SentimentTrack, bit_data_tuning=SentimentRelationshipTrackData,
  _add_bit_on_threshold=None,
  display_priority=1)