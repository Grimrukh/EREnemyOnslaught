"""DONE
Road's End Catacombs

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
from .entities.m30_03_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005646(
        0,
        flag=Flags.SnailDead,
        left_flag=30032840,
        cancel_flag__right_flag=30032841,
        asset=Assets.AEG099_065_9000,
        player_start=30032840,
        area_id=30,
        block_id=3,
        cc_id=0,
        dd_id=0,
    )
    RegisterGrace(grace_flag=300300, asset=Assets.AEG099_060_9001)
    SnailDies()
    SnailBattleTrigger()
    SnailCommonEvents()
    SnailWarpRequest(
        0,
        snail=Characters.Snail,
        flag_1=Flags.SnailWarpingDisabled,
        flag_2=Flags.SnailWarpFlag0,
        flag_3=Flags.SnailWarpFlag1,
        flag_4=Flags.SnailWarpFlag2,
        flag_5=Flags.SnailWarpFlag3,
        flag_6=Flags.SnailWarpFlag4,
        flag_7=Flags.SnailWarpFlag5,
        flag_8=Flags.SnailWarpFlag6,
        flag_9=Flags.SnailWarpFlag7,
        flag_10=Flags.SnailWarpFlag8,
        flag_11=Flags.SnailWarpFlag9,
        flag_12=Flags.SnailWarpFlag10,
        flag_13=Flags.SnailWarpFlag11,
        warping_flag=Flags.SnailIsWarping,
    )
    SnailWarpRequest(
        30,
        snail=Characters.CLONE_Snail,
        flag_1=Flags.CLONE_SnailWarpingDisabled,
        flag_2=Flags.CLONE_SnailWarpFlag0,
        flag_3=Flags.CLONE_SnailWarpFlag1,
        flag_4=Flags.CLONE_SnailWarpFlag2,
        flag_5=Flags.CLONE_SnailWarpFlag3,
        flag_6=Flags.CLONE_SnailWarpFlag4,
        flag_7=Flags.CLONE_SnailWarpFlag5,
        flag_8=Flags.CLONE_SnailWarpFlag6,
        flag_9=Flags.CLONE_SnailWarpFlag7,
        flag_10=Flags.CLONE_SnailWarpFlag8,
        flag_11=Flags.CLONE_SnailWarpFlag9,
        flag_12=Flags.CLONE_SnailWarpFlag10,
        flag_13=Flags.CLONE_SnailWarpFlag11,
        warping_flag=Flags.CLONE_SnailIsWarping,
    )
    SnailWarps(
        0,
        snail=Characters.Snail,
        warping_disabled_flag=Flags.SnailWarpingDisabled,
        warp_flag_0=Flags.SnailWarpFlag0,
        warp_flag_1=Flags.SnailWarpFlag1,
        warp_flag_2=Flags.SnailWarpFlag2,
        warp_flag_3=Flags.SnailWarpFlag3,
        warp_flag_4=Flags.SnailWarpFlag4,
        warp_flag_5=Flags.SnailWarpFlag5,
        warp_flag_6=Flags.SnailWarpFlag6,
        warp_flag_7=Flags.SnailWarpFlag7,
        warp_flag_8=Flags.SnailWarpFlag8,
        warp_flag_9=Flags.SnailWarpFlag9,
        warp_flag_10=Flags.SnailWarpFlag10,
        warp_flag_11=Flags.SnailWarpFlag11,
        is_warping_flag=Flags.SnailIsWarping,
    )
    SnailWarps(  # 30032848
        10,
        snail=Characters.CLONE_Snail,
        warping_disabled_flag=Flags.CLONE_SnailWarpingDisabled,
        warp_flag_0=Flags.CLONE_SnailWarpFlag0,
        warp_flag_1=Flags.CLONE_SnailWarpFlag1,
        warp_flag_2=Flags.CLONE_SnailWarpFlag2,
        warp_flag_3=Flags.CLONE_SnailWarpFlag3,
        warp_flag_4=Flags.CLONE_SnailWarpFlag4,
        warp_flag_5=Flags.CLONE_SnailWarpFlag5,
        warp_flag_6=Flags.CLONE_SnailWarpFlag6,
        warp_flag_7=Flags.CLONE_SnailWarpFlag7,
        warp_flag_8=Flags.CLONE_SnailWarpFlag8,
        warp_flag_9=Flags.CLONE_SnailWarpFlag9,
        warp_flag_10=Flags.CLONE_SnailWarpFlag10,
        warp_flag_11=Flags.CLONE_SnailWarpFlag11,
        is_warping_flag=Flags.CLONE_SnailIsWarping,
    )
    SnailSummonSpawning(
        0,
        snail=Characters.Snail,
        summon_0=Characters.CrucibleKnightSummon0,
        summon_1=Characters.CrucibleKnightSummon1,
        summon_2=Characters.CrucibleKnightSummon2,
        summon_3=Characters.CrucibleKnightSummon3,
        summon_4=Characters.CrucibleKnightSummon4,
        summon_5=Characters.CrucibleKnightSummon5,
        summon_6=Characters.CrucibleKnightSummon6,
        summon_7=Characters.CrucibleKnightSummon7,
        summon_8=Characters.CrucibleKnightSummon8,
        summon_9=Characters.CrucibleKnightSummon9,
        spawner_1=Spawners.SnailCrucibleKnightSpawner1,
        spawner_2=Spawners.SnailCrucibleKnightSpawner2,
        spawner_3=Spawners.SnailCrucibleKnightSpawner3,
        spawner_4=Spawners.SnailCrucibleKnightSpawner4,
        spawner_5=Spawners.SnailCrucibleKnightSpawner5,
        spawner_6=Spawners.SnailCrucibleKnightSpawner6,
        summoning_unlocked_flag=Flags.SnailSummoningActivated,
        summon_0_unlocked_flag=Flags.CrucibleKnightSummon0Unlocked,
        summon_1_unlocked_flag=Flags.CrucibleKnightSummon1Unlocked,
        summons_23_unlocked_flag=Flags.CrucibleKnightSummons23Unlocked,
        summons_45_unlocked_flag=Flags.CrucibleKnightSummons45Unlocked,
        summons_67_unlocked_flag=Flags.CrucibleKnightSummons67Unlocked,
        summons_89_unlocked_flag=Flags.CrucibleKnightSummons89Unlocked,
        summon_0_killed_flag=Flags.CrucibleKnightSummon0Killed,
        summon_1_killed_flag=Flags.CrucibleKnightSummon1Killed,
        summons_23_killed_flag=Flags.CrucibleKnightSummons23Killed,
        summons_45_killed_flag=Flags.CrucibleKnightSummons45Killed,
        summons_67_killed_flag=Flags.CrucibleKnightSummons67Killed,
        warping_disabled_flag=Flags.SnailWarpingDisabled,
        is_warping_flag=Flags.SnailIsWarping,
    )
    SnailSummonSpawning(  # 30032891
        1,
        snail=Characters.CLONE_Snail,
        summon_0=Characters.CLONE_CrucibleKnightSummon0,
        summon_1=Characters.CLONE_CrucibleKnightSummon1,
        summon_2=Characters.CLONE_CrucibleKnightSummon2,
        summon_3=Characters.CLONE_CrucibleKnightSummon3,
        summon_4=Characters.CLONE_CrucibleKnightSummon4,
        summon_5=Characters.CLONE_CrucibleKnightSummon5,
        summon_6=Characters.CLONE_CrucibleKnightSummon6,
        summon_7=Characters.CLONE_CrucibleKnightSummon7,
        summon_8=Characters.CLONE_CrucibleKnightSummon8,
        summon_9=Characters.CLONE_CrucibleKnightSummon9,
        spawner_1=Spawners.CLONE_SnailCrucibleKnightSpawner1,
        spawner_2=Spawners.CLONE_SnailCrucibleKnightSpawner2,
        spawner_3=Spawners.CLONE_SnailCrucibleKnightSpawner3,
        spawner_4=Spawners.CLONE_SnailCrucibleKnightSpawner4,
        spawner_5=Spawners.CLONE_SnailCrucibleKnightSpawner5,
        spawner_6=Spawners.CLONE_SnailCrucibleKnightSpawner6,
        summoning_unlocked_flag=Flags.CLONE_SnailSummoningActivated,
        summon_0_unlocked_flag=Flags.CLONE_CrucibleKnightSummon0Unlocked,
        summon_1_unlocked_flag=Flags.CLONE_CrucibleKnightSummon1Unlocked,
        summons_23_unlocked_flag=Flags.CLONE_CrucibleKnightSummons23Unlocked,
        summons_45_unlocked_flag=Flags.CLONE_CrucibleKnightSummons45Unlocked,
        summons_67_unlocked_flag=Flags.CLONE_CrucibleKnightSummons67Unlocked,
        summons_89_unlocked_flag=Flags.CLONE_CrucibleKnightSummons89Unlocked,
        summon_0_killed_flag=Flags.CLONE_CrucibleKnightSummon0Killed,
        summon_1_killed_flag=Flags.CLONE_CrucibleKnightSummon1Killed,
        summons_23_killed_flag=Flags.CLONE_CrucibleKnightSummons23Killed,
        summons_45_killed_flag=Flags.CLONE_CrucibleKnightSummons45Killed,
        summons_67_killed_flag=Flags.CLONE_CrucibleKnightSummons67Killed,
        warping_disabled_flag=Flags.CLONE_SnailWarpingDisabled,
        is_warping_flag=Flags.CLONE_SnailIsWarping,
    )
    SnailPhaseTwoTransition(
        0,
        snail=Characters.Snail,
        warping_disabled_flag=Flags.SnailWarpingDisabled,
        warp_flag=Flags.SnailWarpFlag11,
    )
    SnailPhaseTwoTransition(  # 30032846
        1,
        snail=Characters.CLONE_Snail,
        warping_disabled_flag=Flags.CLONE_SnailWarpingDisabled,
        warp_flag=Flags.CLONE_SnailWarpFlag11,
    )
    BuffFirstSnailSummon(0, summon=Characters.CrucibleKnightSummon0, flag=Flags.CrucibleKnightSummon0Unlocked)
    BuffAdditionalSnailSummon(0, summon=Characters.CrucibleKnightSummon1, flag=Flags.CrucibleKnightSummon1Unlocked)
    BuffAdditionalSnailSummon(1, summon=Characters.CrucibleKnightSummon2, flag=Flags.CrucibleKnightSummons23Unlocked)
    BuffAdditionalSnailSummon(2, summon=Characters.CrucibleKnightSummon3, flag=Flags.CrucibleKnightSummons23Unlocked)
    BuffAdditionalSnailSummon(3, summon=Characters.CrucibleKnightSummon4, flag=Flags.CrucibleKnightSummons45Unlocked)
    BuffAdditionalSnailSummon(4, summon=Characters.CrucibleKnightSummon5, flag=Flags.CrucibleKnightSummons45Unlocked)
    BuffAdditionalSnailSummon(5, summon=Characters.CrucibleKnightSummon6, flag=Flags.CrucibleKnightSummons67Unlocked)
    BuffAdditionalSnailSummon(6, summon=Characters.CrucibleKnightSummon7, flag=Flags.CrucibleKnightSummons67Unlocked)
    BuffAdditionalSnailSummon(7, summon=Characters.CrucibleKnightSummon8, flag=Flags.CrucibleKnightSummons89Unlocked)
    BuffAdditionalSnailSummon(8, summon=Characters.CrucibleKnightSummon9, flag=Flags.CrucibleKnightSummons89Unlocked)

    BuffFirstSnailSummon(
        10, summon=Characters.CLONE_CrucibleKnightSummon0, flag=Flags.CLONE_CrucibleKnightSummon0Unlocked
    )
    BuffAdditionalSnailSummon(
        10, summon=Characters.CLONE_CrucibleKnightSummon1, flag=Flags.CLONE_CrucibleKnightSummon1Unlocked
    )
    BuffAdditionalSnailSummon(
        11, summon=Characters.CLONE_CrucibleKnightSummon2, flag=Flags.CLONE_CrucibleKnightSummons23Unlocked
    )
    BuffAdditionalSnailSummon(
        12, summon=Characters.CLONE_CrucibleKnightSummon3, flag=Flags.CLONE_CrucibleKnightSummons23Unlocked
    )
    BuffAdditionalSnailSummon(
        13, summon=Characters.CLONE_CrucibleKnightSummon4, flag=Flags.CLONE_CrucibleKnightSummons45Unlocked
    )
    BuffAdditionalSnailSummon(
        14, summon=Characters.CLONE_CrucibleKnightSummon5, flag=Flags.CLONE_CrucibleKnightSummons45Unlocked
    )
    BuffAdditionalSnailSummon(
        15, summon=Characters.CLONE_CrucibleKnightSummon6, flag=Flags.CLONE_CrucibleKnightSummons67Unlocked
    )
    BuffAdditionalSnailSummon(
        16, summon=Characters.CLONE_CrucibleKnightSummon7, flag=Flags.CLONE_CrucibleKnightSummons67Unlocked
    )
    BuffAdditionalSnailSummon(
        17, summon=Characters.CLONE_CrucibleKnightSummon8, flag=Flags.CLONE_CrucibleKnightSummons89Unlocked
    )
    BuffAdditionalSnailSummon(
        18, summon=Characters.CLONE_CrucibleKnightSummon9, flag=Flags.CLONE_CrucibleKnightSummons89Unlocked
    )

    CommonFunc_90005650(
        0,
        flag=30030540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_0500,
        obj_act_id=30033541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30030540, anchor_entity=Assets.AEG027_041_0500)
    Event_30032400(
        0,
        owner_entity=Characters.TalkDummy2,
        entity=Assets.AEG027_044_0500,
        region=30032600,
        behavior_id=0,
        source_entity=30032601,
        source_entity_1=30032602,
        source_entity_2=30032603,
    )
    CommonFunc_90005525(0, flag=30030570, asset=Assets.AEG027_157_0500)
    CommonFunc_90005525(0, flag=30030571, asset=Assets.AEG027_157_0501)
    CommonFunc_90005525(0, flag=30030572, asset=Assets.AEG027_157_0502)
    CommonFunc_90005525(0, flag=30030573, asset=Assets.AEG027_157_0503)
    CommonFunc_90005525(0, flag=30030574, asset=Assets.AEG027_157_0504)
    CommonFunc_90005525(0, flag=30030575, asset=Assets.AEG027_157_0505)
    CommonFunc_90005525(0, flag=30030576, asset=Assets.AEG027_157_0506)
    CommonFunc_90005525(0, flag=30030577, asset=Assets.AEG027_157_0507)
    Event_30032579()
    CommonFunc_90005410(0, flag=30032100, character=30031100, entity_b=30035100)
    CommonFunc_90005411(0, asset=Assets.AEG099_053_9000, character=Characters.TalkDummy1, left=10)
    CommonFunc_91005600(0, flag=Flags.SnailDead, asset=30031695, model_point=3)
    CommonFunc_90005920(0, 30030520, 30031520, 30033520)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_30030050()
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Imp0, region=30032200, seconds=0.0, animation_id=3005)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0, character=Characters.Imp1, region=30032201, radius=1.0, seconds=0.0, animation_id=3012
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.Imp2,
        animation_id=30010,
        animation_id_1=20010,
        region=30032202,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Imp3,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=30032203,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.Imp4,
        inactive_animation=30010,
        active_animation=20010,
        radius=15.0,
        delay=2.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    Event_30032205(
        0,
        character=Characters.Imp5,
        animation_id=30010,
        animation_id_1=20010,
        region=30032204,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_30032205(
        1,
        character=Characters.Imp6,
        animation_id=30010,
        animation_id_1=20010,
        region=30032204,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Imp7, region=30032207, seconds=0.0, animation_id=0)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Imp8, region=30032208, seconds=0.0, animation_id=0)
    Event_30032207(0, character=Characters.Imp7, region=30032307)
    Event_30032207(1, character=Characters.Imp8, region=30032308)
    Event_30032207(2, character=Characters.Imp9, region=30032307)
    CommonFunc_TriggerInactiveEnemy_WithRegion(0, 30030209, 30002, 20002, 30032207, 3.0, 0, 0, 0, 0)


@ContinueOnRest(30030050)
def Event_30030050():
    """Event 30030050"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(30030500)


