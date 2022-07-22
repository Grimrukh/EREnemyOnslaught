"""
Leyndell, Ashen Capital

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
from .entities.m11_05_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=11050002, asset=Assets.AEG099_060_9002, enemy_block_distance=8.0)
    RegisterGrace(grace_flag=11050003, asset=Assets.AEG099_060_9003, enemy_block_distance=8.0)
    RegisterGrace(grace_flag=11050004, asset=Assets.AEG099_060_9004, enemy_block_distance=8.0)
    RegisterGrace(grace_flag=11050005, asset=Assets.AEG099_060_9005, enemy_block_distance=8.0)
    CommonFunc_RegisterGraceIfFlagEnabled(
        0,
        flag=Flags.HoarahLouxDead,
        grace_flag=11050000,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=8.0,
    )
    CommonFunc_RegisterGraceIfFlagEnabled(
        0,
        flag=Flags.SirGideonOfnirDead,
        grace_flag=11050001,
        character=Characters.TalkDummy1,
        asset=Assets.AEG099_060_9001,
        enemy_block_distance=8.0,
    )
    
    # HOARAH LOUX
    HoarahLouxDies()
    GodfreyHoarahLouxBattleTrigger()
    # TODO: Changing one boss health bar might clear both. Will need a flag to track each name change in that case.
    HoarahLouxPhaseTwoTransition(
        0,
        godfrey=Characters.Godfrey,
        hoarah_loux=Characters.HoarahLoux,
        boss_name=NameText.HoarahLoux,
        bar_slot=1,
    )
    HoarahLouxPhaseTwoTransition(  # 11052812
        1,
        godfrey=Characters.CLONE_Godfrey,
        hoarah_loux=Characters.CLONE_HoarahLoux,
        boss_name=NameText.CLONE_HoarahLoux,
        bar_slot=0,
    )
    HoarahLouxCameraChange()
    GodfreyHoarahLouxCommonEvents()

    # SIR GIDEON OFNIR
    SirGideonOfnirDies()
    SirGideonOfnirBattleTrigger()
    SirGideonOfnirPhaseTwoTransition()
    SirGideonOfnirCommonEvents()
    
    # SHABRIRI SUMMON
    CommonFunc_90005780(
        0,
        flag=Flags.HoarahLouxDead,
        summon_flag=11052160,
        dismissal_flag=11052161,
        character=Characters.Shabriri,
        sign_type=20,
        region=11052160,
        right=11059350,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=Flags.HoarahLouxDead, flag_1=11052160, flag_2=11052161, character=Characters.Shabriri)
    CommonFunc_90005784(
        0,
        flag=11052160,
        flag_1=11052805,
        character=Characters.Shabriri,
        region=11052800,
        region_1=11052805,
        animation=0,
    )
    CommonFunc_90005780(
        0,
        flag=Flags.HoarahLouxDead,
        summon_flag=11052164,
        dismissal_flag=11052165,
        character=Characters.NepheliLoux,
        sign_type=20,
        region=11052164,
        right=10009719,
        unknown=1,
        right_1=0,
    )
    
    # NEPHELI LOUX SUMMON
    CommonFunc_90005781(
        0, flag=Flags.HoarahLouxDead, flag_1=11052164, flag_2=11052165, character=Characters.NepheliLoux
    )
    CommonFunc_90005784(
        0,
        flag=11052164,
        flag_1=11052805,
        character=Characters.NepheliLoux,
        region=11052800,
        region_1=11052805,
        animation=0,
    )
    
    CommonFunc_90005501(
        0,
        flag=11050525,
        flag_1=11051525,
        left=0,
        asset=Assets.AEG227_003_0500,
        asset_1=Assets.AEG227_051_0500,
        asset_2=Assets.AEG227_051_0501,
        flag_2=11050526,
    )
    CommonFunc_90005501(
        0,
        flag=11050530,
        flag_1=11051530,
        left=0,
        asset=Assets.AEG227_090_0500,
        asset_1=Assets.AEG227_052_0503,
        asset_2=Assets.AEG227_052_0502,
        flag_2=11050531,
    )
    CommonFunc_90005501(
        0,
        flag=11050535,
        flag_1=11051535,
        left=1,
        asset=Assets.AEG227_090_0501,
        asset_1=Assets.AEG227_052_0500,
        asset_2=Assets.AEG227_052_0501,
        flag_2=11050536,
    )
    CommonFunc_90005501(
        0,
        flag=11050610,
        flag_1=11051610,
        left=2,
        asset=Assets.AEG227_001_0500,
        asset_1=Assets.AEG227_050_0507,
        asset_2=Assets.AEG227_050_0508,
        flag_2=11050611,
    )
    Event_11052510()
    CommonFunc_90005511(
        0,
        flag=11050560,
        asset=Assets.AEG227_010_0500,
        obj_act_id=11053560,
        obj_act_id_1=227010,
        left=0,
    )
    CommonFunc_90005512(0, flag=11050560, region=11052560, region_1=11052561)
    Event_11052580()
    CommonFunc_90005520(
        0,
        flag=11050578,
        asset=Assets.AEG227_029_0500,
        start_climbing_flag=11052578,
        stop_climbing_flag=11052579,
    )
    Event_11052691()
    Event_11052692()
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=34,
        block_id=15,
        cc_id=0,
        dd_id=0,
        player_start=34152692,
        unk_8_12=11050000,
        flag=11052680,
        left_flag=11052681,
        cancel_flag__right_flag=11052682,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    ControlHoarahLouxTalkRange(
        0,
        character=Characters.Godfrey,
        character_1=Characters.HoarahLoux,
        flag=Flags.HoarahLouxDead,
        flag_1=11052805,
        distance=90.0,
    )
    Event_11053705(0, character=Characters.BrotherCorhyn)
    CommonFunc_90005704(0, attacked_entity=Characters.BrotherCorhyn, flag=4201, flag_1=4200, flag_2=1040529251, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.BrotherCorhyn,
        flag=4201,
        flag_1=4202,
        flag_2=1040529251,
        flag_3=4201,
        first_flag=4200,
        last_flag=4203,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.BrotherCorhyn, flag=4203, first_flag=4200, last_flag=4204)
    Event_11053706(0, character=Characters.Goldmask)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9000,
        action_button_id=6450,
        item_lot=4900,
        first_flag=9500,
        last_flag=9500,
        flag=11059206,
        model_point=806780,
    )
    Event_11053707()
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9000,
        action_button_id=4110,
        item_lot=105000,
        first_flag=400500,
        last_flag=400500,
        flag=11059305,
        model_point=0,
    )
    RunCommonEvent(
        11053708,
        slot=0,
        args=(11051740, 4110, 103700, 400370, 400370, 4208, 0, 4203),
        arg_types="IiiIIIiI",
    )
    CommonFunc_90005706(0, character=Characters.Commoner1, animation_id=930025, left=0)
    CommonFunc_90005706(0, character=Characters.Commoner0, animation_id=930010, left=0)
    Event_11053710(0, character=Characters.SirGideonOfnir)
    Event_11053720()
    CommonFunc_90005703(
        0,
        character=Characters.DemiHumanShaman,
        flag=3941,
        flag_1=3942,
        flag_2=1039409251,
        flag_3=3941,
        first_flag=3940,
        last_flag=3943,
        right=0,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.DemiHumanShaman,
        flag=3941,
        flag_1=3940,
        flag_2=1039409251,
        right=3,
    )
    CommonFunc_90005702(0, character=Characters.DemiHumanShaman, flag=3943, first_flag=3940, last_flag=3944)
    Event_11053730(0, character=Characters.DemiHumanShaman)
    Event_11053731(0, 11050730)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Goldmask)
    DisableBackread(Characters.BrotherCorhyn)
    DisableBackread(11050715)
    DisableBackread(Characters.Commoner0)
    DisableBackread(Characters.Commoner1)
    Event_11052500()
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Commoner2, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Commoner3, radius=3.5, seconds=0.0, animation_id=0)
    CommonFunc_90005221(
        0,
        character=Characters.Commoner4,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Commoner5,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Commoner6,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Commoner7,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.GiantMirandaFlower,
        region=11052240,
        radius=3.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.MirandaFlower0,
        region=11052240,
        radius=1.0,
        seconds=0.5,
        animation_id=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.MirandaFlower0,
        region=11052240,
        radius=1.0,
        seconds=0.20000000298023224,
        animation_id=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.UlceratedTreeSpirit0,
        animation_id=30002,
        animation_id_1=20002,
        region=11052300,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.UlceratedTreeSpirit1,
        animation_id=30002,
        animation_id_1=20002,
        region=11052301,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(0, 11050302, 30002, 20002, 11052302, 5.0, 0.0, 0, 0, 0, 0)


@ContinueOnRest(11052500)
def Event_11052500():
    """Event 11052500"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(11050500):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(9116))
    AND_1.Add(InsideMap(game_map=LEYNDELL_ASHEN_CAPITAL))
    
    MAIN.Await(AND_1)
    
    PlayCutscene(13000060, cutscene_flags=0, player_id=PLAYER)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(11050500)
    ForceAnimation(PLAYER, 0)
    Wait(1.0)
    DisplayAreaWelcomeMessage(text=11050)


