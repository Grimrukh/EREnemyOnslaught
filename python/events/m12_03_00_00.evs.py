"""DONE
Deeproot Depths

linked:
0
82

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: 
168: 
170: 
172: 
174: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m12_03_00_00_entities import *
from .entities.m12_02_00_00_entities import Assets as m12_02_Assets


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=71231, asset=Assets.AEG099_060_9001)
    RegisterGrace(grace_flag=71232, asset=Assets.AEG099_060_9002)
    RegisterGrace(grace_flag=71233, asset=Assets.AEG099_060_9003)
    RegisterGrace(grace_flag=71234, asset=Assets.AEG099_060_9004)
    RegisterGrace(grace_flag=71235, asset=Assets.AEG099_060_9005)
    CommonFunc_RegisterGraceIfFlagEnabled(
        0,
        flag=Flags.FiasChampionsDead,
        grace_flag=71230,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    FiasChampionsDie()
    FiasChampionsBattleTrigger()
    SorcererRogierTransition()
    LionelTheLionheartedTransition()
    FiasChampionsCommonEvents()
    Event_12032841()

    LichdragonFortissaxDies()
    LichdragonFortissaxBattleTrigger()
    TravelToFortissaxBattle()
    LichdragonFortissaxCommonEvents()
    FortissaxLightning(0, Characters.LichdragonFortissax)
    FortissaxLightning(2, Characters.CLONE_LichdragonFortissax)  # 12032863
    LichdragonFortissaxPhaseTwoTransition()

    Event_12032310(0, character=Characters.GiantAnt14)
    Event_12032310(1, character=Characters.GiantAnt15)
    Event_12032310(2, character=Characters.GiantAnt16)
    Event_12032310(3, character=Characters.GiantAnt17)
    Event_12032310(4, character=Characters.GiantAnt18)
    Event_12032310(5, character=Characters.GiantAnt19)
    Event_12032310(6, character=Characters.GiantAnt20)
    Event_12032310(7, character=Characters.GiantAnt21)
    Event_12032310(8, character=Characters.GiantAnt22)
    Event_12032310(9, character=Characters.GiantAnt23)
    Event_12032310(10, character=Characters.GiantAnt24)
    Event_12032310(11, character=Characters.GiantAnt25)
    Event_12032310(12, character=Characters.GiantAnt26)
    Event_12032310(13, character=Characters.GiantAnt27)
    Event_12032310(14, character=Characters.GiantAnt28)
    Event_12032310(15, character=Characters.GiantAnt29)
    Event_12032310(16, character=Characters.GiantAnt30)
    Event_12032310(17, character=Characters.GiantAnt31)
    Event_12032241(0, character=Characters.GiantAnt16, seconds=0.0)
    Event_12032241(1, character=Characters.GiantAnt17, seconds=0.0)
    Event_12032241(2, character=Characters.GiantAnt18, seconds=8.0)
    Event_12032241(3, character=Characters.GiantAnt19, seconds=0.0)
    Event_12032241(4, character=Characters.GiantAnt20, seconds=9.0)
    Event_12032241(5, character=Characters.GiantAnt21, seconds=9.0)
    Event_12032241(6, character=Characters.GiantAnt22, seconds=15.5)
    Event_12032241(7, character=Characters.GiantAnt23, seconds=16.0)
    Event_12032241(8, character=Characters.GiantAnt24, seconds=16.0)
    Event_12032241(9, character=Characters.GiantAnt25, seconds=28.0)
    Event_12032241(10, character=Characters.GiantAnt26, seconds=28.0)
    Event_12032241(11, character=Characters.GiantAnt27, seconds=28.0)
    Event_12032241(12, character=Characters.GiantAnt28, seconds=25.0)
    Event_12032241(13, character=Characters.GiantAnt29, seconds=20.0)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0, character=12030200, region=12032200, radius=50.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0, character=Characters.GiantAnt1, region=12032200, radius=50.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0, character=Characters.GiantAnt2, region=12032200, radius=50.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0, character=Characters.GiantAnt3, region=12032200, radius=50.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0, character=Characters.GiantAnt4, region=12032200, radius=50.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0, character=Characters.GiantAnt5, region=12032200, radius=50.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=12030240,
        character=Characters.GiantAnt14,
        item_lot=12030800,
        reward_delay=1.5,
        skip_reward=0,
        clone=0,
    )
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=12030241,
        character=Characters.GiantAnt15,
        item_lot=12030810,
        reward_delay=1.5,
        skip_reward=0,
        clone=0,
    )
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=12030256,
        character=Characters.GiantAnt30,
        item_lot=12030820,
        reward_delay=1.5,
        skip_reward=0,
        clone=0,
    )
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=12030257,
        character=Characters.GiantAnt31,
        item_lot=12030830,
        reward_delay=1.5,
        skip_reward=0,
        clone=0,
    )
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=12030297,
        character=Characters.GiantAnt13,
        item_lot=12030840,
        reward_delay=1.5,
        skip_reward=0,
        clone=0,
    )
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=12030201,
        character=Characters.GiantAnt0,
        item_lot=12030850,
        reward_delay=1.5,
        skip_reward=0,
        clone=0,
    )
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=12030303, radius=8.0, seconds=0.0, animation_id=-1)
    CommonFunc_NonRespawningWithReward(
        0, dead_flag=12030350, character=Characters.Scarab0, item_lot=40660, reward_delay=1.5, skip_reward=0,
        clone=0,
    )
    CommonFunc_NonRespawningWithReward(
        0, dead_flag=12030354, character=Characters.Scarab1, item_lot=40668, reward_delay=1.5, skip_reward=0,
        clone=0,
    )
    CommonFunc_NonRespawningWithReward(
        0, dead_flag=12030355, character=Characters.Scarab2, item_lot=40670, reward_delay=1.5, skip_reward=0,
        clone=0,
    )
    CommonFunc_FieldBossNonRespawningWithReward(
        0,
        dead_flag=12030390,
        extra_flag_to_enable=0,
        boss=Characters.CrucibleKnightSiluria,
        boss_banner_choice=1,
        item_lot=12030950,
        seconds=0.0,
        clone_boss=Characters.CLONE_CrucibleKnightSiluria,
    )
    CommonFunc_FieldBossMusicHealthBar(
        0, boss=Characters.CrucibleKnightSiluria, name=NameText.CrucibleKnightSiluria, npc_threat_level=12,
        clone_boss=Characters.CLONE_CrucibleKnightSiluria, clone_name=NameText.CLONE_CrucibleKnightSiluria,
    )
    CommonFunc_FieldBossMusicHeatUp(
        0, boss=Characters.CrucibleKnightSiluria, npc_threat_level=12, optional_trigger_flag=0
    )
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=Flags.ErdtreeAvatarDead,
        character=Characters.ErdtreeAvatar,
        item_lot=12030960,
        reward_delay=1.5,
        skip_reward=0,
        clone=Characters.CLONE_ErdtreeAvatar,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.ErdtreeAvatar, region=12032391, seconds=0.0, animation_id=-1
    )
    Event_12032504()
    Event_12032509()
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.WalkingMausoleum, radius=200.0, seconds=10.0, animation_id=-1
    )
    CommonFunc_MausoleumAssetDestruction(0, mausoleum=Characters.WalkingMausoleum, asset_group=12036420)
    CommonFunc_90005452(0, character=Characters.WalkingMausoleum, flag=12030400)
    CommonFunc_90005454(0, character=Characters.WalkingMausoleum, flag=12032400, flag_1=12030400)
    CommonFunc_90005456(
        0,
        character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_004_9000,
        asset_1=Assets.AEG300_005_9000,
        flag=12030400,
    )
    CommonFunc_WalkingMausoleumDefeated(0, mausoleum=Characters.WalkingMausoleum, asset=Assets.AEG300_015_9000)
    CommonFunc_90005453(
        0, asset__character=Characters.WalkingMausoleum, asset=Assets.AEG300_006_9000, model_point=60, seconds=0.0
    )
    CommonFunc_90005453(
        1,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9001,
        model_point=61,
        seconds=0.10000000149011612,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9002,
        model_point=62,
        seconds=0.20000000298023224,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9003,
        model_point=63,
        seconds=0.30000001192092896,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9004,
        model_point=64,
        seconds=0.4000000059604645,
    )
    CommonFunc_90005453(
        0, asset__character=Characters.WalkingMausoleum, asset=Assets.AEG300_006_9005, model_point=65, seconds=0.5
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9006,
        model_point=66,
        seconds=0.6000000238418579,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9007,
        model_point=67,
        seconds=0.699999988079071,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9008,
        model_point=68,
        seconds=0.800000011920929,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9009,
        model_point=69,
        seconds=0.8999999761581421,
    )
    CommonFunc_90005453(
        0, asset__character=Characters.WalkingMausoleum, asset=Assets.AEG300_006_9010, model_point=70, seconds=1.0
    )
    CommonFunc_90005453(
        0, asset__character=Characters.WalkingMausoleum, asset=12031431, model_point=71, seconds=0.10000000149011612
    )
    CommonFunc_90005453(
        0, asset__character=Characters.WalkingMausoleum, asset=12031432, model_point=72, seconds=0.20000000298023224
    )
    CommonFunc_90005453(
        0, asset__character=Characters.WalkingMausoleum, asset=12031433, model_point=73, seconds=0.30000001192092896
    )
    CommonFunc_90005453(
        0, asset__character=Characters.WalkingMausoleum, asset=12031434, model_point=74, seconds=0.4000000059604645
    )
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=12031435, model_point=75, seconds=0.5)
    Event_12032300(0, character=12035380, seconds=1.0)
    Event_12032500()
    Event_12030050()
    CommonFunc_MakeNPCHostile(
        0,
        npc=Characters.DHunteroftheDead,
        flag=4061,
        required_flag=4060,
        hostile_flag=12039001,
        hostile_hits=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.DHunteroftheDead,
        flag=4061,
        flag_1=4062,
        flag_2=12039001,
        flag_3=4061,
        first_flag=4060,
        last_flag=4063,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.DHunteroftheDead, flag=4063, first_flag=4060, last_flag=4063)
    Event_12030710(0, character=Characters.DHunteroftheDead)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9001,
        action_button_id=4350,
        item_lot=103410,
        first_flag=400348,
        last_flag=400348,
        flag=4067,
        model_point=0,
    )
    CommonFunc_MakeNPCHostile(
        0,
        npc=Characters.FiaDeathbedCompanion2,
        flag=4121,
        required_flag=4120,
        hostile_flag=12039051,
        hostile_hits=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.FiaDeathbedCompanion2,
        flag=4121,
        flag_1=4122,
        flag_2=12039051,
        flag_3=4121,
        first_flag=4120,
        last_flag=4123,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.FiaDeathbedCompanion2, flag=4123, first_flag=4120, last_flag=4123)
    Event_12030700(0, character=Characters.FiaDeathbedCompanion2)
    Event_12030701(0, character=Characters.FiaDeathbedCompanion0, asset=Assets.AEG099_320_9003)
    Event_12030702(0, character=Characters.FiaDeathbedCompanion3)
    Event_12030703(
        0,
        character=Characters.FiaDeathbedCompanion1,
        asset=Assets.AEG099_422_9000,
        asset_1=Assets.AEG099_429_9000,
    )
    Event_12030709(0, flag=12039179)
    Event_12030704()
    Event_12030705()
    Event_12030706()
    CommonFunc_90005740(
        0,
        flag=12032715,
        flag_1=12032716,
        left=12032717,
        character=Characters.FiaDeathbedCompanion2,
        model_point=702,
        asset=Assets.AEG099_090_9003,
        model_point_1=702,
        radius=0.4000000059604645,
        animation=90305,
        animation_id=90307,
        special_effect=-1,
        radius_1=1.2999999523162842,
    )
    CommonFunc_90005741(
        0,
        flag=12032718,
        flag_1=12032719,
        left=12032717,
        character=Characters.FiaDeathbedCompanion2,
        animation__animation_id=90330,
        left_1=0,
        animation_id=90332,
        special_effect=-1,
        seconds=0.5,
    )
    Event_12030707()
    Event_12030708(0, entity=Characters.FiaDeathbedCompanion2)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9002,
        action_button_id=6460,
        item_lot=103350,
        first_flag=9502,
        last_flag=9502,
        flag=4131,
        model_point=806781,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9002,
        action_button_id=4110,
        item_lot=113300,
        first_flag=400339,
        last_flag=400339,
        flag=12039162,
        model_point=0,
    )
    CommonFunc_90005733(0, flag=12032714)
    CommonFunc_90005740(
        0,
        flag=12032725,
        flag_1=12032726,
        left=0,
        character=Characters.FiaDeathbedCompanion0,
        model_point=0,
        asset=0,
        model_point_1=0,
        radius=1.2999999523162842,
        animation=90305,
        animation_id=90307,
        special_effect=-1,
        radius_1=1.2999999523162842,
    )
    CommonFunc_90005752(0, asset=Assets.AEG099_320_9003, vfx_id=200, model_point=120, seconds=3.0)
    Event_12030720(0, 12030725)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.FiaDeathbedCompanion0)
    DisableBackread(Characters.FiaDeathbedCompanion1)
    DisableBackread(Characters.FiaDeathbedCompanion2)
    DisableBackread(Characters.FiaDeathbedCompanion3)
    DisableBackread(12030705)
    DisableBackread(Characters.DHunteroftheDead)
    DisableBackread(12030715)
    DisableBackread(12030720)
    DisableBackread(12030721)
    DisableBackread(Characters.FingerReader)
    DisableAsset(Assets.AEG099_320_9003)
    GetFiasChampionPlayerData()
    CommonFunc_PrepareWalkingMausoleum(0, Characters.WalkingMausoleum, 12031400, 12031410, 12031418)


@RestartOnRest(12030050)
def Event_12030050():
    """Event 12030050"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(12030401)
    DisableFlag(12030402)