@RestartOnRest(30032579)
def Event_30032579():
    """Event 30032579"""
    DisableAsset(Assets.AEG027_157_0505)


@RestartOnRest(30032400)
def Event_30032400(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
):
    """Event 30032400"""
    CreateProjectileOwner(entity=owner_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))

    MAIN.Await(AND_1)

    ForceAnimation(entity, 1, wait_for_completion=True)
    Wait(0.5)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L1)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L2)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            model_point=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(3.0)

    MAIN.Await(AllPlayersOutsideRegion(region=region))

    ForceAnimation(entity, 3, wait_for_completion=True)
    Restart()


@RestartOnRest(30032205)
def Event_30032205(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 30032205"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    if UnsignedNotEqual(left=0, right=region):
        OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)

    MAIN.Await(OR_2)

    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    Wait(2.0)
    ForceAnimation(character, 3016, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(30032207)
def Event_30032207(_, character: uint, region: uint):
    """Event 30032207"""
    OR_15.Add(CharacterDead(character))
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    AddSpecialEffect(character, 17155)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))

    MAIN.Await(OR_2)

    RemoveSpecialEffect(character, 17155)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(30032800)
def SnailDies():
    """Event 30032800"""
    if FlagEnabled(Flags.SnailDead):
        return

    AND_7.Add(HealthValue(Characters.Snail) <= 0)
    AND_7.Add(HealthValue(Characters.CLONE_Snail) <= 0)
    MAIN.Await(AND_7)

    Kill(Characters.CrucibleKnightSummon0)
    Kill(Characters.CrucibleKnightSummon1)
    Kill(Characters.CrucibleKnightSummon2)
    Kill(Characters.CrucibleKnightSummon3)
    Kill(Characters.CrucibleKnightSummon4)
    Kill(Characters.CrucibleKnightSummon5)
    Kill(Characters.CrucibleKnightSummon6)
    Kill(Characters.CrucibleKnightSummon7)
    Kill(Characters.CrucibleKnightSummon8)
    Kill(Characters.CrucibleKnightSummon9)
    Kill(Characters.CLONE_CrucibleKnightSummon0)
    Kill(Characters.CLONE_CrucibleKnightSummon3)
    Kill(Characters.CLONE_CrucibleKnightSummon4)
    Kill(Characters.CLONE_CrucibleKnightSummon5)
    Kill(Characters.CLONE_CrucibleKnightSummon1)
    Kill(Characters.CLONE_CrucibleKnightSummon2)
    Kill(Characters.CLONE_CrucibleKnightSummon6)
    Kill(Characters.CLONE_CrucibleKnightSummon7)
    Kill(Characters.CLONE_CrucibleKnightSummon8)
    Kill(Characters.CLONE_CrucibleKnightSummon9)
    DisableSpawner(entity=Spawners.SnailCrucibleKnightSpawner1)
    DisableSpawner(entity=Spawners.SnailCrucibleKnightSpawner2)
    DisableSpawner(entity=Spawners.SnailCrucibleKnightSpawner3)
    DisableSpawner(entity=Spawners.SnailCrucibleKnightSpawner4)
    DisableSpawner(entity=Spawners.SnailCrucibleKnightSpawner5)
    DisableSpawner(entity=Spawners.SnailCrucibleKnightSpawner6)
    DisableSpawner(entity=Spawners.CLONE_SnailCrucibleKnightSpawner1)
    DisableSpawner(entity=Spawners.CLONE_SnailCrucibleKnightSpawner2)
    DisableSpawner(entity=Spawners.CLONE_SnailCrucibleKnightSpawner3)
    DisableSpawner(entity=Spawners.CLONE_SnailCrucibleKnightSpawner4)
    DisableSpawner(entity=Spawners.CLONE_SnailCrucibleKnightSpawner5)
    DisableSpawner(entity=Spawners.CLONE_SnailCrucibleKnightSpawner6)
    Wait(4.0)
    PlaySoundEffect(Characters.Snail, 888880000, sound_type=SoundType.s_SFX)

    AND_8.Add(CharacterDead(Characters.Snail))
    AND_8.Add(CharacterDead(Characters.CLONE_Snail))
    MAIN.Await(AND_8)

    KillBossAndDisplayBanner(character=Characters.Snail, banner_type=BannerType.EnemyFelled)
    EnableFlag(Flags.SnailDead)
    if PlayerInOwnWorld():
        EnableFlag(61206)
    EnableFlag(9206)


