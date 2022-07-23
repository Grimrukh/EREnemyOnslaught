"""
Astel Arena

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
from .entities.m12_04_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_RegisterGraceIfFlagEnabled(
        0,
        flag=Flags.AstelDead,
        grace_flag=71240,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    Event_12042680()
    Event_12042400()
    AstelCommonEvents()
    AstelDies()
    AstelBattleTrigger()


@ContinueOnRest(12042400)
def Event_12042400():
    """Event 12042400"""
    GotoIfFlagDisabled(Label.L0, flag=114)
    DisableAsset(Assets.AEG099_002_9002)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerNotInOwnWorld():
        Goto(Label.L10)
    if ThisEventSlotFlagDisabled():
        DeleteVFX(12041400)
        CreateAssetVFX(Assets.AEG099_002_9002, vfx_id=101, model_point=1507)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9506, entity=Assets.AEG099_002_9002))
    AND_2.Add(FlagEnabled(114))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFlagEnabled(Label.L1, flag=114)
    if PlayerInOwnWorld():
        DisplayDialog(text=20006, anchor_entity=0, display_distance=5.0)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DeleteVFX(12041400)
    DisableAsset(Assets.AEG099_002_9002)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DeleteVFX(12041400)
    CreateAssetVFX(Assets.AEG099_002_9002, vfx_id=101, model_point=1507)
    OR_9.Add(FlagEnabled(114))
    
    MAIN.Await(OR_9)
    
    DeleteVFX(12041400)
    DisableAsset(Assets.AEG099_002_9002)
    End()


@RestartOnRest(12042680)
def Event_12042680():
    """Event 12042680"""
    DisableNetworkSync()
    if ThisEventSlotFlagDisabled():
        DeleteVFX(12043680, erase_root_only=False)
    AND_1.Add(OutsideMap(game_map=ASTEL_ARENA))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12042680))
    OR_1.Add(AND_1)
    AND_2.Add(InsideMap(game_map=ASTEL_ARENA))
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=1034412680))
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    CreateVFX(12043680)
    Wait(1.0)
    AND_10.Add(InsideMap(game_map=ASTEL_ARENA))
    AND_10.Add(CharacterInsideRegion(character=PLAYER, region=1034412680))
    OR_10.Add(AND_10)
    AND_11.Add(OutsideMap(game_map=ASTEL_ARENA))
    AND_11.Add(CharacterOutsideRegion(character=PLAYER, region=12042680))
    OR_10.Add(AND_11)
    
    MAIN.Await(OR_10)
    
    DeleteVFX(12043680)
    Wait(1.0)
    Restart()


@ContinueOnRest(12042800)
def AstelDies():
    """Event 12042800"""
    if FlagEnabled(Flags.AstelDead):
        return

    AND_1.Add(HealthRatio(Characters.Astel) <= 0.0)
    AND_1.Add(HealthRatio(Characters.CLONE_Astel) <= 0.0)
    MAIN.Await(AND_1)

    Wait(5.0)
    PlaySoundEffect(Characters.Astel, 77777777, sound_type=SoundType.s_SFX)

    AND_2.Add(CharacterDead(Characters.Astel))
    AND_2.Add(CharacterDead(Characters.CLONE_Astel))
    MAIN.Await(AND_2)
    
    KillBossAndDisplayBanner(character=Characters.Astel, banner_type=BannerType.LegendFelled)
    EnableFlag(Flags.AstelDead)
    EnableFlag(9108)
    if PlayerInOwnWorld():
        EnableFlag(61108)


@RestartOnRest(12042810)
def AstelBattleTrigger():
    """Event 12042810"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.AstelDead)
    DisableCharacter(Characters.Astel)
    DisableAnimations(Characters.Astel)
    Kill(Characters.Astel)
    DisableCharacter(Characters.CLONE_Astel)
    DisableAnimations(Characters.CLONE_Astel)
    Kill(Characters.CLONE_Astel)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Astel)
    DisableAI(Characters.CLONE_Astel)
    EnableNavmeshType(navmesh_id=12044300, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=12044301, navmesh_type=NavmeshType.Solid)
    AND_2.Add(FlagEnabled(12042805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=12042800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.Astel)
    EnableAI(Characters.CLONE_Astel)
    SetNetworkUpdateRate(Characters.Astel, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_Astel, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Astel, name=NameText.Astel, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_Astel, name=NameText.CLONE_Astel, bar_slot=0)
    SetCharacterEventTarget(Characters.Astel, region=12040810)
    SetCharacterEventTarget(Characters.CLONE_Astel, region=12040810)


@ContinueOnRest(12042849)
def AstelCommonEvents():
    """Event 12042849"""
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.AstelDead, fog_asset=Assets.AEG099_002_9001, model_point=8, required_flag=0)
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.AstelDead,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=12042800,
        host_entered_fog_flag=12042805,
        boss_characters=12045800,
        action_button_id=10000,
        first_time_done_flag=0,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.AstelDead,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=12042800,
        host_entered_fog_flag=12042805,
        summon_entered_fog_flag=12042806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.AstelDead, fog_asset=Assets.AEG099_002_9000, model_point=8, required_flag=0)
    CommonFunc_ControlBossMusic(0, Flags.AstelDead, 920700, 12042805, 12042806, 0, 12042802, 0, 0)
