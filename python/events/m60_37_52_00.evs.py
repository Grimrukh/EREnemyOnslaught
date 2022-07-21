"""
West Altus Plateau (SW) (SE)

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
from .entities.m60_37_52_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005600(0, grace_flag=76354, asset=1037521950, enemy_block_distance=3.0, character=0)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1037520204, region=1037522204, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1037520205, region=1037522204, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1037520206, region=1037522204, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.DemiHuman2,
        region=1037522500,
        radius=7.0,
        seconds=1.5,
        animation_id=3022,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.IronVirgin,
        region=1037522500,
        radius=10.0,
        seconds=1.0,
        animation_id=3013,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.DemiHumanShaman0,
        region=1037522301,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.DemiHumanShaman1,
        region=1037522301,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.LargeDemiHuman,
        region=1037522301,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.DemiHuman8,
        region=1037522301,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.DemiHumanBeastman1,
        region=1037522301,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.DemiHumanBeastman0,
        animation_id=30000,
        animation_id_1=20000,
        region=1037522405,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.DemiHuman6, region=1037522302, radius=5.0, seconds=2.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.DemiHuman1,
        region=1037522350,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        1,
        character=Characters.DemiHuman3,
        region=1037522350,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(2, character=1037520312, region=1037522350, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        3,
        character=Characters.DemiHuman4,
        region=1037522350,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        4,
        character=Characters.DemiHuman7,
        region=1037522350,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(5, character=1037520315, region=1037522350, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        6,
        character=Characters.RayaLucariaScholar,
        region=1037522350,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005771(0, 1037520951, 1037522700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_NonRespawningWithReward(0, dead_flag=1037520355, character=1037525350, item_lot_param_id=0, reward_delay=0.0, skip_reward=0)
    CommonFunc_90005600(0, grace_flag=1037520001, asset=Assets.AEG099_060_9001, enemy_block_distance=5.0, character=0)
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MirandaFlower0,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=1037522614,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MirandaFlower1,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=1037522614,
        trigger_delay=1.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MirandaFlower2,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=1037522614,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MirandaFlower3,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=1037522614,
        trigger_delay=2.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MirandaFlower4,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=1037522614,
        trigger_delay=0.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MirandaFlower5,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=1037522614,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MirandaFlower6,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=1037522614,
        trigger_delay=2.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MirandaFlower7,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=1037522614,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(0, 1037520622, 30000, 20000, 1037522614, 0.0, 0, 0, 0, 0)


@RestartOnRest(1035542210)
def Event_1035542210(_, character: uint):
    """Event 1035542210"""
    AND_1.Add(FlagEnabled(1037520350))
    if AND_1:
        return
    DisableCharacter(character)
    
    MAIN.Await(HealthRatio(Characters.RayaLucariaScholar) < 0.699999988079071)
    
    EnableCharacter(character)
    AddSpecialEffect(character, 8971)


@RestartOnRest(1037522220)
def Event_1037522220():
    """Event 1037522220"""
    Kill(1037520220)
    Kill(1037520221)
    Kill(1037520222)
    Kill(1037520223)
    Kill(1037520224)
    Kill(1037520225)
    Kill(1037520226)
    Kill(1037520227)
    Kill(1037520228)
    Kill(1037520229)


@RestartOnRest(1037522900)
def Event_1037522900(
    _,
    grace_flag: uint,
    character: uint,
    asset: uint,
    enemy_block_distance: float,
    character_1: uint,
    character_2: uint,
    flag: uint,
):
    """Event 1037522900"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableCharacter(character_2)
    DisableAsset(asset)
    Wait(1.0)
    
    MAIN.Await(CharacterDead(character_1))
    
    CreateTemporaryVFX(vfx_id=1060, anchor_entity=asset, model_point=200, anchor_type=CoordEntityType.Asset)
    EnableFlag(flag)
    Wait(0.5)
    EnableCharacter(character)
    EnableCharacter(character_2)
    EnableAsset(asset)

    # --- Label 0 --- #
    DefineLabel(0)
    RegisterGrace(
        grace_flag=grace_flag,
        asset=asset,
        reaction_distance=5.0,
        reaction_angle=180.0,
        enemy_block_distance=enemy_block_distance,
    )


@RestartOnRest(1037522300)
def Event_1037522300():
    """Event 1037522300"""
    RemoveSpecialEffect(Characters.DemiHuman6, 5070)
    RemoveSpecialEffect(Characters.DemiHumanShaman0, 5070)


@RestartOnRest(1037522350)
def Event_1037522350(_, character: uint):
    """Event 1037522350"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    ForceAnimation(character, 3021, wait_for_completion=True)
    DisableThisSlotFlag()
    End()


@RestartOnRest(1037522370)
def Event_1037522370(_, character: uint):
    """Event 1037522370"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    ForceAnimation(character, 3022, wait_for_completion=True)
    DisableThisSlotFlag()
    End()
