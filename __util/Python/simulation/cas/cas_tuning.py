# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: T:\InGame\Gameplay\Scripts\Server\cas\cas_tuning.py
# Compiled at: 2020-10-20 21:05:58
# Size of source mod 2**32: 35004 bytes
from cas.cas_enums import CASPaintPose, CASMode, CASMenuState, CASRandomizeFlag, SimRegion, CASBrandedLogoBackground, CASEditMode, CASSkinToneType
from interactions.utils.tunable_icon import TunableIcon
from sims.occult.occult_enums import OccultType
from sims.outfits.outfit_enums import BodyType
from sims.sim_info_types import SpeciesExtended, Age, Gender
from sims4.common import Pack
from sims4.localization import TunableLocalizedStringFactory, TunableLocalizedString
from sims4.resources import Types
from sims4.tuning.instances import HashedTunedInstanceMetaclass
from sims4.tuning.tunable import TunableEnumEntry, TunableTuple, TunableList, TunableMapping, HasTunableReference, Tunable, TunableVariant, TunablePackSafeReference, OptionalTunable, TunableEnumSet, TunableEnumFlags, TunableSet, TunableResourceKey, TunableReference, TunableRange
from sims4.tuning.tunable_base import ExportModes, GroupNames, EnumBinaryExportType
from tag import TunableTag, TunableTags
from tutorials.tutorial_tip import TutorialTipUiElement
import enum, services, sims4

class CASContextCriterion(TunableVariant):

    def __init__(self, **kwargs):
        (super().__init__)(species=TunableEnumSet(description="\n                Compare the current sim's species with this list.\n                ",
  enum_type=SpeciesExtended,
  enum_default=(SpeciesExtended.HUMAN),
  invalid_enums=(
 SpeciesExtended.INVALID,)), 
         age=TunableEnumSet(description="\n                Compare the current sim's age with this list.\n                ",
  enum_type=Age,
  enum_default=(Age.YOUNGADULT)), 
         gender=TunableEnumSet(description="\n                Compare the current sim's gender with this list.\n                ",
  enum_type=Gender,
  enum_default=(Gender.MALE)), 
         occult_type=TunableEnumFlags(description="\n                Compare the current sim's occult type with this list.\n                ",
  enum_type=OccultType,
  default=(OccultType.HUMAN)), 
         active_occult_form=TunableEnumFlags(description="\n                Compare the current sim's active occult form with this list.\n                (This is only if the sim has an occult form active.)\n                ",
  enum_type=OccultType,
  default=(OccultType.HUMAN)), 
         in_genetics_mode=Tunable(description='\n                Check if genetics mode is currently active.\n                ',
  tunable_type=bool,
  default=False), 
         is_mannequin=Tunable(description='\n                Check if the current sim is a mannequin.\n                ',
  tunable_type=bool,
  default=False), 
         is_new_sim=Tunable(description='\n                Check if this is a newly-made sim.\n                ',
  tunable_type=bool,
  default=False), 
         is_full_edit_mode=Tunable(description='\n                Check if full edit mode is enabled for the sim.\n                ',
  tunable_type=bool,
  default=False), 
         is_direct_manip_enabled=Tunable(description='\n                Check if direct manip is enabled for the sim.\n                ',
  tunable_type=bool,
  default=False), 
         has_paint_layer=Tunable(description='\n                Check if the current sim has a paint layer present.\n                Note: This is currently only valid for pets.\n                ',
  tunable_type=bool,
  default=False), 
         allowed_packs=TunableEnumSet(description='\n                Will only be allowed for packs in this list.\n                ',
  enum_type=Pack,
  enum_default=(Pack.BASE_GAME)), **kwargs)


class CASContextCriterionList(TunableList):

    def __init__(self, **kwargs):
        (super().__init__)(tunable=TunableTuple(criterion=CASContextCriterion(description='\n                    An element of CAS state to match against.\n                    '),
                    exclude_if_matched=Tunable(description='\n                    Whether the item this criteria applies to should be excluded\n                    instead of included if this criteria is satisfied.\n                    ',
                    tunable_type=bool,
                    default=False),
                    export_class_name='CASContextCriterionListEntry'), **kwargs)