@ContinueOnRest(11052510)
def Event_11052510():
    """Event 11052510"""
    CommonFunc_90005500(
        0,
        flag=11050525,
        flag_1=11051525,
        left=0,
        asset=Assets.AEG227_003_0500,
        asset_1=Assets.AEG227_051_0500,
        obj_act_id=11053526,
        asset_2=Assets.AEG227_051_0501,
        obj_act_id_1=11053527,
        region=11052526,
        region_1=11052527,
        flag_2=11050526,
        flag_3=11052527,
        left_1=0,
    )
    CommonFunc_90005505(
        0,
        flag=11050530,
        flag_1=11051530,
        left=0,
        asset=Assets.AEG227_090_0500,
        asset_1=Assets.AEG227_052_0503,
        obj_act_id=11053531,
        asset_2=Assets.AEG227_052_0502,
        obj_act_id_1=11053532,
        flag_2=11050531,
        flag_3=11052532,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        11050610,
        11051610,
        2,
        11051610,
        11051611,
        11053611,
        11051612,
        11053612,
        11052611,
        11052612,
        11050611,
        11052612,
        0,
    )


@RestartOnRest(11052580)
def Event_11052580():
    """Event 11052580"""
    RegisterLadder(start_climbing_flag=11050580, stop_climbing_flag=11050581, asset=11051580)
    RegisterLadder(start_climbing_flag=11050582, stop_climbing_flag=11050583, asset=11051582)
    RegisterLadder(start_climbing_flag=11050584, stop_climbing_flag=11050585, asset=11051584)
    RegisterLadder(start_climbing_flag=11050586, stop_climbing_flag=11050587, asset=11051586)
    RegisterLadder(start_climbing_flag=11050588, stop_climbing_flag=11050589, asset=11051588)
    RegisterLadder(start_climbing_flag=11050590, stop_climbing_flag=11050591, asset=11051590)
    RegisterLadder(start_climbing_flag=11050592, stop_climbing_flag=11050593, asset=Assets.AEG227_026_0500)
    RegisterLadder(start_climbing_flag=11050594, stop_climbing_flag=11050595, asset=11051594)
    RegisterLadder(start_climbing_flag=11050596, stop_climbing_flag=11050597, asset=11051596)


