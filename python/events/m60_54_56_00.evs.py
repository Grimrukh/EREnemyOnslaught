"""DONE
Northeast Mountaintops (SE) (SW)

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
from .entities.m60_54_56_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1054562200(0, character=1054565200)
    Event_1054562500()


@RestartOnRest(1054562200)
def Event_1054562200(_, character: uint):
    """Event 1054562200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@RestartOnRest(1054562500)
def Event_1054562500():
    """Event 1054562500"""
    if FlagEnabled(1254560800):
        return
    SetCharacterTalkRange(character=Characters.Dummy, distance=300.0)


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    CommonFunc_FieldBossMusicHealthBar(
        0, boss=Characters.BorealistheFreezingFog, name=904503600, npc_threat_level=25,
        clone_boss=Characters.CLONE_BorealistheFreezingFog, clone_name=NameText.CLONE_BorealisTheFreezingFog,
    )
    CommonFunc_FieldBossNonRespawningWithRewardAndMessage(
        0,
        dead_flag=1254560800,
        extra_flag_to_enable=0,
        boss=Characters.BorealistheFreezingFog,
        boss_banner_choice=1,
        item_lot=30510,
        message=30066,
        seconds=0.0,
        clone_boss=Characters.CLONE_BorealistheFreezingFog,
    )
    ControlBorealisWeather()
    TriggerBorealisAppearance(
        0,
        dragon=Characters.BorealistheFreezingFog,
        clone=Characters.CLONE_BorealistheFreezingFog,
        animation_id=30003,
        animation_id_1=20003,
        region_0=1054562830,
        region_1=1054562831,
        region_2=1054562832,
        region_3=1054562833,
        region_4=1054562834,
        region_5=1054562835,
    )


