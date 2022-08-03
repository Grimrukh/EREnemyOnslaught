"""DONE
West Limgrave (SE) (SE)

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
from .entities.m60_43_36_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1043362210(1, character=Characters.WanderingNoble1, radius=30.0, sound_id=430008500)
    Event_1043362210(2, character=Characters.WanderingNoble2, radius=30.0, sound_id=430008501)
    Event_1043362210(3, character=Characters.WanderingNoble3, radius=30.0, sound_id=430008502)
    Event_1043362210(5, character=Characters.WanderingNoble5, radius=30.0, sound_id=430008503)
    Event_1043362210(6, character=Characters.WanderingNoble6, radius=30.0, sound_id=430008501)
    Event_1043362210(7, character=Characters.WanderingNoble7, radius=30.0, sound_id=430008502)
    CommonFunc_90005633(
        0,
        character=580300,
        flag=580000,
        character_1=Characters.WanderingNoble8,
        animation_id=30015,
        animation_id_1=20015,
        asset=Assets.AEG099_166_9000,
        asset_1=Assets.AEG099_090_9006,
    )
    AgheelInitialPosition(
        0, agheel=Characters.FlyingDragonAgheel, clone=Characters.CLONE_FlyingDragonAgheel, player_region=1043362340,
        agheel_point=RegionPoints.AgheelPosition0, clone_point=RegionPoints.CLONE_AgheelPosition0
    )
    AgheelInitialPosition(
        1, agheel=Characters.FlyingDragonAgheel, clone=Characters.CLONE_FlyingDragonAgheel, player_region=1043362341,
        agheel_point=RegionPoints.AgheelPosition1, clone_point=RegionPoints.CLONE_AgheelPosition1
    )
    AgheelInitialPosition(
        2, agheel=Characters.FlyingDragonAgheel, clone=Characters.CLONE_FlyingDragonAgheel, player_region=1043362342,
        agheel_point=RegionPoints.AgheelPosition2, clone_point=RegionPoints.CLONE_AgheelPosition2
    )
    AgheelInitialPosition(
        3, agheel=Characters.FlyingDragonAgheel, clone=Characters.CLONE_FlyingDragonAgheel, player_region=1043362343,
        agheel_point=RegionPoints.AgheelPosition3, clone_point=RegionPoints.CLONE_AgheelPosition3
    )
    AgheelInitialPosition(
        4, agheel=Characters.FlyingDragonAgheel, clone=Characters.CLONE_FlyingDragonAgheel, player_region=1043362344,
        agheel_point=RegionPoints.AgheelPosition4, clone_point=RegionPoints.CLONE_AgheelPosition4
    )
    AgheelInitialPosition(
        5, agheel=Characters.FlyingDragonAgheel, clone=Characters.CLONE_FlyingDragonAgheel, player_region=1043362345,
        agheel_point=RegionPoints.AgheelPosition5, clone_point=RegionPoints.CLONE_AgheelPosition5
    )
    AgheelInitialPosition(
        6, agheel=Characters.FlyingDragonAgheel, clone=Characters.CLONE_FlyingDragonAgheel, player_region=1043362346,
        agheel_point=RegionPoints.AgheelPosition6, clone_point=RegionPoints.CLONE_AgheelPosition6
    )
    AgheelInitialPosition(
        7, agheel=Characters.FlyingDragonAgheel, clone=Characters.CLONE_FlyingDragonAgheel, player_region=1043362347,
        agheel_point=RegionPoints.AgheelPosition7, clone_point=RegionPoints.CLONE_AgheelPosition7
    )
    AgheelInitialPosition(
        8, agheel=Characters.FlyingDragonAgheel, clone=Characters.CLONE_FlyingDragonAgheel, player_region=1043362348,
        agheel_point=RegionPoints.AgheelPosition8, clone_point=RegionPoints.CLONE_AgheelPosition8
    )
    AgheelInitialPosition(
        9, agheel=Characters.FlyingDragonAgheel, clone=Characters.CLONE_FlyingDragonAgheel, player_region=1043362349,
        agheel_point=RegionPoints.AgheelPosition9, clone_point=RegionPoints.CLONE_AgheelPosition9
    )
    AgheelInitialPosition(
        10, agheel=Characters.FlyingDragonAgheel, clone=Characters.CLONE_FlyingDragonAgheel, player_region=1043362350,
        agheel_point=RegionPoints.AgheelPosition10, clone_point=RegionPoints.CLONE_AgheelPosition10
    )
    AgheelInitialPosition(
        11, agheel=Characters.FlyingDragonAgheel, clone=Characters.CLONE_FlyingDragonAgheel, player_region=1043362351,
        agheel_point=RegionPoints.AgheelPosition11, clone_point=RegionPoints.CLONE_AgheelPosition11
    )
    AgheelInitialPosition(
        12, agheel=Characters.FlyingDragonAgheel, clone=Characters.CLONE_FlyingDragonAgheel, player_region=1043362352,
        agheel_point=RegionPoints.AgheelPosition12, clone_point=RegionPoints.CLONE_AgheelPosition12
    )
    CommonFunc_FieldBossNonRespawningWithRewardAndMessage(
        0,
        dead_flag=1043360800,
        extra_flag_to_enable=0,
        boss=Characters.FlyingDragonAgheel,
        boss_banner_choice=1,
        item_lot=30110,
        message=30060,
        seconds=0.0,
        clone_boss=Characters.CLONE_FlyingDragonAgheel,
    )
    CommonFunc_FieldBossMusicHealthBar(
        0, boss=Characters.FlyingDragonAgheel, name=NameText.FlyingDragonAgheel, npc_threat_level=25,
        clone_boss=Characters.CLONE_FlyingDragonAgheel, clone_name=NameText.CLONE_FlyingDragonAgheel,
    )
    Event_1043362380()
    Event_1043362510(0, asset=Assets.AEG099_290_9001, region=1043362510, flag=1043362500, obj_act_id=1043363600)
    CommonFunc_90005781(
        0,
        flag=1043360800,
        flag_1=1043362700,
        flag_2=1043362701,
        character=Characters.YuraHunterofBloodyFingers,
    )
    CommonFunc_90005780(
        0,
        flag=1043360800,
        summon_flag=1043362700,
        dismissal_flag=1043362701,
        character=Characters.YuraHunterofBloodyFingers,
        sign_type=20,
        region=1043362700,
        right=1043369200,
        unknown=0,
        right_1=0,
    )
    CommonFunc_90005783(
        0,
        flag=1043360800,
        flag_1=1043362700,
        flag_2=1043362701,
        character=Characters.YuraHunterofBloodyFingers,
        other_entity=1043362700,
        region=1043362100,
        left=0,
    )
    Event_1043363700()
    Event_1043363701(0, character=Characters.YuraHunterofBloodyFingers)
    Event_1043363702(0, entity=Characters.YuraHunterofBloodyFingers)
    Event_1043363704()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.YuraHunterofBloodyFingers)
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.WanderingNoble0, radius=20.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.WanderingNoble1, radius=10.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.WanderingNoble2, radius=20.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.WanderingNoble3, radius=20.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.WanderingNoble4, radius=20.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.WanderingNoble5, radius=20.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.WanderingNoble6, radius=20.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.WanderingNoble7, radius=20.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRadius(0, 1043360200, 5.0, 0.0, -1)


@RestartOnRest(1043362210)
def Event_1043362210(_, character: uint, radius: float, sound_id: int):
    """Event 1043362210"""
    DisableNetworkSync()
    WaitRandomSeconds(min_seconds=4.0, max_seconds=18.0)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(CharacterDead(character, target_comparison_type=ComparisonType.NotEqual))
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    PlaySoundEffect(character, sound_id, sound_type=SoundType.c_CharacterMotion)
    WaitRandomSeconds(min_seconds=4.0, max_seconds=18.0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(1043362220)
def Event_1043362220(
    _,
    character: uint,
    asset: uint,
    flag: uint,
    flag_1: uint,
    radius: float,
    animation_id: int,
    asset_1: uint,
):
    """Event 1043362220"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAsset(asset)
    DisableAsset(asset_1)
    DisableTreasure(asset=asset)
    DisableCharacter(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(asset)
    DisableAsset(asset_1)
    DisableTreasure(asset=asset)
    AddSpecialEffect(character, 10124)
    DisableInvincibility(character)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))

    MAIN.Await(AND_1)

    EnableAsset(asset)
    EnableAsset(asset_1)
    EnableTreasure(asset=asset)
    RemoveSpecialEffect(character, 10124)
    ForceAnimation(character, animation_id)
    End()