@RestartOnRest(11052691)
def Event_11052691():
    """Event 11052691"""
    EnableAssetInvulnerability(Assets.AEG228_098_1038)


@RestartOnRest(11052692)
def Event_11052692():
    """Event 11052692"""
    DisableAssetActivation(Assets.AEG227_090_0501, obj_act_id=-1)
    DisableAssetActivation(Assets.AEG227_052_0500, obj_act_id=-1)
    DisableAssetActivation(Assets.AEG227_052_0501, obj_act_id=-1)


@ContinueOnRest(11052800)
def HoarahLouxDies():
    """Event 11052800"""
    if FlagEnabled(Flags.HoarahLouxDead):
        return
    
    # Hoarah Loux is not immortal, so we can wait for both to die.
    AND_1.Await(HealthValue(Characters.HoarahLoux) <= 0)
    AND_1.Await(HealthValue(Characters.CLONE_HoarahLoux) <= 0)
    MAIN.Await(AND_1)
    
    Wait(4.0)
    PlaySoundEffect(11058000, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(Characters.HoarahLoux))
    AND_2.Add(CharacterDead(Characters.CLONE_HoarahLoux))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(Flags.HoarahLouxDead))
    
    MAIN.Await(OR_2)
    
    KillBossAndDisplayBanner(character=Characters.HoarahLoux, banner_type=BannerType.LegendFelled)
    EnableFlag(Flags.HoarahLouxDead)
    EnableNetworkFlag(Flags.HoarahLouxDead)
    EnableFlag(9107)
    if PlayerInOwnWorld():
        EnableFlag(61107)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    AND_9.Add(CharacterInsideRegion(character=PLAYER, region=11052840))
    
    MAIN.Await(AND_9)
    
    SuppressSoundEvent(sound_id=6, unk_4_8=0, suppression_active=False)