@RestartOnRest(12032400)
def Event_12032400():
    """Event 12032400"""
    if ThisEventSlotFlagEnabled():
        return
    SetNetworkUpdateRate(Characters.WalkingMausoleum, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(12032500)
def Event_12032500():
    """Event 12032500"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(12032501)
    DisableFlag(12032502)
    DisableFlag(12032504)
    if ThisEventSlotFlagDisabled():
        DeleteAssetVFX(Assets.AEG099_510_9000)
        DisableFlag(12032503)
        WaitFrames(frames=1)
    OR_11.Add(Multiplayer())
    OR_11.Add(MultiplayerPending())
    SkipLinesIfConditionFalse(1, OR_11)
    EnableFlag(12032504)
    OR_10.Add(Multiplayer())
    OR_10.Add(MultiplayerPending())
    OR_10.Add(FlagDisabled(182))
    OR_10.Add(FlagDisabled(105))
    OR_10.Add(FlagEnabled(300))
    OR_10.Add(FlagDisabled(Flags.FiasChampionsDead))
    OR_10.Add(FlagEnabled(12032870))
    GotoIfConditionTrue(Label.L1, input_condition=OR_10)
    GotoIfFlagEnabled(Label.L1, flag=12032503)
    CreateAssetVFX(Assets.AEG099_510_9000, vfx_id=200, model_point=806870)
    EnableFlag(12032503)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(ActionButtonParamActivated(action_button_id=9140, entity=Assets.AEG099_510_9000))
    OR_4.Add(Multiplayer())
    OR_4.Add(MultiplayerPending())
    OR_4.Add(FlagDisabled(182))
    OR_4.Add(FlagDisabled(105))
    OR_4.Add(FlagEnabled(300))
    AND_4.Add(OR_4)
    AND_4.Add(FlagEnabled(12032503))
    AND_7.Add(FlagEnabled(12032504))
    OR_8.Add(Multiplayer())
    OR_8.Add(MultiplayerPending())
    AND_7.Add(not OR_8)
    AND_7.Add(FlagDisabled(12032503))
    OR_9.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 182))
    OR_9.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 105))
    OR_9.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 300))
    OR_9.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 12032870))
    OR_9.Add(FlagState(FlagSetting.Change, FlagType.Absolute, Flags.FiasChampionsDead))
    AND_9.Add(OR_9)
    OR_14.Add(AND_1)
    OR_14.Add(AND_4)
    OR_14.Add(AND_7)
    OR_14.Add(AND_9)

    MAIN.Await(OR_14)

    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_1)
    GotoIfFinishedConditionFalse(Label.L2, input_condition=AND_4)
    DeleteAssetVFX(Assets.AEG099_510_9000)
    DisableFlag(12032503)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(0.032999999821186066)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L10, flag=Flags.FiasChampionsDead)
    GotoIfFlagEnabled(Label.L10, flag=12032870)
    GotoIfFlagEnabled(Label.L10, flag=300)
    GotoIfFlagDisabled(Label.L4, flag=182)
    GotoIfFlagEnabled(Label.L5, flag=105)

    # --- Label 4 --- #
    DefineLabel(4)
    DisplayDialog(text=20004, anchor_entity=Assets.AEG099_510_9000, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    DisplayDialog(text=30040, anchor_entity=Assets.AEG099_510_9000, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    DisplayDialogAndSetFlags(
        message=4300,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=Assets.AEG099_510_9000,
        display_distance=3.0,
        left_flag=12032501,
        right_flag=12032502,
        cancel_flag=12032502,
    )
    GotoIfFlagEnabled(Label.L6, flag=12032501)
    Wait(1.0)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    OR_15.Add(Multiplayer())
    OR_15.Add(MultiplayerPending())
    if OR_15:
        return RESTART
    RotateToFaceEntity(PLAYER, Assets.AEG099_510_9000, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490)
    EnableFlag(11000600)
    EnableFlag(11000603)
    Wait(3.0)
    WarpToMap(game_map=LEYNDELL_ROYAL_CAPITAL, player_start=11002500)
    Restart()

    # --- Label 16 --- #
    DefineLabel(16)

    MAIN.Await(FlagEnabled(Flags.FiasChampionsDead))

    Restart()

    # --- Label 18 --- #
    DefineLabel(18)
    DeleteAssetVFX(Assets.AEG099_510_9000)

    MAIN.Await(FlagDisabled(12032870))

    Restart()


@ContinueOnRest(12032504)
def Event_12032504():
    """Event 12032504"""
    if PlayerNotInOwnWorld():
        return
    DisableNetworkSync()
    AddSpecialEffect(PLAYER, 191)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9710, entity=Assets.AEG237_018_0500))

    MAIN.Await(AND_1)

    AddSpecialEffect(PLAYER, 190)
    Wait(0.10000000149011612)
    EnableFlag(9021)
    BanishPhantoms(unknown=0)

    # --- Label 5 --- #
    DefineLabel(5)
    Wait(1.0)
    GotoIfMultiplayer(Label.L5)
    SetRespawnPoint(respawn_point=12012504)
    SaveRequest()
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=12030010,
        cutscene_flags=0,
        move_to_region=12012504,
        map_id=12010000,
        player_id=PLAYER,
        unk_20_24=12030000,
        unk_24_25=False,
    )
    WaitFramesAfterCutscene(frames=1)
    PlayCutscene(12030011, cutscene_flags=CutsceneFlags.Unknown16, player_id=PLAYER)
    WaitFramesAfterCutscene(frames=1)
    AddSpecialEffect(PLAYER, 191)
    Wait(1.0)
    DisplayAreaWelcomeMessage(text=12010)


@ContinueOnRest(12032509)
def Event_12032509():
    """Event 12032509"""
    DisableNetworkSync()
    AND_2.Add(FlagEnabled(12020800))
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(ActionButtonParamActivated(action_button_id=9710, entity=m12_02_Assets.AEG237_018_5000))

    MAIN.Await(AND_2)

    EnableFlag(12020502)
    Wait(0.10000000149011612)
    EnableFlag(9021)
    SetRespawnPoint(respawn_point=12032502)
    SaveRequest()
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=12020000,
        cutscene_flags=0,
        move_to_region=12032502,
        map_id=12030000,
        player_id=PLAYER,
        unk_20_24=12020000,
        unk_24_25=False,
    )
    PlayCutscene(12020001, cutscene_flags=CutsceneFlags.Unknown16, player_id=PLAYER)
    WaitFrames(frames=1)
    Wait(1.0)
    DisplayAreaWelcomeMessage(text=12030)


@RestartOnRest(12032300)
def Event_12032300(_, character: uint, seconds: float):
    """Event 12032300"""
    GotoIfFlagDisabled(Label.L0, flag=12030400)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagEnabled(12030400))

    MAIN.Await(OR_1)

    Wait(seconds)
    Kill(character)


@RestartOnRest(12032310)
def Event_12032310(_, character: uint):
    """Event 12032310"""
    if FlagEnabled(12032240):
        return
    DisableFlag(12032240)
    AddSpecialEffect(character, 10949)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=12032240))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)

    MAIN.Await(OR_2)

    EnableFlag(12032240)


@RestartOnRest(12032241)
def Event_12032241(_, character: uint, seconds: float):
    """Event 12032241"""
    SetTeamType(12035240, TeamType.Enemy)
    SetTeamType(12035241, TeamType.Enemy)
    SetTeamType(12035256, TeamType.Enemy)
    SetTeamType(12035257, TeamType.Enemy)
    SetTeamType(character, TeamType.Enemy)
    AddSpecialEffect(character, 2900)
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    ForceAnimation(character, 30001, loop=True)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(FlagEnabled(12032240))

    MAIN.Await(OR_2)

    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    Wait(seconds)
    ForceAnimation(character, 20001, loop=True)
    End()


@RestartOnRest(12032800)
def FiasChampionsDie():
    """Event 12032800"""
    if FlagEnabled(Flags.FiasChampionsDead):
        return
    AND_1.Add(HealthValue(Characters.FirstFiasChampion) <= 0)
    AND_1.Add(HealthValue(Characters.SorcererRogier) <= 0)
    AND_1.Add(HealthValue(Characters.LioneltheLionhearted) <= 0)
    AND_1.Add(HealthValue(Characters.LionelSidekick2) <= 0)
    AND_1.Add(HealthValue(Characters.LionelSidekick1) <= 0)
    # Clones are immortal and refer their damage to the originals.

    MAIN.Await(AND_1)

    Wait(1.0)
    PlaySoundEffect(Characters.FirstFiasChampion, 888880000, sound_type=SoundType.s_SFX)
    DisableCharacter(Characters.UnknownFiasChampion)
    AND_2.Add(CharacterDead(Characters.FirstFiasChampion))
    AND_2.Add(CharacterDead(Characters.SorcererRogier))
    AND_2.Add(CharacterDead(Characters.LioneltheLionhearted))
    AND_2.Add(CharacterDead(Characters.LionelSidekick2))
    AND_2.Add(CharacterDead(Characters.LionelSidekick1))
    AND_2.Add(CharacterDead(Characters.CLONE_FiasChampion0))
    AND_2.Add(CharacterDead(Characters.CLONE_SorcererRogier))
    AND_2.Add(CharacterDead(Characters.CLONE_LioneltheLionhearted))
    AND_2.Add(CharacterDead(Characters.CLONE_LionelSidekick2))
    AND_2.Add(CharacterDead(Characters.CLONE_LionelSidekick1))

    MAIN.Await(AND_2)

    KillBossAndDisplayBanner(character=Characters.FirstFiasChampion, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(Flags.FiasChampionsDead)
    EnableTreasure(asset=12031490)
    DisableAsset(Assets.AEG099_120_9000)
    DeleteAssetVFX(Assets.AEG099_120_9000)
    EnableFlag(9135)
    EnableFlag(61135)


@RestartOnRest(12032810)
def FiasChampionsBattleTrigger():
    """Event 12032810"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.FiasChampionsDead)
    DisableCharacter(Characters.FirstFiasChampion)
    DisableAnimations(Characters.FirstFiasChampion)
    Kill(Characters.FirstFiasChampion)
    DisableCharacter(Characters.SorcererRogier)
    DisableAnimations(Characters.SorcererRogier)
    Kill(Characters.SorcererRogier)
    DisableCharacter(Characters.LioneltheLionhearted)
    DisableAnimations(Characters.LioneltheLionhearted)
    Kill(Characters.LioneltheLionhearted)
    DisableCharacter(Characters.LionelSidekick2)
    DisableAnimations(Characters.LionelSidekick2)
    Kill(Characters.LionelSidekick2)
    DisableCharacter(Characters.LionelSidekick1)
    DisableAnimations(Characters.LionelSidekick1)
    Kill(Characters.LionelSidekick1)
    DisableCharacter(Characters.UnknownFiasChampion)
    DisableAnimations(Characters.UnknownFiasChampion)
    Kill(Characters.UnknownFiasChampion)
    DisableCharacter(Characters.CLONE_FiasChampion0)
    DisableAnimations(Characters.CLONE_FiasChampion0)
    Kill(Characters.CLONE_FiasChampion0)
    DisableCharacter(Characters.CLONE_SorcererRogier)
    DisableAnimations(Characters.CLONE_SorcererRogier)
    Kill(Characters.CLONE_SorcererRogier)
    DisableCharacter(Characters.CLONE_LioneltheLionhearted)
    DisableAnimations(Characters.CLONE_LioneltheLionhearted)
    Kill(Characters.CLONE_LioneltheLionhearted)
    DisableCharacter(Characters.CLONE_LionelSidekick2)
    DisableAnimations(Characters.CLONE_LionelSidekick2)
    Kill(Characters.CLONE_LionelSidekick2)
    DisableCharacter(Characters.CLONE_LionelSidekick1)
    DisableAnimations(Characters.CLONE_LionelSidekick1)
    Kill(Characters.CLONE_LionelSidekick1)
    DisableCharacter(Characters.CLONE_UnknownFiasChampion)
    DisableAnimations(Characters.CLONE_UnknownFiasChampion)
    Kill(Characters.CLONE_UnknownFiasChampion)
    EnableTreasure(asset=12031490)
    DisableAsset(Assets.AEG099_120_9000)
    DeleteAssetVFX(Assets.AEG099_120_9000, erase_root=False)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.FirstFiasChampion)
    DisableAI(Characters.SorcererRogier)
    DisableAI(Characters.LioneltheLionhearted)
    DisableAI(Characters.LionelSidekick2)
    DisableAI(Characters.LionelSidekick1)
    DisableAI(Characters.UnknownFiasChampion)
    DisableCharacter(Characters.FirstFiasChampion)
    DisableCharacter(Characters.SorcererRogier)
    DisableCharacter(Characters.LioneltheLionhearted)
    DisableCharacter(Characters.LionelSidekick2)
    DisableCharacter(Characters.LionelSidekick1)
    DisableCharacter(Characters.UnknownFiasChampion)
    DisableAI(Characters.CLONE_FiasChampion0)
    DisableAI(Characters.CLONE_SorcererRogier)
    DisableAI(Characters.CLONE_LioneltheLionhearted)
    DisableAI(Characters.CLONE_LionelSidekick2)
    DisableAI(Characters.CLONE_LionelSidekick1)
    DisableAI(Characters.CLONE_UnknownFiasChampion)
    DisableCharacter(Characters.CLONE_FiasChampion0)
    DisableCharacter(Characters.CLONE_SorcererRogier)
    DisableCharacter(Characters.CLONE_LioneltheLionhearted)
    DisableCharacter(Characters.CLONE_LionelSidekick2)
    DisableCharacter(Characters.CLONE_LionelSidekick1)
    DisableCharacter(Characters.CLONE_UnknownFiasChampion)
    DisableTreasure(asset=12031490)
    DisableAsset(Assets.AEG099_120_9000)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=12032801))

    MAIN.Await(AND_2)

    EnableFlag(12030801)
    EnableFlag(12032803)
    DeleteAssetVFX(Assets.AEG099_120_9000)
    EnableAsset(Assets.AEG099_120_9000)
    CreateAssetVFX(Assets.AEG099_120_9000, vfx_id=200, model_point=806700)
    CreateTemporaryVFX(
        vfx_id=600940,
        anchor_entity=Characters.FirstFiasChampion,
        model_point=900,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600940,
        anchor_entity=Characters.CLONE_FiasChampion0,
        model_point=900,
        anchor_type=CoordEntityType.Character,
    )
    Wait(0.5)
    if FlagEnabled(50):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23611,
            target_character=Characters.FirstFiasChampion,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23611,
            target_character=Characters.CLONE_FiasChampion0,
        )
        Goto(Label.L8)
    if FlagEnabled(51):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23612,
            target_character=Characters.FirstFiasChampion,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23612,
            target_character=Characters.CLONE_FiasChampion0,
        )
        Goto(Label.L8)
    if FlagEnabled(52):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23613,
            target_character=Characters.FirstFiasChampion,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23613,
            target_character=Characters.CLONE_FiasChampion0,
        )
        Goto(Label.L8)
    if FlagEnabled(52):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23614,
            target_character=Characters.FirstFiasChampion,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23614,
            target_character=Characters.CLONE_FiasChampion0,
        )
        Goto(Label.L8)
    if FlagEnabled(54):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23615,
            target_character=Characters.FirstFiasChampion,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23615,
            target_character=Characters.CLONE_FiasChampion0,
        )
        Goto(Label.L8)
    if FlagEnabled(55):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23616,
            target_character=Characters.FirstFiasChampion,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23616,
            target_character=Characters.CLONE_FiasChampion0,
        )
        Goto(Label.L8)
    if FlagEnabled(56):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23617,
            target_character=Characters.FirstFiasChampion,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23617,
            target_character=Characters.CLONE_FiasChampion0,
        )
        Goto(Label.L8)
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=0,
        failcase_player_param_id=23618,
        target_character=Characters.FirstFiasChampion,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=0,
        failcase_player_param_id=23618,
        target_character=Characters.CLONE_FiasChampion0,
    )

    # --- Label 8 --- #
    DefineLabel(8)
    WaitFrames(frames=1)
    EnableCharacter(Characters.FirstFiasChampion)
    EnableCharacter(Characters.CLONE_FiasChampion0)
    EnableCharacter(Characters.UnknownFiasChampion)
    EnableCharacter(Characters.CLONE_UnknownFiasChampion)
    WaitFrames(frames=1)
    ForceAnimation(Characters.FirstFiasChampion, 63010)
    ForceAnimation(Characters.CLONE_FiasChampion0, 63010)
    EnableAI(Characters.FirstFiasChampion)
    EnableAI(Characters.CLONE_FiasChampion0)
    SetNetworkUpdateRate(Characters.FirstFiasChampion, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_FiasChampion0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableImmortality(Characters.CLONE_FiasChampion0)
    DisableHealthBar(Characters.CLONE_FiasChampion0)
    ReferDamageToEntity(Characters.CLONE_FiasChampion0, Characters.FirstFiasChampion)
    Wait(3.0)
    EnableBossHealthBar(Characters.FirstFiasChampion, name=NameText.FiasChampion0)
    # TODO: Second health bar? Or refer clone damage to original?
    WaitFrames(frames=1)
    EnableNetworkFlag(Flags.FiasChampionsBattleStarted)


@RestartOnRest(12032811)
def SorcererRogierTransition():
    """Event 12032811"""
    if FlagEnabled(Flags.FiasChampionsDead):
        return
    # NEW: Handle referred-damage clone.
    AND_2.Add(HealthValue(Characters.FirstFiasChampion) <= 0)
    AND_2.Add(FlagEnabled(Flags.FiasChampionsBattleStarted))
    MAIN.Await(AND_2)

    Kill(Characters.CLONE_FiasChampion0)

    AND_1.Add(CharacterDead(Characters.FirstFiasChampion))
    AND_1.Add(CharacterDead(Characters.CLONE_FiasChampion0))
    AND_1.Add(FlagEnabled(Flags.FiasChampionsBattleStarted))

    MAIN.Await(AND_1)

    Wait(3.0)
    DisableBossHealthBar(Characters.FirstFiasChampion, name=NameText.FiasChampion0)
    CreateTemporaryVFX(
        vfx_id=600940,
        anchor_entity=Characters.SorcererRogier,
        model_point=900,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600940,
        anchor_entity=Characters.CLONE_SorcererRogier,
        model_point=900,
        anchor_type=CoordEntityType.Character,
    )
    Wait(0.5)
    EnableCharacter(Characters.SorcererRogier)
    EnableCharacter(Characters.CLONE_SorcererRogier)
    WaitFrames(frames=1)
    ForceAnimation(Characters.SorcererRogier, 63010)
    ForceAnimation(Characters.CLONE_SorcererRogier, 63010)
    EnableAI(Characters.SorcererRogier)
    EnableAI(Characters.CLONE_SorcererRogier)
    SetNetworkUpdateRate(Characters.SorcererRogier, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_SorcererRogier, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableImmortality(Characters.CLONE_SorcererRogier)
    DisableHealthBar(Characters.CLONE_SorcererRogier)
    ReferDamageToEntity(Characters.CLONE_SorcererRogier, Characters.SorcererRogier)
    WaitFrames(frames=1)
    EnableNetworkFlag(Flags.SorcererRogierBattleStarted)
    Wait(3.0)
    EnableBossHealthBar(Characters.SorcererRogier, name=NameText.SorcererRogier)


@RestartOnRest(12032812)
def LionelTheLionheartedTransition():
    """Event 12032812"""
    if FlagEnabled(Flags.FiasChampionsDead):
        return
    AND_2.Add(HealthValue(Characters.SorcererRogier) <= 0)
    AND_2.Add(FlagEnabled(Flags.SorcererRogierBattleStarted))
    MAIN.Await(AND_2)

    Kill(Characters.CLONE_SorcererRogier)

    AND_1.Add(CharacterDead(Characters.SorcererRogier))
    AND_1.Add(CharacterDead(Characters.CLONE_SorcererRogier))
    AND_1.Add(FlagEnabled(Flags.SorcererRogierBattleStarted))

    MAIN.Await(AND_1)

    Wait(3.0)
    DisableBossHealthBar(Characters.SorcererRogier, name=NameText.SorcererRogier)
    CreateTemporaryVFX(
        vfx_id=600940,
        anchor_entity=Characters.LioneltheLionhearted,
        model_point=900,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600940,
        anchor_entity=Characters.CLONE_LioneltheLionhearted,
        model_point=900,
        anchor_type=CoordEntityType.Character,
    )
    Wait(0.5)
    CreateTemporaryVFX(
        vfx_id=600940,
        anchor_entity=Characters.LionelSidekick1,
        model_point=900,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600940,
        anchor_entity=Characters.CLONE_LionelSidekick1,
        model_point=900,
        anchor_type=CoordEntityType.Character,
    )
    EnableCharacter(Characters.LioneltheLionhearted)
    EnableCharacter(Characters.CLONE_LioneltheLionhearted)
    EnableImmortality(Characters.CLONE_LioneltheLionhearted)
    DisableHealthBar(Characters.CLONE_LioneltheLionhearted)
    ReferDamageToEntity(Characters.CLONE_LioneltheLionhearted, Characters.LioneltheLionhearted)
    WaitFrames(frames=1)
    ForceAnimation(Characters.LioneltheLionhearted, 63010)
    ForceAnimation(Characters.CLONE_LioneltheLionhearted, 63010)
    EnableAI(Characters.LioneltheLionhearted)
    EnableAI(Characters.CLONE_LioneltheLionhearted)
    SetNetworkUpdateRate(Characters.LioneltheLionhearted, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_LioneltheLionhearted, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    CreateTemporaryVFX(
        vfx_id=600940,
        anchor_entity=Characters.LionelSidekick2,
        model_point=900,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600940,
        anchor_entity=Characters.CLONE_LionelSidekick2,
        model_point=900,
        anchor_type=CoordEntityType.Character,
    )
    Wait(0.5)
    if FlagEnabled(50):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23701,
            target_character=Characters.LionelSidekick1,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23701,
            target_character=Characters.CLONE_LionelSidekick1,
        )
        Goto(Label.L8)
    if FlagEnabled(51):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23702,
            target_character=Characters.LionelSidekick1,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23702,
            target_character=Characters.CLONE_LionelSidekick1,
        )
        Goto(Label.L8)
    if FlagEnabled(52):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23703,
            target_character=Characters.LionelSidekick1,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23703,
            target_character=Characters.CLONE_LionelSidekick1,
        )
        Goto(Label.L8)
    if FlagEnabled(53):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23704,
            target_character=Characters.LionelSidekick1,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23704,
            target_character=Characters.CLONE_LionelSidekick1,
        )
        Goto(Label.L8)
    if FlagEnabled(54):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23705,
            target_character=Characters.LionelSidekick1,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23705,
            target_character=Characters.CLONE_LionelSidekick1,
        )
        Goto(Label.L8)
    if FlagEnabled(55):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23706,
            target_character=Characters.LionelSidekick1,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23706,
            target_character=Characters.CLONE_LionelSidekick1,
        )
        Goto(Label.L8)
    if FlagEnabled(56):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23707,
            target_character=Characters.LionelSidekick1,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23707,
            target_character=Characters.CLONE_LionelSidekick1,
        )
        Goto(Label.L8)
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=0,
        failcase_player_param_id=23708,
        target_character=Characters.LionelSidekick1,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=0,
        failcase_player_param_id=23708,
        target_character=Characters.CLONE_LionelSidekick1,
    )

    # --- Label 8 --- #
    DefineLabel(8)
    WaitFrames(frames=1)
    EnableCharacter(Characters.LionelSidekick1)
    EnableCharacter(Characters.CLONE_LionelSidekick1)
    EnableImmortality(Characters.CLONE_LionelSidekick1)
    DisableHealthBar(Characters.CLONE_LionelSidekick1)
    ReferDamageToEntity(Characters.CLONE_LionelSidekick1, Characters.LionelSidekick1)
    WaitFrames(frames=1)

    ForceAnimation(Characters.LionelSidekick1, 63010)
    ForceAnimation(Characters.CLONE_LionelSidekick1, 63010)
    EnableAI(Characters.LionelSidekick1)
    EnableAI(Characters.CLONE_LionelSidekick1)
    SetNetworkUpdateRate(Characters.LionelSidekick1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_LionelSidekick1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(0.5)
    if FlagEnabled(50):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23711,
            target_character=Characters.LionelSidekick2,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23711,
            target_character=Characters.CLONE_LionelSidekick2,
        )
        Goto(Label.L9)
    if FlagEnabled(51):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23712,
            target_character=Characters.LionelSidekick2,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23712,
            target_character=Characters.CLONE_LionelSidekick2,
        )
        Goto(Label.L9)
    if FlagEnabled(52):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23713,
            target_character=Characters.LionelSidekick2,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23713,
            target_character=Characters.CLONE_LionelSidekick2,
        )
        Goto(Label.L9)
    if FlagEnabled(53):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23714,
            target_character=Characters.LionelSidekick2,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23714,
            target_character=Characters.CLONE_LionelSidekick2,
        )
        Goto(Label.L9)
    if FlagEnabled(54):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23715,
            target_character=Characters.LionelSidekick2,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23715,
            target_character=Characters.CLONE_LionelSidekick2,
        )
        Goto(Label.L9)
    if FlagEnabled(55):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23716,
            target_character=Characters.LionelSidekick2,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23716,
            target_character=Characters.CLONE_LionelSidekick2,
        )
        Goto(Label.L9)
    if FlagEnabled(56):
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23717,
            target_character=Characters.LionelSidekick2,
        )
        CopyPlayerCharacterDataFromOnlinePlayers(
            pool_type=0,
            failcase_player_param_id=23717,
            target_character=Characters.CLONE_LionelSidekick2,
        )
        Goto(Label.L9)
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=0,
        failcase_player_param_id=23718,
        target_character=Characters.LionelSidekick2,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=0,
        failcase_player_param_id=23718,
        target_character=Characters.CLONE_LionelSidekick2,
    )

    # --- Label 9 --- #
    DefineLabel(9)
    WaitFrames(frames=1)
    EnableCharacter(Characters.LionelSidekick2)
    EnableCharacter(Characters.CLONE_LionelSidekick2)
    EnableImmortality(Characters.CLONE_LionelSidekick2)
    DisableHealthBar(Characters.CLONE_LionelSidekick2)
    ReferDamageToEntity(Characters.CLONE_LionelSidekick2, Characters.LionelSidekick2)
    WaitFrames(frames=1)

    ForceAnimation(Characters.LionelSidekick2, 63010)
    ForceAnimation(Characters.CLONE_LionelSidekick2, 63010)
    EnableAI(Characters.LionelSidekick2)
    EnableAI(Characters.CLONE_LionelSidekick2)
    SetNetworkUpdateRate(Characters.LionelSidekick2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_LionelSidekick2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(2.0)
    EnableBossHealthBar(Characters.LioneltheLionhearted, name=NameText.LionelTheLionhearted)
    EnableBossHealthBar(Characters.LionelSidekick1, name=NameText.LionelSidekick1, bar_slot=1)
    EnableBossHealthBar(Characters.LionelSidekick2, name=NameText.LionelSidekick2, bar_slot=2)


@ContinueOnRest(12032820)
def GetFiasChampionPlayerData():
    """Event 12032820"""
    if PlayerNotInOwnWorld():
        return

    MAIN.Await(InsideMap(game_map=DEEPROOT_DEPTHS))

    RequestPlayerCharacterDataFromOnlinePlayers(pool_type=0, data_count=3)


@RestartOnRest(12032830)
def Event_12032830(
    _,
    flag: uint,
    entity: uint,
    region: uint,
    flag_1: uint,
    character: uint,
    seconds: float,
    flag_2: uint,
    region_1: uint,
):
    """Event 12032830"""
    GotoIfFlagEnabled(Label.L10, flag=flag)
    WaitFrames(frames=1)
    GotoIfFlagDisabled(Label.L0, flag=flag_2)

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=region_1, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(flag))

    MAIN.Await(OR_2)

    GotoIfPlayerNotInOwnWorld(Label.L2)
    if FlagDisabled(flag_2):
        BanishInvaders(unknown=0)
    if FlagEnabled(flag):
        return RESTART
    Goto(Label.L1)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_5.Add(OR_4)
    AND_4.Add(OR_5)
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(FlagDisabled(flag))
    OR_6.Add(AND_4)
    OR_6.Add(FlagEnabled(flag))

    MAIN.Await(OR_6)

    if FlagEnabled(flag):
        return RESTART
    RestartIfFinishedConditionTrue(input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(character)
    EnableNetworkFlag(flag_1)
    if PlayerNotInOwnWorld():
        return
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(PlayerInOwnWorld())
    AND_10.Add(FlagEnabled(flag))
    OR_10.Add(Invasion())
    OR_10.Add(InvasionPending())
    AND_10.Add(OR_10)
    AND_10.Add(ActionButtonParamActivated(action_button_id=10000, entity=entity))

    MAIN.Await(AND_10)

    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()
    Wait(seconds)


@RestartOnRest(12032840)
def Event_12032840():
    """Event 12032840"""
    DisableNetworkSync()
    if FlagEnabled(Flags.FiasChampionsDead):
        return
    AND_1.Add(FlagDisabled(Flags.FiasChampionsDead))
    AND_1.Add(FlagEnabled(12032805))
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(ActionButtonParamActivated(action_button_id=10000, entity=Assets.AEG099_002_9000))

    MAIN.Await(AND_1)

    SuppressSoundForFogGate(duration=5.0)
    RotateToFaceEntity(PLAYER, 12032800, animation=60060, wait_for_completion=True)
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=12032800))
    OR_1.Add(TimeElapsed(seconds=3.0))
    OR_2.Add(OR_1)
    AND_2.Add(OR_2)

    MAIN.Await(AND_2)

    Wait(1.0)
    RestartIfFinishedConditionTrue(input_condition=OR_1)
    EnableFlag(12032806)
    DisplayNetworkMessage(text=2920000, unk_4_5=False)
    Wait(4.0)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=12032806,
        model_point=-1,
        copy_draw_parent=0,
        use_bonfire_effect=False,
        reset_camera=False,
    )
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 63010)
    Wait(0.5)
    CreateTemporaryVFX(vfx_id=30320, anchor_entity=PLAYER, model_point=900, anchor_type=CoordEntityType.Character)
    Restart()


