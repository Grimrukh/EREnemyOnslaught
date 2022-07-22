"""
Southeast Mountaintops (NW) (SW)

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
from .entities.m60_52_54_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1052540000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76510,
        flag_1=76506,
        asset=Assets.AEG099_090_9000,
        source_flag=77500,
        value=6,
        flag_2=78500,
        flag_3=78501,
        flag_4=78502,
        flag_5=78503,
        flag_6=78504,
        flag_7=78505,
        flag_8=78506,
        flag_9=78507,
        flag_10=78508,
        flag_11=78509,
    )
    Event_1052542200(0, character=1052545200)
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.LesserFingercreeper0,
        inactive_animation=30003,
        active_animation=20003,
        trigger_region=1052542304,
        trigger_delay=1.7000000476837158,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.LesserFingercreeper1,
        inactive_animation=30003,
        active_animation=20003,
        trigger_region=1052542304,
        trigger_delay=1.7000000476837158,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.LesserFingercreeper2,
        inactive_animation=30004,
        active_animation=20004,
        trigger_region=1052542304,
        trigger_delay=1.7000000476837158,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Fingercreeper,
        inactive_animation=30003,
        active_animation=20003,
        trigger_region=1052542311,
        trigger_delay=1.899999976158142,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=1052540320,
        inactive_animation=30005,
        active_animation=20005,
        trigger_region=1052542320,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.MassiveFingercreeper,
        inactive_animation=30005,
        active_animation=20005,
        trigger_region=1052542321,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=1052540322,
        inactive_animation=30005,
        active_animation=20005,
        trigger_region=1052542322,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.SnowTroll0,
        inactive_animation=30003,
        active_animation=20003,
        trigger_region=1052542331,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.SnowTroll2, region=1052542334, radius=50.0, seconds=0.0, animation_id=0)
    CommonFunc_NonRespawningWithReward(0, dead_flag=1052540491, character=Characters.SnowTroll0, item_lot_param_id=0, reward_delay=0.0, skip_reward=0)
    CommonFunc_NonRespawningWithReward(0, dead_flag=1052540492, character=Characters.SnowTroll1, item_lot_param_id=0, reward_delay=0.0, skip_reward=0)
    CommonFunc_NonRespawningWithReward(0, dead_flag=1052540494, character=Characters.SnowTroll2, item_lot_param_id=0, reward_delay=0.0, skip_reward=0)
    CommonFunc_90005771(0, 1052540950, 1052542700)


@RestartOnRest(1052542200)
def Event_1052542200(_, character: uint):
    """Event 1052542200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()