@RestartOnRest(11052810)
def GodfreyHoarahLouxBattleTrigger():
    """Event 11052810"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.HoarahLouxDead)
    DisableCharacter(CharacterGroups.GodfreyHoarahLouxBoss)
    DisableAnimations(CharacterGroups.GodfreyHoarahLouxBoss)
    Kill(CharacterGroups.GodfreyHoarahLouxBoss)
    DisableAsset(Assets.AEG228_076_3500)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(CharacterGroups.GodfreyHoarahLouxBoss)
    DisableGravity(Characters.HoarahLoux)
    DisableGravity(Characters.CLONE_HoarahLoux)
    DisableAnimations(Characters.HoarahLoux)
    DisableAnimations(Characters.CLONE_HoarahLoux)
    EnableImmortality(Characters.Godfrey)
    EnableImmortality(Characters.CLONE_Godfrey)
    DisableAnimations(Characters.Godfrey)
    DisableAnimations(Characters.CLONE_Godfrey)
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.Invader))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.Invader2))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.Invader3))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    if OR_15:
        return
    
    GotoIfFlagEnabled(Label.L1, flag=Flags.GodfreyHoarahLouxFirstTimeDone)
    DisableAnimations(Characters.Godfrey)
    DisableAnimations(Characters.CLONE_Godfrey)
    ForceAnimation(Characters.Godfrey, 30010)
    ForceAnimation(Characters.CLONE_Godfrey, 30010)
    AND_1.Add(FlagEnabled(11052805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=11052801))
    
    MAIN.Await(AND_1)
    
    BanishInvaders(unknown=0)
    WaitFrames(frames=1)
    EnableFlag(9021)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=11050010,
            cutscene_flags=0,
            move_to_region=11052811,
            map_id=11050000,
            player_id=PLAYER,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(11050010, cutscene_flags=0, player_id=PLAYER)
    WaitFramesAfterCutscene(frames=1)
    EnableNetworkFlag(Flags.GodfreyHoarahLouxFirstTimeDone)
    if PlayerNotInOwnWorld():
        SetBossMusic(bgm_boss_conv_param_id=472000, state=BossMusicState.Stop2)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=7.5, y_angle=-37.15999984741211)
    DisableAsset(Assets.AEG228_076_3500)

    EnableCharacter(Characters.Godfrey)
    EnableAnimations(Characters.Godfrey)
    Move(
        Characters.Godfrey,
        destination=RegionPoints.GodfreyPostCutscenePosition,  # TODO: Create
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.Godfrey,
    )
    ForceAnimation(Characters.Godfrey, 20020)
    
    EnableCharacter(Characters.CLONE_Godfrey)
    EnableAnimations(Characters.CLONE_Godfrey)
    Move(
        Characters.CLONE_Godfrey,
        destination=RegionPoints.CLONE_GodfreyPostCutscenePosition,  # TODO: Create
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.CLONE_Godfrey,
    )
    ForceAnimation(Characters.CLONE_Godfrey, 20020)

    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAsset(Assets.AEG228_076_3500)
    AND_2.Add(FlagEnabled(11052805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=11052800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAnimations(Characters.Godfrey)
    EnableAnimations(Characters.CLONE_Godfrey)
    EnableAI(Characters.Godfrey)
    EnableAI(Characters.CLONE_Godfrey)
    SetNetworkUpdateRate(Characters.Godfrey, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_Godfrey, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ReferDamageToEntity(Characters.Godfrey, target_entity=Characters.HoarahLoux)
    ReferDamageToEntity(Characters.CLONE_Godfrey, target_entity=Characters.CLONE_HoarahLoux)
    DisableHealthBar(Characters.Godfrey)
    DisableHealthBar(Characters.CLONE_Godfrey)
    EnableBossHealthBar(Characters.HoarahLoux, name=NameText.GodfreyFirstEldenLord, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_HoarahLoux, name=NameText.CLONE_GodfreyFirstEldenLord, bar_slot=0)


@RestartOnRest(11052811)
def HoarahLouxPhaseTwoTransition(_, godfrey: uint, hoarah_loux: uint, boss_name: int, bar_slot: short):
    """Event 11052811"""
    if FlagEnabled(Flags.HoarahLouxDead):
        return
    
    AND_1.Add(HealthValue(godfrey) <= 1)
    
    MAIN.Await(AND_1)
    
    DisableAnimations(godfrey)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=11050020,
            cutscene_flags=0,
            move_to_region=RegionPoints.PlayerPostHoarahLouxCutscenePosition,
            map_id=11050000,
            player_id=PLAYER,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(11050020, cutscene_flags=0, player_id=PLAYER)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(Flags.HoarahLouxInPhaseTwo)  # only used for music
    DisableCharacter(godfrey)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=8.09000015258789, y_angle=-37.15999984741211)
    EnableCharacter(hoarah_loux)
    WaitFrames(frames=1)
    EnableGravity(hoarah_loux)
    Move(
        hoarah_loux,
        destination=RegionPoints.HoarahLouxPostCutscenePosition,  # both can use this
        destination_type=CoordEntityType.Region,
        copy_draw_parent=hoarah_loux,
    )
    WaitFrames(frames=1)
    EnableAnimations(hoarah_loux)
    ForceAnimation(hoarah_loux, 20020)
    EnableAI(hoarah_loux)
    EnableBossHealthBar(hoarah_loux, name=boss_name, bar_slot=bar_slot)


@RestartOnRest(11052830)
def HoarahLouxCameraChange():
    """Event 11052830"""
    DisableNetworkSync()
    if FlagEnabled(Flags.HoarahLouxDead):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(11052805))
    AND_1.Add(FlagDisabled(Flags.HoarahLouxDead))
    AND_2.Add(PlayerNotInOwnWorld())
    AND_2.Add(FlagEnabled(11052806))
    AND_2.Add(FlagDisabled(Flags.HoarahLouxDead))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    ChangeCamera(normal_camera_id=4721, locked_camera_id=4721)
    OR_1.Add(CharacterHasSpecialEffect(Characters.HoarahLoux, 12298))
    OR_1.Add(CharacterHasSpecialEffect(Characters.CLONE_HoarahLoux, 12298))
    AND_4.Add(OR_1)
    AND_4.Add(FlagDisabled(Flags.HoarahLouxDead))
    
    MAIN.Await(AND_4)
    
    ChangeCamera(normal_camera_id=4725, locked_camera_id=4725)

    OR_1.Add(CharacterHasSpecialEffect(Characters.HoarahLoux, 12298))
    OR_1.Add(CharacterHasSpecialEffect(Characters.CLONE_HoarahLoux, 12298))
    AND_4.Add(OR_1)
    AND_4.Add(FlagDisabled(Flags.HoarahLouxDead))
    
    MAIN.Await(not AND_4)
    
    Restart()


@RestartOnRest(11052849)
def GodfreyHoarahLouxCommonEvents():
    """Event 11052849"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.HoarahLouxDead,
        fog_asset=Assets.AEG099_001_9001,
        fog_region=11052800,
        host_entered_fog_flag=11052805,
        boss_characters=CharacterGroups.GodfreyHoarahLouxBoss,
        action_button_id=10000,
        first_time_done_flag=0,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.HoarahLouxDead,
        fog_asset=Assets.AEG099_001_9001,
        fog_region=11052800,
        host_entered_fog_flag=11052805,
        summon_entered_fog_flag=11052806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.HoarahLouxDead, fog_asset=Assets.AEG099_001_9001, model_point=17, required_flag=0)
    CommonFunc_9005813(
        0, 
        flag=Flags.HoarahLouxDead, 
        asset=Assets.AEG099_001_9002, 
        model_point=18, 
        right=Flags.GodfreyHoarahLouxFirstTimeDone, 
        model_point_1=18,
    )
    CommonFunc_ControlBossMusic(
        0,
        Flags.HoarahLouxDead,
        472000, 
        11052805, 
        11052806, 
        Flags.GodfreyHoarahLouxFirstTimeDone, 
        Flags.HoarahLouxInPhaseTwo, 
        1, 
        1,
    )


