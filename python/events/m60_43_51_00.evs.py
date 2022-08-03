"""DONE
South Altus Plateau (NE) (NE)

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
from .entities.m60_43_51_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_NonRespawningWithReward(0, dead_flag=1043510500, character=1043510500, item_lot=40314, reward_delay=0.0, skip_reward=0, clone=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Slug0,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=1043512400,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Slug1,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=1043512400,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Slug2,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=1043512400,
        trigger_delay=0.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Slug3,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=1043512400,
        trigger_delay=0.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(0, 1043510404, 30001, 20001, 1043512400, 0.0, 0, 0, 0, 0)