class CASContextCriteria(TunableTuple):

    def __init__(self, **kwargs):
        (super().__init__)(match_any=CASContextCriterionList(description='\n                Any criteria in this list can be matched to consider this\n                collection of criteria satisfied. Any criteria in match_all\n                must also be matched.\n                '), 
         match_all=CASContextCriterionList(description='\n                All criteria in this list must be matched to consider this\n                collection of criteria satisfied.\n                '), **kwargs)


class CASMenuItemIconSet(TunableTuple):

    def __init__(self, description='', **kwargs):
        (super().__init__)(default_icon=TunableIcon(description='\n                Icon to display for this menu item.\n                '), 
         selected_icon=TunableIcon(description='\n                Icon to use for the selected state of the item.\n                If not specified, will fall back to the default icon.\n                ',
  allow_none=True), 
         new_content_icon=TunableIcon(description='\n                Icon to use when there is new content related to this item.\n                If not specified, will fall back to the default icon.\n                ',
  allow_none=True), 
         description=description, **kwargs)


class CASMenuItem(metaclass=HashedTunedInstanceMetaclass, manager=services.get_instance_manager(Types.CAS_MENU_ITEM)):

    class RemoveActions(enum.Int):
        DISALLOW_REMOVAL = 0
        REMOVE_PART = 1
        REMOVE_PAINT_LAYER = 2

    INSTANCE_TUNABLES = {'icons':CASMenuItemIconSet(description='\n            Default icons to use for the menu item.\n            ',
       tuning_group=GroupNames.UI,
       export_modes=ExportModes.ClientBinary), 
     'icon_overrides':TunableList(description='\n            List of possible overrides for the icons for this menu item.\n            Each override will be evaluated in the order listed, the last\n            override to satisfy its criteria will be used.\n            ',
       tunable=TunableTuple(override_criteria=CASContextCriterionList(description='\n                    Criteria to determine when this set of icons should be used.\n                    '),
       icons=CASMenuItemIconSet(description='\n                    Icons to use instead of the default icons.\n                    Note that you must specify all the desired icons here, even\n                    if they differ from the defaults.  For example, if you wish\n                    to only override the selected icon, you still need to specify\n                    the default icon here as well.\n                    '),
       export_class_name='CASMenuItemIconOverride'),
       export_modes=ExportModes.ClientBinary,
       tuning_group=GroupNames.UI), 
     'name':TunableLocalizedStringFactory(description='\n            Item name\n            ',
       export_modes=ExportModes.ClientBinary,
       tuning_group=GroupNames.UI), 
     'actions':TunableTuple(description='\n            Actions to perform when this menu item is selected.\n            ',
       change_menu_state=OptionalTunable(TunableTuple(description='\n                MenuState to change into. This value must be supported by the\n                code, so this will most likely be provided by an engineer.\n                To be deprecated.  It is part of the old system.\n                ',
       menu_type=TunableEnumEntry(tunable_type=(CASMenuState.MenuType),
       default=(CASMenuState.MenuType.NONE)),
       menu_mode=TunableEnumEntry(tunable_type=(CASMenuState.MenuMode),
       default=(CASMenuState.MenuMode.NONE)),
       menu_section=TunableEnumEntry(tunable_type=(CASMenuState.MenuSection),
       default=(CASMenuState.MenuSection.NONE)),
       menu_item=TunableEnumEntry(tunable_type=(CASMenuState.MenuItem),
       default=(CASMenuState.MenuItem.NONE)),
       export_class_name='CASMenuState')),
       display_ui_widget=OptionalTunable(Tunable(description='\n                Name of a UI widget that should be shown when this item is selected.\n                ',
       tunable_type=str,
       default='')),
       export_class_name='CASMenuItemActions',
       export_modes=ExportModes.ClientBinary), 
     'remove_action':TunableEnumEntry(description='\n            What action to perform when the remove button is clicked, if present.\n            ',
       tunable_type=RemoveActions,
       default=RemoveActions.REMOVE_PART,
       export_modes=ExportModes.ClientBinary), 
     'audio_component_name':Tunable(description='\n            Optional name to associate with this item for the UI audio system.\n            ',
       tunable_type=str,
       default='',
       allow_empty=True,
       tuning_group=GroupNames.UI,
       export_modes=ExportModes.ClientBinary), 
     'disable_reasons':TunableList(description='\n            List of possible conditions under which this menu item should appear disabled.\n            ',
       tunable=TunableTuple(criteria=CASContextCriterionList(description='\n                    Criteria which defines when this menu item should be disabled for\n                    the given reason.\n                    '),
       reason=TunableLocalizedStringFactory(description='\n                    The reason for disabling this menu item.\n                    '),
       export_class_name='CASMenuItemDisableReason'),
       tuning_group=GroupNames.UI,
       export_modes=ExportModes.ClientBinary), 
     'sim_click_activations':TunableList(description='\n            Defines a list of areas on the sim that when clicked should cause\n            this menu item to become selected.\n            ',
       tunable=TunableTuple(criteria=CASContextCriteria(description='\n                    Criteria to determine if this click source should be enabled.\n                    '),
       click_source=TunableVariant(description='\n                    The possible areas on which a sim might be clicked.\n                    \n                    Note: Clothing is only a valid option for pet sims.\n                    ',
       locked_args={'clothing': True},
       body_types=TunableEnumSet(description='\n                        Areas corresponding to sim BodyTypes.\n                        ',
       enum_type=BodyType,
       enum_default=(BodyType.NONE)),
       sim_regions=TunableEnumSet(description='\n                        Areas corresponding to SimRegions.\n                        ',
       enum_type=SimRegion,
       enum_default=(SimRegion.INVALID))),
       export_class_name='CASMenuItemSimClickActivation'),
       export_modes=ExportModes.ClientBinary), 
     'part_tags':TunableSet(description='\n            Tags to use for what parts to include in the displayed catalog.\n            (09/26/2017 - Currently only one tag is supported but will be expanded to multiple later.)\n            ',
       tunable=TunableTag(),
       maxlength=1,
       export_modes=ExportModes.ClientBinary)}