@RestartOnRest(11052850)
def SirGideonOfnirDies():
    """Event 11052850"""
    if FlagEnabled(Flags.SirGideonOfnirDead):
        return
    
    AND_1.Add(HealthValue(Characters.SirGideonOfnir) <= 0)
    AND_1.Add(HealthValue(Characters.CLONE_SirGideonOfnir) <= 0)
    MAIN.Await(AND_1)
    
    Wait(4.0)
    PlaySoundEffect(11058050, 888880000, sound_type=SoundType.s_SFX)
    AddSpecialEffect(20000, 1899)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(Characters.SirGideonOfnir))
    AND_2.Add(CharacterDead(Characters.CLONE_SirGideonOfnir))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(Flags.SirGideonOfnirDead))
    
    MAIN.Await(OR_2)
    
    KillBossAndDisplayBanner(character=Characters.SirGideonOfnir, banner_type=BannerType.GreatEnemyFelled)
    SetBackreadStateAlternate(Characters.SirGideonOfnir, False)
    SetBackreadStateAlternate(Characters.CLONE_SirGideonOfnir, False)
    EnableNetworkFlag(Flags.SirGideonOfnirDead)
    EnableFlag(9106)
    if PlayerInOwnWorld():
        EnableFlag(61106)


@RestartOnRest(11052860)
def SirGideonOfnirBattleTrigger():
    """Event 11052860"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.SirGideonOfnirDead)
    DisableCharacter(CharacterGroups.SirGideonOfnirBoss)
    DisableAnimations(CharacterGroups.SirGideonOfnirBoss)
    Kill(CharacterGroups.SirGideonOfnirBoss)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(CharacterGroups.SirGideonOfnirVariants)
    DisableAnimations(CharacterGroups.SirGideonOfnirVariants)
    DisableAI(CharacterGroups.SirGideonOfnirBoss)
    SetBackreadStateAlternate(Characters.SirGideonOfnir, True)
    SetBackreadStateAlternate(Characters.CLONE_SirGideonOfnir, True)
    AND_8.Add(FlagEnabled(9120))
    AND_8.Add(FlagEnabled(9122))
    AND_8.Add(FlagEnabled(9112))
    GotoIfConditionTrue(Label.L8, input_condition=AND_8)
    AND_7.Add(FlagDisabled(9120))
    AND_7.Add(FlagEnabled(9122))
    AND_7.Add(FlagEnabled(9112))
    GotoIfConditionTrue(Label.L7, input_condition=AND_7)
    AND_6.Add(FlagEnabled(9120))
    AND_6.Add(FlagDisabled(9122))
    AND_6.Add(FlagEnabled(9112))
    GotoIfConditionTrue(Label.L6, input_condition=AND_6)
    AND_5.Add(FlagEnabled(9120))
    AND_5.Add(FlagEnabled(9122))
    AND_5.Add(FlagDisabled(9112))
    GotoIfConditionTrue(Label.L5, input_condition=AND_5)
    AND_4.Add(FlagDisabled(9120))
    AND_4.Add(FlagDisabled(9122))
    AND_4.Add(FlagEnabled(9112))
    GotoIfConditionTrue(Label.L4, input_condition=AND_4)
    AND_3.Add(FlagEnabled(9120))
    AND_3.Add(FlagDisabled(9122))
    AND_3.Add(FlagDisabled(9112))
    GotoIfConditionTrue(Label.L3, input_condition=AND_3)
    AND_2.Add(FlagDisabled(9120))
    AND_2.Add(FlagEnabled(9122))
    AND_2.Add(FlagDisabled(9112))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    Goto(Label.L1)

    # Choose a Gideon variant to copy player (CharaInit) data from, for spells, etc.

    # --- Label 2 --- #
    DefineLabel(2)
    CopyPlayerCharacterData(
        source_character=Characters.SirGideonOfnirVariant1,
        dest_characterentity=Characters.SirGideonOfnir,
    )
    CopyPlayerCharacterData(
        source_character=Characters.SirGideonOfnirVariant1,
        dest_characterentity=Characters.CLONE_SirGideonOfnir,
    )
    Goto(Label.L1)

    # --- Label 3 --- #
    DefineLabel(3)
    CopyPlayerCharacterData(
        source_character=Characters.SirGideonOfnirVariant2,
        dest_characterentity=Characters.SirGideonOfnir,
    )
    CopyPlayerCharacterData(
        source_character=Characters.SirGideonOfnirVariant2,
        dest_characterentity=Characters.CLONE_SirGideonOfnir,
    )
    Goto(Label.L1)

    # --- Label 4 --- #
    DefineLabel(4)
    CopyPlayerCharacterData(
        source_character=Characters.SirGideonOfnirVariant3,
        dest_characterentity=Characters.SirGideonOfnir,
    )
    CopyPlayerCharacterData(
        source_character=Characters.SirGideonOfnirVariant3,
        dest_characterentity=Characters.CLONE_SirGideonOfnir,
    )
    Goto(Label.L1)

    # --- Label 5 --- #
    DefineLabel(5)
    CopyPlayerCharacterData(
        source_character=Characters.SirGideonOfnirVariant4,
        dest_characterentity=Characters.SirGideonOfnir,
    )
    CopyPlayerCharacterData(
        source_character=Characters.SirGideonOfnirVariant4,
        dest_characterentity=Characters.CLONE_SirGideonOfnir,
    )
    Goto(Label.L1)

    # --- Label 6 --- #
    DefineLabel(6)
    CopyPlayerCharacterData(
        source_character=Characters.SirGideonOfnirVariant5,
        dest_characterentity=Characters.SirGideonOfnir,
    )
    CopyPlayerCharacterData(
        source_character=Characters.SirGideonOfnirVariant5,
        dest_characterentity=Characters.CLONE_SirGideonOfnir,
    )
    Goto(Label.L1)

    # --- Label 7 --- #
    DefineLabel(7)
    CopyPlayerCharacterData(
        source_character=Characters.SirGideonOfnirVariant6,
        dest_characterentity=Characters.SirGideonOfnir,
    )
    CopyPlayerCharacterData(
        source_character=Characters.SirGideonOfnirVariant6,
        dest_characterentity=Characters.CLONE_SirGideonOfnir,
    )
    Goto(Label.L1)

    # --- Label 8 --- #
    DefineLabel(8)
    CopyPlayerCharacterData(
        source_character=Characters.SirGideonOfnirVariant7,
        dest_characterentity=Characters.SirGideonOfnir,
    )
    CopyPlayerCharacterData(
        source_character=Characters.SirGideonOfnirVariant7,
        dest_characterentity=Characters.CLONE_SirGideonOfnir,
    )
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L1, flag=Flags.SirGideonOfnirFirstTimeDone)
    ForceAnimation(Characters.SirGideonOfnir, 90102, loop=True)
    ForceAnimation(Characters.CLONE_SirGideonOfnir, 90102, loop=True)
    if PlayerInOwnWorld():
        DisableFlag(11050854)
    AND_11.Add(PlayerInOwnWorld())
    AND_11.Add(CharacterHasSpecialEffect(Characters.SirGideonOfnir, 9770))  # not copying this trigger
    OR_11.Add(AND_11)
    OR_11.Add(AttackedWithDamageType(attacked_entity=Characters.SirGideonOfnir))
    OR_11.Add(AttackedWithDamageType(attacked_entity=Characters.CLONE_SirGideonOfnir))

    MAIN.Await(OR_11)
    
    EnableNetworkFlag(Flags.SirGideonOfnirFirstTimeDone)
    AddSpecialEffect(Characters.SirGideonOfnir, 9644)
    AddSpecialEffect(Characters.CLONE_SirGideonOfnir, 9644)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_12.Add(FlagEnabled(11052855))
    OR_12.Add(CharacterInsideRegion(character=PLAYER, region=11052850))
    OR_12.Add(CharacterInsideRegion(character=PLAYER, region=11052855))
    
    MAIN.Await(OR_12)
    
    MAIN.Await(AND_12)

    # --- Label 10 --- #
    DefineLabel(10)
    SetTeamType(Characters.SirGideonOfnir, TeamType.Enemy)
    SetTeamType(Characters.CLONE_SirGideonOfnir, TeamType.Enemy)
    EnableAI(Characters.SirGideonOfnir)
    EnableAI(Characters.CLONE_SirGideonOfnir)
    SetNetworkUpdateRate(CharacterGroups.SirGideonOfnirBoss, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.SirGideonOfnir, name=NameText.SirGideonOfnir, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_SirGideonOfnir, name=NameText.CLONE_SirGideonOfnir, bar_slot=0)


@RestartOnRest(11052861)
def SirGideonOfnirPhaseTwoTransition():
    """Waits for either Gideon to fall below 60% health."""
    if FlagEnabled(Flags.SirGideonOfnirDead):
        return
    OR_1.Add(HealthRatio(Characters.SirGideonOfnir) <= 0.6000000238418579)
    OR_1.Add(HealthRatio(Characters.CLONE_SirGideonOfnir) <= 0.6000000238418579)

    MAIN.Await(OR_1)
    
    EnableFlag(Flags.SirGideonOfnirInPhaseTwo)


@RestartOnRest(11052859)
def SirGideonOfnirCommonEvents():
    """Event 11052859"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.SirGideonOfnirDead,
        fog_asset=Assets.AEG099_001_9003,
        fog_region=11052850,
        host_entered_fog_flag=11052855,
        boss_characters=CharacterGroups.SirGideonOfnirBoss,
        action_button_id=10000,
        first_time_done_flag=Flags.SirGideonOfnirFirstTimeDone,
        first_time_trigger_region=0,
    )
    if FlagDisabled(Flags.SirGideonOfnirFirstTimeDone):
        CommonFunc_HostEntersBossFog(
            0,
            boss_dead_flag=Flags.SirGideonOfnirDead,
            fog_asset=Assets.AEG099_001_9004,
            fog_region=11052855,
            host_entered_fog_flag=11052855,
            boss_characters=CharacterGroups.SirGideonOfnirBoss,
            action_button_id=10000,
            first_time_done_flag=6000,
            first_time_trigger_region=0,
        )
    else:
        CommonFunc_HostEntersBossFog(
            0,
            boss_dead_flag=Flags.SirGideonOfnirDead,
            fog_asset=Assets.AEG099_001_9004,
            fog_region=11052855,
            host_entered_fog_flag=11052855,
            boss_characters=CharacterGroups.SirGideonOfnirBoss,
            action_button_id=10000,
            first_time_done_flag=Flags.SirGideonOfnirFirstTimeDone,
            first_time_trigger_region=0,
        )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.SirGideonOfnirDead,
        fog_asset=Assets.AEG099_001_9003,
        fog_region=11052850,
        host_entered_fog_flag=11052855,
        summon_entered_fog_flag=11052856,
        action_button_id=10000,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.SirGideonOfnirDead,
        fog_asset=Assets.AEG099_001_9004,
        fog_region=11052855,
        host_entered_fog_flag=11052855,
        summon_entered_fog_flag=11052856,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.SirGideonOfnirDead, fog_asset=Assets.AEG099_001_9003, model_point=5, required_flag=11050854)
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.SirGideonOfnirDead, fog_asset=Assets.AEG099_001_9004, model_point=4, required_flag=11050854)
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.SirGideonOfnirDead, fog_asset=Assets.AEG099_001_9005, model_point=4, required_flag=11050854)
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.SirGideonOfnirDead, fog_asset=Assets.AEG099_002_9000, model_point=8, required_flag=11050854)
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.SirGideonOfnirDead, fog_asset=Assets.AEG099_001_9006, model_point=4, required_flag=11050854)
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.SirGideonOfnirDead, fog_asset=Assets.AEG099_001_9007, model_point=5, required_flag=11050854)
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.SirGideonOfnirDead, fog_asset=Assets.AEG099_001_9008, model_point=5, required_flag=11050854)
    CommonFunc_ControlBossMusic(
        0,
        Flags.SirGideonOfnirDead,
        921100,
        11052855,
        11052856,
        0,
        Flags.SirGideonOfnirInPhaseTwo,
        0,
        0,
    )


