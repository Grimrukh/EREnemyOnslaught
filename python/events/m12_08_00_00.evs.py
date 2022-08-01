"""DONE
Ancestor Spirit Arena

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
from .entities.m12_08_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    AncestorSpiritCommonEvents()
    AncestorSpiritDies()
    AncestorSpiritBattleTrigger()
    ReturnToSiofraRiver()


@ContinueOnRest(12082848)
def ReturnToSiofraRiver():
    """Event 12082848"""
    GotoIfFlagEnabled(Label.L0, flag=Flags.AncestorSpiritDead)
    DeleteAssetVFX(Assets.AEG099_065_9000, erase_root=False)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(Flags.AncestorSpiritDead))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(Assets.AEG099_065_9000)
    CreateAssetVFX(Assets.AEG099_065_9000, vfx_id=190, model_point=1300)
    OR_2.Add(MultiplayerPending())
    OR_2.Add(Multiplayer())
    AND_2.Add(not OR_2)
    AND_2.Add(ActionButtonParamActivated(action_button_id=9526, entity=Assets.AEG099_065_9000))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(PLAYER, 60460)
    Wait(2.5)
    SetRespawnPoint(respawn_point=12022200)
    SaveRequest()
    WarpToMap(game_map=SIOFRA_RIVER, player_start=12022200)


@ContinueOnRest(12082800)
def AncestorSpiritDies():
    """Event 12082800"""
    if FlagEnabled(Flags.AncestorSpiritDead):
        return

    AND_1.Add(HealthRatio(Characters.AncestorSpirit) <= 0.0)
    AND_1.Add(HealthRatio(Characters.CLONE_AncestorSpirit) <= 0.0)
    MAIN.Await(AND_1)
    
    Wait(2.0)
    PlaySoundEffect(Characters.AncestorSpirit, 77777777, sound_type=SoundType.s_SFX)

    AND_2.Add(CharacterDead(Characters.AncestorSpirit))
    AND_2.Add(CharacterDead(Characters.CLONE_AncestorSpirit))
    MAIN.Await(AND_2)
    
    KillBossAndDisplayBanner(character=Characters.AncestorSpirit, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(Flags.AncestorSpiritDead)
    EnableFlag(9132)
    if PlayerInOwnWorld():
        EnableFlag(61132)


@RestartOnRest(12082810)
def AncestorSpiritBattleTrigger():
    """Event 12082810"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.AncestorSpiritDead)
    DisableCharacter(Characters.AncestorSpirit)
    DisableAnimations(Characters.AncestorSpirit)
    Kill(Characters.AncestorSpirit)
    DisableCharacter(Characters.CLONE_AncestorSpirit)
    DisableAnimations(Characters.CLONE_AncestorSpirit)
    Kill(Characters.CLONE_AncestorSpirit)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.AncestorSpirit)
    DisableAI(Characters.CLONE_AncestorSpirit)
    AND_2.Add(FlagEnabled(12082805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=12082800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.AncestorSpirit)
    EnableAI(Characters.CLONE_AncestorSpirit)
    SetNetworkUpdateRate(Characters.AncestorSpirit, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_AncestorSpirit, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.AncestorSpirit, name=NameText.AncestorSpirit, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_AncestorSpirit, name=NameText.CLONE_AncestorSpirit, bar_slot=0)


@ContinueOnRest(12082849)
def AncestorSpiritCommonEvents():
    """Event 12082849"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.AncestorSpiritDead,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=12082800,
        host_entered_fog_flag=12082805,
        boss_characters=12085800,
        action_button_id=10000,
        first_time_done_flag=0,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.AncestorSpiritDead,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=12082800,
        host_entered_fog_flag=12082805,
        summon_entered_fog_flag=12082806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.AncestorSpiritDead, fog_asset=Assets.AEG099_002_9000, model_point=8, required_flag=0)
    CommonFunc_ControlBossMusic(0, Flags.AncestorSpiritDead, 467000, 12082805, 12082806, 0, 12082802, 0, 0)
