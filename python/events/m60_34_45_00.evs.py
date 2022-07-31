"""
West Liurnia (SE) (NW)

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
from .entities.m60_34_45_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_FieldBossMusicHealthBar(
        0, boss=Characters.GlintstoneDragonSmarag, name=NameText.GlintstoneDragonSmarag, npc_threat_level=25,
        clone_boss=Characters.CLONE_GlintstoneDragonSmarag, clone_name=NameText.CLONE_GlintstoneDragonSmarag,
    )
    CommonFunc_FieldBossNonRespawningWithRewardAndMessage(
        0,
        dead_flag=1034450800,
        extra_flag_to_enable=0,
        boss=Characters.GlintstoneDragonSmarag,
        boss_banner_choice=1,
        item_lot=30210,
        message=30061,
        seconds=0.0,
        clone_boss=Characters.CLONE_GlintstoneDragonSmarag,
    )
    Event_1034452800()
    Event_1034452805()
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.GlintstoneDragonSmarag,
        animation_id=30000,
        animation_id_1=20000,
        region=1034452800,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.CLONE_GlintstoneDragonSmarag,
        animation_id=30000,
        animation_id_1=20000,
        region=1034452800,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.GlintstoneDragonSmarag,
        region=1034452800,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.CLONE_GlintstoneDragonSmarag,
        region=1034452800,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Scarab4, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Scarab5, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Scarab6, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Scarab7, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Scarab8, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Scarab0, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Scarab1, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Scarab2, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Scarab3, radius=7.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005460(0, character=Characters.RayaLucariaScholar)
    CommonFunc_90005460(0, character=1034450201)
    CommonFunc_90005460(0, character=1034450202)
    CommonFunc_90005460(0, character=1034450203)
    CommonFunc_90005460(0, character=1034450204)
    CommonFunc_90005461(0, character=Characters.RayaLucariaScholar)
    CommonFunc_90005462(0, character=Characters.RayaLucariaScholar)
    CommonFunc_90005461(0, character=1034450201)
    CommonFunc_90005462(0, character=1034450201)
    CommonFunc_90005461(0, character=1034450202)
    CommonFunc_90005462(0, character=1034450202)
    CommonFunc_90005461(0, character=1034450203)
    CommonFunc_90005462(0, character=1034450203)
    CommonFunc_90005461(0, character=1034450204)
    CommonFunc_90005462(0, character=1034450204)
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.RayaLucariaScholar,
        inactive_animation=30010,
        active_animation=-1,
        radius=0.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_900005610(0, asset=Assets.AEG003_316_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005620(
        0,
        flag=1034450570,
        asset=Assets.AEG027_078_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=Assets.AEG027_217_9000,
        left_flag=1034452571,
        cancel_flag__right_flag=1034452572,
        right=1034452573,
    )
    CommonFunc_90005621(0, 1034450570, 1034451573)


@RestartOnRest(1034452800)
def Event_1034452800():
    """Event 1034452800"""
    if FlagEnabled(1034450800):
        return
    AddSpecialEffect(Characters.GlintstoneDragonSmarag, 10247)
    AddSpecialEffect(Characters.CLONE_GlintstoneDragonSmarag, 10247)


@RestartOnRest(1034452805)
def Event_1034452805():
    """Event 1034452805"""
    if FlagEnabled(1034450800):
        return
    SetNest(Characters.GlintstoneDragonSmarag, region=1034452810)
    SetNest(Characters.CLONE_GlintstoneDragonSmarag, region=1034452810)
    Wait(1.0)
    Restart()