class CASMenu(HasTunableReference, metaclass=HashedTunedInstanceMetaclass, manager=services.get_instance_manager(Types.CAS_MENU)):
    INSTANCE_TUNABLES = {'cas_mode':TunableEnumEntry(description='\n            The CAS mode for which this menu should be used.\n            ',
       tunable_type=CASMode,
       default=CASMode.BODY,
       export_modes=ExportModes.ClientBinary), 
     'criteria':CASContextCriteria(description='\n            List of criteria to determine when this menu should be used.\n            If more than one menu has its criteria met, the menu with the larger\n            number of criteria will be used.\n            ',
       export_modes=ExportModes.ClientBinary), 
     'items':TunableList(description='\n            List of menu items.\n            ',
       tunable=TunableTuple(description='\n                A menu item and its inclusion (and/or exclusion) criteria.\n                ',
       criteria=CASContextCriteria(description='\n                    Include this item in the list of available menu items when all specified\n                    criteria are met.  If no criteria are defined, this item is always included.\n                    '),
       item=TunablePackSafeReference(description='\n                    Reference to a menu item for inclusion in this list.\n                    ',
       manager=(services.get_instance_manager(Types.CAS_MENU_ITEM))),
       sub_items=TunableList(description='\n                    Show the sub-menu, including this list of items.\n                    ',
       tunable=TunableTuple(description='\n                        A sub-menu item and its inclusion (and/or exclusion) criteria.\n                        ',
       criteria=CASContextCriteria(description='\n                            Include this item in the list of available menu items when all specified\n                            criteria are met.  If no criteria are defined, this item is always included.\n                            '),
       item=TunablePackSafeReference(description='\n                            Reference to a menu item for inclusion in this list.\n                            ',
       manager=(services.get_instance_manager(Types.CAS_MENU_ITEM))),
       export_class_name='CASSubMenuEntry')),
       export_class_name='CASMenuEntry'),
       export_modes=ExportModes.ClientBinary)}


class CASAddSimAction(enum.Int):
    ACTION_NONE = 0
    ACTION_CATEGORY = 1
    ACTION_ADD_SIM = 2
    ACTION_GENETICS = 3
    ACTION_GALLERY = 4
    ACTION_LIBRARY = 5
    ACTION_STORY = 6