@RestartOnRest(1054562815)
def ControlBorealisWeather():
    """Event 1054562815"""
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1054562811))
    AwaitConditionTrue(OR_1)
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=1254560800)
    GotoIfSpecialStandbyEndedFlagEnabled(Label.L1, character=Characters.BorealistheFreezingFog)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1054562810))
    GotoIfConditionTrue(Label.L2, input_condition=OR_2)
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=1054562812))
    GotoIfConditionFalse(Label.L3, input_condition=OR_3)
    Wait(1.0)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    RemoveSpecialEffect(PLAYER, 4213)
    SetWeather(weather=Weather.HeavySnow, duration=30.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    SetWeather(weather=Weather.SnowyHeavyFog, duration=-1.0, immediate_change=False)
    Wait(5.0)
    AddSpecialEffect(PLAYER, 4213)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SetWeather(weather=Weather.HeavySnow, duration=30.0, immediate_change=False)
    Wait(3.0)
    RemoveSpecialEffect(PLAYER, 4213)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveSpecialEffect(PLAYER, 4213)
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    End()


@RestartOnRest(1054562820)
def TriggerBorealisAppearance(
    _,
    dragon: uint,
    clone: uint,
    animation_id: int,
    animation_id_1: int,
    region_0: uint,
    region_1: uint,
    region_2: uint,
    region_3: uint,
    region_4: uint,
    region_5: uint,
):
    """A bunch of these arguments are useless, but this whole function was obviously copied from `common_func`."""
    EndIffSpecialStandbyEndedFlagEnabled(character=dragon)

    ForceAnimation(dragon, animation_id, loop=True)
    ForceAnimation(clone, animation_id, loop=True)

    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    if UnsignedNotEqual(left=0, right=region_0):
        OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region_0))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region_4))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region_5))
    AND_1.Add(OR_3)
    AND_1.Add(OutsideMap(game_map=SPIRITCALLER_CAVE))
    AND_1.Add(CharacterBackreadEnabled(dragon))
    AND_1.Add(CharacterBackreadEnabled(clone))
    AND_1.Add(WeatherState(weather=Weather.SnowyHeavyFog, unk_4_8=3.0, unk_8_12=0.0))
    OR_11.Add(CharacterHasSpecialEffect(dragon, 5080))
    OR_11.Add(CharacterHasSpecialEffect(dragon, 5450))
    OR_11.Add(CharacterHasSpecialEffect(clone, 5080))
    OR_11.Add(CharacterHasSpecialEffect(clone, 5450))
    AND_1.Add(OR_11)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=dragon))
    OR_2.Add(CharacterHasStateInfo(character=dragon, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=dragon, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=dragon, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=dragon, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=dragon, state_info=260))
    OR_2.Add(AttackedWithDamageType(attacked_entity=clone))
    OR_2.Add(CharacterHasStateInfo(character=clone, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=clone, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=clone, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=clone, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=clone, state_info=260))
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    SetSpecialStandbyEndedFlag(character=dragon, state=True)
    SetSpecialStandbyEndedFlag(character=clone, state=True)
    EnableNetworkFlag(1054562820)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(dragon, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(dragon, 5450))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(clone, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(clone, 5450))

    GotoIfConditionTrue(Label.L0, input_condition=AND_2)

    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=region_0))
    GotoIfConditionTrue(Label.L5, input_condition=OR_5)
    OR_6.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    GotoIfConditionTrue(Label.L6, input_condition=OR_6)
    OR_7.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    GotoIfConditionTrue(Label.L7, input_condition=OR_7)
    OR_8.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    GotoIfConditionTrue(Label.L8, input_condition=OR_8)
    OR_8.Add(CharacterInsideRegion(character=PLAYER, region=region_4))
    GotoIfConditionTrue(Label.L9, input_condition=OR_8)
    OR_8.Add(CharacterInsideRegion(character=PLAYER, region=region_5))
    GotoIfConditionTrue(Label.L10, input_condition=OR_8)
    Goto(Label.L14)

    # --- Label 5 --- #
    DefineLabel(5)
    Move(
        dragon, destination=Regions.BorealisPoint0, destination_type=CoordEntityType.Region, copy_draw_parent=dragon
    )
    Move(
        clone, destination=Regions.CLONE_BorealisPoint0, destination_type=CoordEntityType.Region, copy_draw_parent=clone
    )
    Goto(Label.L14)

    # --- Label 6 --- #
    DefineLabel(6)
    Move(
        dragon, destination=Regions.BorealisPoint1, destination_type=CoordEntityType.Region, copy_draw_parent=dragon
    )
    Move(
        clone, destination=Regions.CLONE_BorealisPoint1, destination_type=CoordEntityType.Region, copy_draw_parent=clone
    )
    Goto(Label.L14)

    # --- Label 7 --- #
    DefineLabel(7)
    Move(
        dragon, destination=Regions.BorealisPoint2, destination_type=CoordEntityType.Region, copy_draw_parent=dragon
    )
    Move(
        clone, destination=Regions.CLONE_BorealisPoint2, destination_type=CoordEntityType.Region, copy_draw_parent=clone
    )
    Goto(Label.L14)

    # --- Label 8 --- #
    DefineLabel(8)
    Move(
        dragon, destination=Regions.BorealisPoint3, destination_type=CoordEntityType.Region, copy_draw_parent=dragon
    )
    Move(
        clone, destination=Regions.CLONE_BorealisPoint3, destination_type=CoordEntityType.Region, copy_draw_parent=clone
    )
    Goto(Label.L14)

    # --- Label 9 --- #
    DefineLabel(9)
    Move(
        dragon, destination=Regions.BorealisPoint4, destination_type=CoordEntityType.Region, copy_draw_parent=dragon
    )
    Move(
        clone, destination=Regions.CLONE_BorealisPoint4, destination_type=CoordEntityType.Region, copy_draw_parent=clone
    )
    Goto(Label.L14)

    # --- Label 10 --- #
    DefineLabel(10)
    Move(
        dragon, destination=Regions.BorealisPoint5, destination_type=CoordEntityType.Region, copy_draw_parent=dragon
    )
    Move(
        clone, destination=Regions.CLONE_BorealisPoint5, destination_type=CoordEntityType.Region, copy_draw_parent=clone
    )
    Goto(Label.L14)

    # --- Label 14 --- #
    DefineLabel(14)
    AddSpecialEffect(dragon, 10206)
    AddSpecialEffect(clone, 10206)
    ForceAnimation(dragon, animation_id_1, loop=True)
    ForceAnimation(clone, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    End()
