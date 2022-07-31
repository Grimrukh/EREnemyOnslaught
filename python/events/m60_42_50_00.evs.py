"""
South Altus Plateau (NE) (SW)

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
from .entities.m60_42_50_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_NonRespawningWithReward(0, dead_flag=1042500300, character=1042500300, item_lot=1042500020, reward_delay=0.0, skip_reward=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.UlceratedTreeSpirit,
        inactive_animation=30000,
        active_animation=20000,
        radius=30.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.LeyndellFootSoldier1,
        inactive_animation=30001,
        active_animation=20001,
        radius=30.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRadius(0, 1042500351, 100.0, 0.0, 0)
