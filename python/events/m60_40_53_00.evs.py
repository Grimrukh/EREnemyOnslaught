"""
North Altus Plateau (SW) (NW)

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
from .entities.m60_40_53_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=76306, asset=Assets.AEG099_060_9000)
    Event_1040532800()
    Event_1040532810()
    Event_1040532849()
    AttachAssetToAsset(child_asset=1040531201, parent_asset=1040531200, parent_model_point=151)
    Event_1040532650()
    Event_1040532660()
    Event_1040532665()
    Event_1040532670()
    Event_1040532680()
    Event_1040532685()
    Event_1040532690()
    CommonFunc_NonRespawningWithReward(0, dead_flag=1040530500, character=1040530500, item_lot=40320, reward_delay=0.0, skip_reward=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.BleedDog1, region=1040532400, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=1040530401,
        region=1040532400,
        radius=7.0,
        seconds=0.4000000059604645,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.AltusDog, region=1040532404, radius=7.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.AltusDog, region=1040532430, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.BleedDog0, region=1040532402, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.LivingMass0,
        region=1040532430,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.LivingMass1,
        region=1040532430,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.LivingMass2,
        region=1040532430,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.LivingMass3,
        region=1040532430,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.LivingMass4,
        region=1040532430,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530435, region=1040532430, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530436, region=1040532430, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530437, region=1040532430, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530438, region=1040532430, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530439, region=1040532430, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530440, region=1040532430, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530441, region=1040532430, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530442, region=1040532430, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530443, region=1040532430, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530444, region=1040532430, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530445, region=1040532430, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.LivingMass6,
        region=1040532452,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.LivingMass7,
        region=1040532452,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.LivingMass8,
        region=1040532452,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.LivingMass9,
        region=1040532452,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.LivingMass10,
        region=1040532452,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530456, region=1040532452, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530457, region=1040532452, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530458, region=1040532452, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530461, region=1040532452, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530462, region=1040532452, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530463, region=1040532452, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=1040530464, region=1040532452, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.LivingMassAlt,
        region=1040532452,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.LivingMass5,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=1040532450,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=1040530250,
        inactive_animation=30010,
        active_animation=20010,
        radius=5.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=1040530260,
        inactive_animation=30010,
        active_animation=20010,
        radius=5.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=1040530212, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=1040530267, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.LeyndellFootSoldier2,
        inactive_animation=30001,
        active_animation=20001,
        radius=5.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.LeyndellSoldier,
        inactive_animation=30004,
        active_animation=20004,
        trigger_region=1040532207,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.LeyndellFootSoldier0,
        inactive_animation=30010,
        active_animation=20010,
        trigger_region=1040532207,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.LeyndellFootSoldier1,
        inactive_animation=30010,
        active_animation=20010,
        trigger_region=1040532207,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.BleedDog2, radius=6.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.LivingMass11, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Wormface3, region=1040532357, seconds=0.0, animation_id=3000)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Wormface3, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.Wormface1,
        inactive_animation=30000,
        active_animation=20000,
        radius=5.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.Wormface6,
        inactive_animation=30000,
        active_animation=20000,
        radius=8.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.Wormface7,
        inactive_animation=30000,
        active_animation=20000,
        radius=8.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.Wormface8,
        inactive_animation=30000,
        active_animation=20000,
        radius=8.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Wormface0, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005221(0, character=1040530390, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Slug0,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=1040532405,
        trigger_delay=1.2000000476837158,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Slug1,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=1040532405,
        trigger_delay=0.30000001192092896,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Slug2,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=1040532405,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(0, 1040530303, 30000, 20000, 1040532405, 0.800000011920929, 0, 0, 0, 0)


@RestartOnRest(1040532800)
def Event_1040532800():
    """Event 1040532800"""
    if FlagEnabled(1040530800):
        return
    
    MAIN.Await(HealthValue(Characters.SanguineNoble) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.SanguineNoble, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.SanguineNoble))
    
    KillBossAndDisplayBanner(character=Characters.SanguineNoble, banner_type=BannerType.EnemyFelled)
    EnableAssetActivation(Assets.AEG004_970_1002, obj_act_id=1110064)
    EnableFlag(1040530800)


@RestartOnRest(1040532810)
def Event_1040532810():
    """Event 1040532810"""
    GotoIfFlagDisabled(Label.L0, flag=1040530800)
    DisableCharacter(Characters.SanguineNoble)
    DisableAnimations(Characters.SanguineNoble)
    Kill(Characters.SanguineNoble)
    EnableAssetActivation(Assets.AEG004_970_1002, obj_act_id=1110064)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.SanguineNoble)
    ForceAnimation(Characters.SanguineNoble, 30000, loop=True)
    AND_2.Add(FlagEnabled(1040532805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=1040532800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkUpdateRate(Characters.SanguineNoble, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(Characters.SanguineNoble, 20000)
    EnableAI(Characters.SanguineNoble)
    Wait(2.799999952316284)
    EnableBossHealthBar(Characters.SanguineNoble, name=903550540)
    DisableAssetActivation(Assets.AEG004_970_1002, obj_act_id=1110064)


@RestartOnRest(1040532849)
def Event_1040532849():
    """Event 1040532849"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=1040530800,
        fog_asset=Assets.AEG099_001_9000,
        fog_region=1040532800,
        host_entered_fog_flag=1040532805,
        boss_characters=1040535800,
        action_button_id=10000,
        first_time_done_flag=0,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=1040530800,
        fog_asset=Assets.AEG099_001_9000,
        fog_region=1040532800,
        host_entered_fog_flag=1040532805,
        summon_entered_fog_flag=1040532806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=1040530800, fog_asset=Assets.AEG099_001_9000, model_point=3, required_flag=0)
    CommonFunc_ControlBossMusic(
        0,
        boss_dead_flag=1040530800,
        bgm_boss_conv_param_id=920900,
        host_in_battle=1040532805,
        summon_in_battle=1040532806,
        extra_required_flag=0,
        phase_two_flag=1040532802,
        useless_phase_two_check=0,
        use_stop_type_1=0,
    )
    CommonFunc_9005812(0, 1040530800, 1040531801, 3, 0, 0)


