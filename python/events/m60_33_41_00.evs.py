"""
Southwest Liurnia (SW) (NE)

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
from .entities.m60_33_41_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=1033410350,
        character=Characters.GlintstoneDragon0,
        item_lot=1033410400,
        reward_delay=0.0,
        skip_reward=0,
    )
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=1033410351,
        character=Characters.GlintstoneDragon1,
        item_lot=1033410410,
        reward_delay=0.0,
        skip_reward=0,
    )
    CommonFunc_NonRespawningWithReward(0, dead_flag=1033410340, character=Characters.RedWolf, item_lot=0, reward_delay=0.0, skip_reward=0)
    CommonFunc_90005920(0, flag=1033410600, asset=1033411600, obj_act_id=1033413600)
    CommonFunc_90005920(0, flag=1033410601, asset=1033411601, obj_act_id=1033413601)
    CommonFunc_90005920(0, 1033410602, 1033411602, 1033413602)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.RedWolf,
        animation_id=30001,
        animation_id_1=20001,
        region=1033412340,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.GlintstoneDragon0,
        inactive_animation=30000,
        active_animation=20000,
        radius=17.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRadius(0, 1033410350, 17.0, 0.0, -1)
