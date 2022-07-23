"""
Regal Ancestor Arena

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
from .entities.m12_09_00_00_entities import *


# TODO: A lot of tricky animal events going on here. Probably just blindly duplicate everything.
#  Good news is that this map has heaps of available ID ranges for clones and flags.


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegalAncestorSpiritCommonEvents()
    Event_12092800()
    Event_12092810()
    ReturnToSiofraRiver()
    AnimalDies(0, animal=Characters.Deer0, dead_flag=12092858)
    AnimalDies(1, animal=Characters.Deer1, dead_flag=12092858)
    AnimalDies(2, animal=Characters.Deer2, dead_flag=12092858)
    AnimalDies(3, animal=Characters.Deer3, dead_flag=12092858)
    AnimalDies(4, animal=Characters.Deer4, dead_flag=12092858)
    AnimalDies(5, animal=Characters.Deer5, dead_flag=12092858)
    AnimalDies(6, animal=Characters.Deer6, dead_flag=12092858)
    AnimalDies(7, animal=Characters.Boar0, dead_flag=12092858)
    AnimalDies(8, animal=Characters.Boar1, dead_flag=12092858)
    AnimalDies(9, animal=Characters.Boar2, dead_flag=12092858)
    AnimalDies(10, animal=Characters.Boar3, dead_flag=12092858)
    AnimalDies(11, animal=Characters.Boar4, dead_flag=12092858)
    AnimalDies(12, animal=Characters.Boar5, dead_flag=12092858)
    AnimalDies(13, animal=Characters.Boar6, dead_flag=12092858)
    AnimalDies(14, animal=Characters.WildMouflon0, dead_flag=12092858)
    AnimalDies(15, animal=Characters.WildMouflon1, dead_flag=12092859)
    AnimalDies(16, animal=Characters.WildMouflon2, dead_flag=12092858)
    AnimalDies(17, animal=Characters.WildMouflon3, dead_flag=12092858)
    AnimalDies(18, animal=Characters.WildMouflon4, dead_flag=12092858)
    AnimalDies(19, animal=Characters.WildMouflon5, dead_flag=12092858)
    AnimalDies(20, animal=Characters.WildMouflon6, dead_flag=12092858)
    AnimalDies(21, animal=Characters.Springhare0, dead_flag=12092858)
    AnimalDies(22, animal=Characters.Springhare1, dead_flag=12092859)
    AnimalDies(23, animal=Characters.Springhare2, dead_flag=12092858)
    AnimalDies(24, animal=Characters.Springhare3, dead_flag=12092858)
    AnimalDies(25, animal=Characters.Springhare4, dead_flag=12092858)
    AnimalDies(26, animal=Characters.Springhare5, dead_flag=12092858)
    AnimalDies(27, animal=Characters.Springhare6, dead_flag=12092858)
    AnimalWanders(0, request_flag=12092870, animal=Characters.Deer0)
    AnimalWanders(1, request_flag=12092871, animal=Characters.Deer1)
    AnimalWanders(2, request_flag=12092872, animal=Characters.Deer2)
    AnimalWanders(3, request_flag=12092873, animal=Characters.Deer3)
    AnimalWanders(4, request_flag=12092874, animal=Characters.Deer4)
    AnimalWanders(5, request_flag=12092875, animal=Characters.Deer5)
    AnimalWanders(6, request_flag=12092876, animal=Characters.Deer6)
    AnimalWanders(7, request_flag=12092877, animal=Characters.Boar0)
    AnimalWanders(8, request_flag=12092878, animal=Characters.Boar1)
    AnimalWanders(9, request_flag=12092879, animal=Characters.Boar2)
    AnimalWanders(10, request_flag=12092880, animal=Characters.Boar3)
    AnimalWanders(11, request_flag=12092881, animal=Characters.Boar4)
    AnimalWanders(12, request_flag=12092882, animal=Characters.Boar5)
    AnimalWanders(13, request_flag=12092883, animal=Characters.Boar6)
    AnimalWanders(14, request_flag=12092884, animal=Characters.WildMouflon0)
    AnimalWanders(15, request_flag=12092885, animal=Characters.WildMouflon1)
    AnimalWanders(16, request_flag=12092886, animal=Characters.WildMouflon2)
    AnimalWanders(17, request_flag=12092887, animal=Characters.WildMouflon3)
    AnimalWanders(18, request_flag=12092888, animal=Characters.WildMouflon4)
    AnimalWanders(19, request_flag=12092889, animal=Characters.WildMouflon5)
    AnimalWanders(20, request_flag=12092890, animal=Characters.WildMouflon6)
    AnimalWanders(21, request_flag=12092891, animal=Characters.Springhare0)
    AnimalWanders(22, request_flag=12092892, animal=Characters.Springhare1)
    AnimalWanders(23, request_flag=12092893, animal=Characters.Springhare2)
    AnimalWanders(24, request_flag=12092894, animal=Characters.Springhare3)
    AnimalWanders(25, request_flag=12092895, animal=Characters.Springhare4)
    AnimalWanders(26, request_flag=12092896, animal=Characters.Springhare5)
    AnimalWanders(27, request_flag=12092897, animal=Characters.Springhare6)
    AncestorSpiritWarpsToAnimal(0, request_flag=12092870, animal=Characters.Deer0, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(1, request_flag=12092871, animal=Characters.Deer1, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(2, request_flag=12092872, animal=Characters.Deer2, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(3, request_flag=12092873, animal=Characters.Deer3, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(4, request_flag=12092874, animal=Characters.Deer4, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(5, request_flag=12092875, animal=Characters.Deer5, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(6, request_flag=12092876, animal=Characters.Deer6, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(7, request_flag=12092877, animal=Characters.Boar0, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(8, request_flag=12092878, animal=Characters.Boar1, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(9, request_flag=12092879, animal=Characters.Boar2, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(10, request_flag=12092880, animal=Characters.Boar3, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(11, request_flag=12092881, animal=Characters.Boar4, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(12, request_flag=12092882, animal=Characters.Boar5, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(13, request_flag=12092883, animal=Characters.Boar6, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(14, request_flag=12092884, animal=Characters.WildMouflon0, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(15, request_flag=12092885, animal=Characters.WildMouflon1, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(16, request_flag=12092886, animal=Characters.WildMouflon2, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(17, request_flag=12092887, animal=Characters.WildMouflon3, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(18, request_flag=12092888, animal=Characters.WildMouflon4, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(19, request_flag=12092889, animal=Characters.WildMouflon5, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(20, request_flag=12092890, animal=Characters.WildMouflon6, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(21, request_flag=12092891, animal=Characters.Springhare0, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(22, request_flag=12092892, animal=Characters.Springhare1, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(23, request_flag=12092893, animal=Characters.Springhare2, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(24, request_flag=12092894, animal=Characters.Springhare3, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(25, request_flag=12092895, animal=Characters.Springhare4, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(26, request_flag=12092896, animal=Characters.Springhare5, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorSpiritWarpsToAnimal(27, request_flag=12092897, animal=Characters.Springhare6, ancestor_spirit=Characters.RegalAncestorSpirit)
    Event_12092290()
    SetUpAncestorAnimals(0, animal_group=CharacterGroups.RegalAncestorAnimals)
    Event_12092854(
        0,
        flag=12092850,
        flag_1=12092851,
        flag_2=12092852,
        flag_3=12092853,
        ancestor_spirit=Characters.RegalAncestorSpirit,
        animal_group=CharacterGroups.RegalAncestorAnimals,
    )
    Event_12092859(
        0,
        flag=12092850,
        flag_1=12092851,
        flag_2=12092852,
        flag_3=12092853,
        first_flag=12092855,
        flag_4=12092856,
        last_flag=12092857,
        character=Characters.RegalAncestorSpirit,
        character_1=CharacterGroups.RegalAncestorAnimals,
        character_2=CharacterGroups.RegalAncestorDeer,
        character_3=CharacterGroups.RegalAncestorBoars,
        character_4=CharacterGroups.RegalAncestorWildMouflons,
        character_5=CharacterGroups.RegalAncestorSpringhares,
        character_6=Characters.Deer0,
        character_7=Characters.Deer1,
        character_8=Characters.Deer2,
        character_9=Characters.Deer3,
        character_10=Characters.Deer4,
        character_11=Characters.Deer5,
        character_12=Characters.Deer6,
        character_13=Characters.Boar0,
        character_14=Characters.Boar1,
        character_15=Characters.Boar2,
        character_16=Characters.Boar3,
        character_17=Characters.Boar4,
        character_18=Characters.Boar5,
        character_19=Characters.Boar6,
        character_20=Characters.WildMouflon0,
        character_21=Characters.WildMouflon1,
        character_22=Characters.WildMouflon2,
        character_23=Characters.WildMouflon3,
        character_24=Characters.WildMouflon4,
        character_25=Characters.WildMouflon5,
        character_26=Characters.WildMouflon6,
        character_27=Characters.Springhare0,
        character_28=Characters.Springhare1,
        character_29=Characters.Springhare2,
        character_30=Characters.Springhare3,
        character_31=Characters.Springhare4,
        character_32=Characters.Springhare5,
        character_33=Characters.Springhare6,
        character_34=12093200,
        character_35=12093201,
        character_36=12093202,
        character_37=12093203,
        character_38=12093204,
        character_39=12093205,
        character_40=12093206,
        character_41=12093220,
        character_42=12093221,
        character_43=12093222,
        character_44=12093223,
        character_45=12093224,
        character_46=12093225,
        character_47=12093226,
        character_48=12093240,
        character_49=12093241,
        character_50=12093242,
        character_51=12093243,
        character_52=12093244,
        character_53=12093245,
        character_54=12093246,
        character_55=12093260,
        character_56=12093261,
        character_57=12093262,
        character_58=12093263,
        character_59=12093264,
        character_60=12093265,
        character_61=12093266,
        flag_5=12092858,
    )
    Event_12092860(
        0,
        flag=12092858,
        ancestor_spirit=Characters.RegalAncestorSpirit,
        deer_group=CharacterGroups.RegalAncestorDeer,
        boar_group=CharacterGroups.RegalAncestorBoars,
        wild_mouflon_group=CharacterGroups.RegalAncestorWildMouflons,
        springhare_group=CharacterGroups.RegalAncestorSpringhares,
        animal_group=CharacterGroups.RegalAncestorAnimals,
    )
    Event_12092861(0, ancestor_spirit=Characters.RegalAncestorSpirit)
    Event_12092862(0, ancestor_spirit=Characters.RegalAncestorSpirit, animal_group=CharacterGroups.RegalAncestorAnimals)
    Event_12092863(0, ancestor_spirit=Characters.RegalAncestorSpirit, animal_group=CharacterGroups.RegalAncestorAnimals, flag=12092862)
    Event_12092864(0, ancestor_spirit=Characters.RegalAncestorSpirit, animal_group=CharacterGroups.RegalAncestorAnimals, flag=12092862, flag_1=12092863)
    CreateAncestorProjectileOwner(0, projectile_dummy=Characters.AncestorProjectileDummy)
    AncestorMegaProjectileAttack(0, ancestor_spirit=Characters.RegalAncestorSpirit)
    AncestorProjectile(0, request_flag=12092907, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092300)
    AncestorProjectile(1, request_flag=12092907, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092301)
    AncestorProjectile(2, request_flag=12092907, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092302)
    AncestorProjectile(3, request_flag=12092907, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092303)
    AncestorProjectile(4, request_flag=12092907, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092304)
    AncestorProjectile(5, request_flag=12092907, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092305)
    AncestorProjectile(6, request_flag=12092907, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092306)
    AncestorProjectile(7, request_flag=12092907, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092307)
    AncestorProjectile(8, request_flag=12092907, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092308)
    AncestorProjectile(9, request_flag=12092907, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092309)
    AncestorProjectile(10, request_flag=12092907, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092310)
    AncestorProjectile(11, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092311)
    AncestorProjectile(12, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092312)
    AncestorProjectile(13, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092313)
    AncestorProjectile(14, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092314)
    AncestorProjectile(15, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092315)
    AncestorProjectile(16, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092316)
    AncestorProjectile(17, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092317)
    AncestorProjectile(18, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092318)
    AncestorProjectile(19, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092319)
    AncestorProjectile(20, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092320)
    AncestorProjectile(21, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092321)
    AncestorProjectile(22, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092322)
    AncestorProjectile(23, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092323)
    AncestorProjectile(24, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092324)
    AncestorProjectile(25, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092325)
    AncestorProjectile(26, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092326)
    AncestorProjectile(27, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092327)
    AncestorProjectile(28, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092328)
    AncestorProjectile(29, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092329)
    AncestorProjectile(30, request_flag=12092908, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092330)
    AncestorProjectile(31, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092331)
    AncestorProjectile(32, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092332)
    AncestorProjectile(33, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092333)
    AncestorProjectile(34, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092334)
    AncestorProjectile(35, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092335)
    AncestorProjectile(36, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092336)
    AncestorProjectile(37, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092337)
    AncestorProjectile(38, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092338)
    AncestorProjectile(39, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092339)
    AncestorProjectile(40, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092340)
    AncestorProjectile(41, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092341)
    AncestorProjectile(42, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092342)
    AncestorProjectile(43, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092343)
    AncestorProjectile(44, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092344)
    AncestorProjectile(45, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092345)
    AncestorProjectile(46, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092346)
    AncestorProjectile(47, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092347)
    AncestorProjectile(48, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092348)
    AncestorProjectile(49, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092349)
    AncestorProjectile(50, request_flag=12092909, owner_entity=Characters.AncestorProjectileDummy, source_entity=12092350)


@ContinueOnRest(12092848)
def ReturnToSiofraRiver():
    """Event 12092848"""
    GotoIfFlagEnabled(Label.L0, flag=Flags.RegalAncestorSpiritDead)
    DeleteAssetVFX(Assets.AEG099_065_9000, erase_root=False)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(Flags.RegalAncestorSpiritDead))
    
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
    SetRespawnPoint(respawn_point=12022201)
    SaveRequest()
    WarpToMap(game_map=SIOFRA_RIVER, player_start=12022201)


@ContinueOnRest(12092800)
def Event_12092800():
    """Event 12092800"""
    if FlagEnabled(Flags.RegalAncestorSpiritDead):
        return

    AND_1.Add(HealthRatio(Characters.RegalAncestorSpirit) <= 0.0)
    AND_1.Add(HealthRatio(Characters.CLONE_AncestorSpirit) <= 0.0)
    MAIN.Await(AND_1)
    
    DisableFlag(12092907)
    DisableFlag(12092908)
    DisableFlag(12092909)
    Kill(CharacterGroups.RegalAncestorAnimals)
    Wait(2.0)
    PlaySoundEffect(Characters.RegalAncestorSpirit, 77777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.RegalAncestorSpirit))
    
    KillBossAndDisplayBanner(character=Characters.RegalAncestorSpirit, banner_type=BannerType.LegendFelled)
    EnableFlag(Flags.RegalAncestorSpiritDead)
    EnableFlag(9133)
    if PlayerInOwnWorld():
        EnableFlag(91133)
    AwardItemLot(48000000, host_only=True)


@RestartOnRest(12092810)
def Event_12092810():
    """Event 12092810"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.RegalAncestorSpiritDead)
    DisableCharacter(Characters.RegalAncestorSpirit)
    DisableAnimations(Characters.RegalAncestorSpirit)
    Kill(Characters.RegalAncestorSpirit)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.RegalAncestorSpirit)
    AND_2.Add(FlagEnabled(12092805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=12092800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.RegalAncestorSpirit)
    SetNetworkUpdateRate(Characters.RegalAncestorSpirit, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.RegalAncestorSpirit, name=904670001)


@ContinueOnRest(12092849)
def RegalAncestorSpiritCommonEvents():
    """Event 12092849"""
    CommonFunc_ControlBossMusic(
        0,
        boss_dead_flag=Flags.RegalAncestorSpiritDead,
        bgm_boss_conv_param_id=467000,
        host_in_battle=12090805,
        summon_in_battle=12090806,
        extra_required_flag=0,
        phase_two_flag=12092802,
        useless_phase_two_check=0,
        use_stop_type_1=0,
    )
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.RegalAncestorSpiritDead,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=12092800,
        host_entered_fog_flag=12092805,
        boss_characters=12095800,
        action_button_id=10000,
        first_time_done_flag=0,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.RegalAncestorSpiritDead,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=12092800,
        host_entered_fog_flag=12092805,
        summon_entered_fog_flag=12092806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.RegalAncestorSpiritDead, fog_asset=Assets.AEG099_002_9000, model_point=8, required_flag=0)
    CommonFunc_ControlBossMusic(0, Flags.RegalAncestorSpiritDead, 467000, 12092805, 12092806, 0, 12092802, 0, 0)


