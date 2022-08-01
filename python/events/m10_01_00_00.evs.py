"""DONE
Chapel of Anticipation

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
from .entities.m10_01_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    ShowUnknownTutorialMessage()

    # GRAFTED SCION
    GraftedScionDies()
    GraftedScionBattleTrigger()
    GraftedScionPhaseTwoTransition()
    GraftedScionCommonEvents()

    ButterflyOutcropBreaks()
    ControlFingerMaiden()
    Event_10010791()
    Event_10010792()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.FingerMaiden)
    Event_10010020()
    TakenToStrandedGraveyard()
    ProloguePlayerImmortality()
    DelayedAreaWelcomeMessage()
    Event_10012560()
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(100):
        return
    if FlagEnabled(102):
        return
    if OutsideMap(game_map=CHAPEL_OF_ANTICIPATION):
        return
    SetCurrentTime(
        time=(23, 45, 0),
        fade_transition=False,
        wait_for_completion=False,
        show_clock=False,
        clock_start_delay=0.0,
        clock_change_duration=0.0,
        clock_finish_delay=0.0,
    )


@RestartOnRest(10010020)
def Event_10010020():
    """Event 10010020"""
    if ThisEventSlotFlagEnabled():
        return
    if OutsideMap(game_map=CHAPEL_OF_ANTICIPATION):
        return
    SetAreaWelcomeMessageState(state=False)
    ForceAnimation(PLAYER, 0)
    SetWindVFX(wind_vfx_id=-1)
    SetCharacterFaceParamOverride(character=PLAYER, override_slot=0, face_param_id=-1)
    SetCharacterFaceParamOverride(character=PLAYER, override_slot=1, face_param_id=-1)
    PlayCutsceneToPlayerWithWeatherAndTime(
        cutscene_id=10000040,
        cutscene_flags=0,
        player_id=PLAYER,
        weather_duration=0.0,
        change_time=True,
        time=(23, 45, 0),
    )
    WaitFramesAfterCutscene(frames=1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetRespawnPoint(respawn_point=10012020)
    SaveRequest()
    EnableThisSlotFlag()
    EnableFlag(100)


@ContinueOnRest(10010030)
def TakenToStrandedGraveyard():
    """Event 10010030"""
    AND_15.Add(ThisEventSlotFlagEnabled())
    AND_15.Add(FlagEnabled(Flags.PrologueGraftedScionBattleDone))
    if AND_15:
        return
    if OutsideMap(game_map=CHAPEL_OF_ANTICIPATION):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(Flags.GraftedScionFirstTimeDone))
    OR_2.Add(HealthValue(Characters.GraftedScion) > 0)
    OR_2.Add(HealthValue(Characters.CLONE_GraftedScion) > 0)
    AND_2.Add(OR_2)
    AND_2.Add(HealthValue(PLAYER) == 1)
    AND_3.Add(CharacterDead(PLAYER))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    AND_1.Add(OR_1)

    MAIN.Await(AND_1)

    SetRespawnPoint(respawn_point=18002020)
    SaveRequest()
    DisableLoadingScreenText()
    EndIfFinishedConditionTrue(input_condition=AND_3)
    if ThisEventSlotFlagDisabled():
        Wait(1.0)
    AddSpecialEffect(PLAYER, 4790)
    EnableFlag(9021)
    SetBossMusic(bgm_boss_conv_param_id=920900, state=BossMusicState.Stop2)
    PlayCutsceneToPlayerAndWarpWithWeatherAndTime(
        cutscene_id=10010000,
        cutscene_flags=0,
        move_to_region=18002020,
        map_id=18000000,
        player_id=PLAYER,
        unk_20_24=10010,
        unk_24_25=False,
        change_weather=True,
        change_time=True,
        time=(10, 30, 0),
    )
    WaitFramesAfterCutscene(frames=1)


@ContinueOnRest(10010031)
def ProloguePlayerImmortality():
    """Event 10010031"""
    if OutsideMap(game_map=CHAPEL_OF_ANTICIPATION):
        return
    if FlagEnabled(Flags.PrologueGraftedScionBattleDone):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(10012805))

    MAIN.Await(AND_1)

    EnableImmortality(PLAYER)

    OR_2.Add(CharacterOutsideRegion(character=PLAYER, region=10012031))
    AND_2.Add(CharacterDead(Characters.GraftedScion))
    AND_2.Add(CharacterDead(Characters.CLONE_GraftedScion))
    OR_2.Add(AND_2)

    MAIN.Await(OR_2)

    DisableImmortality(PLAYER)


@RestartOnRest(10012500)
def ButterflyOutcropBreaks():
    """Event 10012500"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.ButterflyOutcropBroken)
    DisableAsset(Assets.AEG210_451_0500)
    DisableAsset(10011501)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=10012500))

    MAIN.Await(AND_1)

    DestroyAsset(Assets.AEG210_451_0500)
    EnableFlag(Flags.ButterflyOutcropBroken)