@RestartOnRest(12032841)
def Event_12032841():
    """Event 12032841"""
    AND_14.Add(PlayerInOwnWorld())
    AND_14.Add(CharacterInsideRegion(character=PLAYER, region=12032807))

    MAIN.Await(AND_14)

    BanishInvaders(unknown=0)
    Wait(1.0)
    Restart()


@RestartOnRest(12032842)
def Event_12032842(_, flag: uint, asset: uint, model_point: int, right: uint):
    """Event 12032842"""
    DisableNetworkSync()
    DisableAsset(asset)
    DeleteAssetVFX(asset)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Invader))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Invader2))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Invader3))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(flag))
    OR_2.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_2.Add(OR_2)
    AND_2.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=0, right=right):
        AND_3.Add(FlagEnabled(right))
    AND_3.Add(FlagDisabled(flag))
    OR_4.Add(Invasion())
    OR_4.Add(InvasionPending())
    AND_4.Add(OR_4)
    AND_4.Add(FlagEnabled(flag))
    AND_7.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_4.Add(not AND_7)
    OR_5.Add(Invasion())
    OR_5.Add(InvasionPending())
    AND_5.Add(OR_5)
    AND_5.Add(FlagEnabled(flag))
    AND_5.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_5.Add(EntityBeyondDistance(entity=PLAYER, other_entity=asset, radius=1.0))
    OR_8.Add(AND_1)
    OR_8.Add(AND_2)
    OR_8.Add(AND_3)
    OR_8.Add(AND_4)
    OR_8.Add(AND_5)

    MAIN.Await(OR_8)

    if PlayerNotInOwnWorld():
        EnableAsset(asset)
        DeleteAssetVFX(asset)
        CreateAssetVFX(asset, vfx_id=101, model_point=model_point)
    OR_11.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_11.Add(CharacterType(PLAYER, character_type=CharacterType.Invader))
    OR_11.Add(CharacterType(PLAYER, character_type=CharacterType.Invader2))
    OR_11.Add(CharacterType(PLAYER, character_type=CharacterType.Invader3))
    AND_11.Add(OR_11)
    AND_11.Add(FlagDisabled(flag))
    OR_12.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_12.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_12.Add(OR_12)
    AND_12.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=0, right=right):
        AND_13.Add(FlagEnabled(right))
    AND_13.Add(FlagDisabled(flag))
    OR_14.Add(Invasion())
    OR_14.Add(InvasionPending())
    AND_14.Add(OR_14)
    AND_14.Add(FlagEnabled(flag))
    OR_7.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_14.Add(not OR_7)
    OR_15.Add(Invasion())
    OR_15.Add(InvasionPending())
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag))
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_15.Add(EntityBeyondDistance(entity=PLAYER, other_entity=asset, radius=1.0))
    AND_9.Add(not AND_11)
    AND_9.Add(not AND_12)
    AND_9.Add(not AND_13)
    AND_9.Add(not AND_14)
    AND_9.Add(not AND_15)

    MAIN.Await(AND_9)

    Restart()