@RestartOnRest(12092200)
def AnimalDies(_, animal: uint, dead_flag: uint):
    """Event 12092200"""
    AND_1.Add(CharacterHasSpecialEffect(animal, Effects.AnimalActive))
    AND_1.Add(HealthRatio(animal) == 0.0)
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(animal, Effects.AnimalActive)
    EnableFlag(dead_flag)
    Restart()


@RestartOnRest(12092230)
def AnimalWanders(_, request_flag: uint, animal: uint):
    """Event 12092230"""
    AND_1.Add(FlagEnabled(request_flag))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(animal, Effects.AnimalActive)
    EnableInvincibility(animal)
    DisableAnimations(animal)
    DisableGravity(animal)
    DisableAI(animal)
    SetNetworkUpdateRate(animal, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(animal, 20000, wait_for_completion=True)
    ForceAnimation(animal, 20001, loop=True)
    Wait(15.0)
    Restart()


@RestartOnRest(12092260)
def AncestorSpiritWarpsToAnimal(_, request_flag: uint, animal: uint, ancestor_spirit: uint):
    """Event 12092260"""
    AND_1.Add(FlagEnabled(request_flag))
    AND_1.Add(CharacterHasSpecialEffect(ancestor_spirit, 13610))
    
    MAIN.Await(AND_1)
    
    DisableFlag(request_flag)
    DisableAnimations(ancestor_spirit)
    Move(
        ancestor_spirit,
        destination=animal,
        destination_type=CoordEntityType.Character,
        model_point=260,
        short_move=True,
    )

    # Ancestor Spirit does attack 3037 if player is between 7 and 40 units away, or 3014 otherwise.
    AND_15.Add(EntityWithinDistance(entity=20000, other_entity=animal, radius=40.0))
    AND_15.Add(EntityBeyondDistance(entity=20000, other_entity=animal, radius=7.0))
    SkipLinesIfConditionTrue(2, AND_15)
    ForceAnimation(ancestor_spirit, 3014)
    SkipLines(1)
    ForceAnimation(ancestor_spirit, 3037)

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=ancestor_spirit, special_effect=13601)
    AddSpecialEffect(ancestor_spirit, 13613)
    AddSpecialEffect(ancestor_spirit, 13618)
    Goto(Label.L0)

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=ancestor_spirit, special_effect=13602)
    AddSpecialEffect(ancestor_spirit, 13614)
    AddSpecialEffect(ancestor_spirit, 13619)
    Goto(Label.L0)

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=ancestor_spirit, special_effect=13603)
    AddSpecialEffect(ancestor_spirit, 13615)
    AddSpecialEffect(ancestor_spirit, 13620)
    Goto(Label.L0)

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=ancestor_spirit, special_effect=13604)
    AddSpecialEffect(ancestor_spirit, 13616)
    AddSpecialEffect(ancestor_spirit, 13621)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(animal, 20002, wait_for_completion=True)
    DisableAI(animal)
    EnableGravity(animal)
    DisableCharacter(animal)
    DisableInvincibility(animal)
    Kill(animal)
    SetNetworkUpdateRate(animal, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    EnableAnimations(ancestor_spirit)
    DisableFlag(request_flag)
    Restart()


@RestartOnRest(12092290)
def Event_12092290():
    """Event 12092290"""
    AND_1.Add(FlagEnabled(12092901))
    AND_1.Add(CharacterHasSpecialEffect(Characters.RegalAncestorSpirit, 13610))
    
    MAIN.Await(AND_1)
    
    DisableFlag(12092901)
    DisableAnimations(Characters.RegalAncestorSpirit)
    Move(
        Characters.RegalAncestorSpirit,
        destination=12092308,
        destination_type=CoordEntityType.Region,
        model_point=0,
        short_move=True,
    )
    ForceAnimation(Characters.RegalAncestorSpirit, 3014)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        line_count=3,
        character=Characters.RegalAncestorSpirit,
        special_effect=13601,
    )
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13613)
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13618)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        line_count=3,
        character=Characters.RegalAncestorSpirit,
        special_effect=13602,
    )
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13614)
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13619)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        line_count=3,
        character=Characters.RegalAncestorSpirit,
        special_effect=13603,
    )
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13615)
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13620)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        line_count=2,
        character=Characters.RegalAncestorSpirit,
        special_effect=13604,
    )
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13616)
    AddSpecialEffect(Characters.RegalAncestorSpirit, 13621)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAnimations(Characters.RegalAncestorSpirit)
    DisableFlag(12092901)
    Restart()


