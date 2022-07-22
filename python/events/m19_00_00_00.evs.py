"""
Stone Platform

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
from .entities.common_entities import CommonFlags
from .entities.m19_00_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_RegisterGraceIfFlagEnabled(
        0,
        flag=Flags.EldenBeastDead,
        grace_flag=19000000,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=8.0,
    )
    PlayEldenLordEndingCutscene()
    PlayAgeOfStarsEndingCutscene()
    PlayFrenziedFlameEndingCutscene()
    TravelToStonePlatform()
    Event_19002502()
    EldenBeastDies()
    RadagonBattleTrigger()
    RadagonDies()
    EldenBeastBattleTrigger()
    EldenBeastCameraChange()
    EldenBeastCommonEvents()
    Event_19002900()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_19000050()


@ContinueOnRest(19000100)
def PlayEldenLordEndingCutscene():
    """Play ending cutscene for one of the four Age of Fracture variants.

    Does NOT include Frenzied Flame ending or Age of the Stars (Ranni) ending.
    """
    GotoIfPlayerInOwnWorld(Label.L0)
    DisableAsset(Assets.AEG227_018_1000)
    DisableAsset(Assets.AEG227_017_1000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(CommonFlags.EndingDone):
        return

    # If an Elden Lord ending was already chosen, play that cutscene immediately.
    OR_15.Add(FlagEnabled(9400))  # not sure where these "cutscene request" flags are enabled
    OR_15.Add(FlagEnabled(9401))
    OR_15.Add(FlagEnabled(9402))
    OR_15.Add(FlagEnabled(9403))
    GotoIfConditionTrue(Label.L15, input_condition=OR_15)

    DisableAsset(Assets.AEG227_018_1000)
    DisableAsset(Assets.AEG227_017_1000)
    AND_1.Add(FlagEnabled(Flags.EndingCanBeChosen))
    
    MAIN.Await(AND_1)
    
    EnableAsset(Assets.AEG227_018_1000)
    EnableAsset(Assets.AEG227_017_1000)
    DisableCharacter(Characters.Radagon)
    DisableAnimations(Characters.Radagon)
    DisableCharacter(Characters.CLONE_Radagon)
    DisableAnimations(Characters.CLONE_Radagon)
    DisableAsset(Assets.AEG301_240_1000)
    AND_2.Add(FlagDisabled(CommonFlags.FrenziedFlameEndingForced))
    OR_4.Add(AND_2)
    AND_3.Add(FlagEnabled(CommonFlags.FrenziedFlameEndingForced))
    AND_3.Add(FlagEnabled(CommonFlags.MiquellasNeedleUsed))
    OR_4.Add(AND_3)
    AND_5.Add(OR_4)
    OR_5.Add(FlagEnabled(9400))
    OR_5.Add(FlagEnabled(9401))
    OR_5.Add(FlagEnabled(9402))
    OR_5.Add(FlagEnabled(9403))
    AND_5.Add(OR_5)

    # One of 9400-9403 enabled AND (Frenzied Flame ending not forced OR Frenzied Flame reversed with Miquella's Needle)
    MAIN.Await(AND_5)
    
    AND_10.Add(PlayerGender(gender=Gender.Female))
    AND_10.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 361000))
    AND_11.Add(PlayerGender(gender=Gender.Male))
    AND_11.Add(CharacterHasSpecialEffect(PLAYER, 361000))
    OR_10.Add(AND_10)
    OR_10.Add(AND_11)
    SkipLinesIfConditionTrue(3, OR_10)
    DisableFlag(780020)
    EnableFlag(780021)
    SkipLines(2)
    EnableFlag(780020)
    DisableFlag(780021)

    # --- Label 15 --- #
    DefineLabel(15)
    EnableFlag(Flags.EldenLordEndingChosen)  # purpose unclear
    EnableFlag(19002100)  # purpose unclear
    GotoIfFlagEnabled(Label.L13, flag=9403)
    GotoIfFlagEnabled(Label.L12, flag=9402)
    GotoIfFlagEnabled(Label.L11, flag=9401)
    PlayCutsceneToPlayerAndWarpWithStablePositionUpdate(
        cutscene_id=19000010,
        cutscene_flags=CutsceneFlags.IsEndingCutscene,
        move_to_region=11712500,
        map_id=11710000,
        player_id=PLAYER,
        unk_16_20=19000,
        unk_20_21=False,
        update_stable_position=False,
    )
    TriggerMultiplayerEvent(event_id=10)
    WaitFramesAfterCutscene(frames=1)
    Goto(Label.L15)

    # --- Label 11 --- #
    DefineLabel(11)
    PlayCutsceneToPlayerAndWarpWithStablePositionUpdate(
        cutscene_id=19000060,
        cutscene_flags=CutsceneFlags.IsEndingCutscene,
        move_to_region=11712500,
        map_id=11710000,
        player_id=PLAYER,
        unk_16_20=19000,
        unk_20_21=False,
        update_stable_position=False,
    )
    TriggerMultiplayerEvent(event_id=20)
    WaitFramesAfterCutscene(frames=1)
    Goto(Label.L15)

    # --- Label 12 --- #
    DefineLabel(12)
    PlayCutsceneToPlayerAndWarpWithStablePositionUpdate(
        cutscene_id=19000070,
        cutscene_flags=CutsceneFlags.IsEndingCutscene,
        move_to_region=11712500,
        map_id=11710000,
        player_id=PLAYER,
        unk_16_20=19000,
        unk_20_21=False,
        update_stable_position=False,
    )
    TriggerMultiplayerEvent(event_id=30)
    WaitFramesAfterCutscene(frames=1)
    Goto(Label.L15)

    # --- Label 13 --- #
    DefineLabel(13)
    PlayCutsceneToPlayerAndWarpWithStablePositionUpdate(
        cutscene_id=19000080,
        cutscene_flags=CutsceneFlags.IsEndingCutscene,
        move_to_region=11712500,
        map_id=11710000,
        player_id=PLAYER,
        unk_16_20=19000,
        unk_20_21=False,
        update_stable_position=False,
    )
    TriggerMultiplayerEvent(event_id=40)
    WaitFramesAfterCutscene(frames=1)
    Goto(Label.L15)

    # --- Label 15 --- #
    DefineLabel(15)


@ContinueOnRest(19000110)
def PlayAgeOfStarsEndingCutscene():
    """Event 19000110"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(CommonFlags.EndingDone):
        return

    # If cutscene already requested (but not complete), go straight to it.
    OR_15.Add(FlagEnabled(9404))
    OR_15.Add(FlagEnabled(9405))
    GotoIfConditionTrue(Label.L15, input_condition=OR_15)

    AND_3.Add(FlagEnabled(Flags.EndingCanBeChosen))
    AND_3.Add(FlagEnabled(Flags.RanniEndingAvailable))
    AND_1.Add(FlagDisabled(CommonFlags.FrenziedFlameEndingForced))
    OR_3.Add(AND_1)
    AND_2.Add(FlagEnabled(CommonFlags.FrenziedFlameEndingForced))
    AND_2.Add(FlagEnabled(CommonFlags.MiquellasNeedleUsed))
    OR_3.Add(AND_2)
    AND_3.Add(OR_3)

    # Ending can be chosen AND Ranni ending available AND (Frenzied Flame not used OR Frenzied Flame undone)
    MAIN.Await(AND_3)

    # Show Ranni summon sign and wait for interaction.
    CreateAssetVFX(Assets.AEG099_090_9001, vfx_id=100, model_point=30070)
    AND_4.Add(ActionButtonParamActivated(action_button_id=9610, entity=Assets.AEG099_090_9001))
    AND_4.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_4)

    # --- Label 15 --- #
    DefineLabel(15)
    # TODO: Investigate this cutscene variant (19000020 with flag vs 19000021 without)
    if FlagDisabled(1034509407):  # unknown flag from Ranni's Rise
        PlayCutscene(19000020, cutscene_flags=0, player_id=PLAYER)
        EnableFlag(9404)
        TriggerMultiplayerEvent(event_id=50)
    else:
        PlayCutscene(19000021, cutscene_flags=0, player_id=PLAYER)
        EnableFlag(9405)
        TriggerMultiplayerEvent(event_id=60)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(CommonFlags.EndingDone)
    EnableFlag(6010)
    AwardAchievement(achievement_id=2)
    SetRespawnPoint(respawn_point=11102020)
    SaveRequest()
    EnableFlag(21)  # credits