@RestartOnRest(12032849)
def FiasChampionsCommonEvents():
    """Event 12032849"""
    Event_12032830(
        0,
        flag=Flags.FiasChampionsDead,
        entity=Assets.AEG099_002_9000,
        region=12032800,
        flag_1=12032805,
        character=12035800,
        seconds=0.0,
        flag_2=12030801,
        region_1=12032801,
    )
    Event_12032840()
    RunCommonEvent(12032842, slot=0, args=(Flags.FiasChampionsDead, 12031800, 5, 12030801), arg_types="IIiI")
    CommonFunc_ControlBossMusic(0, Flags.FiasChampionsDead, 921100, 12032805, 12032806, 12032803, 0, 0, 0)


@RestartOnRest(12032859)
def TravelToFortissaxBattle():
    """Event 12032859"""
    DisableCharacter(Characters.LichdragonFortissax)
    DisableCharacter(Characters.CLONE_LichdragonFortissax)
    if FlagEnabled(Flags.LichdragonFortissaxDead):
        return

    MAIN.Await(FlagEnabled(12032859))

    EnableFlag(9021)
    Wait(1.0)
    FadeToBlack(strength=1.0, duration=1.0, freeze_player=True, freeze_player_delay=1.0)
    Wait(1.0)
    SetWeather(weather=Weather.PuffyClouds, duration=-1.0, immediate_change=True)
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=12030020,
        cutscene_flags=0,
        move_to_region=12032859,
        map_id=12030000,
        player_id=PLAYER,
        unk_20_24=12030000,
        unk_24_25=False,
    )
    WaitFramesAfterCutscene(frames=1)
    FadeToBlack(strength=0.0, duration=0.0, freeze_player=False, freeze_player_delay=0.0)
    WaitFramesAfterCutscene(frames=1)
    EnableCharacter(Characters.LichdragonFortissax)
    EnableCharacter(Characters.CLONE_LichdragonFortissax)
    DisableCharacter(Characters.TalkDummy0)
    DisableAsset(Assets.AEG099_060_9000)
    EnableFlag(Flags.PlayerInFortissaxArena)


