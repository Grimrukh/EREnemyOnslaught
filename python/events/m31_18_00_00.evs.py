"""DONE
Perfumer's Grotto

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
from .entities.m31_18_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=311800, asset=Assets.AEG099_060_9000)
    Event_31182800()
    Event_31182801(0, boss=Characters.MirandaTheBlightedBloom)
    Event_31182801(1, boss=Characters.CLONE_MirandaTheBlightedBloom)
    Event_31182801(2, boss=Characters.Omenkiller)
    Event_31182801(3, boss=Characters.CLONE_Omenkiller)
    Event_31182810()
    Event_31182849()
    Event_31182811()
    KillBossClone(0, Characters.MirandaTheBlightedBloom, Characters.CLONE_MirandaTheBlightedBloom)
    KillBossClone(1, Characters.Omenkiller, Characters.CLONE_Omenkiller)
    CommonFunc_90005646(
        0,
        flag=31180800,
        left_flag=31182840,
        cancel_flag__right_flag=31182841,
        asset=Assets.AEG099_065_9000,
        player_start=31182840,
        area_id=31,
        block_id=18,
        cc_id=0,
        dd_id=0,
    )
    Event_31182500(0, asset=31181500, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(1, asset=31181501, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(2, asset=31181502, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(3, asset=31181503, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(4, asset=31181504, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(5, asset=31181505, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(6, asset=31181506, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(7, asset=31181507, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182500(8, asset=31181508, vfx_id=200, model_point=800023, model_point_1=402001)
    Event_31182515()
    CommonFunc_900005610(0, 31181200, 100, 800, 0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.DepravedPerfumer0,
        region=31182200,
        radius=2.0,
        seconds=3.4000000953674316,
        animation_id=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.DepravedPerfumer2,
        region=31182200,
        radius=2.0,
        seconds=3.0,
        animation_id=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.DepravedPerfumer3,
        animation_id=30000,
        animation_id_1=20000,
        region=31182203,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.DepravedPerfumer4,
        animation_id=30000,
        animation_id_1=20000,
        region=31182207,
        radius=2.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_31182200(0, character=Characters.DepravedPerfumer0, region=31182250)
    Event_31182200(1, character=Characters.DepravedPerfumer1, region=31182251)
    Event_31182200(2, character=Characters.DepravedPerfumer2, region=31182252)
    Event_31182200(3, character=Characters.DepravedPerfumer4, region=31182257)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=31180300, region=31182300, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.MirandaFlower0,
        region=31182306,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.MirandaFlower1,
        region=31182307,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=31180310,
        animation_id=30000,
        animation_id_1=20000,
        region=31182310,
        radius=0.0,
        seconds=9.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=31180311,
        animation_id=30000,
        animation_id_1=20000,
        region=31182310,
        radius=0.0,
        seconds=10.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.MirandaFlower2,
        region=31182314,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.MirandaFlower3,
        region=31182314,
        radius=10.0,
        seconds=0.5,
        animation_id=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.GiantMirandaFlower1,
        region=31182351,
        radius=2.0,
        seconds=0.0,
        animation_id=3001,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.GiantMirandaFlower2,
        region=31182355,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_31182402(
        0,
        character=Characters.MalformedStar,
        region=31182400,
        radius=3.0,
        seconds=0.0,
        animation_id=3012,
        region_1=32052401,
    )
    # Malformed Star clones despawn separately.
    CommonFunc_NonRespawningWithReward(0, dead_flag=31180400, character=Characters.MalformedStar, item_lot=0, reward_delay=0.0, skip_reward=0, clone=0)
    CommonFunc_NonRespawningWithReward(0, dead_flag=31180401, character=Characters.CLONE_MalformedStar, item_lot=0, reward_delay=0.0, skip_reward=0, clone=0)
    Event_31182400()


@RestartOnRest(31182500)
def Event_31182500(_, asset: uint, vfx_id: int, model_point: int, model_point_1: int):
    """Event 31182500"""
    CreateAssetVFX(asset, vfx_id=vfx_id, model_point=model_point)
    CreateAssetVFX(asset, vfx_id=vfx_id, model_point=model_point_1)


@RestartOnRest(31182515)
def Event_31182515():
    """Event 31182515"""
    CreateTemporaryVFX(vfx_id=802020, anchor_entity=31182515, anchor_type=CoordEntityType.Region)


@RestartOnRest(31182200)
def Event_31182200(_, character: uint, region: uint):
    """Event 31182200"""
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    AddSpecialEffect(character, 8082)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_2.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=6.0))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
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
    OR_5.Add(AND_1)
    OR_5.Add(AND_2)
    OR_5.Add(OR_3)
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_5.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    OR_5.Add(OR_2)
    
    MAIN.Await(OR_5)
    
    RemoveSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31182400)
def Event_31182400():
    """Event 31182400"""
    AND_1.Add(CharacterDead(Characters.MalformedStar))
    if AND_1:
        return
    ForceAnimation(Characters.MalformedStar, 0)


@RestartOnRest(31182401)
def Event_31182401():
    """Event 31182401"""
    if FlagEnabled(31180400):
        return
    OR_1.Add(CharacterDead(Characters.MalformedStar))
    EnableFlag(31180400)


@RestartOnRest(31182402)
def Event_31182402(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int, region_1: uint):
    """Event 31182402"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_15.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_15.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(OR_15)
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    OR_14.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    GotoIfConditionTrue(Label.L1, input_condition=OR_14)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(31182800)
def Event_31182800():
    """Event 31182800"""
    if FlagEnabled(31180800):
        return
    AND_1.Add(CharacterDead(Characters.MirandaTheBlightedBloom))
    AND_1.Add(CharacterDead(Characters.CLONE_MirandaTheBlightedBloom))
    AND_1.Add(CharacterDead(Characters.Omenkiller))
    AND_1.Add(CharacterDead(Characters.CLONE_Omenkiller))

    MAIN.Await(AND_1)
    
    KillBossAndDisplayBanner(character=Characters.MirandaTheBlightedBloom, banner_type=BannerType.EnemyFelled)
    EnableFlag(31180800)
    EnableFlag(9241)
    if PlayerInOwnWorld():
        EnableFlag(61241)