@ContinueOnRest(19000120)
def PlayFrenziedFlameEndingCutscene():
    """Event 19000120"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(CommonFlags.EndingDone):
        return
    OR_15.Add(FlagEnabled(9406))
    OR_15.Add(FlagEnabled(9407))
    GotoIfConditionTrue(Label.L15, input_condition=OR_15)
    AND_1.Add(FlagEnabled(19001100))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    AND_1.Add(FlagEnabled(CommonFlags.FrenziedFlameEndingForced))
    AND_1.Add(FlagDisabled(CommonFlags.MiquellasNeedleUsed))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9620, entity=Assets.AEG099_090_9002))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 67070)
    Wait(10.0)

    # --- Label 15 --- #
    DefineLabel(15)
    if FlagDisabled(109):  # unknown variant (flag enabled in Shunning-Grounds)
        PlayCutscene(19000030, cutscene_flags=0, player_id=PLAYER)
        EnableFlag(9406)
        TriggerMultiplayerEvent(event_id=70)
    else:
        PlayCutscene(19000031, cutscene_flags=0, player_id=PLAYER)
        EnableFlag(9407)
        TriggerMultiplayerEvent(event_id=80)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(CommonFlags.EndingDone)
    EnableFlag(6010)
    AwardAchievement(achievement_id=3)
    SetRespawnPoint(respawn_point=11102020)
    SaveRequest()
    EnableFlag(22)


@ContinueOnRest(19000050)
def Event_19000050():
    """Event 19000050"""
    if ThisEventSlotFlagEnabled():
        return


@ContinueOnRest(19002500)
def TravelToStonePlatform():
    """Event 19002500"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.EldenBeastDead)
    CreateAssetVFX(Assets.AEG099_003_9000, vfx_id=101, model_point=1530)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerInOwnWorld(Label.L1)
    GotoIfFlagDisabled(Label.L1, flag=Flags.RadagonBattleStarted)
    # Summon arrives in Stone Platform.
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=20000,
        destination_type=CoordEntityType.Region,
        destination=19002811,
        model_point=-1,
        copy_draw_parent=20000,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    CreateAssetVFX(Assets.AEG099_003_9000, vfx_id=101, model_point=1530)
    if PlayerNotInOwnWorld():
        GotoIfFlagEnabled(Label.L2, flag=Flags.StonePlatformEntered)

    # Host activates Erdtree fog.
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(Flags.EldenBeastDead))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9501, entity=Assets.AEG099_003_9000))
    
    MAIN.Await(AND_1)
    
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    OR_9.Add(CharacterInvadeType(character=20000, invade_type=2))
    OR_9.Add(CharacterInvadeType(character=20000, invade_type=3))
    OR_9.Add(CharacterInvadeType(character=20000, invade_type=4))
    OR_9.Add(CharacterInvadeType(character=20000, invade_type=5))
    OR_9.Add(CharacterInvadeType(character=20000, invade_type=7))
    if OR_9:
        return

    ForceAnimation(PLAYER, 67080)
    if PlayerNotInOwnWorld():
        GotoIfFlagEnabled(Label.L2, flag=Flags.StonePlatformEntered)
    Wait(2.4000000953674316)
    CreateAssetVFX(Assets.AEG099_003_9001, vfx_id=101, model_point=1531)
    if PlayerNotInOwnWorld():
        GotoIfFlagEnabled(Label.L2, flag=Flags.StonePlatformEntered)
    Wait(3.5999999046325684)
    EnableNetworkFlag(Flags.StonePlatformEntered)

    # --- Label 2 --- #
    DefineLabel(2)
    # Player arrives in Stone Platform.

    if FlagEnabled(Flags.RadagonDead):
        # Radagon already dead. Elden Beast transition cutscene will trigger instead.
        return

    EnableFlag(9021)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=19000040,
            cutscene_flags=CutsceneFlags.Unknown32,
            move_to_region=19002810,
            map_id=19000000,
            player_id=PLAYER,
            unk_20_24=19000,
            unk_24_25=False,
        )
    else:
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=19000040,
            cutscene_flags=CutsceneFlags.Unknown32,
            move_to_region=19002811,
            map_id=19000000,
            player_id=PLAYER,
            unk_20_24=19000,
            unk_24_25=False,
        )
    WaitFramesAfterCutscene(frames=1)
    if FlagDisabled(CommonFlags.RadagonChallenged):
        EnableFlag(CommonFlags.RadagonChallenged)
    DeleteAssetVFX(Assets.AEG099_003_9001, erase_root=False)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=13.0600004196167, y_angle=-63.06999969482422)