@RestartOnRest(12032850)
def LichdragonFortissaxDies():
    """Event 12032850"""
    GotoIfFlagDisabled(Label.L10, flag=Flags.LichdragonFortissaxDead)
    EnableCharacter(Characters.TalkDummy0)
    EnableAsset(Assets.AEG099_060_9000)
    DisableAsset(Assets.AEG099_002_9001)
    DeleteAssetVFX(Assets.AEG099_002_9001)
    DisableAsset(Assets.AEG099_053_9003)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    AND_8.Add(FlagEnabled(12032859))
    AND_8.Add(HealthValue(Characters.LichdragonFortissax) <= 0)
    AND_8.Add(HealthValue(Characters.CLONE_LichdragonFortissax) <= 0)

    MAIN.Await(AND_8)

    SetLockedCameraSlot(area_id=12, block_id=3, camera_slot=0)
    Wait(4.0)
    PlaySoundEffect(Characters.LichdragonFortissax, 888880000, sound_type=SoundType.s_SFX)

    AND_1.Add(CharacterDead(Characters.LichdragonFortissax))
    AND_1.Add(CharacterDead(Characters.CLONE_LichdragonFortissax))
    MAIN.Await(AND_1)

    KillBossAndDisplayBanner(character=Characters.LichdragonFortissax, banner_type=BannerType.LegendFelled)
    EnableFlag(Flags.LichdragonFortissaxDead)
    EnableFlag(9111)
    if PlayerInOwnWorld():
        EnableFlag(61111)
    if PlayerInOwnWorld():
        AddSpecialEffect(PLAYER, 4280)
        AddSpecialEffect(PLAYER, 4282)
    Wait(9.0)
    # Return to Fia.
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=12030021,
        cutscene_flags=0,
        move_to_region=12032858,
        map_id=12030000,
        player_id=PLAYER,
        unk_20_24=0,
        unk_24_25=True,
    )
    WaitFramesAfterCutscene(frames=1)
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=True)
    DisableAsset(Assets.AEG099_002_9001)
    DeleteAssetVFX(Assets.AEG099_002_9001)
    EnableCharacter(Characters.TalkDummy0)
    EnableAsset(Assets.AEG099_060_9000)
    DisableAsset(Assets.AEG099_053_9003)
    if PlayerInOwnWorld():
        AddSpecialEffect(PLAYER, 4281)
        AddSpecialEffect(PLAYER, 4283)
    Wait(0.10000000149011612)
    DisableNetworkFlag(12032870)