@RestartOnRest(10012501)
def Event_10012501():
    """Event 10012501"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(100):
        return
    if FlagEnabled(102):
        return
    if OutsideMap(game_map=CHAPEL_OF_ANTICIPATION):
        return
    SetWindVFX(wind_vfx_id=808004)
    AddSpecialEffect(PLAYER, 4200)


@RestartOnRest(10012502)
def DelayedAreaWelcomeMessage():
    """Event 10012502"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(Flags.DelayedAreaWelcomeMessageDone):
        return
    if OutsideMap(game_map=CHAPEL_OF_ANTICIPATION):
        return
    SetAreaWelcomeMessageState(state=False)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=10012502))

    MAIN.Await(AND_1)

    SetAreaWelcomeMessageState(state=True)
    DisplayAreaWelcomeMessage(text=10010)
    EnableFlag(Flags.DelayedAreaWelcomeMessageDone)


@RestartOnRest(10012504)
def Event_10012504():
    """Event 10012504"""
    if FlagEnabled(10018540):
        return
    if FlagEnabled(60210):
        return
    DisableAssetActivation(Assets.AEG219_002_0500, obj_act_id=-1)
    AND_1.Add(FlagEnabled(60210))

    MAIN.Await(AND_1)

    EnableAssetActivation(Assets.AEG219_002_0500, obj_act_id=-1)


@RestartOnRest(10012560)
def Event_10012560():
    """Event 10012560"""
    GotoIfFlagEnabled(Label.L0, flag=10018560)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(102))

    MAIN.Await(AND_1)

    EnableFlag(10018560)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAssetActivation(Assets.AEG219_000_0500, obj_act_id=2219000, relative_index=0)
    DisableAssetActivation(Assets.AEG219_000_0500, obj_act_id=2219000, relative_index=1)
    DisableAssetActivation(Assets.AEG219_000_0500, obj_act_id=2219000, relative_index=2)
    DisableAssetActivation(Assets.AEG219_000_0500, obj_act_id=2219000, relative_index=3)


@RestartOnRest(10012680)
def Event_10012680():
    """Event 10012680"""
    DisableNetworkSync()
    if FlagEnabled(18000020):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(10010020))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=10012680))

    MAIN.Await(AND_1)

    EnableFlag(710000)
    DisplayTutorialMessage(tutorial_param_id=1000, unk_4_5=True, unk_5_6=True)
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=10012680))

    MAIN.Await(AND_2)

    DisplayTutorialMessage(tutorial_param_id=1000, unk_4_5=False, unk_5_6=True)


@RestartOnRest(10012682)
def ShowUnknownTutorialMessage():
    """Event 10012682"""
    DisableNetworkSync()
    if FlagEnabled(18000020):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=10012682))

    MAIN.Await(AND_1)

    EnableFlag(710000)
    DisplayTutorialMessage(tutorial_param_id=1000, unk_4_5=True, unk_5_6=True)


@RestartOnRest(10012800)
def GraftedScionDies():
    """Event 10012800"""
    if FlagEnabled(Flags.GraftedScionDead):
        return

    AND_1.Add(HealthValue(Characters.GraftedScion) <= 0)
    AND_1.Add(HealthValue(Characters.CLONE_GraftedScion) <= 0)
    MAIN.Await(AND_1)

    Wait(4.0)
    PlaySoundEffect(10018000, 888880000, sound_type=SoundType.s_SFX)

    AND_2.Add(CharacterDead(Characters.GraftedScion))
    AND_2.Add(CharacterDead(Characters.CLONE_GraftedScion))
    MAIN.Await(AND_2)

    KillBossAndDisplayBanner(character=Characters.GraftedScion, banner_type=BannerType.EnemyFelled)
    EnableFlag(Flags.GraftedScionDead)
    EnableFlag(9103)
    if PlayerInOwnWorld():
        EnableFlag(61103)