@RestartOnRest(1043362221)
def Event_1043362221(_, character: uint, flag: uint, flag_1: uint, animation_id: int, asset: uint):
    """Event 1043362221"""
    if FlagEnabled(flag):
        return
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=7.0))
    AND_1.Add(FlagEnabled(flag_1))

    MAIN.Await(AND_1)

    ForceAnimation(character, animation_id)
    ForceAnimation(asset, 1)
    Wait(3.799999952316284)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableAsset(asset)
    EnableFlag(flag)
    End()


@RestartOnRest(1043362340)
def AgheelInitialPosition(
    _,
    agheel: uint,
    clone: uint,
    player_region: uint,
    agheel_point: uint,
    clone_point: uint,
):
    """Event 1043362340"""
    if FlagEnabled(1043360340):
        EnableCharacter(agheel)
        EnableAnimations(agheel)
        EnableCharacter(clone)
        EnableAnimations(clone)
        EnableNetworkFlag(1043362379)
        End()
    DisableCharacter(agheel)
    DisableAnimations(agheel)
    ForceAnimation(agheel, 30005, loop=True)
    DisableCharacter(clone)
    DisableAnimations(clone)
    ForceAnimation(clone, 30005, loop=True)

    AND_1.Add(FlagDisabled(1043360340))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=player_region))
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)

    MAIN.Await(AND_1)

    Move(agheel, destination=agheel_point, destination_type=CoordEntityType.Region, copy_draw_parent=agheel)
    Move(clone, destination=clone_point, destination_type=CoordEntityType.Region, copy_draw_parent=agheel)
    EnableCharacter(agheel)
    EnableAnimations(agheel)
    ForceAnimation(agheel, 20005, loop=True)
    EnableCharacter(clone)
    EnableAnimations(clone)
    ForceAnimation(clone, 20005, loop=True)
    EnableNetworkFlag(1043360340)
    End()


