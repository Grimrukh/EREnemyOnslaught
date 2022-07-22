"""
East Liurnia (NW) (NE)

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
from .entities.m60_37_47_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.AncestralFollower,
        region=1037472200,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.WildMouflon,
        inactive_animation=30005,
        active_animation=20021,
        radius=15.0,
        delay=2.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.Runebear,
        inactive_animation=30000,
        active_animation=20000,
        radius=10.0,
        delay=1.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.WildMouflon, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Runebear, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_900005610(0, 1037471680, 100, 800, 0)