@RestartOnRest(19002502)
def Event_19002502():
    """Event 19002502"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(71900):
        return
    if FlagEnabled(121):
        return
    AND_1.Add(InsideMap(game_map=STONE_PLATFORM))
    AND_1.Add(FlagEnabled(9123))
    AND_1.Add(FlagDisabled(71900))
    AND_1.Add(FlagDisabled(121))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    AND_2.Add(FlagEnabled(71900))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(PLAYER, 4281)
    AddSpecialEffect(PLAYER, 4283)


@RestartOnRest(19002800)
def EldenBeastDies():
    """Event 19002800"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=19002815))
    AND_1.Add(FlagEnabled(19000804))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    if FlagEnabled(19000804):
        return
    GotoIfFlagEnabled(Label.L0, flag=Flags.EldenBeastDead)

    AND_3.Add(HealthValue(Characters.EldenBeast) <= 0)
    AND_3.Add(HealthValue(Characters.CLONE_EldenBeast) <= 0)
    MAIN.Await(AND_3)
    
    Wait(4.0)
    PlaySoundEffect(19008000, 888880000, sound_type=SoundType.s_SFX)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)

    AND_4.Add(CharacterDead(Characters.EldenBeast))
    AND_4.Add(CharacterDead(Characters.CLONE_EldenBeast))
    MAIN.Await(AND_4)
    
    Wait(4.5)
    KillBossAndDisplayBanner(character=Characters.EldenBeast, banner_type=BannerType.GodSlain)
    EnableFlag(Flags.EldenBeastDead)
    EnableFlag(Flags.EndingCanBeChosen)
    EnableFlag(9123)
    if PlayerNotInOwnWorld():
        return
    EnableFlag(61123)
    SetRespawnPoint(respawn_point=19002814)
    SaveRequest()
    Wait(7.5)
    AND_2.Add(HealthRatio(PLAYER) == 0.0)
    if AND_2:
        return

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(9021)
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=19000050,
        cutscene_flags=0,
        move_to_region=19002814,
        map_id=19000000,
        player_id=PLAYER,
        unk_20_24=19000,
        unk_24_25=False,
    )
    WaitFramesAfterCutscene(frames=1)
    SetCameraAngle(x_angle=20.899999618530273, y_angle=-51.560001373291016)
    SetPlayerPositionDisplay(
        state=True,
        aboveground=True,
        game_map=STONE_PLATFORM,
        x=181.10000610351562,
        y=102.3499984741211,
        z=-607.0599975585938,
    )
    SetRespawnPoint(respawn_point=19002814)
    SaveRequest()
    EnableFlag(19000804)
    SetBackreadStateAlternate(35000, False)
    SetNetworkUpdateRate(35000, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryFiveFrames)