@RestartOnRest(12092295)
def SetUpAncestorAnimals(_, animal_group: uint):
    """Event 12092295"""
    SetLockOnPoint(character=animal_group, lock_on_model_point=220, state=False)
    DisableAnimations(animal_group)


@RestartOnRest(12092854)
def Event_12092854(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint, ancestor_spirit: uint, animal_group: uint):
    """Event 12092854"""
    MAIN.Await(CharacterHasSpecialEffect(ancestor_spirit, 13642))
    
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    AND_15.Add(CharacterHasSpecialEffect(animal_group, Effects.AnimalActive, target_comparison_type=ComparisonType.LessThan, target_count=5.0))
    SkipLinesIfConditionFalse(2, AND_15)
    EnableFlag(flag_2)
    Goto(Label.L0)
    AND_14.Add(CharacterHasSpecialEffect(animal_group, Effects.AnimalActive, target_comparison_type=ComparisonType.LessThan, target_count=10.0))
    SkipLinesIfConditionFalse(2, AND_14)
    EnableFlag(flag_1)
    Goto(Label.L0)
    AND_13.Add(CharacterHasSpecialEffect(
        animal_group,
        Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=10.0,
    ))
    SkipLinesIfConditionFalse(2, AND_13)
    EnableFlag(flag)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveSpecialEffect(animal_group, 13643)
    DisableFlag(flag_3)
    Wait(2.0)
    EnableFlag(flag_3)
    Restart()


