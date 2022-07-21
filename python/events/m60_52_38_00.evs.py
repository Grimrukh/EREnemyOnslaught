"""
Southeast Caelid (NW) (SW)

linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_52_38_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_RegisterGraceIfFlagEnabled(
        0,
        flag=310,
        grace_flag=1052380000,
        character=Characters.TalkDummy,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    Event_1052382699()
    CommonFunc_90005646(
        0,
        flag=76422,
        left_flag=1052382690,
        cancel_flag__right_flag=1052382691,
        asset=Assets.AEG099_065_9000,
        player_start=1050362690,
        area_id=60,
        block_id=50,
        cc_id=36,
        dd_id=0,
    )
    Event_1252380700(0, character=Characters.BlaiddNPC)
    CommonFunc_90005704(0, attacked_entity=Characters.BlaiddNPC, flag=3601, flag_1=3600, flag_2=1052389301, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.BlaiddNPC,
        flag=3601,
        flag_1=3602,
        flag_2=1052389301,
        flag_3=3603,
        first_flag=3600,
        last_flag=3603,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.BlaiddNPC, flag=3603, first_flag=3600, last_flag=3604)
    Event_1252380705(0, character=Characters.AlexanderNPC)
    CommonFunc_90005704(0, attacked_entity=Characters.AlexanderNPC, flag=3661, flag_1=3660, flag_2=1043399301, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.AlexanderNPC,
        flag=3661,
        flag_1=3662,
        flag_2=1043399301,
        flag_3=3661,
        first_flag=3660,
        last_flag=3663,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.AlexanderNPC, flag=3663, first_flag=3660, last_flag=3664)
    Event_1252380710()
    Event_1252380720()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1052380700)
    DisableBackread(1052380710)
    DisableBackread(1052380715)
    DisableBackread(1052380720)
    DisableBackread(Characters.BlaiddNPC)
    DisableBackread(1052380730)
    DisableBackread(1052380735)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RadahnDies()
    RadahnBattleTrigger()
    RadahnPhaseTwoTransition(0, radahn=Characters.StarscourgeRadahn, radahn_meteor_dummy=Characters.RadahnMeteorDummy)
    RadahnPhaseTwoTransition(  # 1252382821
        1, radahn=Characters.CLONE_StarscourgeRadahn, radahn_meteor_dummy=Characters.CLONE_RadahnMeteorDummy
    )
    RadahnMusicControl()

    Event_1252382680(0, asset=Assets.AEG007_299_1003)
    Event_1252382680(1, asset=Assets.AEG007_299_1013)
    Event_1252382680(2, asset=Assets.AEG007_299_9000)
    Event_1252382680(3, asset=Assets.AEG007_299_9001)
    Event_1252382680(4, asset=Assets.AEG007_299_9002)
    Event_1252382680(5, asset=Assets.AEG007_299_9003)
    Event_1252382680(6, asset=Assets.AEG007_299_9004)
    Event_1252382680(7, asset=Assets.AEG007_299_9005)
    Event_1252382680(8, asset=Assets.AEG007_299_9007)
    Event_1252382680(9, asset=Assets.AEG007_299_9006)
    SetWailingDunesTime()
    Event_1252382696()
    Event_1252382695()

    SummonRequest(
        0,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382100,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        summon_point=Assets.AEG099_090_9000,
        action_button_id=9540,
    )
    ControlSummonCharacter(
        0,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382100,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        asset=Assets.AEG099_090_9000,
        summoning_animation=63021,
        summoned_message=80800,
    )
    CreateSummonVFX(
        0,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382100,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        asset=Assets.AEG099_090_9000,
    )
    MoveSummonPreview(
        0,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382100,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        destination=Assets.AEG099_090_9000,
        standby_animation=63040,
    )
    SummonDies(
        0,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382100,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80801,
        destination=Assets.AEG099_090_9080,
    )
    DismissSummon(
        0,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382100,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        dismiss_flag=0,
        animation_id=0,
        text=80802,
    )
    SummonRequest(
        2,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382102,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        summon_point=Assets.AEG099_090_9002,
        action_button_id=9542,
    )
    ControlSummonCharacter(
        2,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382102,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        asset=Assets.AEG099_090_9002,
        summoning_animation=20040,
        summoned_message=80820,
    )
    CreateSummonVFX(
        2,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382102,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        asset=Assets.AEG099_090_9002,
    )
    MoveSummonPreview(
        2,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382102,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        destination=Assets.AEG099_090_9002,
        standby_animation=63040,
    )
    SummonDies(
        2,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382102,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        death_animation=20049,
        standby_animation=0,
        dead_message=80821,
        destination=Assets.AEG099_090_9082,
    )
    DismissSummon(
        2,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382102,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        dismiss_flag=0,
        animation_id=0,
        text=80822,
    )
    SummonRequest(
        6,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382106,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        summon_point=Assets.AEG099_090_9006,
        action_button_id=9546,
    )
    ControlSummonCharacter(
        6,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382106,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        asset=Assets.AEG099_090_9006,
        summoning_animation=63021,
        summoned_message=80860,
    )
    CreateSummonVFX(
        6,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382106,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        asset=Assets.AEG099_090_9006,
    )
    MoveSummonPreview(
        6,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382106,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        destination=Assets.AEG099_090_9006,
        standby_animation=63040,
    )
    SummonDies(
        6,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382106,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80861,
        destination=Assets.AEG099_090_9086,
    )
    DismissSummon(
        6,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382106,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        dismiss_flag=0,
        animation_id=0,
        text=80862,
    )
    SummonRequest(
        8,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382108,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        summon_point=Assets.AEG099_090_9008,
        action_button_id=9540,
    )
    ControlSummonCharacter(
        8,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382108,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        asset=Assets.AEG099_090_9008,
        summoning_animation=63021,
        summoned_message=80800,
    )
    CreateSummonVFX(
        8,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382108,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        asset=Assets.AEG099_090_9008,
    )
    MoveSummonPreview(
        8,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382108,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        destination=Assets.AEG099_090_9008,
        standby_animation=63040,
    )
    SummonDies(
        8,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382108,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80801,
        destination=Assets.AEG099_090_9080,
    )
    DismissSummon(
        8,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382108,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        dismiss_flag=0,
        animation_id=0,
        text=80802,
    )
    SummonRequest(
        9,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382109,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        summon_point=Assets.AEG099_090_9009,
        action_button_id=9541,
    )
    ControlSummonCharacter(
        9,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382109,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        asset=Assets.AEG099_090_9009,
        summoning_animation=20054,
        summoned_message=80810,
    )
    CreateSummonVFX(
        9,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382109,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        asset=Assets.AEG099_090_9009,
    )
    MoveSummonPreview(
        9,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382109,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        destination=Assets.AEG099_090_9009,
        standby_animation=63040,
    )
    SummonDies(
        9,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382109,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        death_animation=20049,
        standby_animation=0,
        dead_message=80811,
        destination=Assets.AEG099_090_9081,
    )
    DismissSummon(
        9,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382109,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        dismiss_flag=0,
        animation_id=0,
        text=80812,
    )
    SummonRequest(
        12,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382112,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        summon_point=Assets.AEG099_090_9012,
        action_button_id=9544,
    )
    ControlSummonCharacter(
        12,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382112,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        asset=Assets.AEG099_090_9012,
        summoning_animation=63021,
        summoned_message=80840,
    )
    CreateSummonVFX(
        12,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382112,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        asset=Assets.AEG099_090_9012,
    )
    MoveSummonPreview(
        12,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382112,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        destination=Assets.AEG099_090_9012,
        standby_animation=63040,
    )
    SummonDies(
        12,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382112,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80841,
        destination=Assets.AEG099_090_9084,
    )
    DismissSummon(
        12,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382112,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        dismiss_flag=0,
        animation_id=0,
        text=80842,
    )
    SummonRequest(
        13,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382113,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        summon_point=Assets.AEG099_090_9013,
        action_button_id=9545,
    )
    ControlSummonCharacter(
        13,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382113,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        asset=Assets.AEG099_090_9013,
        summoning_animation=63021,
        summoned_message=80850,
    )
    CreateSummonVFX(
        13,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382113,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        asset=Assets.AEG099_090_9013,
    )
    MoveSummonPreview(
        13,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382113,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        destination=Assets.AEG099_090_9013,
        standby_animation=63040,
    )
    SummonDies(
        13,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382113,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80851,
        destination=Assets.AEG099_090_9085,
    )
    DismissSummon(
        13,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382113,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        dismiss_flag=0,
        animation_id=0,
        text=80852,
    )
    SummonRequest(
        14,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382114,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        summon_point=Assets.AEG099_090_9014,
        action_button_id=9546,
    )
    ControlSummonCharacter(
        14,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382114,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        asset=Assets.AEG099_090_9014,
        summoning_animation=63021,
        summoned_message=80860,
    )
    CreateSummonVFX(
        14,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382114,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        asset=Assets.AEG099_090_9014,
    )
    MoveSummonPreview(
        14,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382114,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        destination=Assets.AEG099_090_9014,
        standby_animation=63040,
    )
    SummonDies(
        14,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382114,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80861,
        destination=Assets.AEG099_090_9086,
    )
    DismissSummon(
        14,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382114,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        dismiss_flag=0,
        animation_id=0,
        text=80862,
    )
    SummonRequest(
        16,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382116,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        summon_point=Assets.AEG099_090_9016,
        action_button_id=9540,
    )
    ControlSummonCharacter(
        16,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382116,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        asset=Assets.AEG099_090_9016,
        summoning_animation=63021,
        summoned_message=80800,
    )
    CreateSummonVFX(
        16,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382116,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        asset=Assets.AEG099_090_9016,
    )
    MoveSummonPreview(
        16,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382116,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        destination=Assets.AEG099_090_9016,
        standby_animation=63040,
    )
    SummonDies(
        16,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382116,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80801,
        destination=Assets.AEG099_090_9080,
    )
    DismissSummon(
        16,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382116,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        dismiss_flag=0,
        animation_id=0,
        text=80802,
    )
    SummonRequest(
        17,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382117,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        summon_point=Assets.AEG099_090_9017,
        action_button_id=9541,
    )
    ControlSummonCharacter(
        17,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382117,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        asset=Assets.AEG099_090_9017,
        summoning_animation=20054,
        summoned_message=80810,
    )
    CreateSummonVFX(
        17,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382117,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        asset=Assets.AEG099_090_9017,
    )
    MoveSummonPreview(
        17,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382117,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        destination=Assets.AEG099_090_9017,
        standby_animation=63040,
    )
    SummonDies(
        17,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382117,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        death_animation=20049,
        standby_animation=0,
        dead_message=80811,
        destination=Assets.AEG099_090_9081,
    )
    DismissSummon(
        17,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382117,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        dismiss_flag=0,
        animation_id=0,
        text=80812,
    )
    SummonRequest(
        18,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382118,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        summon_point=Assets.AEG099_090_9018,
        action_button_id=9542,
    )
    ControlSummonCharacter(
        18,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382118,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        asset=Assets.AEG099_090_9018,
        summoning_animation=20040,
        summoned_message=80820,
    )
    CreateSummonVFX(
        18,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382118,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        asset=Assets.AEG099_090_9018,
    )
    MoveSummonPreview(
        18,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382118,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        destination=Assets.AEG099_090_9018,
        standby_animation=63040,
    )
    SummonDies(
        18,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382118,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        death_animation=20049,
        standby_animation=0,
        dead_message=80821,
        destination=Assets.AEG099_090_9082,
    )
    DismissSummon(
        18,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382118,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        dismiss_flag=0,
        animation_id=0,
        text=80822,
    )
    SummonRequest(
        19,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382119,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        summon_point=Assets.AEG099_090_9019,
        action_button_id=9543,
    )
    ControlSummonCharacter(
        19,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382119,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        asset=Assets.AEG099_090_9019,
        summoning_animation=63021,
        summoned_message=80830,
    )
    CreateSummonVFX(
        19,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382119,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        asset=Assets.AEG099_090_9019,
    )
    MoveSummonPreview(
        19,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382119,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        destination=Assets.AEG099_090_9019,
        standby_animation=63040,
    )
    SummonDies(
        19,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382119,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80831,
        destination=Assets.AEG099_090_9083,
    )
    DismissSummon(
        19,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382119,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        dismiss_flag=0,
        animation_id=0,
        text=80832,
    )
    SummonRequest(
        21,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382121,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        summon_point=Assets.AEG099_090_9021,
        action_button_id=9545,
    )
    ControlSummonCharacter(
        21,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382121,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        asset=Assets.AEG099_090_9021,
        summoning_animation=63021,
        summoned_message=80850,
    )
    CreateSummonVFX(
        21,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382121,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        asset=Assets.AEG099_090_9021,
    )
    MoveSummonPreview(
        21,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382121,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        destination=Assets.AEG099_090_9021,
        standby_animation=63040,
    )
    SummonDies(
        21,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382121,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80851,
        destination=Assets.AEG099_090_9085,
    )
    DismissSummon(
        21,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382121,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        dismiss_flag=0,
        animation_id=0,
        text=80852,
    )
    SummonRequest(
        23,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382123,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        summon_point=Assets.AEG099_090_9023,
        action_button_id=9547,
    )
    ControlSummonCharacter(
        23,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382123,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        asset=Assets.AEG099_090_9023,
        summoning_animation=63021,
        summoned_message=80870,
    )
    CreateSummonVFX(
        23,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382123,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        asset=Assets.AEG099_090_9023,
    )
    MoveSummonPreview(
        23,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382123,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        destination=Assets.AEG099_090_9023,
        standby_animation=63040,
    )
    SummonDies(
        23,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382123,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80871,
        destination=Assets.AEG099_090_9087,
    )
    DismissSummon(
        23,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382123,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        dismiss_flag=0,
        animation_id=0,
        text=80872,
    )
    SummonRequest(
        24,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382124,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        summon_point=Assets.AEG099_090_9024,
        action_button_id=9540,
    )
    ControlSummonCharacter(
        24,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382124,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        asset=Assets.AEG099_090_9024,
        summoning_animation=63021,
        summoned_message=80800,
    )
    CreateSummonVFX(
        24,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382124,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        asset=Assets.AEG099_090_9024,
    )
    MoveSummonPreview(
        24,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382124,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        destination=Assets.AEG099_090_9024,
        standby_animation=63040,
    )
    SummonDies(
        24,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382124,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80801,
        destination=Assets.AEG099_090_9080,
    )
    DismissSummon(
        24,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382124,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        dismiss_flag=0,
        animation_id=0,
        text=80802,
    )
    SummonRequest(
        25,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382125,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        summon_point=Assets.AEG099_090_9025,
        action_button_id=9541,
    )
    ControlSummonCharacter(
        25,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382125,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        asset=Assets.AEG099_090_9025,
        summoning_animation=20054,
        summoned_message=80810,
    )
    CreateSummonVFX(
        25,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382125,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        asset=Assets.AEG099_090_9025,
    )
    MoveSummonPreview(
        25,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382125,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        destination=Assets.AEG099_090_9025,
        standby_animation=63040,
    )
    SummonDies(
        25,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382125,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        death_animation=20049,
        standby_animation=0,
        dead_message=80811,
        destination=Assets.AEG099_090_9081,
    )
    DismissSummon(
        25,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382125,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        dismiss_flag=0,
        animation_id=0,
        text=80812,
    )
    SummonRequest(
        29,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382129,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        summon_point=Assets.AEG099_090_9029,
        action_button_id=9545,
    )
    ControlSummonCharacter(
        29,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382129,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        asset=Assets.AEG099_090_9029,
        summoning_animation=63021,
        summoned_message=80850,
    )
    CreateSummonVFX(
        29,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382129,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        asset=Assets.AEG099_090_9029,
    )
    MoveSummonPreview(
        29,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382129,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        destination=Assets.AEG099_090_9029,
        standby_animation=63040,
    )
    SummonDies(
        29,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382129,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80851,
        destination=Assets.AEG099_090_9085,
    )
    DismissSummon(
        29,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382129,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        dismiss_flag=0,
        animation_id=0,
        text=80852,
    )
    SummonRequest(
        35,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382135,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        summon_point=Assets.AEG099_090_9035,
        action_button_id=9543,
    )
    ControlSummonCharacter(
        35,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382135,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        asset=Assets.AEG099_090_9035,
        summoning_animation=63021,
        summoned_message=80830,
    )
    CreateSummonVFX(
        35,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382135,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        asset=Assets.AEG099_090_9035,
    )
    MoveSummonPreview(
        35,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382135,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        destination=Assets.AEG099_090_9035,
        standby_animation=63040,
    )
    SummonDies(
        35,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382135,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80831,
        destination=Assets.AEG099_090_9083,
    )
    DismissSummon(
        35,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382135,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        dismiss_flag=0,
        animation_id=0,
        text=80832,
    )
    SummonRequest(
        36,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382136,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        summon_point=Assets.AEG099_090_9036,
        action_button_id=9544,
    )
    ControlSummonCharacter(
        36,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382136,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        asset=Assets.AEG099_090_9036,
        summoning_animation=63021,
        summoned_message=80840,
    )
    CreateSummonVFX(
        36,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382136,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        asset=Assets.AEG099_090_9036,
    )
    MoveSummonPreview(
        36,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382136,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        destination=Assets.AEG099_090_9036,
        standby_animation=63040,
    )
    SummonDies(
        36,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382136,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80841,
        destination=Assets.AEG099_090_9084,
    )
    DismissSummon(
        36,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382136,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        dismiss_flag=0,
        animation_id=0,
        text=80842,
    )
    SummonRequest(
        38,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382138,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        summon_point=Assets.AEG099_090_9038,
        action_button_id=9546,
    )
    ControlSummonCharacter(
        38,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382138,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        asset=Assets.AEG099_090_9038,
        summoning_animation=63021,
        summoned_message=80860,
    )
    CreateSummonVFX(
        38,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382138,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        asset=Assets.AEG099_090_9038,
    )
    MoveSummonPreview(
        38,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382138,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        destination=Assets.AEG099_090_9038,
        standby_animation=63040,
    )
    SummonDies(
        38,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382138,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80861,
        destination=Assets.AEG099_090_9086,
    )
    DismissSummon(
        38,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382138,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        dismiss_flag=0,
        animation_id=0,
        text=80862,
    )
    SummonRequest(
        40,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382140,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        summon_point=Assets.AEG099_090_9040,
        action_button_id=9540,
    )
    ControlSummonCharacter(
        40,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382140,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        asset=Assets.AEG099_090_9040,
        summoning_animation=63021,
        summoned_message=80800,
    )
    CreateSummonVFX(
        40,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382140,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        asset=Assets.AEG099_090_9040,
    )
    MoveSummonPreview(
        40,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382140,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        destination=Assets.AEG099_090_9040,
        standby_animation=63040,
    )
    SummonDies(
        40,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382140,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80801,
        destination=Assets.AEG099_090_9080,
    )
    DismissSummon(
        40,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382140,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        dismiss_flag=0,
        animation_id=0,
        text=80802,
    )
    SummonRequest(
        41,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382141,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        summon_point=Assets.AEG099_090_9041,
        action_button_id=9541,
    )
    ControlSummonCharacter(
        41,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382141,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        asset=Assets.AEG099_090_9041,
        summoning_animation=20054,
        summoned_message=80810,
    )
    CreateSummonVFX(
        41,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382141,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        asset=Assets.AEG099_090_9041,
    )
    MoveSummonPreview(
        41,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382141,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        destination=Assets.AEG099_090_9041,
        standby_animation=63040,
    )
    SummonDies(
        41,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382141,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        death_animation=20049,
        standby_animation=0,
        dead_message=80811,
        destination=Assets.AEG099_090_9081,
    )
    DismissSummon(
        41,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382141,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        dismiss_flag=0,
        animation_id=0,
        text=80812,
    )
    SummonRequest(
        43,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382143,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        summon_point=Assets.AEG099_090_9043,
        action_button_id=9543,
    )
    ControlSummonCharacter(
        43,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382143,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        asset=Assets.AEG099_090_9043,
        summoning_animation=63021,
        summoned_message=80830,
    )
    CreateSummonVFX(
        43,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382143,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        asset=Assets.AEG099_090_9043,
    )
    MoveSummonPreview(
        43,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382143,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        destination=Assets.AEG099_090_9043,
        standby_animation=63040,
    )
    SummonDies(
        43,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382143,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80831,
        destination=Assets.AEG099_090_9083,
    )
    DismissSummon(
        43,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382143,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        dismiss_flag=0,
        animation_id=0,
        text=80832,
    )
    SummonRequest(
        44,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382144,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        summon_point=Assets.AEG099_090_9044,
        action_button_id=9544,
    )
    ControlSummonCharacter(
        44,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382144,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        asset=Assets.AEG099_090_9044,
        summoning_animation=63021,
        summoned_message=80840,
    )
    CreateSummonVFX(
        44,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382144,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        asset=Assets.AEG099_090_9044,
    )
    MoveSummonPreview(
        44,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382144,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        destination=Assets.AEG099_090_9044,
        standby_animation=63040,
    )
    SummonDies(
        44,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382144,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80841,
        destination=Assets.AEG099_090_9084,
    )
    DismissSummon(
        44,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382144,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        dismiss_flag=0,
        animation_id=0,
        text=80842,
    )
    SummonRequest(
        45,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382145,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        summon_point=Assets.AEG099_090_9045,
        action_button_id=9545,
    )
    ControlSummonCharacter(
        45,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382145,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        asset=Assets.AEG099_090_9045,
        summoning_animation=63021,
        summoned_message=80850,
    )
    CreateSummonVFX(
        45,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382145,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        asset=Assets.AEG099_090_9045,
    )
    MoveSummonPreview(
        45,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382145,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        destination=Assets.AEG099_090_9045,
        standby_animation=63040,
    )
    SummonDies(
        45,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382145,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80851,
        destination=Assets.AEG099_090_9085,
    )
    DismissSummon(
        45,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382145,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        dismiss_flag=0,
        animation_id=0,
        text=80852,
    )
    SummonRequest(
        47,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382147,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        summon_point=Assets.AEG099_090_9047,
        action_button_id=9547,
    )
    ControlSummonCharacter(
        47,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382147,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        asset=Assets.AEG099_090_9047,
        summoning_animation=63021,
        summoned_message=80870,
    )
    CreateSummonVFX(
        47,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382147,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        asset=Assets.AEG099_090_9047,
    )
    MoveSummonPreview(
        47,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382147,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        destination=Assets.AEG099_090_9047,
        standby_animation=63040,
    )
    SummonDies(
        47,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382147,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80871,
        destination=Assets.AEG099_090_9087,
    )
    DismissSummon(
        47,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382147,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        dismiss_flag=0,
        animation_id=0,
        text=80872,
    )
    SummonRequest(
        48,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382148,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        summon_point=Assets.AEG099_090_9048,
        action_button_id=9540,
    )
    ControlSummonCharacter(
        48,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382148,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        asset=Assets.AEG099_090_9048,
        summoning_animation=63021,
        summoned_message=80800,
    )
    CreateSummonVFX(
        48,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382148,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        asset=Assets.AEG099_090_9048,
    )
    MoveSummonPreview(
        48,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382148,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        destination=Assets.AEG099_090_9048,
        standby_animation=63040,
    )
    SummonDies(
        48,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382148,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80801,
        destination=Assets.AEG099_090_9080,
    )
    DismissSummon(
        48,
        summon=Characters.CastellanJerren,
        summon_clone=Characters.CLONE_CastellanJerren,
        optional_required_flag=Flags.RadahnPhaseTwoTransitionFinished,
        summon_point_used_flag=1252382148,
        summon_in_progress_flag=1252382180,
        summon_active_flag=1252382190,
        dismiss_flag=0,
        animation_id=0,
        text=80802,
    )
    SummonRequest(
        51,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382151,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        summon_point=Assets.AEG099_090_9051,
        action_button_id=9543,
    )
    ControlSummonCharacter(
        51,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382151,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        asset=Assets.AEG099_090_9051,
        summoning_animation=63021,
        summoned_message=80830,
    )
    CreateSummonVFX(
        51,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382151,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        asset=Assets.AEG099_090_9051,
    )
    MoveSummonPreview(
        51,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382151,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        destination=Assets.AEG099_090_9051,
        standby_animation=63040,
    )
    SummonDies(
        51,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382151,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80831,
        destination=Assets.AEG099_090_9083,
    )
    DismissSummon(
        51,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382151,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        dismiss_flag=0,
        animation_id=0,
        text=80832,
    )
    SummonRequest(
        52,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382152,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        summon_point=Assets.AEG099_090_9052,
        action_button_id=9544,
    )
    ControlSummonCharacter(
        52,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382152,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        asset=Assets.AEG099_090_9052,
        summoning_animation=63021,
        summoned_message=80840,
    )
    CreateSummonVFX(
        52,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382152,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        asset=Assets.AEG099_090_9052,
    )
    MoveSummonPreview(
        52,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382152,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        destination=Assets.AEG099_090_9052,
        standby_animation=63040,
    )
    SummonDies(
        52,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382152,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80841,
        destination=Assets.AEG099_090_9084,
    )
    DismissSummon(
        52,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382152,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        dismiss_flag=0,
        animation_id=0,
        text=80842,
    )
    SummonRequest(
        53,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382153,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        summon_point=Assets.AEG099_090_9053,
        action_button_id=9545,
    )
    ControlSummonCharacter(
        53,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382153,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        asset=Assets.AEG099_090_9053,
        summoning_animation=63021,
        summoned_message=80850,
    )
    CreateSummonVFX(
        53,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382153,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        asset=Assets.AEG099_090_9053,
    )
    MoveSummonPreview(
        53,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382153,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        destination=Assets.AEG099_090_9053,
        standby_animation=63040,
    )
    SummonDies(
        53,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382153,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80851,
        destination=Assets.AEG099_090_9085,
    )
    DismissSummon(
        53,
        summon=Characters.FingerMaidenTherolina,
        summon_clone=Characters.CLONE_FingerMaidenTherolina,
        optional_required_flag=0,
        summon_point_used_flag=1252382153,
        summon_in_progress_flag=1252382185,
        summon_active_flag=1252382195,
        dismiss_flag=0,
        animation_id=0,
        text=80852,
    )
    SummonRequest(
        54,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382154,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        summon_point=Assets.AEG099_090_9054,
        action_button_id=9546,
    )
    ControlSummonCharacter(
        54,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382154,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        asset=Assets.AEG099_090_9054,
        summoning_animation=63021,
        summoned_message=80860,
    )
    CreateSummonVFX(
        54,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382154,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        asset=Assets.AEG099_090_9054,
    )
    MoveSummonPreview(
        54,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382154,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        destination=Assets.AEG099_090_9054,
        standby_animation=63040,
    )
    SummonDies(
        54,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382154,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80861,
        destination=Assets.AEG099_090_9086,
    )
    DismissSummon(
        54,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382154,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        dismiss_flag=0,
        animation_id=0,
        text=80862,
    )
    SummonRequest(
        55,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382155,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        summon_point=Assets.AEG099_090_9055,
        action_button_id=9547,
    )
    ControlSummonCharacter(
        55,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382155,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        asset=Assets.AEG099_090_9055,
        summoning_animation=63021,
        summoned_message=80870,
    )
    CreateSummonVFX(
        55,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382155,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        asset=Assets.AEG099_090_9055,
    )
    MoveSummonPreview(
        55,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382155,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        destination=Assets.AEG099_090_9055,
        standby_animation=63040,
    )
    SummonDies(
        55,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382155,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80871,
        destination=Assets.AEG099_090_9087,
    )
    DismissSummon(
        55,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382155,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        dismiss_flag=0,
        animation_id=0,
        text=80872,
    )
    SummonRequest(
        57,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382157,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        summon_point=Assets.AEG099_090_9057,
        action_button_id=9541,
    )
    ControlSummonCharacter(
        57,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382157,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        asset=Assets.AEG099_090_9057,
        summoning_animation=20054,
        summoned_message=80810,
    )
    CreateSummonVFX(
        57,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382157,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        asset=Assets.AEG099_090_9057,
    )
    MoveSummonPreview(
        57,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382157,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        destination=Assets.AEG099_090_9057,
        standby_animation=63040,
    )
    SummonDies(
        57,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382157,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        death_animation=20049,
        standby_animation=0,
        dead_message=80811,
        destination=Assets.AEG099_090_9081,
    )
    DismissSummon(
        57,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382157,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        dismiss_flag=0,
        animation_id=0,
        text=80812,
    )
    SummonRequest(
        59,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382159,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        summon_point=Assets.AEG099_090_9059,
        action_button_id=9543,
    )
    ControlSummonCharacter(
        59,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382159,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        asset=Assets.AEG099_090_9059,
        summoning_animation=63021,
        summoned_message=80830,
    )
    CreateSummonVFX(
        59,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382159,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        asset=Assets.AEG099_090_9059,
    )
    MoveSummonPreview(
        59,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382159,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        destination=Assets.AEG099_090_9059,
        standby_animation=63040,
    )
    SummonDies(
        59,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382159,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80831,
        destination=Assets.AEG099_090_9083,
    )
    DismissSummon(
        59,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382159,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        dismiss_flag=0,
        animation_id=0,
        text=80832,
    )
    SummonRequest(
        62,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382162,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        summon_point=Assets.AEG099_090_9062,
        action_button_id=9546,
    )
    ControlSummonCharacter(
        62,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382162,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        asset=Assets.AEG099_090_9062,
        summoning_animation=63021,
        summoned_message=80860,
    )
    CreateSummonVFX(
        62,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382162,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        asset=Assets.AEG099_090_9062,
    )
    MoveSummonPreview(
        62,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382162,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        destination=Assets.AEG099_090_9062,
        standby_animation=63040,
    )
    SummonDies(
        62,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382162,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80861,
        destination=Assets.AEG099_090_9086,
    )
    DismissSummon(
        62,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382162,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        dismiss_flag=0,
        animation_id=0,
        text=80862,
    )
    SummonRequest(
        66,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382166,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        summon_point=Assets.AEG099_090_9066,
        action_button_id=9542,
    )
    ControlSummonCharacter(
        66,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382166,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        asset=Assets.AEG099_090_9066,
        summoning_animation=20040,
        summoned_message=80820,
    )
    CreateSummonVFX(
        66,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382166,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        asset=Assets.AEG099_090_9066,
    )
    MoveSummonPreview(
        66,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382166,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        destination=Assets.AEG099_090_9066,
        standby_animation=63040,
    )
    SummonDies(
        66,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382166,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        death_animation=20049,
        standby_animation=0,
        dead_message=80821,
        destination=Assets.AEG099_090_9082,
    )
    DismissSummon(
        66,
        summon=Characters.AlexanderSummon,
        summon_clone=Characters.CLONE_AlexanderSummon,
        optional_required_flag=Flags.AlexanderSummonAvailable,
        summon_point_used_flag=1252382166,
        summon_in_progress_flag=1252382182,
        summon_active_flag=1252382192,
        dismiss_flag=0,
        animation_id=0,
        text=80822,
    )
    SummonRequest(
        68,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382168,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        summon_point=Assets.AEG099_090_9068,
        action_button_id=9544,
    )
    ControlSummonCharacter(
        68,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382168,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        asset=Assets.AEG099_090_9068,
        summoning_animation=63021,
        summoned_message=80840,
    )
    CreateSummonVFX(
        68,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382168,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        asset=Assets.AEG099_090_9068,
    )
    MoveSummonPreview(
        68,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382168,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        destination=Assets.AEG099_090_9068,
        standby_animation=63040,
    )
    SummonDies(
        68,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382168,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80841,
        destination=Assets.AEG099_090_9084,
    )
    DismissSummon(
        68,
        summon=Characters.Okina,
        summon_clone=Characters.CLONE_Okina,
        optional_required_flag=0,
        summon_point_used_flag=1252382168,
        summon_in_progress_flag=1252382184,
        summon_active_flag=1252382194,
        dismiss_flag=0,
        animation_id=0,
        text=80842,
    )
    SummonRequest(
        73,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382173,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        summon_point=Assets.AEG099_090_9073,
        action_button_id=9541,
    )
    ControlSummonCharacter(
        73,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382173,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        asset=Assets.AEG099_090_9073,
        summoning_animation=20054,
        summoned_message=80810,
    )
    CreateSummonVFX(
        73,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382173,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        asset=Assets.AEG099_090_9073,
    )
    MoveSummonPreview(
        73,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382173,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        destination=Assets.AEG099_090_9073,
        standby_animation=63040,
    )
    SummonDies(
        73,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382173,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        death_animation=20049,
        standby_animation=0,
        dead_message=80811,
        destination=Assets.AEG099_090_9081,
    )
    DismissSummon(
        73,
        summon=Characters.BlaiddSummon,
        summon_clone=Characters.CLONE_BlaiddSummon,
        optional_required_flag=1051369359,
        summon_point_used_flag=1252382173,
        summon_in_progress_flag=1252382181,
        summon_active_flag=1252382191,
        dismiss_flag=0,
        animation_id=0,
        text=80812,
    )
    SummonRequest(
        75,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382175,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        summon_point=Assets.AEG099_090_9075,
        action_button_id=9543,
    )
    ControlSummonCharacter(
        75,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382175,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        asset=Assets.AEG099_090_9075,
        summoning_animation=63021,
        summoned_message=80830,
    )
    CreateSummonVFX(
        75,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382175,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        asset=Assets.AEG099_090_9075,
    )
    MoveSummonPreview(
        75,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382175,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        destination=Assets.AEG099_090_9075,
        standby_animation=63040,
    )
    SummonDies(
        75,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382175,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80831,
        destination=Assets.AEG099_090_9083,
    )
    DismissSummon(
        75,
        summon=Characters.GreatHornedTragoth,
        summon_clone=Characters.CLONE_GreatHornedTragoth,
        optional_required_flag=1052389200,
        summon_point_used_flag=1252382175,
        summon_in_progress_flag=1252382183,
        summon_active_flag=1252382193,
        dismiss_flag=0,
        animation_id=0,
        text=80832,
    )
    SummonRequest(
        78,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382178,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        summon_point=Assets.AEG099_090_9078,
        action_button_id=9546,
    )
    ControlSummonCharacter(
        78,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382178,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        asset=Assets.AEG099_090_9078,
        summoning_animation=63021,
        summoned_message=80860,
    )
    CreateSummonVFX(
        78,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382178,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        asset=Assets.AEG099_090_9078,
    )
    MoveSummonPreview(
        78,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382178,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        destination=Assets.AEG099_090_9078,
        standby_animation=63040,
    )
    SummonDies(
        78,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382178,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80861,
        destination=Assets.AEG099_090_9086,
    )
    DismissSummon(
        78,
        summon=Characters.LionelTheLionhearted,
        summon_clone=Characters.CLONE_LionelTheLionhearted,
        optional_required_flag=0,
        summon_point_used_flag=1252382178,
        summon_in_progress_flag=1252382186,
        summon_active_flag=1252382196,
        dismiss_flag=0,
        animation_id=0,
        text=80862,
    )
    SummonRequest(
        79,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382179,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        summon_point=Assets.AEG099_090_9079,
        action_button_id=9547,
    )
    ControlSummonCharacter(
        79,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382179,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        asset=Assets.AEG099_090_9079,
        summoning_animation=63021,
        summoned_message=80870,
    )
    CreateSummonVFX(
        79,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382179,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        asset=Assets.AEG099_090_9079,
    )
    MoveSummonPreview(
        79,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382179,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        destination=Assets.AEG099_090_9079,
        standby_animation=63040,
    )
    SummonDies(
        79,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382179,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        death_animation=90009,
        standby_animation=90007,
        dead_message=80871,
        destination=Assets.AEG099_090_9087,
    )
    DismissSummon(
        79,
        summon=Characters.Patches,
        summon_clone=Characters.CLONE_Patches,
        optional_required_flag=1052389250,
        summon_point_used_flag=1252382179,
        summon_in_progress_flag=1252382187,
        summon_active_flag=1252382197,
        dismiss_flag=0,
        animation_id=0,
        text=80872,
    )


@RestartOnRest(1252382200)
def SummonRequest(
    _,
    summon: uint,
    summon_clone: uint,
    optional_required_flag: uint,
    summon_point_used_flag: uint,
    summon_in_progress_flag: uint,
    summon_active_flag: uint,
    summon_point: uint,
    action_button_id: int,
):
    """Event 1252382200"""
    if FlagEnabled(Flags.RadahnDead):
        return
    if PlayerNotInOwnWorld():
        return
    if UnsignedNotEqual(left=optional_required_flag, right=0):
        GotoIfFlagDisabled(Label.L3, flag=optional_required_flag)
    AND_1.Add(PlayerInOwnWorld())
    AND_2.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=summon_point))
    AND_2.Add(FlagDisabled(summon_point_used_flag))
    AND_2.Add(FlagDisabled(summon_in_progress_flag))
    OR_1.Add(AND_2)
    OR_1.Add(FlagEnabled(summon_in_progress_flag))
    OR_1.Add(FlagEnabled(Flags.RadahnDead))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L0, flag=summon_in_progress_flag)
    if FlagEnabled(Flags.RadahnDead):
        return

    # --- Label 1 --- #
    DefineLabel(1)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(summon, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateAuthority(summon_clone, authority_level=UpdateAuthority.Forced)
    WaitFrames(frames=1)
    SkipLinesIfSingleplayer(1)
    if PlayerInOwnWorld():
        Move(
            summon,
            destination=summon_point,
            destination_type=CoordEntityType.Asset,
            model_point=100,
            copy_draw_parent=PLAYER,
        )
        Move(
            summon_clone,
            destination=summon_point,
            destination_type=CoordEntityType.Asset,
            model_point=100,
            copy_draw_parent=PLAYER,
        )
    Wait(1.0)
    EnableNetworkFlag(summon_point_used_flag)
    EnableNetworkFlag(summon_in_progress_flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_3.Add(FlagDisabled(summon_in_progress_flag))
    AND_3.Add(FlagDisabled(summon_active_flag))
    
    MAIN.Await(AND_3)
    
    WaitFrames(frames=1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    
    MAIN.Await(FlagEnabled(optional_required_flag))
    
    Restart()


@RestartOnRest(1252382280)
def ControlSummonCharacter(
    _,
    summon: uint,
    summon_clone: uint,
    optional_required_flag: uint,
    summon_point_used_flag: uint,
    summon_in_progress_flag: uint,
    summon_active_flag: uint,
    asset: uint,
    summoning_animation: int,
    summoned_message: int,
):
    """Event 1252382280"""
    DisableCharacter(summon)
    DisableAnimations(summon)
    DisableGravity(summon)
    DisableAI(summon)
    SetCharacterFadeOnEnable(character=summon, state=True)
    DisableCharacter(summon_clone)
    DisableAnimations(summon_clone)
    DisableGravity(summon_clone)
    DisableAI(summon_clone)
    SetCharacterFadeOnEnable(character=summon_clone, state=True)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(summon, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateAuthority(summon_clone, authority_level=UpdateAuthority.Forced)
    if FlagEnabled(Flags.RadahnDead):
        return

    EnableCharacter(summon)
    AddSpecialEffect(summon, 18677)
    DisableAnimations(summon)
    DisableGravity(summon)
    DisableAI(summon)
    SetTeamType(summon, TeamType.NoTeam)
    EnableImmortality(summon)

    EnableCharacter(summon_clone)
    AddSpecialEffect(summon_clone, 18677)
    DisableAnimations(summon_clone)
    DisableGravity(summon_clone)
    DisableAI(summon_clone)
    SetTeamType(summon_clone, TeamType.NoTeam)
    EnableImmortality(summon_clone)

    AND_1.Add(FlagEnabled(summon_point_used_flag))
    if UnsignedNotEqual(left=optional_required_flag, right=0):
        AND_1.Add(FlagEnabled(optional_required_flag))
    AND_1.Add(CharacterBackreadEnabled(summon))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(Flags.RadahnDead):
        DisableCharacter(summon)
        DisableAnimations(summon)
        DisableCharacterCollision(summon)
        DisableGravity(summon)
        DisableAI(summon)
        DisableCharacter(summon_clone)
        DisableAnimations(summon_clone)
        DisableCharacterCollision(summon_clone)
        DisableGravity(summon_clone)
        DisableAI(summon_clone)
        End()

    SetNetworkUpdateRate(summon, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AddSpecialEffect(summon, 110)
    AddSpecialEffect(summon, 111)
    CreateAssetVFX(asset, vfx_id=100, model_point=30320)
    RemoveSpecialEffect(summon, 4380)
    RemoveSpecialEffect(summon, 18677)
    EnableCharacter(summon)
    EnableInvincibility(summon)
    if ValueNotEqual(left=summoning_animation, right=0):
        ForceAnimation(summon, summoning_animation, wait_for_completion=True)
    EnableAnimations(summon)
    EnableCharacterCollision(summon)
    EnableGravity(summon)
    DisableInvincibility(summon)
    EnableImmortality(summon)
    EnableAI(summon)
    ReplanAI(summon)
    ClearTargetList(summon)
    EnableHealthBar(summon)
    SetTeamType(summon, TeamType.WhitePhantom)
    SetCharacterEventTarget(summon, region=1052380800)

    # CLONE
    SetNetworkUpdateRate(summon_clone, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AddSpecialEffect(summon_clone, 110)
    AddSpecialEffect(summon_clone, 111)
    RemoveSpecialEffect(summon_clone, 4380)
    RemoveSpecialEffect(summon_clone, 18677)
    EnableCharacter(summon_clone)
    EnableInvincibility(summon_clone)
    if ValueNotEqual(left=summoning_animation, right=0):
        ForceAnimation(summon_clone, summoning_animation, wait_for_completion=True)
    EnableAnimations(summon_clone)
    EnableCharacterCollision(summon_clone)
    EnableGravity(summon_clone)
    DisableInvincibility(summon_clone)
    EnableImmortality(summon_clone)
    EnableAI(summon_clone)
    ReplanAI(summon_clone)
    ClearTargetList(summon_clone)
    EnableHealthBar(summon_clone)
    SetTeamType(summon_clone, TeamType.WhitePhantom)
    SetCharacterEventTarget(summon_clone, region=1052380800)

    DisplayFlashingMessage(summoned_message)
    DeleteAssetVFX(asset)
    DisableFlag(summon_in_progress_flag)
    EnableFlag(summon_active_flag)
    End()


@RestartOnRest(1252382360)
def CreateSummonVFX(
    _,
    summon: uint,
    summon_clone: uint,
    optional_required_flag: uint,
    summon_point_used_flag: uint,
    summon_in_progress_flag: uint,
    summon_active_flag: uint,
    asset: uint,
):
    """Event 1252382360"""
    GotoIfFlagEnabled(Label.L2, flag=Flags.RadahnDead)
    if PlayerNotInOwnWorld():
        return
    if UnsignedNotEqual(left=optional_required_flag, right=0):
        AND_5.Add(FlagDisabled(optional_required_flag))
        GotoIfConditionTrue(Label.L3, input_condition=AND_5)  # wait for required flag, then restart

    AND_1.Add(FlagDisabled(summon_point_used_flag))
    AND_1.Add(FlagEnabled(summon_in_progress_flag))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)  # delete VFX and wait for summon to NOT be active

    AND_2.Add(FlagEnabled(summon_point_used_flag))
    AND_2.Add(FlagEnabled(summon_active_flag))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)  # permanently gone

    AND_3.Add(FlagEnabled(summon_active_flag))
    AND_3.Add(CharacterBackreadEnabled(summon))
    AND_3.Add(CharacterBackreadEnabled(summon_clone))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)  # delete VFX and wait for summon to NOT be active

    AND_4.Add(FlagEnabled(summon_point_used_flag))
    AND_4.Add(FlagEnabled(summon_in_progress_flag))
    GotoIfConditionTrue(Label.L1, input_condition=AND_4)  # wait one second and restart
    
    CreateAssetVFX(asset, vfx_id=100, model_point=30080)

    OR_1.Add(FlagEnabled(summon_in_progress_flag))
    OR_1.Add(FlagEnabled(Flags.RadahnDead))
    MAIN.Await(OR_1)
    
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(asset)
    OR_2.Add(FlagDisabled(summon_active_flag))
    OR_2.Add(FlagEnabled(Flags.RadahnDead))
    
    MAIN.Await(OR_2)
    
    AND_6.Add(FlagEnabled(summon_point_used_flag))
    GotoIfConditionTrue(Label.L2, input_condition=AND_6)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    DeleteAssetVFX(asset)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    
    MAIN.Await(FlagEnabled(optional_required_flag))
    
    Restart()


@RestartOnRest(1252382440)
def MoveSummonPreview(
    _,
    summon: uint,
    summon_clone: uint,
    optional_required_flag: uint,
    summon_point_used_flag: uint,
    summon_in_progress_flag: uint,
    summon_active_flag: uint,
    destination: uint,
    standby_animation: int,
):
    """Event 1252382440"""
    if FlagEnabled(Flags.RadahnDead):
        return
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L1, flag=summon_point_used_flag)
    AND_1.Add(PlayerInOwnWorld())
    if UnsignedNotEqual(left=optional_required_flag, right=0):
        AND_1.Add(FlagEnabled(optional_required_flag))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=destination, radius=15.0))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L1, flag=Flags.RadahnDead)
    GotoIfFlagEnabled(Label.L1, flag=summon_point_used_flag)
    GotoIfFlagEnabled(Label.L0, flag=summon_in_progress_flag)
    GotoIfFlagEnabled(Label.L0, flag=summon_active_flag)
    EnableCharacter(summon)
    EnableInvincibility(summon)
    DisableAI(summon)
    AddSpecialEffect(summon, 4380)
    EnableCharacter(summon_clone)
    EnableInvincibility(summon_clone)
    DisableAI(summon_clone)
    AddSpecialEffect(summon_clone, 4380)
    WaitFrames(frames=1)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(summon, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateAuthority(summon_clone, authority_level=UpdateAuthority.Forced)
    WaitFrames(frames=1)
    Move(
        summon,
        destination=destination,
        destination_type=CoordEntityType.Asset,
        model_point=100,
        copy_draw_parent=PLAYER,
    )
    Move(
        summon_clone,
        destination=destination,
        destination_type=CoordEntityType.Asset,
        model_point=100,
        copy_draw_parent=PLAYER,
    )
    WaitFrames(frames=1)
    RemoveSpecialEffect(summon, 18677)
    DisableInvincibility(summon)
    DisableAnimations(summon)
    DisableCharacterCollision(summon)
    DisableGravity(summon)
    DisableInvincibility(summon_clone)
    DisableAnimations(summon_clone)
    DisableCharacterCollision(summon_clone)
    DisableGravity(summon_clone)
    WaitFrames(frames=1)
    if ValueNotEqual(left=standby_animation, right=0):
        ForceAnimation(summon, standby_animation, loop=True)
        ForceAnimation(summon_clone, standby_animation, loop=True)
    AND_2.Add(PlayerInOwnWorld())
    if UnsignedNotEqual(left=optional_required_flag, right=0):
        AND_2.Add(FlagEnabled(optional_required_flag))
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=destination, radius=15.0))
    
    MAIN.Await(AND_2)
    
    GotoIfFlagEnabled(Label.L1, flag=Flags.RadahnDead)
    GotoIfFlagEnabled(Label.L1, flag=summon_point_used_flag)
    GotoIfFlagEnabled(Label.L0, flag=summon_in_progress_flag)
    GotoIfFlagEnabled(Label.L0, flag=summon_active_flag)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagDisabled(summon_active_flag))
    
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    End()


@RestartOnRest(1252382520)
def SummonDies(
    _,
    summon: uint,
    summon_clone: uint,
    optional_required_flag: uint,
    summon_point_used_flag: uint,
    summon_in_progress_flag: uint,
    summon_active_flag: uint,
    death_animation: int,
    standby_animation: int,
    dead_message: int,
    destination: uint,
):
    """Event 1252382520"""
    if FlagEnabled(Flags.RadahnDead):
        return
    AND_1.Add(PlayerInOwnWorld())
    if UnsignedNotEqual(left=optional_required_flag, right=0):
        AND_1.Add(FlagEnabled(optional_required_flag))
    AND_1.Add(FlagEnabled(summon_point_used_flag))
    AND_1.Add(FlagEnabled(summon_active_flag))
    AND_1.Add(CharacterBackreadEnabled(summon))
    OR_1.Add(HealthRatio(summon) <= 0.009999999776482582)  # both summons die when either dies
    OR_1.Add(HealthRatio(summon_clone) <= 0.009999999776482582)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)

    EnableInvincibility(summon)
    DisableAnimations(summon)
    SetTeamType(summon, TeamType.NoTeam)
    EnableInvincibility(summon_clone)
    DisableAnimations(summon_clone)
    SetTeamType(summon_clone, TeamType.NoTeam)
    Wait(0.10000000149011612)
    DisableCharacterCollision(summon)
    DisableGravity(summon)
    ClearTargetList(summon)
    DisableCharacterCollision(summon_clone)
    DisableGravity(summon_clone)
    ClearTargetList(summon_clone)

    SkipLinesIfValueEqual(7, left=death_animation, right=0)
    SkipLinesIfValueEqual(2, left=death_animation, right=90009)
    ForceAnimation(summon, death_animation, wait_for_completion=True)
    ForceAnimation(summon_clone, death_animation, wait_for_completion=True)
    SkipLinesIfValueNotEqual(3, left=death_animation, right=90009)
    ForceAnimation(summon, death_animation)
    ForceAnimation(summon_clone, death_animation)
    WaitFrames(frames=200)

    if ValueNotEqual(left=standby_animation, right=0):
        ForceAnimation(summon, standby_animation, loop=True)
        ForceAnimation(summon_clone, standby_animation, loop=True)
    if ValueEqual(left=death_animation, right=90009):
        AddSpecialEffect(summon, 18677)
        AddSpecialEffect(summon_clone, 18677)
        Wait(3.0)

    DisplayFlashingMessage(dead_message)
    ResetAnimation(summon, disable_interpolation=True)
    ResetAnimation(summon_clone, disable_interpolation=True)
    ForceAnimation(summon, 20, loop=True)
    ForceAnimation(summon_clone, 20, loop=True)
    AddSpecialEffect(summon, 4380)
    AddSpecialEffect(summon_clone, 4380)

    Wait(30.0)  # don't enable other summon points for this summon yet

    AddSpecialEffect(summon, 110)  # probably a heal
    AddSpecialEffect(summon, 111)
    AddSpecialEffect(summon_clone, 110)  # probably a heal
    AddSpecialEffect(summon_clone, 111)
    Move(
        summon,
        destination=destination,
        destination_type=CoordEntityType.Asset,
        model_point=100,
        copy_draw_parent=PLAYER,
    )
    Move(
        summon_clone,
        destination=destination,
        destination_type=CoordEntityType.Asset,
        model_point=100,
        copy_draw_parent=PLAYER,
    )
    ClearTargetList(summon)
    ClearTargetList(summon_clone)
    WaitFrames(frames=1)
    ReplanAI(summon)
    RemoveSpecialEffect(summon, 18677)
    SetNetworkUpdateRate(summon, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    ReplanAI(summon_clone)
    RemoveSpecialEffect(summon_clone, 18677)
    SetNetworkUpdateRate(summon_clone, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    if PlayerNotInOwnWorld():
        return

    GotoIfUnsignedEqual(Label.L0, left=summon, right=Characters.Patches)

    EnableFlag(summon_point_used_flag)
    GotoIfFlagEnabled(Label.L0, flag=Flags.RadahnDead)
    DisableFlag(summon_in_progress_flag)
    DisableFlag(summon_active_flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(summon_in_progress_flag)
    EnableFlag(summon_active_flag)
    End()


@RestartOnRest(1252382600)
def DismissSummon(
    _,
    summon: uint,
    summon_clone: uint,
    optional_required_flag: uint,
    summon_point_used_flag: uint,
    summon_in_progress_flag: uint,
    summon_active_flag: uint,
    dismiss_flag: uint,
    animation_id: int,
    text: int,
):
    """Event 1252382600"""
    if FlagEnabled(Flags.RadahnDead):
        return
    GotoIfUnsignedEqual(Label.L2, left=summon, right=Characters.Patches)
    GotoIfUnsignedEqual(Label.L0, left=dismiss_flag, right=0)

    AND_1.Add(PlayerInOwnWorld())
    if UnsignedNotEqual(left=optional_required_flag, right=0):
        AND_1.Add(FlagEnabled(optional_required_flag))
    AND_1.Add(HealthRatio(summon) > 0.009999999776482582)
    AND_1.Add(HealthRatio(summon_clone) > 0.009999999776482582)
    AND_1.Add(FlagEnabled(summon_point_used_flag))
    AND_1.Add(CharacterBackreadEnabled(summon))
    AND_1.Add(CharacterBackreadEnabled(summon_clone))
    OR_1.Add(FlagEnabled(Flags.RadahnDead))
    OR_1.Add(FlagEnabled(dismiss_flag))
    OR_1.Add(EntityBeyondDistance(entity=summon, other_entity=PLAYER, radius=200.0))
    OR_1.Add(EntityBeyondDistance(entity=summon_clone, other_entity=PLAYER, radius=200.0))
    AND_1.Add(OR_1)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(CharacterBackreadEnabled(summon))
    AND_3.Add(CharacterBackreadEnabled(summon_clone))
    OR_5.Add(HealthRatio(summon) <= 0.009999999776482582)
    OR_5.Add(HealthRatio(summon_clone) <= 0.009999999776482582)
    AND_3.Add(OR_5)
    AND_3.Add(FlagEnabled(summon_point_used_flag))
    OR_3.Add(AND_1)  # Radahn dead OR `dismiss_flag` OR player > 200 away
    OR_3.Add(AND_3)  # Summon died
    
    MAIN.Await(OR_3)
    
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(HealthRatio(summon) > 0.009999999776482582)
    AND_2.Add(HealthRatio(summon_clone) > 0.009999999776482582)
    AND_2.Add(FlagEnabled(summon_point_used_flag))
    AND_2.Add(CharacterBackreadEnabled(summon))
    AND_2.Add(CharacterBackreadEnabled(summon_clone))
    OR_2.Add(FlagEnabled(Flags.RadahnDead))
    OR_2.Add(EntityBeyondDistance(entity=summon, other_entity=PLAYER, radius=200.0))
    OR_2.Add(EntityBeyondDistance(entity=summon_clone, other_entity=PLAYER, radius=200.0))
    AND_2.Add(OR_2)
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(CharacterBackreadEnabled(summon))
    AND_4.Add(CharacterBackreadEnabled(summon_clone))
    OR_7.Add(HealthRatio(summon) <= 0.009999999776482582)
    OR_7.Add(HealthRatio(summon_clone) <= 0.009999999776482582)
    AND_4.Add(OR_7)
    AND_4.Add(FlagEnabled(summon_point_used_flag))
    OR_4.Add(AND_2)
    OR_4.Add(AND_4)
    
    MAIN.Await(OR_4)
    
    Goto(Label.L1)

    # --- Label 2 --- #
    DefineLabel(2)  # PATCHES ONLY
    AND_5.Add(PlayerInOwnWorld())
    AND_5.Add(HealthRatio(summon) > 0.009999999776482582)
    AND_5.Add(HealthRatio(summon_clone) > 0.009999999776482582)
    AND_5.Add(FlagEnabled(summon_point_used_flag))
    AND_5.Add(FlagEnabled(summon_active_flag))
    AND_5.Add(CharacterBackreadEnabled(summon))
    AND_5.Add(CharacterBackreadEnabled(summon_clone))
    AND_6.Add(PlayerInOwnWorld())
    AND_6.Add(CharacterBackreadEnabled(summon))
    AND_6.Add(CharacterBackreadEnabled(summon_clone))
    OR_8.Add(HealthRatio(summon) <= 0.009999999776482582)
    OR_8.Add(HealthRatio(summon_clone) <= 0.009999999776482582)
    AND_6.Add(OR_8)
    AND_6.Add(FlagEnabled(summon_point_used_flag))
    OR_6.Add(AND_5)
    OR_6.Add(AND_6)
    
    MAIN.Await(OR_6)
    
    Wait(20.0)  # delay before Patches flees

    # --- Label 1 --- #
    DefineLabel(1)
    OR_10.Add(HealthRatio(summon) <= 0.009999999776482582)
    OR_10.Add(HealthRatio(summon_clone) <= 0.009999999776482582)
    if OR_10:
        return  # separate event handles summon "death"
    SetTeamType(summon, TeamType.NoTeam)
    DisableAnimations(summon)
    EnableInvincibility(summon)
    SetTeamType(summon_clone, TeamType.NoTeam)
    DisableAnimations(summon_clone)
    EnableInvincibility(summon_clone)
    SkipLines(3)
    if ValueNotEqual(left=animation_id, right=0):
        ForceAnimation(summon, animation_id, wait_for_completion=True)
        ForceAnimation(summon_clone, animation_id, wait_for_completion=True)
    AddSpecialEffect(summon, 18677)
    ReplanAI(summon)
    ClearTargetList(summon)
    AddSpecialEffect(summon_clone, 18677)
    ReplanAI(summon_clone)
    ClearTargetList(summon_clone)
    Wait(3.0)
    DisableAI(summon)
    DisableInvincibility(summon)
    ResetAnimation(summon, disable_interpolation=True)
    SetNetworkUpdateRate(summon, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    DisableAI(summon_clone)
    DisableInvincibility(summon_clone)
    ResetAnimation(summon_clone, disable_interpolation=True)
    SetNetworkUpdateRate(summon_clone, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    OR_11.Add(HealthRatio(summon) <= 0.009999999776482582)
    OR_11.Add(HealthRatio(summon_clone) <= 0.009999999776482582)
    if OR_11:
        return
    if FlagDisabled(Flags.RadahnDead):
        DisplayFlashingMessage(text)
    GotoIfUnsignedEqual(Label.L3, left=summon, right=Characters.Patches)  # Patches cannot be summoned again anywhere
    EnableFlag(summon_point_used_flag)
    GotoIfFlagEnabled(Label.L3, flag=Flags.RadahnDead)
    AddSpecialEffect(summon, 4380)
    AddSpecialEffect(summon_clone, 4380)
    DisableFlag(summon_in_progress_flag)
    DisableFlag(summon_active_flag)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(summon)
    DisableCharacter(summon_clone)
    EnableFlag(summon_in_progress_flag)
    EnableFlag(summon_active_flag)
    End()


@RestartOnRest(1252382680)
def Event_1252382680(_, asset: uint):
    """Event 1252382680"""
    GotoIfFlagEnabled(Label.L0, flag=9411)
    GotoIfFlagEnabled(Label.L1, flag=Flags.RadahnDead)
    DisableAsset(asset)
    
    MAIN.Await(FlagEnabled(9411))

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAsset(asset)
    
    MAIN.Await(FlagEnabled(Flags.RadahnDead))

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAsset(asset)


@RestartOnRest(1252382695)
def Event_1252382695():
    """Event 1252382695"""
    DisableNetworkSync()
    DisableBackread(Characters.CastellanJerren)
    DisableBackread(Characters.BlaiddSummon)
    DisableBackread(Characters.AlexanderSummon)
    DisableBackread(Characters.GreatHornedTragoth)
    DisableBackread(Characters.Okina)
    DisableBackread(Characters.FingerMaidenTherolina)
    DisableBackread(Characters.LionelTheLionhearted)
    DisableBackread(Characters.Patches)
    if FlagEnabled(Flags.RadahnDead):
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=1052382695))
    
    EnableBackread(Characters.CastellanJerren)
    EnableBackread(Characters.BlaiddSummon)
    EnableBackread(Characters.AlexanderSummon)
    EnableBackread(Characters.GreatHornedTragoth)
    EnableBackread(Characters.Okina)
    EnableBackread(Characters.FingerMaidenTherolina)
    EnableBackread(Characters.LionelTheLionhearted)
    EnableBackread(Characters.Patches)
    SetBackreadStateAlternate(Characters.CastellanJerren, True)
    SetBackreadStateAlternate(Characters.BlaiddSummon, True)
    SetBackreadStateAlternate(Characters.AlexanderSummon, True)
    SetBackreadStateAlternate(Characters.GreatHornedTragoth, True)
    SetBackreadStateAlternate(Characters.Okina, True)
    SetBackreadStateAlternate(Characters.FingerMaidenTherolina, True)
    SetBackreadStateAlternate(Characters.LionelTheLionhearted, True)
    SetBackreadStateAlternate(Characters.Patches, True)
    OR_1.Add(CharacterOutsideRegion(character=PLAYER, region=1052382695))
    OR_1.Add(FlagEnabled(Flags.RadahnDead))
    
    MAIN.Await(OR_1)
    
    SetBackreadStateAlternate(Characters.CastellanJerren, False)
    SetBackreadStateAlternate(Characters.BlaiddSummon, False)
    SetBackreadStateAlternate(Characters.AlexanderSummon, False)
    SetBackreadStateAlternate(Characters.GreatHornedTragoth, False)
    SetBackreadStateAlternate(Characters.Okina, False)
    SetBackreadStateAlternate(Characters.FingerMaidenTherolina, False)
    SetBackreadStateAlternate(Characters.LionelTheLionhearted, False)
    SetBackreadStateAlternate(Characters.Patches, False)
    if FlagEnabled(Flags.RadahnDead):
        Wait(30.0)
    DisableBackread(Characters.CastellanJerren)
    DisableBackread(Characters.BlaiddSummon)
    DisableBackread(Characters.AlexanderSummon)
    DisableBackread(Characters.GreatHornedTragoth)
    DisableBackread(Characters.Okina)
    DisableBackread(Characters.FingerMaidenTherolina)
    DisableBackread(Characters.LionelTheLionhearted)
    DisableBackread(Characters.Patches)
    Wait(1.0)
    Restart()


@RestartOnRest(1252382696)
def Event_1252382696():
    """Event 1252382696"""
    if FlagEnabled(1252382699):
        return
    
    MAIN.Await(FlagEnabled(1252382183))
    
    EnableFlag(1252382699)


@RestartOnRest(1052382699)
def Event_1052382699():
    """Event 1052382699"""
    MAIN.Await(CharacterBackreadEnabled(Characters.CleanrotKnight))
    
    DisableCharacter(Characters.CleanrotKnight)
    DisableAnimations(Characters.CleanrotKnight)


@RestartOnRest(1252382800)
def RadahnDies():
    """Event 1252382800"""
    if FlagEnabled(Flags.RadahnDead):
        return

    AND_1.Add(HealthValue(Characters.StarscourgeRadahn) <= 0)
    AND_1.Add(HealthValue(Characters.CLONE_StarscourgeRadahn) <= 0)
    
    MAIN.Await(AND_1)
    
    Wait(4.0)
    PlaySoundEffect(Characters.StarscourgeRadahn, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(CharacterDead(Characters.StarscourgeRadahn))
    AND_2.Add(CharacterDead(Characters.CLONE_StarscourgeRadahn))
    AND_2.Add(CharacterAlive(PLAYER))
    
    MAIN.Await(AND_2)
    
    RemoveSpecialEffect(PLAYER, 13925)
    if PlayerInOwnWorld():
        AddSpecialEffect(PLAYER, 4280)
        AddSpecialEffect(PLAYER, 4282)
    SetNetworkUpdateRate(Characters.RadahnMeteorDummy, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_RadahnMeteorDummy, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.StarscourgeRadahn, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_StarscourgeRadahn, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    KillBossAndDisplayBanner(character=Characters.StarscourgeRadahn, banner_type=BannerType.DemigodFelled)
    if PlayerInOwnWorld():
        TriggerMultiplayerEvent(event_id=0)
    UnfreezeTime()
    EnableFlag(Flags.RadahnDead)
    EnableFlag(9130)
    if PlayerInOwnWorld():
        EnableFlag(61130)
    EnableFlag(9412)
    SetWeather(weather=Weather.Cloudless, duration=300.0, immediate_change=False)


@RestartOnRest(1252382810)
def RadahnBattleTrigger():
    """Event 1252382810"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.RadahnDead)
    DisableCharacter(Characters.StarscourgeRadahn)
    DisableAnimations(Characters.StarscourgeRadahn)
    Kill(Characters.StarscourgeRadahn)
    DisableCharacter(Characters.CLONE_StarscourgeRadahn)
    DisableAnimations(Characters.CLONE_StarscourgeRadahn)
    Kill(Characters.CLONE_StarscourgeRadahn)
    DisableCharacter(Characters.RadahnMeteorDummy)
    DisableAnimations(Characters.RadahnMeteorDummy)
    Kill(Characters.RadahnMeteorDummy)
    SetBackreadStateAlternate(Characters.RadahnMeteorDummy, False)
    SetTeamType(Characters.RadahnMeteorDummy, TeamType.NoTeam)
    DisableCharacter(Characters.CLONE_RadahnMeteorDummy)
    DisableAnimations(Characters.CLONE_RadahnMeteorDummy)
    Kill(Characters.CLONE_RadahnMeteorDummy)
    SetBackreadStateAlternate(Characters.CLONE_RadahnMeteorDummy, False)
    SetTeamType(Characters.CLONE_RadahnMeteorDummy, TeamType.NoTeam)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAnimations(Characters.RadahnMeteorDummy)
    DisableGravity(Characters.RadahnMeteorDummy)
    SetLockOnPoint(character=Characters.RadahnMeteorDummy, lock_on_model_point=220, state=False)
    SetTeamType(Characters.RadahnMeteorDummy, TeamType.NoTeam)
    DisableAI(Characters.RadahnMeteorDummy)
    SetDistanceBasedNetworkAuthorityUpdate(character=Characters.RadahnMeteorDummy, state=True)
    DisableAI(Characters.StarscourgeRadahn)
    DisableAI(Characters.CLONE_StarscourgeRadahn)
    SetDistanceBasedNetworkAuthorityUpdate(character=Characters.StarscourgeRadahn, state=True)
    SetDistanceBasedNetworkAuthorityUpdate(character=Characters.CLONE_StarscourgeRadahn, state=True)
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.StarscourgeRadahn, radius=220.0))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.CLONE_StarscourgeRadahn, radius=220.0))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterAlive(Characters.StarscourgeRadahn))
    AND_1.Add(CharacterAlive(Characters.CLONE_StarscourgeRadahn))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1252380801)
    SetBackreadStateAlternate(Characters.RadahnMeteorDummy, True)
    SetBackreadStateAlternate(Characters.StarscourgeRadahn, True)
    SetBackreadStateAlternate(Characters.CLONE_StarscourgeRadahn, True)
    SetNetworkUpdateRate(Characters.RadahnMeteorDummy, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.StarscourgeRadahn, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_StarscourgeRadahn, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(Characters.StarscourgeRadahn)
    EnableAI(Characters.CLONE_StarscourgeRadahn)
    AddSpecialEffect(PLAYER, 13925)
    AddSpecialEffect(Characters.StarscourgeRadahn, 13918)
    AddSpecialEffect(Characters.CLONE_StarscourgeRadahn, 13918)
    AND_5.Add(CharacterAlive(Characters.StarscourgeRadahn))
    AND_5.Add(CharacterAlive(Characters.CLONE_StarscourgeRadahn))
    AND_5.Add(CharacterBackreadEnabled(Characters.StarscourgeRadahn))
    AND_5.Add(CharacterBackreadEnabled(Characters.CLONE_StarscourgeRadahn))
    AND_5.Add(HasAIStatus(Characters.StarscourgeRadahn, ai_status=AIStatusType.Battle))
    AND_5.Add(HasAIStatus(Characters.CLONE_StarscourgeRadahn, ai_status=AIStatusType.Battle))
    
    MAIN.Await(AND_5)
    
    EnableBossHealthBar(Characters.StarscourgeRadahn, name=NameText.StarscourgeRadahn, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_StarscourgeRadahn, name=NameText.CLONE_StarscourgeRadahn, bar_slot=0)
    EnableNetworkFlag(Flags.RadahnMusicTrigger)


@RestartOnRest(1252382820)
def RadahnPhaseTwoTransition(_, radahn: uint, radahn_meteor_dummy: uint):
    """Event 1252382820"""
    if FlagEnabled(Flags.RadahnDead):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(radahn, 13906))  # at the top of Radahn's leap
    
    MAIN.Await(AND_1)
    
    DisableAI(radahn)
    DisableCharacter(radahn)
    DisableAnimations(radahn)
    AddSpecialEffect(radahn, 13918)
    GotoIfFlagEnabled(Label.L0, flag=Flags.RadahnPhaseTwoTransitionFinished)
    SetWeather(weather=Weather.Cloudless, duration=-1.0, immediate_change=False)
    EnableNetworkFlag(Flags.RadahnPhaseTwoMusicTrigger)  # music doesn't care which Radahn transitions first

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(5.0)
    GotoIfMultiplayer(Label.L2)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=radahn, radius=200.0))
    GotoIfConditionFalse(Label.L2, input_condition=AND_2)
    SetNetworkUpdateAuthority(radahn, authority_level=UpdateAuthority.Forced)
    AND_3.Add(CharacterOutsideRegion(character=PLAYER, region=1052382298))
    GotoIfConditionTrue(Label.L1, input_condition=AND_3)
    Move(
        radahn_meteor_dummy,
        destination=PLAYER,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=PLAYER,
    )
    RotateToFaceEntity(radahn_meteor_dummy, RegionVolumes.RadahnMeteorDummyRotation, wait_for_completion=True)
    RotateToFaceEntity(radahn_meteor_dummy, RegionVolumes.RadahnMeteorDummyRotation, wait_for_completion=True)
    Wait(1.0)
    Move(
        radahn,
        destination=radahn_meteor_dummy,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=radahn_meteor_dummy,
    )
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    Move(
        radahn,
        destination=PLAYER,
        destination_type=CoordEntityType.Character,
        model_point=229,
        copy_draw_parent=PLAYER,
    )

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(radahn)
    EnableAnimations(radahn)
    EnableAI(radahn)
    ForceAnimation(radahn, 3037)
    if FlagDisabled(Flags.RadahnPhaseTwoTransitionFinished):
        EnableNetworkFlag(Flags.RadahnPhaseTwoTransitionFinished)
    Wait(1.0)
    Restart()