@RestartOnRest(19002810)
def RadagonBattleTrigger():
    """Now treated as a separate fight from Elden Beast."""
    GotoIfFlagDisabled(Label.L0, flag=Flags.RadagonDead)
    DisableCharacter(Characters.Radagon)
    DisableAnimations(Characters.Radagon)
    Kill(Characters.Radagon)
    DisableCharacter(Characters.CLONE_Radagon)
    DisableAnimations(Characters.CLONE_Radagon)
    Kill(Characters.CLONE_Radagon)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Radagon)
    DisableCharacter(Characters.Radagon)
    DisableAnimations(Characters.Radagon)
    SetCharacterFadeOnEnable(character=Characters.Radagon, state=False)
    DisableAI(Characters.CLONE_Radagon)
    DisableCharacter(Characters.CLONE_Radagon)
    DisableAnimations(Characters.CLONE_Radagon)
    SetCharacterFadeOnEnable(character=Characters.CLONE_Radagon, state=False)
    DisableAsset(Assets.AEG301_240_1000)

    # Battle starts when host gets close to either Radagon.
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.Radagon, radius=20.0))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.CLONE_Radagon, radius=20.0))
    AND_1.Add(OR_1)
    MAIN.Await(AND_1)
    
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=14.600000381469727, y_angle=-72.33000183105469)
    EnableNetworkFlag(Flags.RadagonFirstTimeDone)  # was unused
    EnableNetworkFlag(Flags.RadagonBattleStarted)
    EnableNetworkFlag(19002806)
    DisableAsset(Assets.AEG301_240_1000)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(Characters.Radagon)
    EnableAnimations(Characters.Radagon)
    ForceAnimation(Characters.Radagon, 20010)
    EnableAI(Characters.Radagon)
    SetNetworkUpdateRate(Characters.Radagon, is_fixed=True, update_rate=CharacterUpdateRate.Always)

    EnableCharacter(Characters.CLONE_Radagon)
    EnableAnimations(Characters.CLONE_Radagon)
    ForceAnimation(Characters.CLONE_Radagon, 20010)
    EnableAI(Characters.CLONE_Radagon)
    SetNetworkUpdateRate(Characters.CLONE_Radagon, is_fixed=True, update_rate=CharacterUpdateRate.Always)

    EnableBossHealthBar(Characters.Radagon, name=NameText.RadagonOfTheGoldenOrder, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_Radagon, name=NameText.CLONE_RadagonOfTheGoldenOrder, bar_slot=0)