@RestartOnRest(1043362380)
def Event_1043362380():
    """Event 1043362380"""
    GotoIfFlagDisabled(Label.L0, flag=1043360380)
    DisableCharacter(1043365340)
    DisableAnimations(1043365340)
    DisableAI(1043365340)
    DisableGravity(1043365340)
    PostDestruction(Assets.AEG007_450_1001)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagEnabled(1043362379))
    OR_1.Add(FlagEnabled(1043360341))

    MAIN.Await(OR_1)

    DisableCharacter(1043365340)
    DisableAnimations(1043365340)
    DisableAI(1043365340)
    DisableGravity(1043365340)
    PostDestruction(Assets.AEG007_450_1001)
    EnableFlag(1043360380)


@RestartOnRest(1043362510)
def Event_1043362510(_, asset: uint, region: uint, flag: uint, obj_act_id: uint):
    """Event 1043362510"""
    DisableNetworkSync()
    GotoIfMultiplayerPending(Label.L1)
    GotoIfMultiplayer(Label.L1)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    OR_1.Add(AssetActivated(obj_act_id=obj_act_id))
    OR_1.Add(MultiplayerPending())
    OR_1.Add(Multiplayer())

    MAIN.Await(OR_1)

    GotoIfMultiplayerPending(Label.L1)
    GotoIfMultiplayer(Label.L1)
    EnableFlag(flag)
    Wait(1.2999999523162842)
    Wait(0.8999999761581421)
    GotoIfMultiplayerPending(Label.L2)
    GotoIfMultiplayer(Label.L2)
    AND_1.Add(HealthValue(PLAYER) == 0)
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    GotoIfCharacterOutsideRegion(Label.L20, character=PLAYER, region=region)
    GotoIfMultiplayerPending(Label.L2)
    GotoIfMultiplayer(Label.L2)
    FadeToBlack(strength=0.0, duration=0.0, freeze_player=True, freeze_player_delay=-1.0)
    DisplayDialog(text=20700, anchor_entity=0, display_distance=5.0, button_type=ButtonType.Yes_or_No)
    Wait(0.699999988079071)
    AddSpecialEffect(PLAYER, 4090)
    PlaySoundEffect(PLAYER, 8700, sound_type=SoundType.c_CharacterMotion)
    Wait(2.700000047683716)
    DisableCharacter(PLAYER)
    AND_3.Add(HealthValue(PLAYER) == 0)
    GotoIfConditionTrue(Label.L20, input_condition=AND_3)
    GotoIfMultiplayerPending(Label.L3)
    GotoIfMultiplayer(Label.L3)
    AddSpecialEffect(PLAYER, 4091)
    FadeToBlack(strength=0.0, duration=0.0, freeze_player=False, freeze_player_delay=-1.0)
    EnableFlag(32080650)
    WarpToMap(game_map=SELLIA_CRYSTAL_TUNNEL, player_start=32082650, unk_8_12=60)
    SaveRequest()
    SetRespawnPoint(respawn_point=32082650)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    AddSpecialEffect(PLAYER, 4091)
    EnableCharacter(PLAYER)
    FadeToBlack(strength=0.0, duration=0.0, freeze_player=False, freeze_player_delay=-1.0)
    Wait(4.400000095367432)

    # --- Label 19 --- #
    DefineLabel(19)
    ForceAnimation(asset, 2, wait_for_completion=True)
    DisableFlag(flag)
    EnableAssetActivation(asset, obj_act_id=-1)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(asset=asset, animation_id=2)
    DisableFlag(flag)
    EnableAssetActivation(asset, obj_act_id=-1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableAssetActivation(asset, obj_act_id=-1)
    AddSpecialEffect(PLAYER, 4091)
    EnableCharacter(PLAYER)
    ForceAnimation(PLAYER, 60131)
    FadeToBlack(strength=0.0, duration=0.0, freeze_player=False, freeze_player_delay=-1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableAssetActivation(asset, obj_act_id=-1)
    ForceAnimation(asset, 2, wait_for_completion=True)
    DisableFlag(flag)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAssetActivation(asset, obj_act_id=-1)
    OR_2.Add(MultiplayerPending())
    AND_2.Add(not OR_2)
    OR_3.Add(Multiplayer())
    AND_2.Add(not OR_3)

    MAIN.Await(AND_2)

    EnableAssetActivation(asset, obj_act_id=-1)
    Restart()


@RestartOnRest(1043362651)
def Event_1043362651(_, tutorial_param_id: int, flag: uint, flag_1: uint, flag_2: uint):
    """Event 1043362651"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(Singleplayer())

    MAIN.Await(AND_1)

    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9126, flag=flag_2, bit_count=1)


@RestartOnRest(1043362652)
def Event_1043362652(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1043362652"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    OR_1.Add(PlayerHasGood(215000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(240000, including_storage=True))
    OR_1.Add(PlayerHasGood(243000, including_storage=True))
    OR_1.Add(PlayerHasGood(234000, including_storage=True))
    OR_1.Add(PlayerHasGood(244000, including_storage=True))
    OR_1.Add(PlayerHasGood(236000, including_storage=True))
    OR_1.Add(PlayerHasGood(232000, including_storage=True))
    OR_1.Add(PlayerHasGood(212000, including_storage=True))
    OR_1.Add(PlayerHasGood(241000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(233000, including_storage=True))
    OR_1.Add(PlayerHasGood(245000, including_storage=True))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9530))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=WEST_LIMGRAVE_SE_SE))
    AND_1.Add(OR_1)

    MAIN.Await(AND_1)

    if FlagEnabled(flag):
        return
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9127, flag=flag_1, bit_count=1)


@RestartOnRest(1043362653)
def Event_1043362653(_, tutorial_param_id: int, flag: uint, flag_1: uint, tutorial_param_id_1: int):
    """Event 1043362653"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=WEST_LIMGRAVE_SE_SE))
    AND_1.Add(PlayerDoesNotHaveGood(9116, including_storage=True))

    MAIN.Await(AND_1)

    if Multiplayer():
        return
    EnableFlag(flag_1)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9116, flag=flag, bit_count=1)


@RestartOnRest(1043362654)
def Event_1043362654(_, tutorial_param_id: int, flag: uint):
    """Event 1043362654"""
    if Multiplayer():
        return
    OR_1.Add(PlayerHasGood(215000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(240000, including_storage=True))
    OR_1.Add(PlayerHasGood(243000, including_storage=True))
    OR_1.Add(PlayerHasGood(234000, including_storage=True))
    OR_1.Add(PlayerHasGood(244000, including_storage=True))
    OR_1.Add(PlayerHasGood(236000, including_storage=True))
    OR_1.Add(PlayerHasGood(232000, including_storage=True))
    OR_1.Add(PlayerHasGood(212000, including_storage=True))
    OR_1.Add(PlayerHasGood(241000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(233000, including_storage=True))
    OR_1.Add(PlayerHasGood(245000, including_storage=True))
    AND_1.Add(Singleplayer())
    AND_1.Add(PlayerDoesNotHaveGood(9111, including_storage=True))
    AND_1.Add(InsideMap(game_map=WEST_LIMGRAVE_SE_SE))
    AND_1.Add(OR_1)

    MAIN.Await(AND_1)

    if Multiplayer():
        return
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9111, flag=flag, bit_count=1)


@RestartOnRest(1043363700)
def Event_1043363700():
    """Event 1043363700"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043359258):
        return
    if FlagEnabled(1043360800):
        return

    MAIN.Await(AttackedWithDamageType(attacked_entity=Characters.FlyingDragonAgheel, attacker=PLAYER))

    EnableFlag(1043359258)
    End()


@RestartOnRest(1043363701)
def Event_1043363701(_, character: uint):
    """Event 1043363701"""
    DisableCharacter(character)
    EnableBackread(character)
    if FlagEnabled(1043360800):
        DisableBackread(character)
    End()


@RestartOnRest(1043363702)
def Event_1043363702(_, entity: uint):
    """Event 1043363702"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043360800):
        return
    OR_1.Add(FlagEnabled(3625))
    OR_1.Add(FlagEnabled(3626))
    SkipLinesIfConditionTrue(2, OR_1)
    DisableFlag(1043369200)
    End()
    AND_1.Add(EntityWithinDistance(entity=entity, other_entity=20000, radius=10.0))
    AND_1.Add(FlagEnabled(1043360340))
    AND_1.Add(FlagEnabled(1043359256))

    MAIN.Await(AND_1)

    if FlagDisabled(3620):
        return
    if FlagEnabled(1043360800):
        return
    EnableFlag(1043369200)
    End()


@RestartOnRest(1043363703)
def Event_1043363703(_, character: uint, other_entity: uint):
    """Event 1043363703"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043360800):
        return
    OR_1.Add(FlagEnabled(3625))
    OR_1.Add(FlagEnabled(3626))
    if not OR_1:
        return
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=80.0))
    AND_1.Add(FlagEnabled(1043362700))
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(1043360800))

    MAIN.Await(OR_2)

    if FlagEnabled(1043360800):
        return
    SendNPCSummonHome(character=character)
    DisableFlag(1043369200)
    End()


@RestartOnRest(1043363704)
def Event_1043363704():
    """Event 1043363704"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043360800):
        return
    OR_1.Add(FlagEnabled(3625))
    OR_1.Add(FlagEnabled(3626))
    if not OR_1:
        return

    MAIN.Await(FlagEnabled(1043360800))

    if FlagEnabled(1043362700):
        EnableFlag(1043369201)
    DisableFlag(1043369200)
    End()