class CASStoriesTuning:
    CAS_STORIES = TunableTuple(description='\n            Tuning for the CAS Stories sim-creation flow.\n            ',
      questions_per_pack=TunableMapping(description='\n                Mapping between the number of packs available and the number of\n                base game questions and questions per pack that should be asked.\n                ',
      key_type=Tunable(description='\n                    The number of available packs.\n                    ',
      tunable_type=int,
      default=0),
      value_type=TunableTuple(description='\n                    The number of questions that should be asked.\n                    ',
      base_game_questions=Tunable(description='\n                        The number of base game questions to ask.\n                        ',
      tunable_type=int,
      default=0),
      per_pack_questions=Tunable(description='\n                        The number of pack questions to ask per pack.\n                        ',
      tunable_type=int,
      default=0),
      export_class_name='CasStoriesQuestionCountTuple'),
      tuple_name='CasStoriesQuestionsPerPackKeyValue'),
      funds_traits=TunableMapping(description='\n                Mapping between specific traits and the amount of starting\n                household funds to give to a sim with that trait.\n                ',
      key_type=TunableReference(description='\n                    Reference to the trait.\n                    ',
      manager=(services.get_instance_manager(Types.TRAIT))),
      value_type=Tunable(description='\n                    The household starting funds.\n                    ',
      tunable_type=int,
      default=0),
      tuple_name='CasStoriesFundsPerTraitKeyValue'),
      additional_sims_funds_percentage=TunableRange(description='\n                If additional CAS Stories sims are added to a household, this is\n                the percentage of their normal funding to add to the household\n                funds as additonal funding. For instance, if we have 1 sim with\n                a 10,000 simoleon trait and a second sim with a 5,000 simoleon\n                trait and this is tuned to .5, the resulting household income\n                would be 10,000 + .5 * 5,000 = 12,500.\n                ',
      tunable_type=float,
      default=0.75,
      minimum=0,
      maximum=1),
      silouetted_sim_info=TunableResourceKey(description='\n                The SimInfo file to use for the silouetted sim in CAS Stories.\n                ',
      default=None,
      resource_types=(
     sims4.resources.Types.SIMINFO,)),
      export_modes=(ExportModes.ClientBinary),
      export_class_name='CasStoriesTuning')


