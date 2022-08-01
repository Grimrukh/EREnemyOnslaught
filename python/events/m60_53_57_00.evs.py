"""
Northeast Mountaintops (SW) (NE)

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


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1053572200(0, character=1053575200)
    CommonFunc_NonRespawningWithReward(0, dead_flag=1053570210, character=1053570210, item_lot=40510, reward_delay=0.0, skip_reward=0, clone=0)


@RestartOnRest(1053572200)
def Event_1053572200(_, character: uint):
    """Event 1053572200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()
