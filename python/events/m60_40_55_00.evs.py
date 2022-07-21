"""
North Altus Plateau (NW) (NW)

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
from .entities.m60_40_55_00_entities import *


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Rat0, region=1040552301, radius=2.0, seconds=0.0, animation_id=3005)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Rat1, region=1040552302, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Rat2, region=1040552302, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Rat3, region=1040552302, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.GiantRat, region=1040552250, seconds=0.0, animation_id=0)
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=1040552403,
        trigger_delay=0.20000000298023224,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=1040552403,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(0, 1040550403, 30000, 20000, 1040552403, 0.0, 0, 0, 0, 0)