class CASTuning:
    CAS_SKINTONE_TYPE_FILTERS = TunableList(description='\n        A list of skin tone type buttons data for its filtering\n        ',
      tunable=TunableTuple(description='\n            Tuning for branded logo to use.\n            ',
      skintone_type=TunableEnumEntry(description='\n                type to filter by\n                ',
      tunable_type=CASSkinToneType,
      default=(CASSkinToneType.ALL)),
      icon=TunableIcon(description='\n                Icon to be displayed on the item\n                '),
      icon_selected=TunableIcon(description='\n                Icon to be displayed on the item when selected\n                '),
      tooltip=TunableLocalizedString(description='\n                Localized name of this type.\n                '),
      export_class_name='CasSkinToneTypesEntry'),
      export_modes=(ExportModes.ClientBinary))
    CAS_BRANDED_TAG_DATA = TunableList(description='\n        A list of CAS tag to data used to show a branded logo on the item\n        ',
      tunable=TunableTuple(description='\n            Tuning for branded logo to use.\n            ',
      tag=TunableTag(description='\n                Tag to use for the brand to be displayed\n                '),
      icon=TunableIcon(description='\n                Icon to be displayed on the item\n                '),
      background_type=TunableEnumEntry(description='\n                Background to be used for it\n                ',
      tunable_type=CASBrandedLogoBackground,
      default=(CASBrandedLogoBackground.LIGHT)),
      export_class_name='CasBrandedTagEntry'),
      export_modes=(ExportModes.ClientBinary))
    CAS_SPECIES_PAINT_POSES = TunableMapping(description='\n        A mapping of species type to data that is required for the paint pose ui\n        ',
      key_type=TunableEnumEntry(description='\n            The species type that this entry applies to.\n            ',
      tunable_type=SpeciesExtended,
      default=(SpeciesExtended.HUMAN),
      invalid_enums=(
     SpeciesExtended.INVALID,)),
      value_type=TunableList(description='\n            A list of CasPaintPostTuples\n            ',
      tunable=TunableTuple(description='\n                Data required for each UI Paint pose button.\n                ',
      icon=TunableIcon(description='\n                    Icon to be displayed on the button for the pose\n                    ',
      tuning_group=(GroupNames.UI)),
      icon_selected=TunableIcon(description='\n                    Icon to be displayed on the button when the pose button is selected\n                    ',
      tuning_group=(GroupNames.UI)),
      pose=TunableEnumEntry(description='\n                    The pose to play when the button is pressed\n                    ',
      tunable_type=CASPaintPose,
      default=(CASPaintPose.NONE)),
      export_class_name='CasPaintPoseTuple')),
      export_modes=(ExportModes.ClientBinary),
      tuple_name='CasPaintPoseKeyValue')
    CAS_VOICES_DATA = TunableMapping(description='\n        A mapping of species type to data required for the personality panel ui.\n        ',
      key_type=TunableEnumEntry(description='\n            The species type that this entry applies to.\n            ',
      tunable_type=SpeciesExtended,
      default=(SpeciesExtended.HUMAN),
      invalid_enums=(
     SpeciesExtended.INVALID,)),
      value_type=TunableMapping(description='\n            A mapping of age type to data required for displaying voices in the ui.\n            ',
      key_type=TunableEnumEntry(description='\n                The age that this entry applies to.\n                ',
      tunable_type=Age,
      default=(Age.ADULT)),
      value_type=TunableList(description='\n                a list of voice data for this species at this age.\n                ',
      tunable=TunableTuple(description='\n                    data required to display this voice in the ui.\n                    ',
      icon=TunableIcon(description='\n                        Icon to be displayed as voice button.\n                        ',
      tuning_group=(GroupNames.UI)),
      icon_selected=TunableIcon(description='\n                        Icon to be displayed as voice button when it is selected.\n                        ',
      tuning_group=(GroupNames.UI)),
      tooltip=TunableLocalizedString(description='\n                        Localized name of this voice.\n                        '),
      export_class_name='CasVoicesDataTuple')),
      tuple_name='CasVoicesAgeKeyValue'),
      export_modes=(ExportModes.ClientBinary),
      tuple_name='CasVoicesSpeciesKeyValue')
    CAS_RANDOMIZE_FILTERS = TunableMapping(description='\n        An Ordered list of randomization menu items that will appear in the randomization panel ui in CAS. \n        The list is filtered by the criteria on each menu item.\n        ',
      key_type=Tunable(description='\n            An integer value used to set the specific order of the menu items\n            in the ui. The lower numbers are displayed first in the ui.\n            ',
      tunable_type=int,
      default=0),
      value_type=TunableTuple(description='\n            A randomization menu item and its inclusion (and/or exclusion) criteria.\n            ',
      criteria=CASContextCriterionList(description='\n                Use this menu item if all of the specified criteria are met.\n                '),
      flags=TunableList(description='\n                A list of randomization flags for this item.\n                ',
      tunable=TunableEnumEntry(description='\n                    A randomization flag.\n                    ',
      tunable_type=CASRandomizeFlag,
      default=(CASRandomizeFlag.RANDOMIZE_BY_MENUSTATE))),
      name=TunableLocalizedString(description='\n                The name of this menu item displayed in the ui.\n                '),
      required_flags=TunableList(description='\n                A list of randomization flags that are required to be enabled \n                in order for this menu item to be enabled. \n                ',
      tunable=TunableEnumEntry(description='\n                    A randomization flag.\n                    ',
      tunable_type=CASRandomizeFlag,
      default=(CASRandomizeFlag.RANDOMIZE_BY_MENUSTATE))),
      export_class_name='CasRandomizeItemTuple'),
      tuple_name='CasRandomizeItemsKeyValue',
      export_modes=(
     ExportModes.ClientBinary,))
    CAS_COPY_FILTERS = TunableList(description='\n        An Ordered list of copy menu items that will appear in the randomization panel ui in CAS. \n        The list is filtered by the criteria on each menu item.\n        ',
      tunable=TunableTuple(description='\n            A copy menu item and its inclusion (and/or exclusion) criteria.\n            ',
      criteria=CASContextCriterionList(description='\n                Use this menu item if all of the specified criteria are met.\n                '),
      flags=TunableList(description='\n                A list of copy flags for this item.\n                ',
      tunable=TunableEnumEntry(description='\n                    A copy flag.\n                    ',
      tunable_type=CASRandomizeFlag,
      default=(CASRandomizeFlag.RANDOMIZE_BY_MENUSTATE))),
      name=TunableLocalizedString(description='\n                The name of this menu item displayed in the ui.\n                '),
      required_flags=TunableList(description='\n                A list of copy flags that are required to be enabled \n                in order for this menu item to be enabled. \n                ',
      tunable=TunableEnumEntry(description='\n                    A copy flag.\n                    ',
      tunable_type=CASRandomizeFlag,
      default=(CASRandomizeFlag.RANDOMIZE_BY_MENUSTATE))),
      export_class_name='CasCopyItemEntry'),
      export_modes=(
     ExportModes.ClientBinary,))
    CAS_ADD_SIM_MENU_DATA = TunableMapping(description='\n        An ordered mapping of menu data used for the Add Sim portion of CAS.\n        ',
      key_name='index',
      key_type=Tunable(description='\n            The order in which these entries should be added. 1 is first, 2 is\n            second, etc.\n            ',
      tunable_type=int,
      default=0),
      value_name='data',
      value_type=TunableTuple(description='\n            Data associated with an add Sim button in CAS.\n            ',
      criteria=CASContextCriterionList(description='\n                Only add this menu item if the criteria are met.\n                '),
      parent_index=Tunable(description='\n                The index of the parent entry if this is a child to another\n                entry in the list. 0 if this entry has no parent.\n                ',
      tunable_type=int,
      default=0),
      tooltip=TunableLocalizedString(description='\n                The tooltip when hovering over this entry.\n                ',
      allow_none=True),
      icon=TunableResourceKey(description='\n                The icon for this entry.\n                ',
      allow_none=True,
      pack_safe=True),
      icon_selected=TunableResourceKey(description='\n                The icon when this entry is selected.\n                ',
      allow_none=True,
      pack_safe=True),
      audio_name=Tunable(description='\n                The audio to play when this entry is selected.\n                ',
      tunable_type=str,
      default='',
      allow_empty=True),
      flair_name=Tunable(description='\n                Flair to apply to this entry (for instance, god rays).\n                ',
      tunable_type=str,
      default='',
      allow_empty=True),
      tutorial_control_enum=TunableEnumEntry(description='\n                The enum used for tutorial controls. UI_INVALID should be\n                used if this entry has no tutorial control.\n                ',
      tunable_type=TutorialTipUiElement,
      default=(TutorialTipUiElement.UI_INVALID)),
      action=TunableEnumEntry(description='\n                The action to take when clicking this entry.\n                ',
      tunable_type=CASAddSimAction,
      default=(CASAddSimAction.ACTION_NONE)),
      species=TunableEnumEntry(description="\n                The species for this entry. Species.INVALID indicates no\n                preference or it's not relevant to this menu entry.\n                ",
      tunable_type=SpeciesExtended,
      default=(SpeciesExtended.INVALID)),
      occult_type=TunableEnumFlags(description='\n                The occult type for this entry, if any.\n                ',
      enum_type=OccultType,
      allow_no_flags=True),
      limit_genetics_species=TunableEnumSet(description='\n                Species in this list will only be allowed through if the action\n                for this entry is GENETICS. This is very likely only going to be\n                used for pet genetics.\n                ',
      enum_type=SpeciesExtended,
      enum_default=(SpeciesExtended.INVALID),
      allow_empty_set=True),
      export_class_name='CasAddSimMenuData'),
      tuple_name='CasAddSimMenuDataKeyValue',
      export_modes=(
     ExportModes.ClientBinary,))
    CAS_PROHIBITED_TAGS_BY_MODE = TunableMapping(description='\n        Any item with any of these tags are filtered out of CAS catalog views for the associated edit mode.\n        ',
      key_name='edit_mode',
      key_type=TunableEnumEntry(description='\n            The edit mode that has a restriction.\n            ',
      tunable_type=CASEditMode,
      default=(CASEditMode.DEFAULT),
      binary_type=(EnumBinaryExportType.EnumUint32)),
      value_name='excluded_tags',
      value_type=TunableTags(description='\n            The tags that are not allowed for the associated edit mode,\n            ',
      filter_prefixes=('Uniform', 'OutfitCategory', 'Style', 'Situation'),
      binary_type=(EnumBinaryExportType.EnumUint32)),
      tuple_name='CasProhibitedTagsByModeKeyValue',
      export_modes=(
     ExportModes.ClientBinary,))