@RestartOnRest(12032860)
def LichdragonFortissaxBattleTrigger():
    """Event 12032860"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.LichdragonFortissaxDead)
    DisableCharacter(Characters.LichdragonFortissax)
    DisableAnimations(Characters.LichdragonFortissax)
    Kill(Characters.LichdragonFortissax)
    DisableCharacter(Characters.CLONE_LichdragonFortissax)
    DisableAnimations(Characters.CLONE_LichdragonFortissax)
    Kill(Characters.CLONE_LichdragonFortissax)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.LichdragonFortissax)
    DisableAI(Characters.CLONE_LichdragonFortissax)
    DisableAsset(Assets.AEG099_002_9001)
    DeleteAssetVFX(Assets.AEG099_002_9001)
    DisableAsset(Assets.AEG099_053_9003)

    MAIN.Await(FlagEnabled(Flags.PlayerInFortissaxArena))

    DeleteAssetVFX(Assets.AEG099_002_9001)
    EnableAsset(Assets.AEG099_002_9001)
    CreateAssetVFX(Assets.AEG099_002_9001, vfx_id=101, model_point=5)
    EnableAsset(Assets.AEG099_053_9003)
    EnableNetworkFlag(12030852)
    EnableAI(Characters.LichdragonFortissax)
    EnableAI(Characters.CLONE_LichdragonFortissax)
    SetNetworkUpdateRate(Characters.LichdragonFortissax, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_LichdragonFortissax, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.LichdragonFortissax, name=NameText.LichdragonFortissax, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_LichdragonFortissax, name=NameText.CLONE_LichdragonFortissax, bar_slot=0)
    ActivateMultiplayerBuffs(12035850)
    SetLockedCameraSlot(area_id=12, block_id=3, camera_slot=1)
    if PlayerNotInOwnWorld():
        return
    EnableNetworkFlag(12032860)
    SetNetworkUpdateAuthority(12035850, authority_level=UpdateAuthority.Forced)
    NotifyBossBattleStart()
    Wait(0.10000000149011612)
    EnableNetworkFlag(12032870)


@RestartOnRest(12032896)
def Event_12032896(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 12032896"""
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))

    MAIN.Await(AND_1)

    EnableFlag(flag_2)
    Restart()


