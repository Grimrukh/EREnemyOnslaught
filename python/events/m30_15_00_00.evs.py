"""DONE
Caelid Catacombs

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
from .entities.m30_15_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=301500, asset=Assets.AEG099_060_9000)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MirandaRotFlower0,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=30152400,
        trigger_delay=0.800000011920929,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MirandaRotFlower1,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=30152400,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MirandaRotFlower2,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=30152400,
        trigger_delay=1.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.CatacombsSkeleton0, region=30152214, seconds=0.0, animation_id=3028)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.GiantMirandaRotFlower, region=30152310, seconds=0.0, animation_id=3003)
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.CatacombsSkeleton1,
        animation_id=30003,
        animation_id_1=20003,
        region=30152213,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MirandaRotFlower3,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=30152217,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MirandaRotFlower4,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=30152211,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MirandaRotFlower5,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=30152217,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MirandaRotFlower6,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=30152217,
        trigger_delay=2.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.MirandaRotFlower7, region=30152200, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.MirandaRotFlower8, region=30152200, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.MirandaRotFlower9, region=30152200, seconds=0.0, animation_id=-1)
    CommonFunc_90005650(
        0,
        flag=30150540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_0500,
        obj_act_id=30153541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30150540, anchor_entity=Assets.AEG027_041_0500)
    CommonFunc_90005525(0, flag=30150570, asset=Assets.AEG027_157_0500)
    CommonFunc_90005525(0, flag=30150571, asset=Assets.AEG027_157_0501)
    Event_30152800()
    Event_30152810()
    Event_30152849()
    Event_30152811()
    CommonFunc_90005646(
        0,
        flag=30150800,
        left_flag=30152840,
        cancel_flag__right_flag=30152841,
        asset=Assets.AEG099_065_9000,
        player_start=30152840,
        area_id=30,
        block_id=15,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_91005600(0, 30152800, 30151695, 5)


@RestartOnRest(30152520)
def Event_30152520(_, flag: uint, asset: uint, flag_1: uint):
    """Event 30152520"""
    if FlagEnabled(flag):
        return
    DisableAssetActivation(asset, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    EnableAssetActivation(asset, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    EnableAssetActivation(asset, obj_act_id=-1)


@RestartOnRest(30152800)
def Event_30152800():
    """Event 30152800"""
    if FlagEnabled(30150800):
        return
    
    AND_7.Add(HealthValue(Characters.CemeteryShade) <= 0)
    AND_7.Add(HealthValue(Characters.CLONE_CemeteryShade) <= 0)
    MAIN.Await(AND_7)
    
    Wait(4.0)
    PlaySoundEffect(Characters.CemeteryShade, 888880000, sound_type=SoundType.s_SFX)
    
    AND_8.Add(CharacterDead(Characters.CemeteryShade))
    AND_8.Add(CharacterDead(Characters.CLONE_CemeteryShade))
    MAIN.Await(AND_8)
    
    KillBossAndDisplayBanner(character=Characters.CemeteryShade, banner_type=BannerType.EnemyFelled)
    EnableFlag(30150800)
    if PlayerInOwnWorld():
        EnableFlag(61215)
    EnableFlag(9215)


@RestartOnRest(30152810)
def Event_30152810():
    """Event 30152810"""
    GotoIfFlagDisabled(Label.L0, flag=30150800)
    DisableCharacter(Characters.CemeteryShade)
    DisableAnimations(Characters.CemeteryShade)
    Kill(Characters.CemeteryShade)
    DisableCharacter(Characters.CLONE_CemeteryShade)
    DisableAnimations(Characters.CLONE_CemeteryShade)
    Kill(Characters.CLONE_CemeteryShade)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.CemeteryShade)
    DisableAI(Characters.CLONE_CemeteryShade)
    AND_2.Add(FlagEnabled(30152805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30152800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkUpdateRate(Characters.CemeteryShade, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_CemeteryShade, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.CemeteryShade, name=903664301, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_CemeteryShade, name=903664301, bar_slot=0)
    Wait(0.5)
    EnableAI(Characters.CemeteryShade)
    EnableAI(Characters.CLONE_CemeteryShade)


@RestartOnRest(30152811)
def Event_30152811():
    """Event 30152811"""
    if FlagEnabled(30150800):
        return
    AND_1.Add(HealthRatio(Characters.CemeteryShade) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30152802)


@RestartOnRest(30152849)
def Event_30152849():
    """Event 30152849"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=30150800,
        fog_asset=Assets.AEG099_001_9000,
        fog_region=30152800,
        host_entered_fog_flag=30152805,
        boss_characters=30155800,
        action_button_id=10000,
        first_time_done_flag=0,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=30150800,
        fog_asset=Assets.AEG099_001_9000,
        fog_region=30152800,
        host_entered_fog_flag=30152805,
        summon_entered_fog_flag=30152806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=30150800, fog_asset=Assets.AEG099_001_9000, model_point=3, required_flag=0)
    CommonFunc_ControlBossMusic(0, 30150800, 930000, 30152805, 30152806, 0, 30152802, 0, 0)
