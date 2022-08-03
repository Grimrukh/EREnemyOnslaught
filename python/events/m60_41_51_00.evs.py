"""DONE
South Altus Plateau (NW) (NE)

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
from .entities.m60_41_51_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""

    # DOUBLE TREE SENTINEL
    CommonFunc_FieldBossMusicHealthBar(
        0, boss=Characters.TreeSentinelLeft, name=903251600, npc_threat_level=12,
        clone_boss=0, clone_name=0,  # no health bar for clones
    )
    CommonFunc_FieldBossMusicHealthBar(
        0, boss=Characters.TreeSentinelRight, name=903251600, npc_threat_level=12,
        clone_boss=0, clone_name=0,  # no health bar for clones
    )
    TreeSentinelDuoDies(
        0,
        flag=1041510800,
        left=0,
        sentinel_1=Characters.TreeSentinelLeft,
        clone_1=Characters.CLONE_TreeSentinelLeft,
        left_1=0,
        item_lot=30335,
        sentinel_2=Characters.TreeSentinelRight,
        clone_2=Characters.CLONE_TreeSentinelRight,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.TreeSentinelLeft,
        region=1041512500,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.CLONE_TreeSentinelLeft,
        region=1041512500,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.TreeSentinelRight,
        region=1041512500,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.CLONE_TreeSentinelRight,
        region=1041512500,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    TreeSentinelEventTargets(
        0, character=Characters.TreeSentinelLeft, character_1=Characters.TreeSentinelRight
    )
    TreeSentinelEventTargets(
        1, character=Characters.CLONE_TreeSentinelLeft, character_1=Characters.CLONE_TreeSentinelRight
    )
    TreeSentinelMusicHeatUp(
        0,
        character=Characters.TreeSentinelLeft,
        character_1=Characters.TreeSentinelRight,
        npc_threat_level=12,
        flag=1041512815,
    )
    TreeSentinelDuoPhaseTwoTransition(
        0, character=Characters.TreeSentinelLeft, character_1=Characters.TreeSentinelRight
    )
    TreeSentinelCloneDies(0, Characters.TreeSentinelLeft, Characters.CLONE_TreeSentinelLeft)
    TreeSentinelCloneDies(1, Characters.TreeSentinelRight, Characters.CLONE_TreeSentinelRight)

    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.LeyndellKnight2,
        region=1041512202,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_1041512200(0, character=Characters.LeyndellKnight0)
    Event_1041512200(1, character=Characters.LeyndellKnight1)
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=1041510410,
        character=Characters.GiantMirandaFlower,
        item_lot=0,
        reward_delay=0.0,
        skip_reward=0,
        clone=Characters.CLONE_GiantMirandaFlower,
    )
    Event_1041512270()
    Event_1041512270(slot=1)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.GiantMirandaFlower, region=1041512410, seconds=0.0, animation_id=700)
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.GraveSkeleton2,
        inactive_animation=30016,
        active_animation=20016,
        radius=100.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.GraveSkeleton0,
        animation_id=30017,
        animation_id_1=20017,
        region=1041512450,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.GraveSkeleton1,
        animation_id=30017,
        animation_id_1=20017,
        region=1041512450,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(0, 1041510453, 30016, 20016, 1041512453, 0.0, 0, 0, 0, 0)


@RestartOnRest(1041512200)
def Event_1041512200(_, character: uint):
    """Event 1041512200"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8092)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(1041512270)
