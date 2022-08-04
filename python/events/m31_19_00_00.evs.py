"""DONE
Sage's Cave

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
from .entities.m31_19_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=31190000, asset=Assets.AEG099_060_9000)

    # BLACK KNIFE ASSASSIN
    Event_31192800()
    Event_31192810()
    Event_31192849()
    Event_31192830()
    Event_31192811()

    # GARRIS
    Event_31192850()
    Event_31192860()
    Event_31192899()
    GarrisPhaseTwo(0, Characters.NecromancerGarris, Spawners.GarrisSnailSpawner1, 31192871)
    GarrisPhaseTwo(8, Characters.CLONE_NecromancerGarris, Spawners.CLONE_GarrisSnailSpawner1, 31192873)  # 31192869
    FirstGarrisSnailDies(0, Characters.Snail0, Spawners.GarrisSnailSpawner0, 31192870)
    FirstGarrisSnailDies(1, Characters.CLONE_Snail0, Spawners.CLONE_GarrisSnailSpawner0, 31192872)
    Event_31192880()
    Event_31192863(0, character=Characters.Snail1, flag=31192870)
    Event_31192863(1, character=Characters.Snail2, flag=31192871)
    Event_31192863(2, character=Characters.CLONE_Snail1, flag=31192872)
    Event_31192863(3, character=Characters.CLONE_Snail2, flag=31192873)

    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Skeleton0, region=31192200, radius=3.0, seconds=0.0, animation_id=0)
    Event_31192210(0, character=Characters.Skeleton1, region=31192210, radius=2.0, seconds=0.0, animation_id=0)
    Event_31192210(1, character=Characters.Skeleton2, region=31192210, radius=2.0, seconds=0.0, animation_id=0)
    Event_31192210(2, character=Characters.Skeleton3, region=31192210, radius=2.0, seconds=0.0, animation_id=0)
    Event_31192210(3, character=Characters.Skeleton4, region=31192210, radius=2.0, seconds=1.0, animation_id=0)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Skeleton5, region=31192219, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Skeleton6, region=31192219, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Skeleton7, region=31192220, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.GraveSkeleton, region=31192219, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=31190280, region=31192218, radius=3.0, seconds=0.0, animation_id=3001)
    CommonFunc_90005525(0, flag=31190600, asset=Assets.AEG027_069_1000)
    CommonFunc_90005525(0, flag=31190601, asset=Assets.AEG027_069_1001)
    CommonFunc_90005525(0, flag=31190602, asset=Assets.AEG027_069_1002)
    CommonFunc_90005525(0, flag=31190603, asset=Assets.AEG027_069_1003)
    CommonFunc_90005525(0, flag=31190604, asset=Assets.AEG027_069_1004)
    CommonFunc_90005525(0, flag=31190605, asset=Assets.AEG027_069_1005)
    CommonFunc_90005646(
        0,
        flag=31190800,
        left_flag=31192840,
        cancel_flag__right_flag=31192841,
        asset=Assets.AEG099_065_9000,
        player_start=31192840,
        area_id=31,
        block_id=19,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_90005646(0, 31190850, 31192890, 31192891, 31191890, 31192840, 31, 19, 0, 0)


@RestartOnRest(31192210)
def Event_31192210(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 31192210"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_2.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(FlagEnabled(31190603))
    AND_2.Add(FlagEnabled(31190603))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Skeleton1))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Skeleton1, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Skeleton1, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Skeleton1, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Skeleton1, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Skeleton1, state_info=260))
    OR_2.Add(HasAIStatus(Characters.Skeleton1, ai_status=AIStatusType.Battle))
    OR_5.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_5.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_5.Add(AND_1)
    OR_5.Add(AND_2)
    OR_5.Add(OR_2)
    
    MAIN.Await(OR_5)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=OR_2)
    Wait(seconds)

    # --- Label 1 --- #
    DefineLabel(1)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)
    EnableAI(character)


@RestartOnRest(35002250)
def Event_35002250(
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
    """Event 35002250"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_2.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Skeleton1))
    OR_2.Add(HasAIStatus(Characters.Skeleton1, ai_status=AIStatusType.Battle))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Skeleton1, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Skeleton1, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Skeleton1, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Skeleton1, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.Skeleton1, state_info=260))
    OR_5.Add(AND_1)
    OR_5.Add(AND_2)
    OR_5.Add(OR_2)
    
    MAIN.Await(OR_5)
    
    AND_10.Add(OR_5)
    
    MAIN.Await(AND_10)
    
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_5)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(31190600)
def Event_31190600(_, flag: uint, asset: uint):
    """Event 31190600"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AttackedWithDamageType(attacked_entity=asset, attacker=20000))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    ForceAnimation(asset, 1, wait_for_completion=True)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(asset)


@RestartOnRest(31192800)
def Event_31192800():
    """Event 31192800"""
    if FlagEnabled(31190800):
        return
    
    AND_7.Add(HealthValue(Characters.BlackKnifeAssassin) <= 0)
    AND_7.Add(HealthValue(Characters.CLONE_BlackKnifeAssassin) <= 0)
    MAIN.Await(AND_7)
    
    Wait(4.0)
    PlaySoundEffect(Characters.BlackKnifeAssassin, 888880000, sound_type=SoundType.s_SFX)
    
    AND_8.Add(CharacterDead(Characters.BlackKnifeAssassin))
    AND_8.Add(CharacterDead(Characters.CLONE_BlackKnifeAssassin))
    MAIN.Await(AND_8)
    
    KillBossAndDisplayBanner(character=Characters.BlackKnifeAssassin, banner_type=BannerType.EnemyFelled)
    EnableFlag(31190800)
    EnableFlag(9242)
    if PlayerInOwnWorld():
        EnableFlag(61242)


@RestartOnRest(31192810)
def Event_31192810():
    """Event 31192810"""
    GotoIfFlagDisabled(Label.L0, flag=31190800)
    DisableCharacter(Characters.BlackKnifeAssassin)
    DisableAnimations(Characters.BlackKnifeAssassin)
    Kill(Characters.BlackKnifeAssassin)
    DisableCharacter(Characters.CLONE_BlackKnifeAssassin)
    DisableAnimations(Characters.CLONE_BlackKnifeAssassin)
    Kill(Characters.CLONE_BlackKnifeAssassin)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.BlackKnifeAssassin)
    DisableAI(Characters.CLONE_BlackKnifeAssassin)
    DisableAnimations(Characters.BlackKnifeAssassin)
    DisableAnimations(Characters.CLONE_BlackKnifeAssassin)
    GotoIfFlagEnabled(Label.L1, flag=31190802)
    AND_1.Add(FlagEnabled(31192805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31192800))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.BlackKnifeAssassin, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.CLONE_BlackKnifeAssassin, attacker=PLAYER))

    MAIN.Await(AND_1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.BlackKnifeAssassin)
    EnableAI(Characters.CLONE_BlackKnifeAssassin)
    EnableAnimations(Characters.BlackKnifeAssassin)
    EnableAnimations(Characters.CLONE_BlackKnifeAssassin)
    SetNetworkUpdateRate(Characters.BlackKnifeAssassin, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_BlackKnifeAssassin, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.BlackKnifeAssassin, name=902100310, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_BlackKnifeAssassin, name=902100310, bar_slot=0)


@RestartOnRest(31192811)
def Event_31192811():
    """Event 31192811"""
    if FlagEnabled(31190800):
        return
    AND_1.Add(HealthRatio(Characters.BlackKnifeAssassin) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(31192802)


@RestartOnRest(31192830)
def Event_31192830():
    """Event 31192830"""
    DisableNetworkSync()
    if FlagEnabled(31190800):
        return
    AND_1.Add(CharacterHasSpecialEffect(20000, 416))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(20000, 14508)
    Wait(1.0)
    Restart()


@RestartOnRest(31192850)
def Event_31192850():
    """Event 31192850"""
    if FlagEnabled(31190850):
        return
    
    AND_7.Add(HealthValue(Characters.NecromancerGarris) <= 0)
    AND_7.Add(HealthValue(Characters.CLONE_NecromancerGarris) <= 0)
    MAIN.Await(AND_7)
    
    Wait(4.0)
    PlaySoundEffect(Characters.NecromancerGarris, 888880000, sound_type=SoundType.s_SFX)
    
    AND_8.Add(CharacterDead(Characters.NecromancerGarris))
    AND_8.Add(CharacterDead(Characters.CLONE_NecromancerGarris))
    MAIN.Await(AND_8)
    
    KillBossAndDisplayBanner(character=Characters.NecromancerGarris, banner_type=BannerType.EnemyFelled)
    Kill(CharacterGroups.GarrisSnails)
    DisableSpawner(entity=Spawners.GarrisSnailSpawner1)
    DisableSpawner(entity=Spawners.CLONE_GarrisSnailSpawner1)
    DisableSpawner(entity=Spawners.GarrisSnailSpawner0)
    DisableSpawner(entity=Spawners.CLONE_GarrisSnailSpawner0)
    EnableFlag(31190850)
    if PlayerInOwnWorld():
        EnableFlag(61249)
    EnableFlag(9249)


@RestartOnRest(31192860)
def Event_31192860():
    """Event 31192860"""
    GotoIfFlagDisabled(Label.L0, flag=31190850)
    DisableCharacter(Characters.NecromancerGarris)
    DisableAnimations(Characters.NecromancerGarris)
    Kill(Characters.NecromancerGarris)
    DisableCharacter(Characters.CLONE_NecromancerGarris)
    DisableAnimations(Characters.CLONE_NecromancerGarris)
    Kill(Characters.CLONE_NecromancerGarris)
    DisableCharacter(CharacterGroups.GarrisSnails)
    DisableAnimations(CharacterGroups.GarrisSnails)
    Kill(CharacterGroups.GarrisSnails)
    DisableSpawner(entity=Spawners.GarrisSnailSpawner1)
    DisableSpawner(entity=Spawners.GarrisSnailSpawner0)
    DisableCharacter(Characters.CLONE_NecromancerGarris)
    DisableAnimations(Characters.CLONE_NecromancerGarris)
    Kill(Characters.CLONE_NecromancerGarris)
    DisableCharacter(Characters.CLONE_CLONE_NecromancerGarris)
    DisableAnimations(Characters.CLONE_CLONE_NecromancerGarris)
    Kill(Characters.CLONE_CLONE_NecromancerGarris)
    DisableSpawner(entity=Spawners.CLONE_GarrisSnailSpawner1)
    DisableSpawner(entity=Spawners.CLONE_GarrisSnailSpawner0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.NecromancerGarris)
    DisableAI(Characters.CLONE_NecromancerGarris)
    ForceAnimation(Characters.NecromancerGarris, 68011)
    ForceAnimation(Characters.CLONE_NecromancerGarris, 68011)
    DisableAI(Characters.Snail0)
    DisableAI(Characters.CLONE_Snail0)
    ForceAnimation(Characters.Snail0, 30000)
    ForceAnimation(Characters.CLONE_Snail0, 30000)
    SetLockOnPoint(character=Characters.Snail0, lock_on_model_point=220, state=False)
    SetLockOnPoint(character=Characters.CLONE_Snail0, lock_on_model_point=220, state=False)
    AND_2.Add(FlagEnabled(31192855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31192850))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(Characters.NecromancerGarris, 68012)
    ForceAnimation(Characters.CLONE_NecromancerGarris, 68012)
    EnableAI(Characters.NecromancerGarris)
    EnableAI(Characters.CLONE_NecromancerGarris)
    SetNetworkUpdateRate(Characters.NecromancerGarris, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_NecromancerGarris, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.NecromancerGarris, name=NameText.NecromancerGarris, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_NecromancerGarris, name=NameText.CLONE_NecromancerGarris, bar_slot=0)
    ForceAnimation(Characters.Snail0, 20000)
    ForceAnimation(Characters.CLONE_Snail0, 20000)
    EnableAI(Characters.Snail0)
    EnableAI(Characters.CLONE_Snail0)
    Wait(3.0)
    SetLockOnPoint(character=Characters.Snail0, lock_on_model_point=220, state=True)
    SetLockOnPoint(character=Characters.CLONE_Snail0, lock_on_model_point=220, state=True)


@RestartOnRest(31192861)
def GarrisPhaseTwo(_, garris: uint, phase_two_spawner: uint, snail_2_flag: int):
    """Event 31192861"""
    DisableNetworkSync()
    if FlagEnabled(31190850):
        return
    AND_1.Add(HealthRatio(garris) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(31192852)  # shared by clone
    if FlagEnabled(31190850):
        return
    EnableSpawner(entity=phase_two_spawner)
    EnableNetworkFlag(snail_2_flag)


@RestartOnRest(31192862)
def FirstGarrisSnailDies(_, snail: uint, spawner: uint, snail_1_flag: int):
    """Event 31192862"""
    DisableNetworkSync()
    if FlagEnabled(31190850):
        return
    
    MAIN.Await(CharacterDead(snail))
    
    if FlagEnabled(31190850):
        return
    EnableSpawner(entity=spawner)
    EnableNetworkFlag(snail_1_flag)


@RestartOnRest(31192863)
def Event_31192863(_, character: uint, flag: uint):
    """Event 31192863"""
    DisableNetworkSync()
    if FlagEnabled(31190850):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterAlive(character))
    AND_2.Add(AND_1)
    AND_3.Add(Singleplayer())
    AND_2.Add(not AND_3)
    
    MAIN.Await(AND_2)
    
    ActivateMultiplayerBuffs(character)
    EnableNetworkFlag(31192875)
    Wait(3.0)
    OR_1.Add(CharacterHasSpecialEffect(character, 7800))
    OR_1.Add(CharacterHasSpecialEffect(character, 7801))
    OR_1.Add(CharacterHasSpecialEffect(character, 7802))
    OR_1.Add(CharacterHasSpecialEffect(character, 7820))
    OR_1.Add(CharacterHasSpecialEffect(character, 7821))
    OR_1.Add(CharacterHasSpecialEffect(character, 7822))
    SkipLinesIfConditionTrue(1, OR_1)
    Restart()
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterDead(character))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(31192875))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(31192875)
    Wait(0.10000000149011612)
    Restart()


@RestartOnRest(31192880)
def Event_31192880():
    """Event 31192880"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(31190605))
    AND_1.Add(FlagDisabled(31190850))
    OR_1.Add(AND_1)
    OR_1.Add(FlagDisabled(31190800))
    EnableFlag(31190890)
    SkipLinesIfConditionFalse(1, OR_1)
    DisableFlag(31190890)
    OR_2.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 31190800))
    OR_2.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 31190850))
    OR_2.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 31190605))
    AwaitConditionTrue(OR_2)
    Wait(1.0)
    Restart()