@RestartOnRest(31182801)
def Event_31182801(_, boss: uint):
    """Event 31182801"""
    if FlagEnabled(31180800):
        return
    
    MAIN.Await(HealthValue(boss) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(boss, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31182810)
def Event_31182810():
    """Event 31182810"""
    GotoIfFlagDisabled(Label.L0, flag=31180800)
    DisableCharacter(Characters.MirandaTheBlightedBloom)
    DisableCharacter(Characters.Omenkiller)
    DisableAnimations(Characters.MirandaTheBlightedBloom)
    DisableAnimations(Characters.Omenkiller)
    Kill(Characters.MirandaTheBlightedBloom)
    Kill(Characters.Omenkiller)
    DisableCharacter(Characters.CLONE_MirandaTheBlightedBloom)
    DisableCharacter(Characters.CLONE_Omenkiller)
    DisableAnimations(Characters.CLONE_MirandaTheBlightedBloom)
    DisableAnimations(Characters.CLONE_Omenkiller)
    Kill(Characters.CLONE_MirandaTheBlightedBloom)
    Kill(Characters.CLONE_Omenkiller)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.MirandaTheBlightedBloom)
    DisableAI(Characters.CLONE_MirandaTheBlightedBloom)
    DisableAI(Characters.Omenkiller)
    DisableAI(Characters.CLONE_Omenkiller)
    ForceAnimation(Characters.MirandaTheBlightedBloom, 30001)
    ForceAnimation(Characters.CLONE_MirandaTheBlightedBloom, 30001)
    AND_1.Add(FlagEnabled(31182805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31182800))
    
    MAIN.Await(AND_1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBossHealthBar(Characters.MirandaTheBlightedBloom, name=NameText.MirandaTheBlightedBloom)
    EnableBossHealthBar(Characters.Omenkiller, name=NameText.Omenkiller, bar_slot=1)
    EnableImmortality(Characters.CLONE_MirandaTheBlightedBloom)
    EnableImmortality(Characters.CLONE_Omenkiller)
    ReferDamageToEntity(Characters.CLONE_MirandaTheBlightedBloom, Characters.MirandaTheBlightedBloom)
    ReferDamageToEntity(Characters.CLONE_Omenkiller, Characters.Omenkiller)
    Wait(0.5)
    EnableAI(Characters.MirandaTheBlightedBloom)
    EnableAI(Characters.CLONE_MirandaTheBlightedBloom)
    EnableAnimations(Characters.MirandaTheBlightedBloom)
    EnableAnimations(Characters.CLONE_MirandaTheBlightedBloom)
    SetNetworkUpdateRate(Characters.MirandaTheBlightedBloom, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_MirandaTheBlightedBloom, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(Characters.MirandaTheBlightedBloom, 20001)
    ForceAnimation(Characters.CLONE_MirandaTheBlightedBloom, 20001)
    EnableAI(Characters.Omenkiller)
    EnableAI(Characters.CLONE_Omenkiller)
    EnableAnimations(Characters.Omenkiller)
    EnableAnimations(Characters.CLONE_Omenkiller)
    SetNetworkUpdateRate(Characters.Omenkiller, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_Omenkiller, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(31182811)
def Event_31182811():
    """Event 31182811"""
    if FlagEnabled(31180800):
        return
    OR_15.Add(CharacterDead(Characters.MirandaTheBlightedBloom))
    OR_15.Add(CharacterDead(Characters.Omenkiller))
    
    MAIN.Await(OR_15)
    
    EnableFlag(31182842)


@RestartOnRest(31182812)
def KillBossClone(_, original: uint, clone: uint):
    if FlagEnabled(31180800):
        return

    MAIN.Await(HealthValue(original) <= 0)
    Kill(clone)


@RestartOnRest(31182849)
def Event_31182849():
    """Event 31182849"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=31180800,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=31182800,
        host_entered_fog_flag=31182805,
        boss_characters=31185800,
        action_button_id=10000,
        first_time_done_flag=0,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=31180800,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=31182800,
        host_entered_fog_flag=31182805,
        summon_entered_fog_flag=31182806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=31180800, fog_asset=Assets.AEG099_002_9000, model_point=5, required_flag=0)
    CommonFunc_ControlBossMusic(0, 31180800, 920900, 31182805, 31182806, 0, 31182842, 0, 0)