def Event_1041512270():
    """Event 1041512270"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=Characters.Dummy)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1041512270))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1041512271,
            model_point=900,
            behavior_id=802103070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.0)
    Restart()


@RestartOnRest(1041512310)
def TreeSentinelEventTargets(_, character: uint, character_1: uint):
    """Event 1041512310"""
    if FlagEnabled(1041510800):
        return
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    Wait(30.0)
    EnableAI(character)
    EnableAI(character_1)
    SetCharacterEventTarget(character, entity=character_1)
    SetCharacterEventTarget(character_1, entity=character)
    Restart()


@RestartOnRest(1041512320)
def TreeSentinelDuoPhaseTwoTransition(_, character: uint, character_1: uint):
    """Event 1041512320"""
    if FlagEnabled(1041510800):
        return
    OR_1.Add(CharacterDead(character))
    OR_1.Add(CharacterDead(character_1))
    OR_2.Add(OR_1)
    AND_1.Add(HealthRatio(character) <= 0.5)
    AND_1.Add(HealthRatio(character_1) <= 0.5)
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableNetworkFlag(1041512815)


@ContinueOnRest(1041512321)
def TreeSentinelMusicHeatUp(_, character: uint, character_1: uint, npc_threat_level: uint, flag: uint):
    """Event 1041512321"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    
    MAIN.Await(AND_1)
    
    EnableFieldBattleMusicHeatUp(npc_threat_level=npc_threat_level)
    AND_2.Add(CharacterDead(character))
    AND_2.Add(CharacterDead(character_1))
    OR_2.Add(AND_2)
    OR_2.Add(FieldBattleMusicDisabled(npc_threat_level=npc_threat_level))
    
    MAIN.Await(OR_2)
    
    DisableFieldBattleMusicHeatUp(npc_threat_level=npc_threat_level)
    Wait(0.30000001192092896)
    Restart()


@RestartOnRest(1041512800)
def TreeSentinelDuoDies(
    _,
    flag: uint,
    left: uint,
    sentinel_1: uint,
    clone_1: uint,
    left_1: uint,
    item_lot: int,
    sentinel_2: uint,
    clone_2: uint,
):
    """Event 1041512800"""
    if ValueNotEqual(left=item_lot, right=0):
        Unknown_2004_76(flag=flag, item_lot=item_lot)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(sentinel_1)
    DisableCharacter(clone_1)
    DisableCharacter(sentinel_2)
    DisableCharacter(clone_2)
    DisableAnimations(sentinel_1)
    DisableAnimations(clone_1)
    DisableAnimations(sentinel_2)
    DisableAnimations(clone_2)
    Kill(sentinel_1)
    Kill(clone_1)
    Kill(sentinel_2)
    Kill(clone_2)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    Wait(1.0)
    AwardItemLot(item_lot, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(sentinel_1)
    EnableCharacter(clone_1)
    EnableCharacter(sentinel_2)
    EnableCharacter(clone_2)
    EnableAnimations(sentinel_1)
    EnableAnimations(clone_1)
    EnableAnimations(sentinel_2)
    EnableAnimations(clone_2)

    # Clones are immortal and refer their damage to the originals.
    EnableImmortality(clone_1)
    ReferDamageToEntity(clone_1, sentinel_1)
    EnableImmortality(clone_2)
    ReferDamageToEntity(clone_2, sentinel_2)

    AND_15.Add(HealthValue(sentinel_1) <= 0)
    AND_15.Add(HealthValue(sentinel_2) <= 0)
    
    MAIN.Await(AND_15)
    
    Wait(2.0)
    PlaySoundEffect(sentinel_1, 888880000, sound_type=SoundType.s_SFX)
    AND_14.Add(CharacterDead(sentinel_1))
    AND_14.Add(CharacterDead(sentinel_2))
    
    MAIN.Await(AND_14)
    
    SkipLinesIfUnsignedEqual(6, left=left_1, right=3)
    SkipLinesIfUnsignedEqual(4, left=left_1, right=2)
    SkipLinesIfUnsignedEqual(2, left=left_1, right=1)
    KillBossAndDisplayBanner(character=sentinel_1, banner_type=BannerType.EnemyFelled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=sentinel_1, banner_type=BannerType.GreatEnemyFelled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=sentinel_1, banner_type=BannerType.DemigodFelled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=sentinel_1, banner_type=BannerType.LegendFelled)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag)
    if UnsignedNotEqual(left=left, right=0):
        EnableFlag(left)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    Wait(5.0)
    AwardItemLot(item_lot, host_only=True)
    End()


@RestartOnRest(1041512810)
def TreeSentinelCloneDies(_, sentinel: uint, clone: uint):
    """Immortal clone dies when Sentinel dies."""
    if FlagEnabled(1041510800):
        return

    MAIN.Await(HealthValue(sentinel) <= 0)

    Kill(clone)
