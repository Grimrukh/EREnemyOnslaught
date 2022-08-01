"""
Southwest Liurnia (NW) (NE)

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
from .entities.m60_33_43_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_FieldBossMusicHealthBar(
        0,
        boss=Characters.ErdtreeAvatar,
        name=904810600,
        npc_threat_level=18,
        clone_boss=Characters.CLONE_ErdtreeAvatar,
        clone_name=0,
    )
    CommonFunc_FieldBossNonRespawningWithReward(
        0,
        dead_flag=1033430800,
        extra_flag_to_enable=0,
        boss=Characters.ErdtreeAvatar,
        boss_banner_choice=0,
        item_lot=30205,
        seconds=0.0,
        clone_boss=Characters.CLONE_ErdtreeAvatar,
    )
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.ErdtreeAvatar, radius=20.0, seconds=0.0, animation_id=0
    )
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.CLONE_ErdtreeAvatar, radius=20.0, seconds=0.0, animation_id=0
    )
    CommonFunc_FieldBossMusicHeatUp(
        0, boss_character=Characters.ErdtreeAvatar, npc_threat_level=18, optional_trigger_flag=0
    )
    CommonFunc_900005610(0, asset=Assets.AEG003_316_9000, vfx_id=100, model_point=800, right=1033438600)
    CommonFunc_NonRespawningWithReward(0, 1033430200, Characters.Scarab, 40238, 0.0, 0, clone=0)