@RestartOnRest(11053700)
def ControlHoarahLouxTalkRange(_, character: uint, character_1: uint, flag: uint, flag_1: uint, distance: float):
    """Event 11053700"""
    if PlayerNotInOwnWorld():
        return
    SetCharacterTalkRange(character=character, distance=17.0)
    if UnsignedNotEqual(left=0, right=character_1):
        SetCharacterTalkRange(character=character_1, distance=17.0)
    if FlagEnabled(flag):
        return
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetCharacterTalkRange(character=character, distance=distance)
    if UnsignedNotEqual(left=0, right=character_1):
        SetCharacterTalkRange(character=character_1, distance=distance)
    End()


@RestartOnRest(11053705)
def Event_11053705(_, character: uint):
    """Event 11053705"""
    WaitFrames(frames=1)
    DisableFlag(11059200)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(4210))
    GotoIfConditionFalse(Label.L20, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=4200)
    GotoIfFlagEnabled(Label.L2, flag=4201)
    GotoIfFlagEnabled(Label.L4, flag=4203)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90102)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagEnabled(11059200))
    
    Restart()


@RestartOnRest(11053706)
def Event_11053706(_, character: uint):
    """Event 11053706"""
    WaitFrames(frames=1)
    DisableFlag(11059200)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagDisabled(4203))
    OR_1.Add(FlagEnabled(4210))
    OR_1.Add(FlagEnabled(4211))
    AND_1.Add(OR_1)
    AND_2.Add(FlagEnabled(4203))
    AND_2.Add(FlagDisabled(4217))
    AND_2.Add(FlagEnabled(118))
    AND_2.Add(FlagEnabled(11009555))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    SkipLinesIfConditionTrue(5, OR_2)
    DisableNetworkFlag(1040549254)
    DisableNetworkFlag(11009554)
    DisableNetworkFlag(1051569454)
    DisableNetworkFlag(11059304)
    Goto(Label.L20)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.NoTeam)
    ForceAnimation(character, 930002)
    DisableNetworkFlag(1040549254)
    DisableNetworkFlag(11009554)
    DisableNetworkFlag(1051569454)
    EnableNetworkFlag(11059304)
    EnableNetworkFlag(11059206)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagEnabled(11059200))
    
    Restart()