@RestartOnRest(12092859)
def Event_12092859(
    _,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
    first_flag: uint,
    flag_4: uint,
    last_flag: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
    character_5: uint,
    character_6: uint,
    character_7: uint,
    character_8: uint,
    character_9: uint,
    character_10: uint,
    character_11: uint,
    character_12: uint,
    character_13: uint,
    character_14: uint,
    character_15: uint,
    character_16: uint,
    character_17: uint,
    character_18: uint,
    character_19: uint,
    character_20: uint,
    character_21: uint,
    character_22: uint,
    character_23: uint,
    character_24: uint,
    character_25: uint,
    character_26: uint,
    character_27: uint,
    character_28: uint,
    character_29: uint,
    character_30: uint,
    character_31: uint,
    character_32: uint,
    character_33: uint,
    character_34: uint,
    character_35: uint,
    character_36: uint,
    character_37: uint,
    character_38: uint,
    character_39: uint,
    character_40: uint,
    character_41: uint,
    character_42: uint,
    character_43: uint,
    character_44: uint,
    character_45: uint,
    character_46: uint,
    character_47: uint,
    character_48: uint,
    character_49: uint,
    character_50: uint,
    character_51: uint,
    character_52: uint,
    character_53: uint,
    character_54: uint,
    character_55: uint,
    character_56: uint,
    character_57: uint,
    character_58: uint,
    character_59: uint,
    character_60: uint,
    character_61: uint,
    flag_5: uint,
):
    """Event 12092859"""
    if ThisEventSlotFlagDisabled():
        EnableFlag(flag_3)
        Restart()
    
    MAIN.Await(FlagDisabled(flag_3))
    
    DisableFlag(first_flag)
    DisableFlag(flag_4)
    DisableFlag(last_flag)
    EnableRandomFlagInRange(flag_range=(first_flag, last_flag))
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=13645)
    GotoIfCharacterHasSpecialEffect(
        Label.L0,
        character=character_2,
        special_effect=Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    EnableCharacter(character_8)
    EnableAI(character_8)
    ForceSpawnerToSpawn(spawner=character_36)
    WaitFrames(frames=1)
    AddSpecialEffect(character_8, 13643)
    AddSpecialEffect(character_8, Effects.AnimalActive)
    DisableAnimations(character_8)
    Goto(Label.L20)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L1, character=character, special_effect=13646)
    SkipLinesIfCharacterHasSpecialEffect(
        line_count=8,
        character=character_3,
        special_effect=Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    EnableCharacter(character_13)
    EnableAI(character_13)
    ForceSpawnerToSpawn(spawner=character_41)
    WaitFrames(frames=1)
    AddSpecialEffect(character_13, 13643)
    AddSpecialEffect(character_13, Effects.AnimalActive)
    DisableAnimations(character_13)
    Goto(Label.L20)
    GotoIfCharacterHasSpecialEffect(
        Label.L1,
        character=character_5,
        special_effect=Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    EnableCharacter(character_27)
    EnableAI(character_27)
    ForceSpawnerToSpawn(spawner=character_55)
    WaitFrames(frames=1)
    AddSpecialEffect(character_27, 13643)
    AddSpecialEffect(character_27, Effects.AnimalActive)
    DisableAnimations(character_27)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L2, character=character, special_effect=13647)
    GotoIfCharacterHasSpecialEffect(
        Label.L2,
        character=character_4,
        special_effect=Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    EnableCharacter(character_20)
    EnableAI(character_20)
    ForceSpawnerToSpawn(spawner=character_48)
    WaitFrames(frames=1)
    AddSpecialEffect(character_20, 13643)
    AddSpecialEffect(character_20, Effects.AnimalActive)
    DisableAnimations(character_20)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagDisabled(first_flag):
        GotoIfFlagEnabled(Label.L3, flag=flag_4)
        GotoIfFlagEnabled(Label.L4, flag=last_flag)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_6, special_effect=Effects.AnimalActive)
    EnableCharacter(character_6)
    EnableAI(character_6)
    ForceSpawnerToSpawn(spawner=character_34)
    WaitFrames(frames=1)
    AddSpecialEffect(character_6, 13643)
    AddSpecialEffect(character_6, Effects.AnimalActive)
    DisableAnimations(character_6)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_13, special_effect=Effects.AnimalActive)
    EnableCharacter(character_13)
    EnableAI(character_13)
    ForceSpawnerToSpawn(spawner=character_41)
    WaitFrames(frames=1)
    AddSpecialEffect(character_13, 13643)
    AddSpecialEffect(character_13, Effects.AnimalActive)
    DisableAnimations(character_13)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_20, special_effect=Effects.AnimalActive)
    EnableCharacter(character_20)
    EnableAI(character_20)
    ForceSpawnerToSpawn(spawner=character_48)
    WaitFrames(frames=1)
    AddSpecialEffect(character_20, 13643)
    AddSpecialEffect(character_20, Effects.AnimalActive)
    DisableAnimations(character_20)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_27, special_effect=Effects.AnimalActive)
    EnableCharacter(character_27)
    EnableAI(character_27)
    ForceSpawnerToSpawn(spawner=character_55)
    WaitFrames(frames=1)
    AddSpecialEffect(character_27, 13643)
    AddSpecialEffect(character_27, Effects.AnimalActive)
    DisableAnimations(character_27)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_7, special_effect=Effects.AnimalActive)
    EnableCharacter(character_7)
    EnableAI(character_7)
    ForceSpawnerToSpawn(spawner=character_35)
    WaitFrames(frames=1)
    AddSpecialEffect(character_7, 13643)
    AddSpecialEffect(character_7, Effects.AnimalActive)
    DisableAnimations(character_7)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_14, special_effect=Effects.AnimalActive)
    EnableCharacter(character_14)
    EnableAI(character_14)
    ForceSpawnerToSpawn(spawner=character_42)
    WaitFrames(frames=1)
    AddSpecialEffect(character_14, 13643)
    AddSpecialEffect(character_14, Effects.AnimalActive)
    DisableAnimations(character_14)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_21, special_effect=Effects.AnimalActive)
    EnableCharacter(character_21)
    EnableAI(character_21)
    ForceSpawnerToSpawn(spawner=character_49)
    WaitFrames(frames=1)
    AddSpecialEffect(character_21, 13643)
    AddSpecialEffect(character_21, Effects.AnimalActive)
    DisableAnimations(character_21)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_28, special_effect=Effects.AnimalActive)
    EnableCharacter(character_28)
    EnableAI(character_28)
    ForceSpawnerToSpawn(spawner=character_56)
    WaitFrames(frames=1)
    AddSpecialEffect(character_28, 13643)
    AddSpecialEffect(character_28, Effects.AnimalActive)
    DisableAnimations(character_28)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_8, special_effect=Effects.AnimalActive)
    EnableCharacter(character_8)
    EnableAI(character_8)
    ForceSpawnerToSpawn(spawner=character_36)
    WaitFrames(frames=1)
    AddSpecialEffect(character_8, 13643)
    AddSpecialEffect(character_8, Effects.AnimalActive)
    DisableAnimations(character_8)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_15, special_effect=Effects.AnimalActive)
    EnableCharacter(character_15)
    EnableAI(character_15)
    ForceSpawnerToSpawn(spawner=character_43)
    WaitFrames(frames=1)
    AddSpecialEffect(character_15, 13643)
    AddSpecialEffect(character_15, Effects.AnimalActive)
    DisableAnimations(character_15)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_22, special_effect=Effects.AnimalActive)
    EnableCharacter(character_22)
    EnableAI(character_22)
    ForceSpawnerToSpawn(spawner=character_50)
    WaitFrames(frames=1)
    AddSpecialEffect(character_22, 13643)
    AddSpecialEffect(character_22, Effects.AnimalActive)
    DisableAnimations(character_22)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_29, special_effect=Effects.AnimalActive)
    EnableCharacter(character_29)
    EnableAI(character_29)
    ForceSpawnerToSpawn(spawner=character_57)
    WaitFrames(frames=1)
    AddSpecialEffect(character_29, 13643)
    AddSpecialEffect(character_29, Effects.AnimalActive)
    DisableAnimations(character_29)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_23, special_effect=Effects.AnimalActive)
    EnableCharacter(character_23)
    EnableAI(character_23)
    ForceSpawnerToSpawn(spawner=character_51)
    WaitFrames(frames=1)
    AddSpecialEffect(character_23, 13643)
    AddSpecialEffect(character_23, Effects.AnimalActive)
    DisableAnimations(character_23)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_9, special_effect=Effects.AnimalActive)
    EnableCharacter(character_9)
    EnableAI(character_9)
    ForceSpawnerToSpawn(spawner=character_37)
    WaitFrames(frames=1)
    AddSpecialEffect(character_9, 13643)
    AddSpecialEffect(character_9, Effects.AnimalActive)
    DisableAnimations(character_9)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_30, special_effect=Effects.AnimalActive)
    EnableCharacter(character_30)
    EnableAI(character_30)
    ForceSpawnerToSpawn(spawner=character_58)
    WaitFrames(frames=1)
    AddSpecialEffect(character_30, 13643)
    AddSpecialEffect(character_30, Effects.AnimalActive)
    DisableAnimations(character_30)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_16, special_effect=Effects.AnimalActive)
    EnableCharacter(character_16)
    EnableAI(character_16)
    ForceSpawnerToSpawn(spawner=character_44)
    WaitFrames(frames=1)
    AddSpecialEffect(character_16, 13643)
    AddSpecialEffect(character_16, Effects.AnimalActive)
    DisableAnimations(character_16)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_24, special_effect=Effects.AnimalActive)
    EnableCharacter(character_24)
    EnableAI(character_24)
    ForceSpawnerToSpawn(spawner=character_52)
    WaitFrames(frames=1)
    AddSpecialEffect(character_24, 13643)
    AddSpecialEffect(character_24, Effects.AnimalActive)
    DisableAnimations(character_24)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_10, special_effect=Effects.AnimalActive)
    EnableCharacter(character_10)
    EnableAI(character_10)
    ForceSpawnerToSpawn(spawner=character_38)
    WaitFrames(frames=1)
    AddSpecialEffect(character_10, 13643)
    AddSpecialEffect(character_10, Effects.AnimalActive)
    DisableAnimations(character_10)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_31, special_effect=Effects.AnimalActive)
    EnableCharacter(character_31)
    EnableAI(character_31)
    ForceSpawnerToSpawn(spawner=character_59)
    WaitFrames(frames=1)
    AddSpecialEffect(character_31, 13643)
    AddSpecialEffect(character_31, Effects.AnimalActive)
    DisableAnimations(character_31)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_17, special_effect=Effects.AnimalActive)
    EnableCharacter(character_17)
    EnableAI(character_17)
    ForceSpawnerToSpawn(spawner=character_45)
    WaitFrames(frames=1)
    AddSpecialEffect(character_17, 13643)
    AddSpecialEffect(character_17, Effects.AnimalActive)
    DisableAnimations(character_17)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_32, special_effect=Effects.AnimalActive)
    EnableCharacter(character_32)
    EnableAI(character_32)
    ForceSpawnerToSpawn(spawner=character_60)
    WaitFrames(frames=1)
    AddSpecialEffect(character_32, 13643)
    AddSpecialEffect(character_32, Effects.AnimalActive)
    DisableAnimations(character_32)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_25, special_effect=Effects.AnimalActive)
    EnableCharacter(character_25)
    EnableAI(character_25)
    ForceSpawnerToSpawn(spawner=character_53)
    WaitFrames(frames=1)
    AddSpecialEffect(character_25, 13643)
    AddSpecialEffect(character_25, Effects.AnimalActive)
    DisableAnimations(character_25)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_18, special_effect=Effects.AnimalActive)
    EnableCharacter(character_18)
    EnableAI(character_18)
    ForceSpawnerToSpawn(spawner=character_46)
    WaitFrames(frames=1)
    AddSpecialEffect(character_18, 13643)
    AddSpecialEffect(character_18, Effects.AnimalActive)
    DisableAnimations(character_18)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_11, special_effect=Effects.AnimalActive)
    EnableCharacter(character_11)
    EnableAI(character_11)
    ForceSpawnerToSpawn(spawner=character_39)
    WaitFrames(frames=1)
    AddSpecialEffect(character_11, 13643)
    AddSpecialEffect(character_11, Effects.AnimalActive)
    DisableAnimations(character_11)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_33, special_effect=Effects.AnimalActive)
    EnableCharacter(character_33)
    EnableAI(character_33)
    ForceSpawnerToSpawn(spawner=character_61)
    WaitFrames(frames=1)
    AddSpecialEffect(character_33, 13643)
    AddSpecialEffect(character_33, Effects.AnimalActive)
    DisableAnimations(character_33)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_26, special_effect=Effects.AnimalActive)
    EnableCharacter(character_26)
    EnableAI(character_26)
    ForceSpawnerToSpawn(spawner=character_54)
    WaitFrames(frames=1)
    AddSpecialEffect(character_26, 13643)
    AddSpecialEffect(character_26, Effects.AnimalActive)
    DisableAnimations(character_26)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_19, special_effect=Effects.AnimalActive)
    EnableCharacter(character_19)
    EnableAI(character_19)
    ForceSpawnerToSpawn(spawner=character_47)
    WaitFrames(frames=1)
    AddSpecialEffect(character_19, 13643)
    AddSpecialEffect(character_19, Effects.AnimalActive)
    DisableAnimations(character_19)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_12, special_effect=Effects.AnimalActive)
    EnableCharacter(character_12)
    EnableAI(character_12)
    ForceSpawnerToSpawn(spawner=character_40)
    WaitFrames(frames=1)
    AddSpecialEffect(character_12, 13643)
    AddSpecialEffect(character_12, Effects.AnimalActive)
    DisableAnimations(character_12)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    EnableFlag(flag_5)
    AND_10.Add(FlagEnabled(flag))
    AND_10.Add(CharacterHasSpecialEffect(
        character_1,
        13643,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=6.0,
    ))
    AND_11.Add(FlagEnabled(flag_1))
    AND_11.Add(CharacterHasSpecialEffect(
        character_1,
        13643,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=8.0,
    ))
    AND_12.Add(FlagEnabled(flag_2))
    AND_12.Add(CharacterHasSpecialEffect(
        character_1,
        13643,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=10.0,
    ))
    OR_10.Add(AND_10)
    OR_10.Add(AND_11)
    OR_10.Add(AND_12)
    SkipLinesIfConditionFalse(2, OR_10)
    EnableFlag(flag_3)
    RemoveSpecialEffect(character_1, 13643)
    Restart()