@RestartOnRest(19002811)
def RadagonDies():
    """Event 19002811"""
    if FlagEnabled(Flags.RadagonDead):
        return
    AND_1.Add(CharacterDead(Characters.Radagon))
    AND_1.Add(CharacterDead(Characters.CLONE_Radagon))

    MAIN.Await(AND_1)
    
    Wait(3.0)
    # TODO: Elden Beast music should start straightaway if Radagon is already dead (no transition event).
    EnableFlag(Flags.RadagonDead)  # will trigger Elden Beast fight immediately


@RestartOnRest(19002812)
def EldenBeastBattleTrigger():
    """Event 19002812"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.EldenBeastDead)
    DisableCharacter(Characters.EldenBeast)
    DisableAnimations(Characters.EldenBeast)
    Kill(Characters.EldenBeast)
    DisableCharacter(Characters.CLONE_EldenBeast)
    DisableAnimations(Characters.CLONE_EldenBeast)
    Kill(Characters.CLONE_EldenBeast)
    DisableCharacter(Characters.Unknown)  # TODO: ?
    DisableAnimations(Characters.Unknown)
    DisableAsset(Assets.AEG301_240_1000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfThisEventSlotFlagEnabled(Label.L1)  # fight already started

    DisableAI(Characters.EldenBeast)
    DisableCharacter(Characters.EldenBeast)
    DisableAnimations(Characters.EldenBeast)
    DisableAI(Characters.CLONE_EldenBeast)
    DisableCharacter(Characters.CLONE_EldenBeast)
    DisableAnimations(Characters.CLONE_EldenBeast)
    DisableCharacter(Characters.Unknown)  # TODO: ?
    DisableAnimations(Characters.Unknown)
    DisableAsset(Assets.AEG301_240_1000)

    DisableHealthBar(Characters.EldenBeast)
    DisableHealthBar(Characters.CLONE_EldenBeast)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(Flags.RadagonDead))
    AND_1.Add(FlagEnabled(Flags.StonePlatformEntered))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.EldenBeast, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.CLONE_EldenBeast, attacker=PLAYER))

    MAIN.Await(OR_1)

    # TODO: Will need to make sure that summons can enter Elden Beast fight properly as well.
    
    SetPlayerPositionDisplay(
        state=False,
        aboveground=True,
        game_map=STONE_PLATFORM,
        x=181.10000610351562,
        y=102.3499984741211,
        z=-607.0599975585938,
    )
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=19000000,
            cutscene_flags=0,
            move_to_region=RegionPoints.HostPositionAfterEldenBeastCutscene,
            map_id=19000000,
            player_id=PLAYER,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=19000000,
            cutscene_flags=0,
            move_to_region=RegionPoints.SummonPositionAfterEldenBeastCutscene,
            map_id=19000000,
            player_id=PLAYER,
            unk_20_24=0,
            unk_24_25=False,
        )
    WaitFramesAfterCutscene(frames=1)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=-11.329999923706055, y_angle=-25.829999923706055)
    if PlayerInOwnWorld():
        # So summons will skip the trigger/cutscene above.
        SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)

    # --- Label 1 --- #
    DefineLabel(1)
    SetBackreadStateAlternate(35000, True)
    SetNetworkUpdateRate(35000, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryFiveFrames)
    Move(35000, destination=19002813, destination_type=CoordEntityType.Region, copy_draw_parent=Characters.EldenBeast)
    Move(
        Characters.TalkDummy3,  # TODO: Needed for clone? Probably not...
        destination=19002813,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.EldenBeast,
    )
    SetCharacterTalkRange(character=Characters.TalkDummy3, distance=200.0)

    EnableCharacter(Characters.EldenBeast)
    EnableAnimations(Characters.EldenBeast)
    EnableAI(Characters.EldenBeast)  # changed from entity group
    ForceAnimation(Characters.EldenBeast, 20000)

    EnableCharacter(Characters.CLONE_EldenBeast)
    EnableAnimations(Characters.CLONE_EldenBeast)
    EnableAI(Characters.CLONE_EldenBeast)
    ForceAnimation(Characters.CLONE_EldenBeast, 20000)

    # TODO: Not sure how to manage this unknown entity. It's never disabled during the Radagon fight, so I assume
    #  I can just leave it.
    # EnableCharacter(Characters.Unknown)
    # EnableAnimations(Characters.Unknown)

    EnableBossHealthBar(Characters.EldenBeast, name=NameText.EldenBeast, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_EldenBeast, name=NameText.CLONE_EldenBeast, bar_slot=0)

    ChangeCamera(normal_camera_id=2200, locked_camera_id=2200)
    WaitFramesAfterCutscene(frames=1)
    AttachAssetToCharacter(character=Characters.TalkDummy3, model_point=10, asset=Assets.AEG099_052_9000)


@RestartOnRest(19002820)
def EldenBeastRandomFlagRequest():
    """UNUSED"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(Flags.EldenBeastDead):
        return
    AND_1.Add(FlagRangeAllDisabled(flag_range=(19002830, 19002834)))
    AND_1.Add(CharacterHasSpecialEffect(Characters.EldenBeast, 18600))
    
    MAIN.Await(AND_1)
    
    EnableRandomFlagInRange(flag_range=(19002830, 19002834))
    Wait(3.0)
    Restart()