@RestartOnRest(1252382850)
def RadahnMusicControl():
    """Event 1252382850"""
    CommonFunc_BossMusicPhaseTransition(
        0,
        dead_flag=Flags.RadahnDead,
        bgm_boss_conv_param_id=473000,
        host_in_battle=Flags.HostInRadahnBattle,
        summon_in_battle=Flags.SummonInRadahnBattle,
        extra_required_flag=Flags.RadahnMusicTrigger,
        phase_two_flag=Flags.RadahnPhaseTwoMusicTrigger,
        useless_phase_two_check=0,
        use_stop_type_1=1,
    )


@RestartOnRest(1252382860)
def SetWailingDunesTime():
    """Event 1252382860"""
    if FlagEnabled(Flags.RadahnDead):
        return
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L0, flag=9411)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetCurrentTime(
        time=(3, 30, 0),
        fade_transition=False,
        wait_for_completion=False,
        show_clock=False,
        clock_start_delay=0.0,
        clock_change_duration=0.0,
        clock_finish_delay=0.0,
    )


@RestartOnRest(1252380700)
def Event_1252380700(_, character: uint):
    """Event 1252380700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3600):
        DisableFlag(1052389302)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L13, flag=3613)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3613))
    
    Restart()

    # --- Label 13 --- #
    DefineLabel(13)
    GotoIfFlagEnabled(Label.L0, flag=3600)
    GotoIfFlagEnabled(Label.L1, flag=3601)
    GotoIfFlagEnabled(Label.L3, flag=3603)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableBackread(character)
    DisableCharacter(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3613))
    
    Restart()


@RestartOnRest(1252380705)
def Event_1252380705(_, character: uint):
    """Event 1252380705"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3660):
        DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3668)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3668))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3660)
    GotoIfFlagEnabled(Label.L2, flag=3661)
    GotoIfFlagEnabled(Label.L4, flag=3663)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930012)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3668))
    
    Restart()


@RestartOnRest(1252380710)
def Event_1252380710():
    """Event 1252380710"""
    WaitFrames(frames=1)
    EnableFlag(1052389200)
    if FlagDisabled(7606):
        return
    DisableFlag(1052389200)
    End()


@RestartOnRest(1252380720)
def Event_1252380720():
    """Event 1252380720"""
    WaitFrames(frames=1)
    DisableFlag(1052389250)
    if FlagDisabled(31009206):
        return
    if FlagEnabled(3681):
        return
    if FlagEnabled(3683):
        return
    EnableFlag(1052389250)
    End()