@RestartOnRest(12092860)
def Event_12092860(
    _,
    flag: uint,
    ancestor_spirit: uint,
    deer_group: uint,
    boar_group: uint,
    wild_mouflon_group: uint,
    springhare_group: uint,
    animal_group: uint,
):
    """Event 12092860"""
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    AND_1.Add(CharacterHasSpecialEffect(deer_group, Effects.AnimalActive, target_count=0.0))
    SkipLinesIfConditionTrue(2, AND_1)
    AddSpecialEffect(ancestor_spirit, 13606)
    SkipLines(1)
    RemoveSpecialEffect(ancestor_spirit, 13606)

    AND_2.Add(CharacterHasSpecialEffect(boar_group, Effects.AnimalActive, target_count=0.0))
    SkipLinesIfConditionTrue(2, AND_2)
    AddSpecialEffect(ancestor_spirit, 13607)
    SkipLines(1)
    RemoveSpecialEffect(ancestor_spirit, 13607)

    AND_3.Add(CharacterHasSpecialEffect(wild_mouflon_group, Effects.AnimalActive, target_count=0.0))
    SkipLinesIfConditionTrue(2, AND_3)
    AddSpecialEffect(ancestor_spirit, 13608)
    SkipLines(1)
    RemoveSpecialEffect(ancestor_spirit, 13608)

    AND_4.Add(CharacterHasSpecialEffect(springhare_group, Effects.AnimalActive, target_count=0.0))
    SkipLinesIfConditionTrue(2, AND_4)
    AddSpecialEffect(ancestor_spirit, 13609)
    SkipLines(1)
    RemoveSpecialEffect(ancestor_spirit, 13609)

    AND_5.Add(CharacterHasSpecialEffect(
        animal_group,
        Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=5.0,
    ))
    SkipLinesIfConditionTrue(2, AND_5)
    AddSpecialEffect(ancestor_spirit, 13625)
    SkipLines(1)
    RemoveSpecialEffect(ancestor_spirit, 13625)

    DisableFlag(12092907)
    DisableFlag(12092908)
    DisableFlag(12092909)
    SkipLinesIfCharacterHasSpecialEffect(
        line_count=3,
        character=animal_group,
        special_effect=Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=20,
    )
    SkipLinesIfCharacterHasSpecialEffect(
        line_count=4,
        character=animal_group,
        special_effect=Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=13,
    )
    SkipLinesIfCharacterHasSpecialEffect(
        line_count=5,
        character=animal_group,
        special_effect=Effects.AnimalActive,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    SkipLines(5)
    EnableFlag(12092909)
    SkipLines(3)
    EnableFlag(12092908)
    SkipLines(1)
    EnableFlag(12092907)
    Restart()


@RestartOnRest(12092861)
def Event_12092861(_, ancestor_spirit: uint):
    """Event 12092861"""
    MAIN.Await(CharacterHasSpecialEffect(ancestor_spirit, 13623))
    
    EnableAnimations(ancestor_spirit)
    ReplanAI(ancestor_spirit)
    Restart()


@RestartOnRest(12092862)
def Event_12092862(_, ancestor_spirit: uint, animal_group: uint):
    """Event 12092862"""
    MAIN.Await(CharacterHasSpecialEffect(ancestor_spirit, 13624))
    
    AddSpecialEffect(ancestor_spirit, 13632)
    AddSpecialEffect(ancestor_spirit, 13646)
    AddSpecialEffect(animal_group, 13617)
    Kill(animal_group)
    Wait(1.0)
    DisableThisSlotFlag()
    EnableFlag(12092802)


@RestartOnRest(12092863)
def Event_12092863(_, ancestor_spirit: uint, animal_group: uint, flag: uint):
    """Event 12092863"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterHasSpecialEffect(ancestor_spirit, 13624))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(ancestor_spirit, 13633)
    AddSpecialEffect(ancestor_spirit, 13647)
    AddSpecialEffect(animal_group, 13617)
    Kill(animal_group)
    Wait(1.0)
    DisableThisSlotFlag()


@RestartOnRest(12092864)
def Event_12092864(_, ancestor_spirit: uint, animal_group: uint, flag: uint, flag_1: uint):
    """Event 12092864"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterHasSpecialEffect(ancestor_spirit, 13624))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(ancestor_spirit, 13634)
    AddSpecialEffect(animal_group, 13617)
    Kill(animal_group)
    Wait(1.0)
    Restart()


@RestartOnRest(12092865)
def AncestorMegaProjectileAttack(_, ancestor_spirit: uint):
    """Event 12092865"""
    MAIN.Await(CharacterHasSpecialEffect(ancestor_spirit, 13624))
    
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092300,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092301,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092302,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092303,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092304,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092305,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092306,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092307,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092308,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092309,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092310,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092311,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092312,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092313,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092314,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092315,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092316,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092317,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092318,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092319,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092320,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092321,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092322,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092323,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092324,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092325,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092326,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092327,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092328,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092329,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092330,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092331,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092332,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092333,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092334,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092335,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092336,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092337,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092338,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092339,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092340,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092341,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092342,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092343,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092344,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092345,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092346,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092347,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092348,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092349,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.AncestorProjectileDummy,
        source_entity=12092350,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Restart()


@RestartOnRest(12092910)
def CreateAncestorProjectileOwner(_, projectile_dummy: uint):
    """Event 12092910"""
    CreateProjectileOwner(entity=projectile_dummy)


@RestartOnRest(12092920)
def AncestorProjectile(_, request_flag: uint, owner_entity: uint, source_entity: uint):
    """Event 12092920"""
    SkipLinesIfUnsignedEqual(2, left=request_flag, right=12092908)
    SkipLinesIfUnsignedEqual(2, left=request_flag, right=12092909)
    OR_1.Add(FlagEnabled(12092907))
    OR_1.Add(FlagEnabled(12092908))
    OR_1.Add(FlagEnabled(12092909))
    AND_1.Add(CharacterAlive(Characters.RegalAncestorSpirit))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=246700900,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagEnabled(3, 12092908)
    SkipLinesIfFlagEnabled(4, 12092909)
    WaitRandomSeconds(min_seconds=8.0, max_seconds=10.0)
    SkipLines(3)
    WaitRandomSeconds(min_seconds=6.0, max_seconds=8.0)
    SkipLines(1)
    WaitRandomSeconds(min_seconds=4.0, max_seconds=6.0)
    Restart()