@RestartOnRest(12032899)
def LichdragonFortissaxCommonEvents():
    """Event 12032899"""
    RunCommonEvent(12032896, slot=0, args=(Flags.LichdragonFortissaxDead, 12032860, 12032856), arg_types="III")
    CommonFunc_ControlBossMusic(
        0, Flags.LichdragonFortissaxDead, 451000, 12032860, 12032856, 12030852, Flags.LichdragonFortissaxInPhaseTwo, 0,
        0
    )


@RestartOnRest(12032861)
def FortissaxLightning(_, fortissax: uint):
    """Event 12032861"""
    if ThisEventSlotFlagDisabled():
        DisableNetworkSync()
    AND_1.Add(CharacterHasSpecialEffect(20000, 14898))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(20000, 14899))
    AND_1.Add(EntityWithinDistance(entity=fortissax, other_entity=20000, radius=15.0))
    AND_1.Add(CharacterHasSpecialEffect(fortissax, 14896))
    AND_1.Add(CharacterAlive(fortissax))

    MAIN.Await(AND_1)

    WaitRandomSeconds(min_seconds=0.0, max_seconds=3.0)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=20000, special_effect=14898)
    AddSpecialEffect(20000, 14899)
    ShootProjectile(
        owner_entity=fortissax,
        source_entity=fortissax,
        model_point=900,
        behavior_id=1131,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitRandomSeconds(min_seconds=2.0, max_seconds=5.0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(12032862)
def LichdragonFortissaxPhaseTwoTransition():
    """Event 12032862"""
    OR_1.Add(CharacterHasSpecialEffect(Characters.LichdragonFortissax, 14875))
    OR_1.Add(CharacterHasSpecialEffect(Characters.CLONE_LichdragonFortissax, 14875))
    MAIN.Await(OR_1)

    SetLockedCameraSlot(area_id=12, block_id=3, camera_slot=0)
    EnableFlag(Flags.LichdragonFortissaxInPhaseTwo)
    Wait(7.0)

    # If BOTH Lichdragons died before the phase transition camera timer elapsed, don't set Phase Two camera.
    AND_1.Add(HealthRatio(Characters.LichdragonFortissax) <= 0.0)
    AND_1.Add(HealthRatio(Characters.CLONE_LichdragonFortissax) <= 0.0)
    SkipLinesIfConditionTrue(2, AND_1)
    # Phase Two camera.
    SetLockedCameraSlot(area_id=12, block_id=3, camera_slot=1)
    Goto(Label.L0)

    # BOTH Lichdragons died before camera timer finished (unlikely).
    SetLockedCameraSlot(area_id=12, block_id=3, camera_slot=0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(12030700)
def Event_12030700(_, character: uint):
    """Event 12030700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(4120):
        DisableFlag(12039152)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L8, flag=4128)
    GotoIfFlagEnabled(Label.L9, flag=4129)
    DisableCharacter(character)
    DisableBackread(character)

    MAIN.Await(FlagRangeAnyEnabled(flag_range=(4128, 4129)))

    Restart()

    # --- Label 8 --- #
    DefineLabel(8)

    # --- Label 9 --- #
    DefineLabel(9)
    GotoIfFlagEnabled(Label.L0, flag=4120)
    GotoIfFlagEnabled(Label.L1, flag=4121)
    GotoIfFlagEnabled(Label.L3, flag=4123)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90103)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 90103)
    AddSpecialEffect(character, 9628)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)

    MAIN.Await(FlagRangeAllDisabled(flag_range=(4128, 4129)))

    Restart()


@RestartOnRest(12030701)
def Event_12030701(_, character: uint, asset: uint):
    """Event 12030701"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L9, flag=4130)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)

    MAIN.Await(FlagEnabled(4130))

    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90104)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)

    MAIN.Await(FlagDisabled(4130))

    Restart()


@RestartOnRest(12030702)
def Event_12030702(_, character: uint):
    """Event 12030702"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L10, flag=4131)
    DisableCharacter(character)
    DisableBackread(character)

    MAIN.Await(FlagEnabled(4131))

    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90106)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)

    MAIN.Await(FlagDisabled(4131))

    Restart()


@RestartOnRest(12030703)
def Event_12030703(_, character: uint, asset: uint, asset_1: uint):
    """Event 12030703"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L11, flag=4132)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    DisableAsset(asset_1)

    MAIN.Await(FlagEnabled(4132))

    Restart()

    # --- Label 11 --- #
    DefineLabel(11)
    EnableCharacter(character)
    EnableBackread(character)
    EnableAsset(asset)
    EnableAsset(asset_1)
    ForceAnimation(character, 90106)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)

    MAIN.Await(FlagDisabled(4132))

    Restart()