@RestartOnRest(31192849)
def Event_31192849():
    """Event 31192849"""
    Event_31192845(
        0,
        flag=31190800,
        entity=Assets.AEG099_001_9000,
        region=31192800,
        flag_1=31192805,
        character=31195800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=31190800,
        fog_asset=Assets.AEG099_001_9000,
        fog_region=31192800,
        host_entered_fog_flag=31192805,
        summon_entered_fog_flag=31192806,
        action_button_id=10000,
    )
    CommonFunc_9005813(0, flag=31190800, asset=Assets.AEG099_001_9000, model_point=3, right=0, model_point_1=3)
    CommonFunc_ControlBossMusic(0, 31190800, 921500, 31192805, 31192806, 0, 31192802, 0, 0)


@RestartOnRest(31192899)
def Event_31192899():
    """Event 31192899"""
    Event_31192845(
        1,
        flag=31190850,
        entity=Assets.AEG099_001_9002,
        region=31192850,
        flag_1=31192855,
        character=CharacterGroups.GarrisSnails,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=31190850,
        fog_asset=Assets.AEG099_001_9002,
        fog_region=31192850,
        host_entered_fog_flag=31192855,
        summon_entered_fog_flag=31192856,
        action_button_id=10000,
    )
    CommonFunc_9005813(0, flag=31190850, asset=Assets.AEG099_001_9002, model_point=3, right=0, model_point_1=3)
    CommonFunc_ControlBossMusic(0, 31190850, 920100, 31192855, 31192856, 0, 31192852, 0, 0)


