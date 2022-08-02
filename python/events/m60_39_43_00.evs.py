"""DONE
Southeast Liurnia (NE) (NE)

linked:
0
82
166

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: N:\\GR\\data\\Param\\event\\m60.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_39_43_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=1039430800,
        character=Characters.NightsCavalryHorse,
        item_lot=0,
        reward_delay=0.0,
        skip_reward=0,
        clone=Characters.CLONE_NightsCavalryHorse,
    )
    CommonFunc_MoveNightsCavalryToHorse(0, nights_cavalry=Characters.NightsCavalry, horse=Characters.NightsCavalryHorse)
    CommonFunc_MoveNightsCavalryToHorse(
        0, nights_cavalry=Characters.CLONE_NightsCavalry, horse=Characters.CLONE_NightsCavalryHorse
    )
    RunCommonEvent(90005477)
    NightsCavalryNoHorse(0, cavalry=Characters.NightsCavalry, horse=Characters.NightsCavalryHorse)
    NightsCavalryNoHorse(1, cavalry=Characters.CLONE_NightsCavalry, horse=Characters.CLONE_NightsCavalryHorse)
    CommonFunc_FieldBossNonRespawningWithReward(
        0,
        dead_flag=1039430800,
        extra_flag_to_enable=0,
        boss=Characters.NightsCavalry,
        boss_banner_choice=0,
        item_lot=1039430400,
        seconds=0.0,
        clone_boss=Characters.CLONE_NightsCavalry,
    )
    CommonFunc_FieldBossMusicHeatUp(0, boss=Characters.NightsCavalry, npc_threat_level=10, optional_trigger_flag=0)
    CommonFunc_NightsCavalryHealthBar(
        0,
        nights_cavalry=Characters.NightsCavalry,
        name=903150602,
        npc_threat_level=10,
        horse=Characters.NightsCavalryHorse,
        clone_cavalry=Characters.CLONE_NightsCavalry,
        clone_horse=Characters.CLONE_NightsCavalryHorse,
    )
    CommonFunc_90005706(0, character=Characters.WanderingNoble, animation_id=930023, left=0)
    CommonFunc_NonRespawningWithReward(
        0, dead_flag=1039430310, character=1039430310, item_lot=40252, reward_delay=0.0, skip_reward=0, clone=0
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.WanderingNoble)


@RestartOnRest(1039432340)
def NightsCavalryNoHorse(_, cavalry: uint, horse: uint):
    """Event 1039432340"""
    AND_1.Add(CharacterAlive(cavalry))
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    AND_2.Add(CharacterHasSpecialEffect(cavalry, 11825))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    AND_3.Add(CharacterBackreadEnabled(horse))

    MAIN.Await(AND_3)

    AddSpecialEffect(cavalry, 11825)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_4.Add(CharacterBackreadDisabled(horse))

    MAIN.Await(AND_4)

    AddSpecialEffect(cavalry, 11826)
    Wait(1.0)
    Restart()
