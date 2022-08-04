"""DONE
Southwest Mountaintops (NE) (NE)

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
from .entities.m60_51_55_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_NonRespawningWithReward(
        0, dead_flag=1051550300, character=Characters.GuardianGolem, item_lot=0, reward_delay=0.0, skip_reward=0,
        clone=Characters.CLONE_GuardianGolem
    )


@ContinueOnRest(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005485(0, 1051550300)
