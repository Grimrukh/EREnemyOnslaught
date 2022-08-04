"""TODO: Pumpkin Head Duo
North Caelid (SW) (SW)

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
from .entities.m60_48_40_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1048400000, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=1048400001, asset=Assets.AEG099_060_9001)
    Event_1048402800()
    Event_1048402810()
    Event_1048402849()
    CommonFunc_90005706(0, 1048400700, 30018, 0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1048400700)


@RestartOnRest(1048402800)
def Event_1048402800():
    """Event 1048402800"""
    if FlagEnabled(1048400800):
        return
    AND_1.Add(HealthValue(Characters.MadPumpkinHead0) <= 0)
    AND_1.Add(HealthValue(Characters.MadPumpkinHead1) <= 0)
    
    MAIN.Await(AND_1)
    
    Wait(4.0)
    PlaySoundEffect(Characters.MadPumpkinHead0, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(CharacterDead(Characters.MadPumpkinHead0))
    AND_2.Add(CharacterDead(Characters.MadPumpkinHead1))
    
    MAIN.Await(AND_2)
    
    KillBossAndDisplayBanner(character=Characters.MadPumpkinHead0, banner_type=BannerType.EnemyFelled)
    EnableFlag(1048400800)
    EnableAssetActivation(Assets.AEG004_970_2000, obj_act_id=-1)


@RestartOnRest(1048402810)
def Event_1048402810():
    """Event 1048402810"""
    GotoIfFlagDisabled(Label.L0, flag=1048400800)
    DisableCharacter(Characters.MadPumpkinHead0)
    DisableAnimations(Characters.MadPumpkinHead0)
    Kill(Characters.MadPumpkinHead0)
    DisableCharacter(Characters.MadPumpkinHead1)
    DisableAnimations(Characters.MadPumpkinHead1)
    Kill(Characters.MadPumpkinHead1)
    EnableAssetActivation(Assets.AEG004_970_2000, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(Characters.MadPumpkinHead0, 30005, loop=True)
    DisableAI(Characters.MadPumpkinHead1)
    DisableAI(Characters.MadPumpkinHead0)
    DisableAssetActivation(Assets.AEG004_970_2000, obj_act_id=-1)
    AND_1.Add(FlagEnabled(1048402805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1048402800))
    
    MAIN.Await(AND_1)
    
    EnableAI(Characters.MadPumpkinHead1)
    SetNetworkUpdateRate(Characters.MadPumpkinHead1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.MadPumpkinHead1, name=904340542)
    ForceAnimation(Characters.MadPumpkinHead1, 3012, loop=True)
    SetNetworkUpdateRate(Characters.MadPumpkinHead0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.MadPumpkinHead0, name=904340541, bar_slot=1)
    Wait(2.200000047683716)
    EnableAI(Characters.MadPumpkinHead0)
    ForceAnimation(Characters.MadPumpkinHead0, 20005, loop=True)


@RestartOnRest(1048402849)
def Event_1048402849():
    """Event 1048402849"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=1048400800,
        fog_asset=Assets.AEG099_003_9000,
        fog_region=1048402800,
        host_entered_fog_flag=1048402805,
        boss_characters=1048405800,
        action_button_id=10000,
        first_time_done_flag=0,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=1048400800,
        fog_asset=Assets.AEG099_003_9000,
        fog_region=1048402800,
        host_entered_fog_flag=1048402805,
        summon_entered_fog_flag=1048402806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=1048400800, fog_asset=Assets.AEG099_003_9000, model_point=3, required_flag=0)
    CommonFunc_ControlBossFog(0, boss_dead_flag=1048400800, fog_asset=Assets.AEG099_003_9001, model_point=3, required_flag=0)
    CommonFunc_ControlBossMusic(0, 1048400800, 920900, 1048402805, 1048402806, 0, 1048402802, 0, 0)