@RestartOnRest(19002821)
def EldenBeastSpecialAttackManager():
    """UNUSED"""
    if FlagEnabled(Flags.EldenBeastDead):
        return
    EldenBeastSpecialAttack(
        0, required_flag=19002830, model_point=110, model_point_1=111, model_point_2=112, model_point_3=113
    )
    EldenBeastSpecialAttack(
        1, required_flag=19002831, model_point=111, model_point_1=112, model_point_2=113, model_point_3=114
    )
    EldenBeastSpecialAttack(
        2, required_flag=19002832, model_point=112, model_point_1=113, model_point_2=114, model_point_3=115
    )
    EldenBeastSpecialAttack(
        3, required_flag=19002833, model_point=113, model_point_1=114, model_point_2=115, model_point_3=116
    )
    EldenBeastSpecialAttack(
        4, required_flag=19002834, model_point=114, model_point_1=115, model_point_2=116, model_point_3=117
    )


@RestartOnRest(19002822)
def EldenBeastSpecialAttack(
    _, required_flag: uint, model_point: int, model_point_1: int, model_point_2: int, model_point_3: int
):
    """UNUSED"""
    if FlagEnabled(Flags.EldenBeastDead):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(required_flag))
    
    MAIN.Await(AND_1)
    
    Move(
        19000801,
        destination=Characters.EldenBeast,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        short_move=True,
    )
    Move(
        19000802,
        destination=Characters.EldenBeast,
        destination_type=CoordEntityType.Character,
        model_point=model_point_1,
        short_move=True,
    )
    Move(
        19000803,
        destination=Characters.EldenBeast,
        destination_type=CoordEntityType.Character,
        model_point=model_point_2,
        short_move=True,
    )
    Move(
        19000804,
        destination=Characters.EldenBeast,
        destination_type=CoordEntityType.Character,
        model_point=model_point_3,
        short_move=True,
    )
    ForceAnimation(Characters.EldenBeast, 3023, skip_transition=True)
    ForceAnimation(19000801, 3000, skip_transition=True)
    ForceAnimation(19000802, 3000, skip_transition=True)
    ForceAnimation(19000803, 3000, skip_transition=True)
    ForceAnimation(19000804, 3000, skip_transition=True)
    Wait(2.0)
    DisableFlag(required_flag)
    Restart()