@RestartOnRest(31192845)
def Event_31192845(
    _,
    flag: uint,
    entity: uint,
    region: uint,
    flag_1: uint,
    character: uint,
    action_button_id: int,
    left: uint,
    region_1: uint,
):
    """Event 31192845"""
    GotoIfFlagEnabled(Label.L10, flag=flag)
    WaitFrames(frames=1)
    GotoIfUnsignedEqual(Label.L0, left=left, right=0)
    GotoIfFlagEnabled(Label.L0, flag=left)
    if UnsignedNotEqual(left=region_1, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_1.Add(FlagEnabled(left))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(flag):
        return RESTART
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagDisabled(flag))
    AND_3.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    OR_3.Add(FlagEnabled(flag))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    GotoIfPlayerNotInOwnWorld(Label.L2)
    if FlagEnabled(flag):
        return RESTART
    SuppressSoundForFogGate(duration=5.0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=PLAYER, special_effect=4250)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    SkipLines(1)
    RotateToFaceEntity(PLAYER, region, animation=60060)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_5.Add(OR_4)
    AND_4.Add(OR_5)
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(FlagDisabled(flag))
    OR_6.Add(AND_4)
    OR_6.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_6)
    
    if FlagEnabled(flag):
        return RESTART
    RestartIfFinishedConditionTrue(input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(character)
    EnableNetworkFlag(flag_1)
    if PlayerNotInOwnWorld():
        return
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(PlayerInOwnWorld())
    AND_10.Add(FlagEnabled(flag))
    OR_10.Add(Invasion())
    OR_10.Add(InvasionPending())
    AND_10.Add(OR_10)
    AND_10.Add(ActionButtonParamActivated(action_button_id=10000, entity=entity))
    
    MAIN.Await(AND_10)
    
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    BanishPhantoms(unknown=0)
    BanishInvaders(unknown=0)
    Restart()
