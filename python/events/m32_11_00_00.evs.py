"""
Yelough Anix Tunnel

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
from .entities.m32_11_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=32110000, asset=Assets.AEG099_060_9000)
    Event_32112800()
    Event_32112810()
    Event_32112811()
    Event_32112849()
    Event_32112820(1, character=Characters.MalformedStar1, destination=Assets.AEG003_316_9001)
    Event_32112820(2, character=Characters.MalformedStar2, destination=Assets.AEG003_316_9002)
    Event_32112820(3, character=Characters.MalformedStar3, destination=Assets.AEG003_316_9003)
    Event_32112820(4, character=Characters.MalformedStar4, destination=Assets.AEG003_316_9004)
    Event_32112820(5, character=Characters.MalformedStar5, destination=Assets.AEG003_316_9005)
    Event_32112820(6, character=Characters.MalformedStar6, destination=Assets.AEG003_316_9006)
    Event_32112820(7, character=Characters.MalformedStar7, destination=Assets.AEG003_316_9007)
    Event_32112820(8, character=Characters.MalformedStar8, destination=Assets.AEG003_316_9008)
    Event_32112830(1, character=Characters.MalformedStar1)
    Event_32112830(2, character=Characters.MalformedStar2)
    Event_32112830(3, character=Characters.MalformedStar3)
    Event_32112830(4, character=Characters.MalformedStar4)
    Event_32112830(5, character=Characters.MalformedStar5)
    Event_32112830(6, character=Characters.MalformedStar6)
    Event_32112830(7, character=Characters.MalformedStar7)
    Event_32112830(8, character=Characters.MalformedStar8)
    Event_32112510()
    CommonFunc_90005501(
        0,
        flag=32110510,
        flag_1=32110511,
        left=0,
        asset=Assets.AEG024_846_0500,
        asset_1=Assets.AEG027_080_0501,
        asset_2=Assets.AEG027_080_0500,
        flag_2=32110512,
    )
    Event_32112580()
    CommonFunc_90005511(
        0,
        flag=32110560,
        asset=Assets.AEG027_043_0500,
        obj_act_id=32113560,
        obj_act_id_1=257013,
        left=0,
    )
    CommonFunc_90005512(0, flag=32110560, region=32112550, region_1=32112551)
    CommonFunc_90005646(
        0,
        flag=32110800,
        left_flag=32112840,
        cancel_flag__right_flag=32112841,
        asset=Assets.AEG099_065_9000,
        player_start=32112840,
        area_id=32,
        block_id=11,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_900005610(0, 32111680, 100, 800, 0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_32110519()
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.TunnelMiner0,
        inactive_animation=30007,
        active_animation=20007,
        trigger_region=32112200,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.TunnelMiner1,
        inactive_animation=30007,
        active_animation=20007,
        trigger_region=32112200,
        trigger_delay=0.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.TunnelMiner2,
        inactive_animation=30007,
        active_animation=20007,
        trigger_region=32112205,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.TunnelMiner3,
        inactive_animation=30007,
        active_animation=20007,
        trigger_region=32112206,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.TunnelMiner3, region=32112206, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.TunnelMiner4,
        inactive_animation=30007,
        active_animation=20007,
        trigger_region=32112206,
        trigger_delay=0.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=32110208,
        inactive_animation=30007,
        active_animation=20007,
        trigger_region=32112208,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=32110208, region=32112208, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.TunnelMiner5,
        inactive_animation=30007,
        active_animation=20007,
        trigger_region=32112209,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.TunnelMiner6,
        inactive_animation=30007,
        active_animation=20007,
        trigger_region=32112209,
        trigger_delay=0.20000000298023224,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.TunnelMiner6, region=32112209, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.TunnelMiner7,
        animation_id=30006,
        animation_id_1=20006,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.TunnelMiner8,
        inactive_animation=30007,
        active_animation=20007,
        trigger_region=32112215,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.TunnelMiner8, region=32112215, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.TunnelMiner9,
        inactive_animation=30007,
        active_animation=20007,
        trigger_region=32112216,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.OnyxLord0, region=32112300, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, 32110301, 32112301, 0.0, -1)


@ContinueOnRest(32112510)
def Event_32112510():
    """Event 32112510"""
    CommonFunc_90005500(
        0,
        32110510,
        32110511,
        0,
        32111510,
        32111511,
        32113511,
        32111512,
        32113512,
        32112511,
        32112512,
        32110512,
        32110513,
        0,
    )


@ContinueOnRest(32110519)
def Event_32110519():
    """Event 32110519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(32110510)
    DisableThisSlotFlag()