@RestartOnRest(1040532650)
def Event_1040532650():
    """Event 1040532650"""
    GotoIfFlagEnabled(Label.L0, flag=1040530655)
    DisableAsset(Assets.AEG003_316_9000)
    DeleteVFX(1040532650, erase_root_only=False)
    
    MAIN.Await(FlagEnabled(1039530505))
    
    EnableAsset(Assets.AEG003_316_9000)
    CreateVFX(1040532650)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(Assets.AEG003_316_9000)
    DeleteVFX(1040532650, erase_root_only=False)
    End()


@RestartOnRest(1040532660)
def Event_1040532660():
    """Event 1040532660"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1040530655):
        return
    AND_1.Add(FlagEnabled(1039530505))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1040532651))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9521, entity=Assets.AEG003_316_9000))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1040530655)
    DisableAsset(Assets.AEG003_316_9000)
    DisableMapPiece(map_piece_id=1040532651)
    RotateToFaceEntity(PLAYER, Assets.AEG003_316_9000, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010)
    Wait(1.0)
    PlaySoundEffect(1040532650, 806855, sound_type=SoundType.s_SFX)
    DeleteVFX(1040532650)
    End()


@RestartOnRest(1040532665)
def Event_1040532665():
    """Event 1040532665"""
    MAIN.Await(FlagEnabled(1040530655))
    
    Wait(1.0)
    PlaySoundEffect(1040532650, 806855, sound_type=SoundType.s_SFX)
    DeleteVFX(1040532650)
    End()


@RestartOnRest(1040532670)
def Event_1040532670():
    """Event 1040532670"""
    GotoIfFlagEnabled(Label.L0, flag=1040530655)
    DisableAsset(Assets.AEG007_234_1000)
    
    MAIN.Await(FlagEnabled(1039530505))
    
    EnableAsset(Assets.AEG007_234_1000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(Assets.AEG007_234_1000)
    End()


@RestartOnRest(1040532680)
def Event_1040532680():
    """Event 1040532680"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AttackedWithDamageType(attacked_entity=1040531651, attacker=20000))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1040530680)
    End()


@RestartOnRest(1040532685)
def Event_1040532685():
    """Event 1040532685"""
    MAIN.Await(FlagEnabled(1040530680))
    
    ForceAnimation(Assets.AEG007_234_1000, 1, wait_for_completion=True)
    DisableAsset(Assets.AEG007_234_1000)
    End()


@RestartOnRest(1040532690)
def Event_1040532690():
    """Event 1040532690"""
    AND_15.Add(FlagEnabled(1040530655))
    GotoIfConditionTrue(Label.L2, input_condition=AND_15)
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)

    # --- Label 2 --- #
    DefineLabel(2)
    Kill(Characters.Imp, award_runes=True)
    if AND_15:
        return

    # --- Label 0 --- #
    DefineLabel(0)
    DisableSpawner(entity=1040533610)
    GotoIfFlagEnabled(Label.L1, flag=1040532701)
    DisableSpawner(entity=1040533610)
    AND_1.Add(FlagEnabled(1039530505))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1040532610))
    
    MAIN.Await(AND_1)
    
    EnableSpawner(entity=1040533610)
    ClearTargetList(Characters.Imp)
    ForceSpawnerToSpawn(spawner=1040533610)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(CharacterDead(Characters.Imp))
    SkipLinesIfConditionFalse(4, AND_2)
    WaitRandomSeconds(min_seconds=10.0, max_seconds=10.0)
    EnableSpawner(entity=1040533610)
    ClearTargetList(Characters.Imp)
    ForceSpawnerToSpawn(spawner=1040533610)
    if FlagEnabled(1040530655):
        Wait(5.0)
    DisableSpawner(entity=1040533610)
    EnableFlag(1040532701)
    Restart()