@RestartOnRest(30032810)
def SnailBattleTrigger():
    """Event 30032810"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.SnailDead)
    DisableCharacter(Characters.Snail)
    DisableAnimations(Characters.Snail)
    Kill(Characters.Snail)
    Kill(Characters.CrucibleKnightSummon0)
    DisableSpawner(entity=Spawners.SnailCrucibleKnightSpawner1)
    DisableSpawner(entity=Spawners.SnailCrucibleKnightSpawner2)
    DisableSpawner(entity=Spawners.SnailCrucibleKnightSpawner3)
    DisableSpawner(entity=Spawners.SnailCrucibleKnightSpawner4)
    DisableSpawner(entity=Spawners.SnailCrucibleKnightSpawner5)
    DisableSpawner(entity=Spawners.SnailCrucibleKnightSpawner6)
    DisableSpawner(entity=Spawners.CLONE_SnailCrucibleKnightSpawner1)
    DisableSpawner(entity=Spawners.CLONE_SnailCrucibleKnightSpawner2)
    DisableSpawner(entity=Spawners.CLONE_SnailCrucibleKnightSpawner3)
    DisableSpawner(entity=Spawners.CLONE_SnailCrucibleKnightSpawner4)
    DisableSpawner(entity=Spawners.CLONE_SnailCrucibleKnightSpawner5)
    DisableSpawner(entity=Spawners.CLONE_SnailCrucibleKnightSpawner6)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Snail)
    DisableAI(Characters.CLONE_Snail)
    if PlayerInOwnWorld():
        ForceAnimation(Characters.Snail, 30013)
        ForceAnimation(Characters.CLONE_Snail, 30013)
    AND_2.Add(FlagEnabled(30032805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30032800))

    MAIN.Await(AND_2)

    EnableAI(Characters.Snail)
    EnableAI(Characters.CLONE_Snail)
    SetNetworkUpdateRate(Characters.Snail, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_Snail, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Snail, name=904140300, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_Snail, name=904140300, bar_slot=0)

    GotoIfPlayerNotInOwnWorld(Label.L1)

    # ORIGINAL
    DisableNetworkConnectedFlagRange(flag_range=(Flags.SnailWarpingDisabled, Flags.SnailIsWarping))
    EnableNetworkFlag(Flags.SnailWarpingDisabled)
    EnableNetworkFlag(Flags.SnailIsWarping)
    Wait(1.2000000476837158)
    EnableFlag(30032812)
    ForceSpawnerToSpawn(spawner=Spawners.SnailCrucibleKnightSpawner1)
    EnableNetworkFlag(Flags.CrucibleKnightSummon0Unlocked)

    # CLONE
    DisableNetworkConnectedFlagRange(flag_range=(30032822, 30032839))
    EnableNetworkFlag(30032822)
    EnableNetworkFlag(30032839)
    Wait(1.2000000476837158)
    EnableFlag(30032812)
    ForceSpawnerToSpawn(spawner=Spawners.SnailCrucibleKnightSpawner1)
    EnableNetworkFlag(Flags.CrucibleKnightSummon0Unlocked)

    ForceAnimation(Characters.Snail, 20013)
    ForceAnimation(Characters.CLONE_Snail, 20013)

    # --- Label 1 --- #
    DefineLabel(1)


@RestartOnRest(30032849)
def SnailCommonEvents():
    """Event 30032849"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.SnailDead,
        fog_asset=Assets.AEG099_001_9000,
        fog_region=30032800,
        host_entered_fog_flag=30032805,
        boss_characters=30035800,
        action_button_id=10000,
        first_time_done_flag=0,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.SnailDead,
        fog_asset=Assets.AEG099_001_9000,
        fog_region=30032800,
        host_entered_fog_flag=30032805,
        summon_entered_fog_flag=30032806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(
        0, boss_dead_flag=Flags.SnailDead, fog_asset=Assets.AEG099_001_9000, model_point=3, required_flag=0
    )
    CommonFunc_ControlBossMusic(0, Flags.SnailDead, 920200, 30032805, 30032806, 0, 30032860, 0, 0)