@ContinueOnRest(32112580)
def Event_32112580():
    """Event 32112580"""
    RegisterLadder(start_climbing_flag=32110580, stop_climbing_flag=32110581, asset=Assets.AEG027_046_0500)
    RegisterLadder(start_climbing_flag=32110582, stop_climbing_flag=32110583, asset=Assets.AEG027_009_0500)
    RegisterLadder(start_climbing_flag=32110584, stop_climbing_flag=32110585, asset=Assets.AEG027_008_0500)


@RestartOnRest(32112800)
def Event_32112800():
    """Event 32112800"""
    if FlagEnabled(32110800):
        return
    
    MAIN.Await(HealthValue(Characters.MalformedStar0) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(32048000, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.MalformedStar0))
    
    KillBossAndDisplayBanner(character=Characters.MalformedStar0, banner_type=BannerType.EnemyFelled)
    EnableFlag(32110800)
    EnableFlag(9268)
    if PlayerInOwnWorld():
        EnableFlag(61268)


@RestartOnRest(32112810)
def Event_32112810():
    """Event 32112810"""
    GotoIfFlagDisabled(Label.L0, flag=32110800)
    DisableCharacter(Characters.MalformedStar0)
    DisableAnimations(Characters.MalformedStar0)
    Kill(Characters.MalformedStar0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.MalformedStar0)
    SetCharacterEventTarget(Characters.MalformedStar0, region=32110810)
    SetBackreadStateAlternate(Characters.TalkDummy2, True)
    GotoIfFlagEnabled(Label.L1, flag=32110801)
    DisableCharacter(Characters.MalformedStar0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=32112801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.MalformedStar0, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(32110801)
    EnableCharacter(Characters.MalformedStar0)
    ForceAnimation(Characters.MalformedStar0, 20016)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(32112805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=32112800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.MalformedStar0)
    SetNetworkUpdateRate(Characters.MalformedStar0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.MalformedStar0, name=904620320)


@RestartOnRest(32112811)
def Event_32112811():
    """Event 32112811"""
    if FlagEnabled(32110800):
        return
    AND_1.Add(HealthRatio(Characters.MalformedStar0) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(32112802)


@RestartOnRest(32112820)
def Event_32112820(_, character: uint, destination: uint):
    """Event 32112820"""
    MAIN.Await(CharacterHasSpecialEffect(character, 16714))
    
    Move(
        character,
        destination=destination,
        destination_type=CoordEntityType.Asset,
        model_point=100,
        copy_draw_parent=character,
    )
    Wait(1.0)
    RemoveSpecialEffect(character, 16714)
    Restart()


@RestartOnRest(32112830)
def Event_32112830(_, character: uint):
    """Event 32112830"""
    GotoIfFlagDisabled(Label.L0, flag=32110800)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 5038))
    AND_1.Add(CharacterDead(Characters.MalformedStar0))
    
    MAIN.Await(AND_1)
    
    DisableCharacter(character)
    DisableAnimations(character)


@RestartOnRest(32112849)
def Event_32112849():
    """Event 32112849"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=32110800,
        fog_asset=Assets.AEG099_003_9000,
        fog_region=32112800,
        host_entered_fog_flag=32112805,
        boss_characters=32115800,
        action_button_id=10000,
        first_time_done_flag=32110801,
        first_time_trigger_region=32112801,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=32110800,
        fog_asset=Assets.AEG099_003_9000,
        fog_region=32112800,
        host_entered_fog_flag=32112805,
        summon_entered_fog_flag=32112806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, flag=32110800, fog_asset=Assets.AEG099_003_9000, model_point=7, first_time_done_flag=32110801)
    CommonFunc_ControlBossMusic(0, 32110800, 920700, 32112805, 32112806, 0, 32112802, 0, 0)