@RestartOnRest(12030704)
def Event_12030704():
    """Event 12030704"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(Flags.FiasChampionsDead):
        return
    AND_1.Add(FlagEnabled(Flags.FiasChampionsDead))
    AND_1.Add(FlagEnabled(4127))

    MAIN.Await(AND_1)

    EnableFlag(4138)


@RestartOnRest(12030705)
def Event_12030705():
    """Event 12030705"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(Flags.LichdragonFortissaxDead):
        return
    AND_1.Add(FlagEnabled(12032870))
    AND_1.Add(FlagEnabled(4130))

    MAIN.Await(AND_1)

    EnableFlag(4138)


@RestartOnRest(12030706)
def Event_12030706():
    """Event 12030706"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(Flags.LichdragonFortissaxDead):
        return
    OR_1.Add(FlagEnabled(4130))
    OR_1.Add(FlagEnabled(4137))
    AND_1.Add(FlagEnabled(Flags.LichdragonFortissaxDead))
    AND_1.Add(FlagDisabled(12032870))
    AND_1.Add(OR_1)

    MAIN.Await(AND_1)

    EnableFlag(4138)


@RestartOnRest(12030707)
def Event_12030707():
    """Event 12030707"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(12032720)

    MAIN.Await(FlagEnabled(12032720))

    ForceAnimation(PLAYER, 90207, wait_for_completion=True)
    EnableFlag(12032721)
    Restart()


@RestartOnRest(12030708)
def Event_12030708(_, entity: uint):
    """Event 12030708"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(12032723)

    MAIN.Await(FlagEnabled(12032723))

    ForceAnimation(entity, 90208, wait_for_completion=True)
    EnableFlag(12032724)
    Restart()


@RestartOnRest(12030709)
def Event_12030709(_, flag: uint):
    """Event 12030709"""
    if PlayerNotInOwnWorld():
        return

    MAIN.Await(FlagDisabled(flag))

    MAIN.Await(FlagEnabled(flag))

    DisableNetworkConnectedFlagRange(flag_range=(4120, 4124))
    EnableNetworkFlag(4120)
    DisableNetworkConnectedFlagRange(flag_range=(4125, 4137))
    EnableNetworkFlag(4130)

    MAIN.Await(FlagDisabled(flag))

    DisableNetworkConnectedFlagRange(flag_range=(4120, 4137))
    EnableFlag(4138)
    Restart()


@RestartOnRest(12030710)
def Event_12030710(_, character: uint):
    """Event 12030710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(4060):
        DisableFlag(12039002)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4066)
    DisableCharacter(character)
    DisableBackread(character)

    MAIN.Await(FlagEnabled(4066))

    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L0, flag=4060)
    GotoIfFlagEnabled(Label.L1, flag=4061)
    GotoIfFlagEnabled(Label.L3, flag=4063)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90102)
    SetCharacterTalkRange(character=character, distance=100.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)

    MAIN.Await(FlagDisabled(4066))

    Restart()


@RestartOnRest(12030720)
def Event_12030720(_, character: uint):
    """Event 12030720"""
    WaitFrames(frames=1)
    ForceAnimation(character, 930013)
    EnableCharacter(character)
    EnableBackread(character)
    EnableAnimations(character)
    if PlayerNotInOwnWorld():
        return
    EnableImmortality(character)

    MAIN.Await(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))

    ForceAnimation(character, 20025)
    DisableAnimations(character)
    Wait(10.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()
