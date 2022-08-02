"""DONE
South Altus Plateau (NW) (NW)

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
from .entities.m60_40_51_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_NonRespawningWithReward(0, dead_flag=1040510500, character=Characters.Scarab, item_lot=40310, reward_delay=0.0, skip_reward=0, clone=0)
    CommonFunc_90005706(0, 1040510700, 930023, 0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Commoner)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.LeyndellFootSoldier1, region=1040512407, seconds=0.0, animation_id=3003)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.LeyndellFootSoldier2, region=1040512407, seconds=0.0, animation_id=3003)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.LeyndellFootSoldier1, region=1040512408, seconds=0.0, animation_id=0)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.LeyndellFootSoldier2, region=1040512408, seconds=0.0, animation_id=0)
    CommonFunc_TriggerInactiveEnemy_WithRadius(0, 1040510406, 30001, 20001, 5.0, 0.0, 0, 0, 0, 0)