@RestartOnRest(10012810)
def GraftedScionBattleTrigger():
    """Event 10012810"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.GraftedScionDead)
    DisableCharacter(Characters.GraftedScion)
    DisableAnimations(Characters.GraftedScion)
    Kill(Characters.GraftedScion)
    DisableCharacter(Characters.CLONE_GraftedScion)
    DisableAnimations(Characters.CLONE_GraftedScion)
    Kill(Characters.CLONE_GraftedScion)
    End()

    # --- Label 0 --- #
    DefineLabel(0)

    DisableAI(Characters.GraftedScion)
    DisableAI(Characters.CLONE_GraftedScion)

    GotoIfFlagEnabled(Label.L1, flag=Flags.GraftedScionFirstTimeDone)

    ForceAnimation(Characters.GraftedScion, 30003)
    DisableHealthBar(Characters.GraftedScion)
    ForceAnimation(Characters.CLONE_GraftedScion, 30003)
    DisableHealthBar(Characters.CLONE_GraftedScion)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=10012801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.GraftedScion, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.CLONE_GraftedScion, attacker=PLAYER))

    MAIN.Await(OR_1)

    # Grafted Scion jumps down from statue.
    EnableNetworkFlag(Flags.GraftedScionFirstTimeDone)
    SetNetworkUpdateRate(Characters.GraftedScion, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(Characters.GraftedScion, 20003)
    SetNetworkUpdateRate(Characters.CLONE_GraftedScion, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(Characters.CLONE_GraftedScion, 20003)
    Wait(4.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)

    # Grafted Scion waiting in arena.
    DisableAnimations(Characters.GraftedScion)
    Move(
        Characters.GraftedScion, destination=Regions.GraftedScionPositionAfterFirstTime,
        destination_type=CoordEntityType.Region, short_move=True
    )
    DisableAnimations(Characters.CLONE_GraftedScion)
    Move(
        Characters.GraftedScion, destination=Regions.CLONE_GraftedScionPositionAfterFirstTime,
        destination_type=CoordEntityType.Region, short_move=True
    )
    AND_2.Add(FlagEnabled(10012805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=10012800))

    MAIN.Await(AND_2)

    EnableAnimations(Characters.GraftedScion)
    EnableAnimations(Characters.CLONE_GraftedScion)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkUpdateRate(Characters.GraftedScion, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_GraftedScion, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(Characters.GraftedScion)
    EnableAI(Characters.CLONE_GraftedScion)
    EnableBossHealthBar(Characters.GraftedScion, name=NameText.GraftedScion, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_GraftedScion, name=NameText.CLONE_GraftedScion, bar_slot=0)
    if FlagEnabled(10010030):
        return
    AddSpecialEffect(PLAYER, 4290)


@RestartOnRest(10012811)
def GraftedScionPhaseTwoTransition():
    """Event 10012811"""
    if FlagEnabled(Flags.GraftedScionDead):
        return
    OR_1.Add(CharacterHasSpecialEffect(Characters.GraftedScion, 16265))
    OR_1.Add(CharacterHasSpecialEffect(Characters.CLONE_GraftedScion, 16265))

    MAIN.Await(OR_1)

    EnableFlag(Flags.GraftedScionInPhaseTwo)


@RestartOnRest(10012849)
def GraftedScionCommonEvents():
    """Event 10012849"""
    if FlagDisabled(Flags.PrologueGraftedScionBattleDone):
        CommonFunc_HostEntersBossFog(
            0,
            boss_dead_flag=Flags.GraftedScionDead,
            fog_asset=Assets.AEG099_001_9000,
            fog_region=10012800,
            host_entered_fog_flag=10012805,
            boss_characters=10015800,
            action_button_id=10000,
            first_time_done_flag=Flags.GraftedScionFirstTimeDone,
            first_time_trigger_region=10012801,
        )
    else:
        CommonFunc_HostEntersBossFog(
            0,
            boss_dead_flag=Flags.GraftedScionDead,
            fog_asset=Assets.AEG099_001_9001,
            fog_region=10012800,
            host_entered_fog_flag=10012805,
            boss_characters=10015800,
            action_button_id=10000,
            first_time_done_flag=Flags.GraftedScionFirstTimeDone,
            first_time_trigger_region=10012801,
        )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.GraftedScionDead,
        fog_asset=Assets.AEG099_001_9001,
        fog_region=10012800,
        host_entered_fog_flag=10012805,
        summon_entered_fog_flag=10012806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(
        0, boss_dead_flag=Flags.GraftedScionDead, fog_asset=Assets.AEG099_001_9000, model_point=16,
        required_flag=Flags.GraftedScionFirstTimeDone
    )
    CommonFunc_ControlBossFog(
        0, boss_dead_flag=Flags.GraftedScionDead, fog_asset=Assets.AEG099_001_9001, model_point=16, required_flag=0
    )
    CommonFunc_ControlBossMusic(
        0, Flags.GraftedScionDead, 920900, 10012805, 10012806, 0, Flags.GraftedScionInPhaseTwo, 0, 0
    )


@RestartOnRest(10010790)
def ControlFingerMaiden():
    """Event 10010790"""
    EnableBackread(Characters.FingerMaiden)
    EnableCharacter(Characters.FingerMaiden)
    ForceAnimation(Characters.FingerMaiden, 90100)
    DisableAnimations(Characters.FingerMaiden)


@RestartOnRest(10010791)
def Event_10010791():
    """Event 10010791"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400033):
        return
    if FlagDisabled(400031):
        return

    MAIN.Await(ActionButtonParamActivated(action_button_id=6471, entity=Characters.FingerMaiden))

    RemoveGoodFromPlayer(item=8154, quantity=1)
    AwardItemLot(100330, host_only=False)
    End()


@RestartOnRest(10010792)
def Event_10010792():
    """Event 10010792"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(50):
        return
    if FlagEnabled(10019200):
        return
    OR_1.Add(PlayerHasGood(9500))
    OR_2.Add(TimeElapsed(seconds=5.0))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)

    MAIN.Await(OR_3)

    WaitFrames(frames=1)
    OR_5.Add(PlayerHasGood(9500))
    SkipLinesIfConditionFalse(3, OR_5)
    EnableFlag(66150)
    EnableFlag(66170)
    EnableFlag(66180)
    EnableFlag(10019200)
    End()


@ContinueOnRest(10012900)
def Event_10012900():
    """Event 10012900"""
    MAIN.Await(FlagEnabled(10010900))

    IncrementEventValue(10010910, bit_count=32, max_value=999999999)
    Restart()
