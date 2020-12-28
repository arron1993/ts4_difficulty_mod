# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\interactions\utils\content_score_mixin.py
# Compiled at: 2020-07-30 20:59:06
# Size of source mod 2**32: 12582 bytes
from relationships.relationship_bit import SocialContextBit, RelationshipBit
from sims4.tuning.tunable import Tunable, TunableMapping, TunableReference, TunableSet, OptionalTunable, TunableTuple, TunableInterval, TunableSimMinute
from sims4.tuning.tunable_base import GroupNames
from traits.traits import Trait
import services, sims4.log, sims4.resources
logger = sims4.log.Logger('ContentScoreMixin', default_owner='msantander')

class ContentScoreMixin:
    INSTANCE_TUNABLES = {'content_score': OptionalTunable(description='\n            If enabled, the interaction will be scored.\n            Otherwise, scoring will be ignored.\n            ',
                        tunable=TunableTuple(base_score=Tunable(description=' \n                    Base score when determining the content set value of any interaction. \n                    This is the base value used before any modification to content score.\n            \n                    Modification to the content score for this interaction can come from\n                    topics and moods.\n            \n                    USAGE: If you would like this mixer to more likely show up no\n                    matter the topic and mood ons the sims tune this value higher.\n                                            \n                    Formula being used to determine the autonomy score is Score =\n                    Avg(Uc, Ucs) * W * SW, Where Uc is the commodity score, Ucs is the\n                    content set score, W is the weight tuned the on mixer, and SW is\n                    the weight tuned on the super interaction.\n                    ',
                        tuning_group=(GroupNames.AUTONOMY),
                        tunable_type=int,
                        default=0),
                        social_context_preference=TunableMapping(description='\n                    A mapping of social contexts that will adjust the content score for\n                    this interaction. This is used conjunction with base_score.\n                    ',
                        tuning_group=(GroupNames.AUTONOMY),
                        key_type=SocialContextBit.TunableReference(pack_safe=True),
                        value_type=Tunable(tunable_type=float,
                        default=0)),
                        relationship_bit_preference=TunableMapping(description='\n                    A mapping of relationship bits that will adjust the content score\n                    for this interaction. This is used conjunction with\n                    base_score.\n                    ',
                        tuning_group=(GroupNames.AUTONOMY),
                        key_type=RelationshipBit.TunableReference(pack_safe=True),
                        value_type=Tunable(tunable_type=float,
                        default=0)),
                        relationship_bit_collection_preference=TunableMapping(description='\n                    A mapping of relationship bit collections that will adjust the content score\n                    for this interaction. This is used conjunction with\n                    base_score.\n                    \n                    The distinction between this and relationship_bit_preference is that\n                    this is specifically meant to support relationship bit collections, and \n                    relationship_bit_preference is for individual bits.\n                    ',
                        tuning_group=(GroupNames.AUTONOMY),
                        key_type=TunableReference((services.relationship_bit_manager()),
                        pack_safe=True),
                        value_type=Tunable(tunable_type=float,
                        default=0)),
                        trait_preference=TunableMapping(description='\n                    A mapping of traits that will adjust the content score for\n                    this interaction. This is used conjunction with base_score.\n                    ',
                        tuning_group=(GroupNames.AUTONOMY),
                        key_type=Trait.TunableReference(pack_safe=True),
                        value_type=Tunable(tunable_type=float,
                        default=0)),
                        buff_preference=TunableMapping(description='\n                    A mapping of buffs that will adjust the content score for\n                    this interaction. This is used in conjunction with base_score.\n                    ',
                        tuning_group=(GroupNames.AUTONOMY),
                        key_type=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.BUFF)),
                        pack_safe=True),
                        value_type=Tunable(tunable_type=float,
                        default=0)),
                        buff_target_preference=TunableMapping(description='\n                    A mapping of buffs on the target that will adjust the \n                    content score for this interaction. This is used in conjunction \n                    with base_score.\n                    Preferably, this will be combined with buff_preference\n                    and merged with a participant type.\n                    ',
                        tuning_group=(GroupNames.AUTONOMY),
                        key_type=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.BUFF)),
                        pack_safe=True),
                        value_type=Tunable(tunable_type=float,
                        default=0)),
                        test_gender_preference=Tunable(description='\n                    If this is set, a gender preference test will be run between \n                    the actor and target sims. If it fails, the social score will be\n                    modified by a large negative penalty tuned with the tunable:\n                    GENDER_PREF_CONTENT_SCORE_PENALTY\n                    ',
                        tuning_group=(GroupNames.AUTONOMY),
                        tunable_type=bool,
                        default=False),
                        topic_preferences=TunableSet(description=' \n                    A set of topics that will increase the content score for this \n                    interaction.  If a sim has a topic that exist in this\n                    set, a value tuned in that topic will increase the content\n                    score.  This is used conjunction with base_score.\n                    ',
                        tunable=TunableReference(description='\n                        The Topic this interaction gets bonus score for. Amount of\n                        score is tuned on the Topic.\n                        ',
                        manager=(services.get_instance_manager(sims4.resources.Types.TOPIC))),
                        tuning_group=(GroupNames.AUTONOMY)),
                        mood_preference=TunableMapping(description="\n                    A mapping of moods that will adjust the content score for this \n                    interaction.  If sim's mood exist in this mapping, the\n                    value mapped to mood will add to the content score.  This is\n                    used conjunction with base_score.\n                    ",
                        key_type=TunableReference(manager=(services.get_instance_manager(sims4.resources.Types.MOOD))),
                        value_type=Tunable(tunable_type=float,
                        default=0),
                        tuning_group=(GroupNames.AUTONOMY)),
                        front_page_cooldown=OptionalTunable(description='\n                    If Enabled, when you run this mixer, it will get a penalty\n                    applied to the front page score of this interaction for a tunable\n                    amount of time. If The interaction is run more than once, the\n                    cooldown will be re-applied, and the penalty will stack making\n                    the mixer less likely to be on the front page as you execute it\n                    more.\n                    ',
                        tunable=TunableTuple(interval=TunableInterval(description='\n                            Time in minutes until the penalty on the front page score\n                            expires.\n                            ',
                        tunable_type=TunableSimMinute,
                        default_lower=1,
                        default_upper=1,
                        minimum=0),
                        penalty=Tunable(description='\n                            For the duration of the tuned interval, this penalty\n                            will be applied to the score used to determine which\n                            interactions are visible on the front page of the pie\n                            menu. The higher this number, the less likely it will\n                            be to see the interaction at the top level.\n                            ',
                        tunable_type=int,
                        default=0)),
                        tuning_group=(GroupNames.AUTONOMY))),
                        enabled_by_default=True)}

    @classmethod
    def get_base_content_set_score(cls, **kwargs):
        return cls.content_score.base_score

    @classmethod
    def get_content_score(cls, sim, resolver, internal_aops, gsi_logging=None, **kwargs):
        if cls.content_score is None:
            return 0
        else:
            base_score = (cls.get_base_content_set_score)(**kwargs)
            if sim is None:
                logger.error('Sim is None when trying to get content score for {}', cls)
                return base_score
                buff_score_adjustment = sim.get_actor_scoring_modifier(cls, resolver)
                topic_score = sum((topic.score_for_sim(sim) for topic in cls.content_score.topic_preferences))
                score_modifier = sum((cls.get_score_modifier(sim, internal_aop.target) for internal_aop in internal_aops))
                front_page_cooldown_penalty = sim.get_front_page_penalty(cls)
                club_service = services.get_club_service()
                if club_service is not None:
                    club_rules_modifier = sum((club_service.get_front_page_bonus_for_mixer(sim.sim_info, aop) for aop in internal_aops))
            else:
                club_rules_modifier = 0
        total_score = base_score + buff_score_adjustment + topic_score + score_modifier + front_page_cooldown_penalty + club_rules_modifier
        if gsi_logging is not None:
            if cls not in gsi_logging:
                gsi_logging[cls] = {}
            gsi_logging[cls]['scored_aop'] = str(cls)
            gsi_logging[cls]['base_score'] = base_score
            gsi_logging[cls]['buff_score_adjustment'] = buff_score_adjustment
            gsi_logging[cls]['topic_score'] = topic_score
            gsi_logging[cls]['score_modifier'] = score_modifier
            gsi_logging[cls]['total_score'] = total_score
        return total_score