@RestartOnRest(30032890)
def SnailSummonSpawning(
    _,
    snail: uint,
    summon_0: uint,
    summon_1: uint,
    summon_2: uint,
    summon_3: uint,
    summon_4: uint,
    summon_5: uint,
    summon_6: uint,
    summon_7: uint,
    summon_8: uint,
    summon_9: uint,
    spawner_1: uint,
    spawner_2: uint,
    spawner_3: uint,
    spawner_4: uint,
    spawner_5: uint,
    spawner_6: uint,
    summoning_unlocked_flag: int,
    summon_0_unlocked_flag: int,
    summon_1_unlocked_flag: int,
    summons_23_unlocked_flag: int,
    summons_45_unlocked_flag: int,
    summons_67_unlocked_flag: int,
    summons_89_unlocked_flag: int,
    summon_0_killed_flag: int,
    summon_1_killed_flag: int,
    summons_23_killed_flag: int,
    summons_45_killed_flag: int,
    summons_67_killed_flag: int,
    warping_disabled_flag: int,
    is_warping_flag: int,
):
    """Event 30032890"""
    DisableNetworkSync()
    if FlagEnabled(Flags.SnailDead):
        return
    if PlayerNotInOwnWorld():
        return

    AwaitFlagEnabled(flag=30032805)  # battle started

    GotoIfFlagEnabled(Label.L1, flag=summon_0_killed_flag)

    MAIN.Await(CharacterDead(summon_0))

    Wait(1.0)
    AddSpecialEffect(snail, 15044)

    AND_1.Add(HealthRatio(snail) < 0.8999999761581421)
    SkipLinesIfConditionTrue(4, AND_1)
    # Snail still has >90% HP. Stay with first spawner only.
    DisableNetworkConnectedFlagRange(flag_range=(warping_disabled_flag, is_warping_flag))
    EnableNetworkFlag(warping_disabled_flag)
    EnableNetworkFlag(is_warping_flag)
    Goto(Label.L0)  # respawn Crucible Knight 0 and restart

    # Snail has less than 90% HP and can start warping.
    DisableNetworkFlag(warping_disabled_flag)
    EnableNetworkFlag(summon_0_killed_flag)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L2, flag=summon_1_killed_flag)

    MAIN.Await(CharacterDead(summon_1))

    Wait(1.0)
    AddSpecialEffect(snail, 15044)
    EnableNetworkFlag(summon_1_killed_flag)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfFlagEnabled(Label.L10, flag=summons_23_killed_flag)
    AND_9.Add(CharacterDead(summon_2))
    AND_9.Add(CharacterDead(summon_3))

    MAIN.Await(AND_9)

    Wait(1.0)
    AddSpecialEffect(snail, 15044)
    EnableNetworkFlag(summons_23_killed_flag)
    Goto(Label.L0)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L11, flag=summons_45_killed_flag)
    AND_10.Add(CharacterDead(summon_4))
    AND_10.Add(CharacterDead(summon_5))

    MAIN.Await(AND_10)

    Wait(1.0)
    AddSpecialEffect(snail, 15044)
    EnableNetworkFlag(summons_45_killed_flag)
    Goto(Label.L0)

    # --- Label 11 --- #
    DefineLabel(11)
    GotoIfFlagEnabled(Label.L12, flag=summons_67_killed_flag)
    AND_2.Add(CharacterDead(summon_6))
    AND_2.Add(CharacterDead(summon_7))

    MAIN.Await(AND_2)

    Wait(1.0)
    AddSpecialEffect(snail, 15044)
    EnableNetworkFlag(summons_67_killed_flag)
    Goto(Label.L0)

    # --- Label 12 --- #
    DefineLabel(12)
    AND_11.Add(CharacterDead(summon_8))
    AND_11.Add(CharacterDead(summon_9))

    MAIN.Await(AND_11)

    Wait(1.0)
    AddSpecialEffect(snail, 15044)

    # --- Label 0 --- #
    DefineLabel(0)

    MAIN.Await(CharacterHasSpecialEffect(snail, 15007))

    AND_3.Add(HealthRatio(snail) >= 0.8999999761581421)
    GotoIfConditionFalse(Label.L3, input_condition=AND_3)
    ForceSpawnerToSpawn(spawner=spawner_1)

    MAIN.Await(CharacterAlive(summon_0))

    EnableNetworkFlag(summon_0_unlocked_flag)
    AddSpecialEffect(snail, 15045)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L9, flag=summons_67_killed_flag)
    ForceSpawnerToSpawn(spawner=spawner_6)
    AND_8.Add(CharacterAlive(summon_8))
    AND_8.Add(CharacterAlive(summon_9))

    MAIN.Await(AND_8)

    EnableNetworkFlag(summons_89_unlocked_flag)
    AddSpecialEffect(snail, 15045)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    GotoIfFlagDisabled(Label.L8, flag=summons_45_killed_flag)
    ForceSpawnerToSpawn(spawner=spawner_5)
    AND_6.Add(CharacterAlive(summon_6))
    AND_6.Add(CharacterAlive(summon_7))

    MAIN.Await(AND_6)

    EnableNetworkFlag(summons_67_unlocked_flag)
    AddSpecialEffect(snail, 15045)
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    GotoIfFlagDisabled(Label.L4, flag=summons_23_killed_flag)
    ForceSpawnerToSpawn(spawner=spawner_4)
    AND_5.Add(CharacterAlive(summon_4))
    AND_5.Add(CharacterAlive(summon_5))

    MAIN.Await(AND_5)

    EnableNetworkFlag(summons_45_unlocked_flag)
    AddSpecialEffect(snail, 15045)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfFlagDisabled(Label.L5, flag=summon_1_killed_flag)
    ForceSpawnerToSpawn(spawner=spawner_3)
    EnableFlag(30032860)
    AND_7.Add(CharacterAlive(summon_2))
    AND_7.Add(CharacterAlive(summon_3))

    MAIN.Await(AND_7)

    EnableNetworkFlag(summons_23_unlocked_flag)
    AddSpecialEffect(snail, 15045)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagDisabled(Label.L6, flag=summon_0_killed_flag)
    ForceSpawnerToSpawn(spawner=spawner_2)

    MAIN.Await(CharacterAlive(summon_1))

    EnableNetworkFlag(summon_1_unlocked_flag)
    AddSpecialEffect(snail, 15045)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagDisabled(Label.L7, flag=summoning_unlocked_flag)
    ForceSpawnerToSpawn(spawner=spawner_1)
    EnableNetworkFlag(summon_0_unlocked_flag)

    MAIN.Await(CharacterAlive(summon_0))

    AddSpecialEffect(snail, 15045)
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)