@RestartOnRest(19002830)
def EldenBeastCameraChange():
    """Event 19002830"""
    DisableNetworkSync()
    if FlagEnabled(Flags.EldenBeastDead):
        return
    OR_1.Add(CharacterHasSpecialEffect(Characters.EldenBeast, 18606))
    OR_1.Add(CharacterHasSpecialEffect(Characters.CLONE_EldenBeast, 18606))

    MAIN.Await(OR_1)
    
    ChangeCamera(normal_camera_id=2201, locked_camera_id=2201)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.EldenBeast, 18606))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.CLONE_EldenBeast, 18606))

    MAIN.Await(AND_2)
    
    ChangeCamera(normal_camera_id=2200, locked_camera_id=2200)
    Restart()


@RestartOnRest(19002849)
def EldenBeastCommonEvents():
    """Event 19002849"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.EldenBeastDead,
        fog_asset=Assets.AEG099_001_9000,
        fog_region=19002800,
        host_entered_fog_flag=19002805,
        boss_characters=CharacterGroups.RadagonEldenBeast,
        action_button_id=10000,
        first_time_done_flag=Flags.RadagonBattleStarted,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.EldenBeastDead,
        fog_asset=Assets.AEG099_001_9000,
        fog_region=19002800,
        host_entered_fog_flag=19002805,
        summon_entered_fog_flag=19002806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(
        0,
        boss_dead_flag=Flags.EldenBeastDead,
        fog_asset=Assets.AEG099_001_9000,
        model_point=5,
        required_flag=Flags.RadagonBattleStarted,
    )
    CommonFunc_ControlBossMusic(0, Flags.EldenBeastDead, 219000, 19002805, 19002806, 0, Flags.RadagonDead, 0, 1)


@RestartOnRest(19002900)
def Event_19002900():
    """Event 19002900"""
    CreateAssetVFX(Assets.AEG099_090_9000, vfx_id=100, model_point=1300)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=9000, entity=Assets.AEG099_090_9000))
    
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=19002900,
        model_point=-1,
        copy_draw_parent=PLAYER,
        use_bonfire_effect=False,
        reset_camera=False,
    )
