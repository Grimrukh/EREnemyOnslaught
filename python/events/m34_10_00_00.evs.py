"""
Divine Tower of Limgrave

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
from .entities.m34_10_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=34100000, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=34100002, asset=Assets.AEG099_060_9002)
    CommonFunc_90005508(
        0,
        flag=34100510,
        flag_1=34101510,
        left=0,
        entity=Assets.AEG027_070_0500,
        asset=Assets.AEG027_203_0501,
        asset_1=Assets.AEG027_203_0500,
        flag_2=34100511,
    )
    Event_34102510()
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=34,
        block_id=10,
        cc_id=0,
        dd_id=0,
        player_start=34102600,
        unk_8_12=0,
        flag=34102610,
        left_flag=34102611,
        cancel_flag__right_flag=34102612,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    CommonFunc_90005110(
        0,
        flag=191,
        flag_1=9101,
        asset=Assets.AEG099_991_9000,
        item_lot=34100500,
        item=8148,
        model_point=806934,
        action_button_id=9080,
        animation_id=60522,
        left=0,
    )
    CommonFunc_NonRespawningWithReward(0, dead_flag=34100300, character=34100300, item_lot=34100300, reward_delay=0.0, skip_reward=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.GuardianGolem0,
        inactive_animation=30020,
        active_animation=20020,
        trigger_region=34102200,
        trigger_delay=15.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.GuardianGolem1,
        inactive_animation=30020,
        active_animation=20020,
        trigger_region=34102200,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, 34100202, 34102200, 8.0, -1)


@ContinueOnRest(34102510)
def Event_34102510():
    """Event 34102510"""
    CommonFunc_90005507(
        0,
        34100510,
        34101510,
        0,
        34101510,
        34101511,
        34102513,
        34101512,
        34102514,
        34102511,
        34102512,
        34100511,
        34102512,
        0,
    )


@RestartOnRest(34102690)
def Event_34102690():
    """Event 34102690"""
    DisableNetworkSync()
    GotoIfCharacterInsideRegion(Label.L0, character=PLAYER, region=34102690)
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=34102691)
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(WeatherState(weather=Weather.RainyClouds, unk_4_8=0.0, unk_8_12=0.0))
    GotoIfConditionTrue(Label.L2, input_condition=OR_1)
    SetWeather(weather=Weather.RainyClouds, duration=-1.0, immediate_change=False)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_1.Add(WeatherState(weather=Weather.HeavyFog, unk_4_8=0.0, unk_8_12=0.0))
    GotoIfConditionTrue(Label.L2, input_condition=OR_1)
    SetWeather(weather=Weather.HeavyFog, duration=-1.0, immediate_change=False)

    # --- Label 2 --- #
    DefineLabel(2)
    Restart()


@RestartOnRest(34102800)
def Event_34102800():
    """Event 34102800"""
    if FlagEnabled(34100800):
        return
    
    MAIN.Await(HealthValue(34100800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(34108000, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(34100800))
    
    KillBossAndDisplayBanner(character=34100800, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(9280)
    EnableFlag(34100800)


@RestartOnRest(34102810)
def Event_34102810():
    """Event 34102810"""
    GotoIfFlagDisabled(Label.L0, flag=34100800)
    DisableCharacter(34100800)
    DisableAnimations(34100800)
    Kill(34100800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(34100800)
    GotoIfFlagEnabled(Label.L1, flag=34100801)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=34102801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=34100800, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(34100801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(34102805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=34102800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(34100800)
    SetNetworkUpdateRate(34100800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(34100800)


@RestartOnRest(34102849)
def Event_34102849():
    """Event 34102849"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=34100800,
        fog_asset=34101800,
        fog_region=34102800,
        host_entered_fog_flag=34102805,
        boss_characters=34105800,
        action_button_id=10000,
        first_time_done_flag=34100801,
        first_time_trigger_region=34102801,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=34100800,
        fog_asset=34101800,
        fog_region=34102800,
        host_entered_fog_flag=34102805,
        summon_entered_fog_flag=34102806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=34100800, fog_asset=34101800, model_point=3, required_flag=34100801)
    CommonFunc_ControlBossMusic(0, 34100800, 90003101, 34102805, 34102806, 0, 11002852, 0, 0)