@RestartOnRest(30032845)
def SnailPhaseTwoTransition(_, snail: uint, warping_disabled_flag: int, warp_flag: int):
    """Event 30032845"""
    DisableNetworkSync()
    if FlagEnabled(Flags.SnailDead):
        return
    if PlayerNotInOwnWorld():
        return

    MAIN.Await(HealthRatio(snail) < 0.8999999761581421)

    DisableNetworkFlag(warping_disabled_flag)
    EnableNetworkFlag(warp_flag)


@RestartOnRest(30032821)
def SnailWarpRequest(
    _,
    snail: uint,
    flag_1: int,
    flag_2: int,
    flag_3: int,
    flag_4: int,
    flag_5: int,
    flag_6: int,
    flag_7: int,
    flag_8: int,
    flag_9: int,
    flag_10: int,
    flag_11: int,
    flag_12: int,
    flag_13: int,
    warping_flag: int,
):
    """Event 30032821"""
    DisableNetworkSync()
    if FlagEnabled(Flags.SnailDead):
        return
    if PlayerNotInOwnWorld():
        return
    AND_15.Add(CharacterHasSpecialEffect(snail, 15046))
    AND_15.Add(FlagEnabled(warping_flag))

    MAIN.Await(AND_15)

    OR_15.Add(HealthRatio(snail) >= 0.8999999761581421)
    GotoIfConditionTrue(Label.L0, input_condition=OR_15)

    GotoIfFlagEnabled(Label.L0, flag=flag_1)

    GotoIfFlagEnabled(Label.L1, flag=flag_2)
    GotoIfFlagEnabled(Label.L1, flag=flag_3)
    GotoIfFlagEnabled(Label.L1, flag=flag_4)

    GotoIfFlagEnabled(Label.L2, flag=flag_5)
    GotoIfFlagEnabled(Label.L2, flag=flag_6)
    GotoIfFlagEnabled(Label.L2, flag=flag_7)

    GotoIfFlagEnabled(Label.L3, flag=flag_8)
    GotoIfFlagEnabled(Label.L3, flag=flag_9)
    GotoIfFlagEnabled(Label.L3, flag=flag_10)

    GotoIfFlagEnabled(Label.L4, flag=flag_11)
    GotoIfFlagEnabled(Label.L4, flag=flag_12)
    GotoIfFlagEnabled(Label.L4, flag=flag_13)

    # --- Label 0 --- #
    DefineLabel(0)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableNetworkConnectedFlagRange(flag_range=(flag_2, flag_13))
    EnableRandomFlagInRange(flag_range=(flag_8, flag_13))
    DisableNetworkFlag(warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableNetworkConnectedFlagRange(flag_range=(flag_2, flag_13))
    EnableRandomFlagInRange(flag_range=(flag_8, flag_13))
    DisableNetworkFlag(warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableNetworkConnectedFlagRange(flag_range=(flag_2, flag_13))
    EnableRandomFlagInRange(flag_range=(flag_2, flag_7))
    DisableNetworkFlag(warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    DisableNetworkConnectedFlagRange(flag_range=(flag_2, flag_13))
    EnableRandomFlagInRange(flag_range=(flag_2, flag_7))
    DisableNetworkFlag(warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()


@ContinueOnRest(30032838)
def SnailWarps(
    _,
    snail: uint,
    warping_disabled_flag: int,
    warp_flag_0: int,
    warp_flag_1: int,
    warp_flag_2: int,
    warp_flag_3: int,
    warp_flag_4: int,
    warp_flag_5: int,
    warp_flag_6: int,
    warp_flag_7: int,
    warp_flag_8: int,
    warp_flag_9: int,
    warp_flag_10: int,
    warp_flag_11: int,
    is_warping_flag: int,
):
    """Event 30032838"""
    DisableNetworkSync()
    if FlagEnabled(Flags.SnailDead):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(warp_flag_0, warp_flag_11)))
    AND_1.Add(FlagDisabled(is_warping_flag))
    AND_1.Add(CharacterHasSpecialEffect(snail, 15046))

    MAIN.Await(AND_1)

    GotoIfFlagEnabled(Label.L0, flag=warping_disabled_flag)
    GotoIfFlagEnabled(Label.L1, flag=warp_flag_0)
    GotoIfFlagEnabled(Label.L2, flag=warp_flag_1)
    GotoIfFlagEnabled(Label.L3, flag=warp_flag_2)
    GotoIfFlagEnabled(Label.L4, flag=warp_flag_3)
    GotoIfFlagEnabled(Label.L5, flag=warp_flag_4)
    GotoIfFlagEnabled(Label.L6, flag=warp_flag_5)
    GotoIfFlagEnabled(Label.L7, flag=warp_flag_6)
    GotoIfFlagEnabled(Label.L8, flag=warp_flag_7)
    GotoIfFlagEnabled(Label.L9, flag=warp_flag_8)
    GotoIfFlagEnabled(Label.L10, flag=warp_flag_9)
    GotoIfFlagEnabled(Label.L11, flag=warp_flag_10)
    GotoIfFlagEnabled(Label.L12, flag=warp_flag_11)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNetworkFlag(is_warping_flag)
    DisableNetworkFlag(warping_disabled_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    Move(snail, destination=30032823, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(is_warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    Move(snail, destination=30032824, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(is_warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    Move(snail, destination=30032825, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(is_warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    Move(snail, destination=30032826, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(is_warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    Move(snail, destination=30032827, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(is_warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    Move(snail, destination=30032828, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(is_warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    Move(snail, destination=30032829, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(is_warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    Move(snail, destination=30032830, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(is_warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    Move(snail, destination=30032831, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(is_warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    Move(snail, destination=30032832, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(is_warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 11 --- #
    DefineLabel(11)
    Move(snail, destination=30032833, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(is_warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()

    # --- Label 12 --- #
    DefineLabel(12)
    Move(snail, destination=30032834, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(is_warping_flag)

    MAIN.Await(CharacterDoesNotHaveSpecialEffect(snail, 15046))

    Restart()


@RestartOnRest(30032870)
def BuffFirstSnailSummon(_, summon: uint, flag: uint):
    """Event 30032870"""
    if FlagEnabled(Flags.SnailDead):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterAlive(summon))

    MAIN.Await(AND_1)

    Wait(1.0)
    ActivateMultiplayerBuffs(summon)

    MAIN.Await(CharacterDead(summon))

    Restart()


@RestartOnRest(30032871)
def BuffAdditionalSnailSummon(_, summon: uint, flag: uint):
    """Event 30032871"""
    if FlagEnabled(Flags.SnailDead):
        return

    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterAlive(summon))
    AND_2.Add(AND_1)
    AND_3.Add(Singleplayer())
    AND_2.Add(not AND_3)

    MAIN.Await(AND_2)

    ActivateMultiplayerBuffs(summon)
    Wait(1.0)
    OR_1.Add(CharacterHasSpecialEffect(summon, 7820))
    OR_1.Add(CharacterHasSpecialEffect(summon, 7821))
    OR_1.Add(CharacterHasSpecialEffect(summon, 7822))
    SkipLinesIfConditionTrue(1, OR_1)
    Restart()
