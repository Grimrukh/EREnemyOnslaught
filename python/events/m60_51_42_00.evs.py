"""DONE
North Caelid (NE) (SE)

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
    CommonFunc_NonRespawningWithReward(0, dead_flag=1051420299, character=1051420299, item_lot=40428, reward_delay=0.0, skip_reward=0, clone=0)