@RestartOnRest(11053707)
def Event_11053707():
    """Event 11053707"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400500):
        return
    if FlagDisabled(9500):
        return
    EnableNetworkFlag(11059305)
    End()


@ContinueOnRest(11053708)
def Event_11053708(
    _,
    asset: uint,
    action_button_id: int,
    item_lot: int,
    first_flag: uint,
    last_flag: uint,
    flag: uint,
    model_point: int,
    flag_1: uint,
):
    """Event 11053708"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagRangeAnyDisabled(flag_range=(first_flag, last_flag)))
    
    MAIN.Await(AND_1)
    
    if ValueNotEqual(left=model_point, right=0):
        CreateAssetVFX(asset, vfx_id=90, model_point=model_point)
    else:
        CreateAssetVFX(asset, vfx_id=90, model_point=6101)
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(FlagRangeAllEnabled(flag_range=(first_flag, last_flag)))
    OR_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=asset))
    OR_1.Add(OR_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    DeleteAssetVFX(asset)
    AwardItemLot(item_lot, host_only=True)
    EzstateAIRequest(PLAYER, command_id=60070, command_slot=0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(asset)
    Restart()


@RestartOnRest(11053710)
def Event_11053710(_, character: uint):
    """Event 11053710"""
    if PlayerInOwnWorld():
        SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.Off)
    
    MAIN.Await(ThisEventSlotFlagEnabled())
    
    GotoIfPlayerNotInOwnWorld(Label.L0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    EnableNetworkFlag(11050854)

    # --- Label 0 --- #
    DefineLabel(0)
    SetTeamType(character, TeamType.Enemy)


@RestartOnRest(11053720)
def Event_11053720():
    """Event 11053720"""
    DisableFlag(11059350)
    WaitFrames(frames=1)
    if FlagDisabled(3631):
        return
    if FlagEnabled(Flags.HoarahLouxDead):
        return
    if FlagDisabled(35000500):
        return
    if FlagEnabled(3621):
        return
    if FlagEnabled(1049539212):
        return
    if FlagEnabled(116):
        return
    EnableFlag(11059350)
    End()


@RestartOnRest(11053730)
def Event_11053730(_, character: uint):
    """Event 11053730"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    if FlagEnabled(3940):
        DisableFlag(1043379353)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L5, flag=3947)
    
    MAIN.Await(FlagEnabled(3947))
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3940)
    GotoIfFlagEnabled(Label.L2, flag=3941)
    GotoIfFlagEnabled(Label.L3, flag=3942)
    GotoIfFlagEnabled(Label.L4, flag=3943)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(4, 3957)
    SkipLinesIfFlagEnabled(3, 11109819)
    AND_6.Add(FlagEnabled(71122))
    AND_6.Add(FlagEnabled(9000))
    AwaitConditionTrue(AND_6)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010)
    EnableNetworkFlag(11109819)
    EnableNetworkFlag(3957)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3947))
    
    Restart()


@RestartOnRest(11053731)
def Event_11053731(_, entity: uint):
    """Event 11053731"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(3943))
    OR_1.Add(FlagDisabled(3947))
    OR_1.Add(FlagEnabled(1039409259))
    if OR_1:
        return
    AND_1.Add(EntityWithinDistance(entity=entity, other_entity=20000, radius=4.0))
    AND_1.Add(CharacterHasSpecialEffect(20000, 9690))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1039402710)
    End()
