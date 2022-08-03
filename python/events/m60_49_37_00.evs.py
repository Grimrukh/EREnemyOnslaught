"""DONE
South Caelid (SW) (NE)

linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_49_37_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1049370000, asset=Assets.AEG099_060_9000)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=1049370200, radius=20.0, seconds=0.0, animation_id=-1)

    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=1049370800,
        character=Characters.NightsCavalryHorse,
        item_lot=0,
        reward_delay=0.0,
        skip_reward=0,
        clone=Characters.CLONE_NightsCavalryHorse,
    )
    CommonFunc_MoveNightsCavalryToHorse(0, nights_cavalry=Characters.NightsCavalry, horse=Characters.NightsCavalryHorse)
    CommonFunc_MoveNightsCavalryToHorse(1, nights_cavalry=Characters.CLONE_NightsCavalry, horse=Characters.CLONE_NightsCavalryHorse)
    Event_1049372291(0, character=Characters.NightsCavalry, character_1=Characters.NightsCavalryHorse)
    Event_1049372291(1, character=Characters.CLONE_NightsCavalry, character_1=Characters.CLONE_NightsCavalryHorse)
    CommonFunc_NightsCavalryHealthBar(
        0,
        nights_cavalry=Characters.NightsCavalry,
        name=903150605,
        npc_threat_level=10,
        horse=Characters.NightsCavalryHorse,
        clone_cavalry=Characters.CLONE_NightsCavalry,
        clone_horse=Characters.CLONE_NightsCavalryHorse,
    )
    CommonFunc_FieldBossNonRespawningWithReward(
        0,
        dead_flag=1049370800,
        extra_flag_to_enable=0,
        boss=Characters.NightsCavalry,
        boss_banner_choice=0,
        item_lot=1049370100,
        seconds=0.0,
        clone_boss=Characters.CLONE_NightsCavalry,
    )
    CommonFunc_FieldBossMusicHeatUp(
        0, boss=Characters.NightsCavalry, npc_threat_level=10, optional_trigger_flag=0,
    )
    CommonFunc_FieldBossMusicHealthBar(
        0, boss=Characters.DeathRiteBird, name=904980606, npc_threat_level=24,
        clone_boss=Characters.CLONE_DeathRiteBird, clone_name=0,
    )
    CommonFunc_FieldBossNonRespawningWithReward(
        0,
        dead_flag=1049370850,
        extra_flag_to_enable=0,
        boss=Characters.DeathRiteBird,
        boss_banner_choice=0,
        item_lot=1049370110,
        seconds=0.0,
        clone_boss=Characters.CLONE_DeathRiteBird,
    )
    Event_1049372299()
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=1049370299,
        character=Characters.LionGuardian,
        item_lot=1049370700,
        reward_delay=0.0,
        skip_reward=0,
        clone=Characters.CLONE_LionGuardian,
    )
    CommonFunc_90005725(
        0,
        flag=4780,
        flag_1=4781,
        flag_2=4783,
        flag_3=1049379205,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        asset=1049376700,
    )
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4781,
        flag_1=4782,
        flag_2=1049379206,
        flag_3=4781,
        first_flag=4780,
        last_flag=4784,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4781, flag_1=4780, flag_2=1049379206, right=3)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4783, first_flag=4780, last_flag=4784)
    CommonFunc_90005703(
        0,
        character=Characters.NomadMule,
        flag=4781,
        flag_1=4782,
        flag_2=1049379207,
        flag_3=4781,
        first_flag=4780,
        last_flag=4784,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.NomadMule, flag=4781, flag_1=4780, flag_2=1049379207, right=3)
    CommonFunc_90005728(0, attacked_entity=Characters.NomadMule, flag=1049372706, flag_1=1049372707)
    CommonFunc_90005727(0, 4781, 1049370700, 1049370701, 4780, 4783)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Merchant)
    DisableBackread(Characters.NomadMule)


@RestartOnRest(1049372291)
def Event_1049372291(_, character: uint, character_1: uint):
    """Event 1049372291"""
    AND_1.Add(CharacterAlive(character))
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    AND_2.Add(CharacterHasSpecialEffect(character, 11825))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    AND_3.Add(CharacterBackreadEnabled(character_1))
    
    MAIN.Await(AND_3)
    
    AddSpecialEffect(character, 11825)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_4.Add(CharacterBackreadDisabled(character_1))
    
    MAIN.Await(AND_4)
    
    AddSpecialEffect(character, 11826)
    Wait(1.0)
    Restart()


@RestartOnRest(1049372299)
def Event_1049372299():
    """Event 1049372299"""
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=1049372299))
    
    ChangePatrolBehavior(Characters.LionGuardian, patrol_information_id=1049373299)
