"""
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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunEvent(1045342580, slot=0, args=(0,))
    Event_1045342250(0, character=1045340204)
    Event_1045342250(1, character=1045340250)
    Event_1045342250(2, character=1045340251)
    RunCommonEvent(0, 90005201, args=(1045340702, 30028, -1, 0.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1045340703, 30028, -1, 0.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1045340704, 30029, -1, 0.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005461, args=(1045340207,))
    RunCommonEvent(1, 90005462, args=(1045340207,))
    RunCommonEvent(0, 90005460, args=(1045340207,))
    RunCommonEvent(0, 900005610, args=(1045341680, 100, 800, 1045348540), arg_types="IiiI")
    RunCommonEvent(0, 90005683, args=(62151, 1045341684, 208, 78198, 78198), arg_types="IIiII")
    RunCommonEvent(0, 90005704, args=(1045340700, 3381, 3380, 1045349201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1045340700, 3381, 3382, 1045349201, 3381, 3380, 3384, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1045340700, 3383, 3380, 3384), arg_types="IIII")
    Event_1045340700(0, character=1045340700)
    Event_1045340701(0, character=1045340701, obj=1045341700)
    RunCommonEvent(0, 90005704, args=(1045340705, 3401, 3400, 1045349251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1045340705, 3401, 3402, 1045349251, 3401, 3400, 3403, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1045340705, 3403, 3400, 3403), arg_types="IIII")
    Event_1045340705(0, character=1045340705)
    RunCommonEvent(0, 90005750, args=(1045341706, 4110, 110620, 400061, 400061, 1045349258, 0), arg_types="IiiIIIi")
    Event_1045340707(0, 1045340705)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1045340700)
    DisableBackread(1045340701)
    DisableBackread(1045340705)
    Event_1045340706()
    RunCommonEvent(0, 90005250, args=(1045340405, 1045342405, 0.0, 0), arg_types="IIfi")


@RestartOnRest(1045342250)
def Event_1045342250(_, character: uint):
    """Event 1045342250"""
    Kill(character)
    End()


@RestartOnRest(1045342680)
def Event_1045342680():
    """Event 1045342680"""
    IfFlagEnabled(MAIN, 1045348540)
    CreateObjectVFX(1045341680, vfx_id=100, model_point=800)


@RestartOnRest(1045340700)
def Event_1045340700(_, character: uint):
    """Event 1045340700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3380)
    DisableFlag(1045349202)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3385)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3385)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L0, flag=3380)
    GotoIfFlagEnabled(Label.L1, flag=3381)
    GotoIfFlagEnabled(Label.L3, flag=3383)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    Move(character, destination=1045342700, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character, 90100, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    Move(character, destination=1045342700, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character, 90100, unknown2=1.0)
    SetTeamType(character, TeamType.HostileNPC)
    AddSpecialEffect(character, 9628)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3385)
    Restart()


@RestartOnRest(1045340701)
def Event_1045340701(_, character: uint, obj: uint):
    """Event 1045340701"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagRangeAnyEnabled(Label.L6, flag_range=(3386, 3397))
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagRangeAnyEnabled(MAIN, flag_range=(3386, 3397))
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableBackread(character)
    EnableCharacter(character)
    DisableAnimations(character)
    ForceAnimation(character, 90105, unknown2=1.0)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagRangeAllDisabled(MAIN, flag_range=(3386, 3397))
    Restart()


@RestartOnRest(1045340705)
def Event_1045340705(_, character: uint):
    """Event 1045340705"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagEnabled(1, 3400)
    DisableFlag(1043319202)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L8, flag=3408)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3408)
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    GotoIfFlagEnabled(Label.L0, flag=3400)
    GotoIfFlagEnabled(Label.L1, flag=3401)
    GotoIfFlagEnabled(Label.L2, flag=3402)
    GotoIfFlagEnabled(Label.L3, flag=3403)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(1045349258)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3408)
    Restart()


@RestartOnRest(1045340706)
def Event_1045340706():
    """Event 1045340706"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1045349256)
    IfFlagEnabled(AND_1, 1043300800)
    IfFlagEnabled(AND_1, 1043319206)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1045342719)
    EnableFlag(3418)


@RestartOnRest(1045340707)
def Event_1045340707(_, attacked_entity: uint):
    """Event 1045340707"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1045349256)
    IfAttackedWithDamageType(MAIN, attacked_entity=attacked_entity, attacker=0)
    EnableFlag(1045349256)
