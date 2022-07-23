"""
Southeast Mountaintops (SW) (SW)

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
from .entities.m60_52_52_00_entities import *
from .entities.m60_52_53_00_entities import Assets as m60_52_Assets, Characters as m60_52_Characters


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    FireGiantDies()
    FireGiantBattleTrigger()
    FireGiantPhaseThreeTransition(
        0,
        fire_giant_phase_onetwo=Characters.FireGiantPhaseOneTwo,
        fire_giant_phase_three=Characters.FireGiantPhaseThree,
    )
    FireGiantPhaseThreeTransition(
        2,
        fire_giant_phase_onetwo=Characters.CLONE_FireGiantPhaseOneTwo,
        fire_giant_phase_three=Characters.CLONE_FireGiantPhaseThree,
    )
    FireGiantPhaseThreeAITrigger()
    FireGiantFirstLeg(
        0,
        fire_giant=Characters.FireGiantPhaseOneTwo,
        part_health=225,
        value_0=200,
        value_1=175,
        value_2=150,
        value_3=125,
        value_4=100,
        value_5=75,
        value_6=50,
        value_7=25,
        value_8=0,
        damage_flag_0=Flags.FireGiantFirstLegDamage0,
        damage_flag_1=Flags.FireGiantFirstLegDamage1,
        damage_flag_2=Flags.FireGiantFirstLegDamage2,
        damage_flag_3=Flags.FireGiantFirstLegDamage3,
        damage_flag_4=Flags.FireGiantFirstLegDamage4,
        damage_flag_5=Flags.FireGiantFirstLegDamage5,
        damage_flag_6=Flags.FireGiantFirstLegDamage6,
        damage_flag_7=Flags.FireGiantFirstLegDamage7,
        damage_flag_8=Flags.FireGiantFirstLegDamage8,
    )
    FireGiantFirstLeg(
        30,
        fire_giant=Characters.CLONE_FireGiantPhaseOneTwo,
        part_health=225,
        value_0=200,
        value_1=175,
        value_2=150,
        value_3=125,
        value_4=100,
        value_5=75,
        value_6=50,
        value_7=25,
        value_8=0,
        damage_flag_0=Flags.CLONE_FireGiantFirstLegDamage0,
        damage_flag_1=Flags.CLONE_FireGiantFirstLegDamage1,
        damage_flag_2=Flags.CLONE_FireGiantFirstLegDamage2,
        damage_flag_3=Flags.CLONE_FireGiantFirstLegDamage3,
        damage_flag_4=Flags.CLONE_FireGiantFirstLegDamage4,
        damage_flag_5=Flags.CLONE_FireGiantFirstLegDamage5,
        damage_flag_6=Flags.CLONE_FireGiantFirstLegDamage6,
        damage_flag_7=Flags.CLONE_FireGiantFirstLegDamage7,
        damage_flag_8=Flags.CLONE_FireGiantFirstLegDamage8,
    )
    FireGiantSecondLeg(
        0,
        fire_giant=Characters.FireGiantPhaseOneTwo,
        part_health=225,
        value_0=200,
        value_1=175,
        value_2=150,
        value_3=125,
        value_4=100,
        value_5=75,
        value_6=50,
        value_7=25,
        value_8=0,
        damage_flag_0=Flags.FireGiantSecondLegDamage0,
        damage_flag_1=Flags.FireGiantSecondLegDamage1,
        damage_flag_2=Flags.FireGiantSecondLegDamage2,
        damage_flag_3=Flags.FireGiantSecondLegDamage3,
        damage_flag_4=Flags.FireGiantSecondLegDamage4,
        damage_flag_5=Flags.FireGiantSecondLegDamage5,
        damage_flag_6=Flags.FireGiantSecondLegDamage6,
        damage_flag_7=Flags.FireGiantSecondLegDamage7,
        damage_flag_8=Flags.FireGiantSecondLegDamage8,
    )
    FireGiantSecondLeg(
        30,
        fire_giant=Characters.CLONE_FireGiantPhaseOneTwo,
        part_health=225,
        value_0=200,
        value_1=175,
        value_2=150,
        value_3=125,
        value_4=100,
        value_5=75,
        value_6=50,
        value_7=25,
        value_8=0,
        damage_flag_0=Flags.CLONE_FireGiantSecondLegDamage0,
        damage_flag_1=Flags.CLONE_FireGiantSecondLegDamage1,
        damage_flag_2=Flags.CLONE_FireGiantSecondLegDamage2,
        damage_flag_3=Flags.CLONE_FireGiantSecondLegDamage3,
        damage_flag_4=Flags.CLONE_FireGiantSecondLegDamage4,
        damage_flag_5=Flags.CLONE_FireGiantSecondLegDamage5,
        damage_flag_6=Flags.CLONE_FireGiantSecondLegDamage6,
        damage_flag_7=Flags.CLONE_FireGiantSecondLegDamage7,
        damage_flag_8=Flags.CLONE_FireGiantSecondLegDamage8,
    )
    FireGiantRegenerate(0, fire_giant=Characters.FireGiantPhaseOneTwo)
    FireGiantRegenerate(30, fire_giant=Characters.CLONE_FireGiantPhaseOneTwo)  # 1052522847
    FireGiantCommonEvents()


@RestartOnRest(1052520800)
def FireGiantDies():
    """Event 1052520800"""
    if FlagEnabled(Flags.FireGiantDead):
        return

    AND_1.Add(HealthValue(Characters.FireGiantPhaseThree) <= 0)
    AND_1.Add(HealthValue(Characters.CLONE_FireGiantPhaseThree) <= 0)
    MAIN.Await(AND_1)
    
    Wait(4.0)
    PlaySoundEffect(Characters.FireGiantPhaseThree, 888880000, sound_type=SoundType.s_SFX)

    AND_2.Add(CharacterDead(Characters.FireGiantPhaseThree))
    AND_2.Add(CharacterDead(Characters.CLONE_FireGiantPhaseThree))
    MAIN.Await(AND_2)
    
    Wait(4.0)
    KillBossAndDisplayBanner(character=Characters.FireGiantPhaseThree, banner_type=BannerType.LegendFelled)
    EnableFlag(Flags.FireGiantDead)
    EnableFlag(9131)
    if PlayerInOwnWorld():
        EnableFlag(61131)


@RestartOnRest(1052522810)
def FireGiantBattleTrigger():
    """Event 1052522810"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.FireGiantDead)
    DisableCharacter(CharacterGroups.FireGiantBoss)
    DisableAnimations(CharacterGroups.FireGiantBoss)
    Kill(CharacterGroups.FireGiantBoss, award_runes=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableGravity(Characters.FireGiantPhaseThree)
    DisableAnimations(Characters.FireGiantPhaseThree)
    DisableAI(Characters.FireGiantPhaseThree)
    DisableAI(Characters.FireGiantPhaseOneTwo)

    DisableGravity(Characters.CLONE_FireGiantPhaseThree)
    DisableAnimations(Characters.CLONE_FireGiantPhaseThree)
    DisableAI(Characters.CLONE_FireGiantPhaseThree)
    DisableAI(Characters.CLONE_FireGiantPhaseOneTwo)

    SetLockOnPoint(character=Characters.FireGiantPhaseThree, lock_on_model_point=221, state=False)
    SetLockOnPoint(character=Characters.FireGiantPhaseThree, lock_on_model_point=222, state=False)
    SetLockOnPoint(character=Characters.FireGiantPhaseThree, lock_on_model_point=225, state=False)
    SetLockOnPoint(character=Characters.FireGiantPhaseThree, lock_on_model_point=226, state=False)
    SetLockOnPoint(character=Characters.FireGiantPhaseThree, lock_on_model_point=227, state=False)
    SetLockOnPoint(character=Characters.FireGiantPhaseOneTwo, lock_on_model_point=221, state=False)
    SetLockOnPoint(character=Characters.FireGiantPhaseOneTwo, lock_on_model_point=223, state=False)
    SetLockOnPoint(character=Characters.FireGiantPhaseOneTwo, lock_on_model_point=224, state=False)
    SetLockOnPoint(character=Characters.FireGiantPhaseOneTwo, lock_on_model_point=225, state=False)
    SetLockOnPoint(character=Characters.FireGiantPhaseOneTwo, lock_on_model_point=226, state=False)
    SetLockOnPoint(character=Characters.FireGiantPhaseOneTwo, lock_on_model_point=227, state=False)

    SetLockOnPoint(character=Characters.CLONE_FireGiantPhaseThree, lock_on_model_point=221, state=False)
    SetLockOnPoint(character=Characters.CLONE_FireGiantPhaseThree, lock_on_model_point=222, state=False)
    SetLockOnPoint(character=Characters.CLONE_FireGiantPhaseThree, lock_on_model_point=225, state=False)
    SetLockOnPoint(character=Characters.CLONE_FireGiantPhaseThree, lock_on_model_point=226, state=False)
    SetLockOnPoint(character=Characters.CLONE_FireGiantPhaseThree, lock_on_model_point=227, state=False)
    SetLockOnPoint(character=Characters.CLONE_FireGiantPhaseOneTwo, lock_on_model_point=221, state=False)
    SetLockOnPoint(character=Characters.CLONE_FireGiantPhaseOneTwo, lock_on_model_point=223, state=False)
    SetLockOnPoint(character=Characters.CLONE_FireGiantPhaseOneTwo, lock_on_model_point=224, state=False)
    SetLockOnPoint(character=Characters.CLONE_FireGiantPhaseOneTwo, lock_on_model_point=225, state=False)
    SetLockOnPoint(character=Characters.CLONE_FireGiantPhaseOneTwo, lock_on_model_point=226, state=False)
    SetLockOnPoint(character=Characters.CLONE_FireGiantPhaseOneTwo, lock_on_model_point=227, state=False)

    GotoIfFlagEnabled(Label.L1, flag=Flags.FireGiantFirstTimeDone)
    if PlayerInOwnWorld():
        DisableFlag(Flags.EnableFireGiantFog)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.FireGiantPhaseOneTwo))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.CLONE_FireGiantPhaseOneTwo))
    OR_1.Add(EntityWithinDistance(
        entity=Characters.FireGiantPhaseOneTwo, other_entity=PLAYER, radius=120.0
    ))
    OR_1.Add(EntityWithinDistance(
        entity=Characters.FireGiantPhaseOneTwo, other_entity=m60_52_Characters.AlexanderSummon1, radius=120.0
    ))
    OR_1.Add(EntityWithinDistance(
        entity=Characters.FireGiantPhaseOneTwo, other_entity=m60_52_Characters.AlexanderSummon2, radius=120.0
    ))
    OR_1.Add(EntityWithinDistance(
        entity=Characters.CLONE_FireGiantPhaseOneTwo, other_entity=PLAYER, radius=120.0
    ))
    OR_1.Add(EntityWithinDistance(
        entity=Characters.CLONE_FireGiantPhaseOneTwo, other_entity=m60_52_Characters.AlexanderSummon1, radius=120.0
    ))
    OR_1.Add(EntityWithinDistance(
        entity=Characters.CLONE_FireGiantPhaseOneTwo, other_entity=m60_52_Characters.AlexanderSummon2, radius=120.0
    ))

    MAIN.Await(OR_1)
    
    EnableFlag(Flags.FireGiantFirstTimeDone)
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.FireGiantPhaseOneTwo))
    OR_1.Add(CharacterHasStateInfo(character=Characters.FireGiantPhaseOneTwo, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.FireGiantPhaseOneTwo, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.FireGiantPhaseOneTwo, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.FireGiantPhaseOneTwo, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.FireGiantPhaseOneTwo, state_info=260))
    OR_1.Add(EntityWithinDistance(entity=Characters.FireGiantPhaseOneTwo, other_entity=PLAYER, radius=120.0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.CLONE_FireGiantPhaseOneTwo))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_FireGiantPhaseOneTwo, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_FireGiantPhaseOneTwo, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_FireGiantPhaseOneTwo, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_FireGiantPhaseOneTwo, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_FireGiantPhaseOneTwo, state_info=260))
    OR_1.Add(EntityWithinDistance(entity=Characters.CLONE_FireGiantPhaseOneTwo, other_entity=PLAYER, radius=120.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1052532800))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1052532801))
    AND_2.Add(OR_2)
    AND_2.Add(FlagEnabled(1252522805))
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableNetworkFlag(Flags.EnableFireGiantFog)

    ReferDamageToEntity(Characters.FireGiantPhaseOneTwo, target_entity=Characters.FireGiantPhaseThree)
    ReferDamageToEntity(Characters.CLONE_FireGiantPhaseOneTwo, target_entity=Characters.CLONE_FireGiantPhaseThree)
    EnableAI(Characters.FireGiantPhaseOneTwo)
    EnableAI(Characters.CLONE_FireGiantPhaseOneTwo)
    EnableBossHealthBar(Characters.FireGiantPhaseThree, name=NameText.FireGiant, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_FireGiantPhaseThree, name=NameText.CLONE_FireGiant, bar_slot=0)
    DisableHealthBar(Characters.FireGiantPhaseOneTwo)
    DisableHealthBar(Characters.CLONE_FireGiantPhaseOneTwo)
    SetNetworkUpdateRate(Characters.FireGiantPhaseOneTwo, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_FireGiantPhaseOneTwo, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(1052522811)
def FireGiantPhaseThreeTransition(_, fire_giant_phase_onetwo: uint, fire_giant_phase_three: uint):
    """Event 1052522811"""
    if FlagEnabled(Flags.FireGiantDead):
        return
    
    MAIN.Await(HealthRatio(fire_giant_phase_onetwo) <= 0.0)
    
    SetTeamType(fire_giant_phase_onetwo, TeamType.Object)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarpWithStablePositionUpdate(
            cutscene_id=60520010,
            cutscene_flags=0,
            move_to_region=1052522810,
            map_id=60525200,
            player_id=PLAYER,
            unk_16_20=65001,
            unk_20_21=False,
            update_stable_position=False,
        )
    else:
        PlayCutscene(60520010, cutscene_flags=0, player_id=PLAYER)
    WaitFramesAfterCutscene(frames=1)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=-32.529998779296875, y_angle=-43.560001373291016)
    EnableCharacter(fire_giant_phase_three)
    WaitFrames(frames=1)
    ForceAnimation(fire_giant_phase_three, 20000)
    Move(
        fire_giant_phase_three,
        destination=1052522815,  # TODO: May want a different placement for clone?
        destination_type=CoordEntityType.Region,
        copy_draw_parent=fire_giant_phase_onetwo,
    )
    EnableGravity(fire_giant_phase_three)
    WaitFrames(frames=1)
    DisableCharacter(fire_giant_phase_onetwo)
    DisableAnimations(fire_giant_phase_onetwo)
    WaitFrames(frames=1)
    EnableAnimations(fire_giant_phase_three)
    EnableFlag(Flags.FireGiantInPhaseThree)


@ContinueOnRest(1052522812)
def FireGiantPhaseThreeAITrigger():
    """Event 1052522812"""
    if FlagEnabled(Flags.FireGiantDead):
        return
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.FireGiantPhaseThree))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.CLONE_FireGiantPhaseThree))
    OR_1.Add(EntityWithinDistance(entity=Characters.FireGiantPhaseThree, other_entity=PLAYER, radius=70.0))
    OR_1.Add(EntityWithinDistance(entity=Characters.CLONE_FireGiantPhaseThree, other_entity=PLAYER, radius=70.0))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(Flags.FireGiantInPhaseThree))
    
    MAIN.Await(AND_1)
    
    EnableAI(Characters.FireGiantPhaseThree)
    EnableAI(Characters.CLONE_FireGiantPhaseThree)
    SetNetworkUpdateRate(Characters.FireGiantPhaseThree, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_FireGiantPhaseThree, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    WaitFrames(frames=1)
    AddSpecialEffect(Characters.FireGiantPhaseThree, 12780)
    AddSpecialEffect(Characters.CLONE_FireGiantPhaseThree, 12780)


@RestartOnRest(1052522815)
def FireGiantFirstLeg(
    _,
    fire_giant: uint,
    part_health: int,
    value_0: int,
    value_1: int,
    value_2: int,
    value_3: int,
    value_4: int,
    value_5: int,
    value_6: int,
    value_7: int,
    value_8: int,
    damage_flag_0: int,
    damage_flag_1: int,
    damage_flag_2: int,
    damage_flag_3: int,
    damage_flag_4: int,
    damage_flag_5: int,
    damage_flag_6: int,
    damage_flag_7: int,
    damage_flag_8: int,
):
    """Event 1052522815"""
    if FlagEnabled(Flags.FireGiantDead):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(CharacterBackreadEnabled(fire_giant))
    
    MAIN.Await(AND_1)
    
    CreateNPCPart(
        fire_giant,
        npc_part_id=9,
        part_index=NPCPartType.Part9,
        part_health=part_health,
        body_damage_correction=1.5,
    )
    GotoIfFlagEnabled(Label.L18, flag=damage_flag_8)
    GotoIfFlagEnabled(Label.L17, flag=damage_flag_7)
    GotoIfFlagEnabled(Label.L16, flag=damage_flag_6)
    GotoIfFlagEnabled(Label.L15, flag=damage_flag_5)
    GotoIfFlagEnabled(Label.L14, flag=damage_flag_4)
    GotoIfFlagEnabled(Label.L13, flag=damage_flag_3)
    GotoIfFlagEnabled(Label.L12, flag=damage_flag_2)
    GotoIfFlagEnabled(Label.L11, flag=damage_flag_1)
    GotoIfFlagEnabled(Label.L10, flag=damage_flag_0)
    OR_10.Add(CharacterPartHealth(fire_giant, npc_part_id=9) <= value_0)
    
    MAIN.Await(OR_10)
    
    EnableNetworkFlag(damage_flag_0)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 10 --- #
    DefineLabel(10)
    AddSpecialEffect(fire_giant, 12730)
    OR_11.Add(CharacterPartHealth(fire_giant, npc_part_id=9) <= value_1)
    
    MAIN.Await(OR_11)
    
    EnableNetworkFlag(damage_flag_1)  # NOTE: this was damage flag 0 (accidentally, I presume)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 11 --- #
    DefineLabel(11)
    AddSpecialEffect(fire_giant, 12731)
    OR_12.Add(CharacterPartHealth(fire_giant, npc_part_id=9) <= value_2)
    
    MAIN.Await(OR_12)
    
    EnableNetworkFlag(damage_flag_2)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 12 --- #
    DefineLabel(12)
    AddSpecialEffect(fire_giant, 12732)
    OR_13.Add(CharacterPartHealth(fire_giant, npc_part_id=9) <= value_3)
    
    MAIN.Await(OR_13)
    
    EnableNetworkFlag(damage_flag_3)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 13 --- #
    DefineLabel(13)
    AddSpecialEffect(fire_giant, 12733)
    OR_14.Add(CharacterPartHealth(fire_giant, npc_part_id=9) <= value_4)
    
    MAIN.Await(OR_14)
    
    EnableNetworkFlag(damage_flag_4)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 14 --- #
    DefineLabel(14)
    AddSpecialEffect(fire_giant, 12734)
    OR_15.Add(CharacterPartHealth(fire_giant, npc_part_id=9) <= value_5)
    
    MAIN.Await(OR_15)
    
    EnableNetworkFlag(damage_flag_5)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 15 --- #
    DefineLabel(15)
    AddSpecialEffect(fire_giant, 12735)
    AND_10.Add(CharacterPartHealth(fire_giant, npc_part_id=9) <= value_6)
    
    MAIN.Await(AND_10)
    
    EnableNetworkFlag(damage_flag_6)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 16 --- #
    DefineLabel(16)
    AddSpecialEffect(fire_giant, 12736)
    AND_11.Add(CharacterPartHealth(fire_giant, npc_part_id=9) <= value_7)
    
    MAIN.Await(AND_11)
    
    EnableNetworkFlag(damage_flag_7)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 17 --- #
    DefineLabel(17)
    AddSpecialEffect(fire_giant, 12737)
    AND_12.Add(CharacterPartHealth(fire_giant, npc_part_id=9) <= value_8)
    
    MAIN.Await(AND_12)
    
    EnableNetworkFlag(damage_flag_8)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 18 --- #
    DefineLabel(18)
    AddSpecialEffect(fire_giant, 12738)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    if CharacterHasSpecialEffect(character=fire_giant, special_effect=12752):
        return
    AddSpecialEffect(fire_giant, 12750)


@RestartOnRest(1052522816)
def FireGiantSecondLeg(
    _,
    fire_giant: uint,
    part_health: int,
    value_0: int,
    value_1: int,
    value_2: int,
    value_3: int,
    value_4: int,
    value_5: int,
    value_6: int,
    value_7: int,
    value_8: int,
    damage_flag_0: int,
    damage_flag_1: int,
    damage_flag_2: int,
    damage_flag_3: int,
    damage_flag_4: int,
    damage_flag_5: int,
    damage_flag_6: int,
    damage_flag_7: int,
    damage_flag_8: int,
):
    """Event 1052522816"""
    if FlagEnabled(Flags.FireGiantDead):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(CharacterBackreadEnabled(fire_giant))
    
    MAIN.Await(AND_1)
    
    CreateNPCPart(
        fire_giant,
        npc_part_id=8,
        part_index=NPCPartType.Part8,
        part_health=part_health,
        body_damage_correction=1.5,
    )
    GotoIfFlagEnabled(Label.L18, flag=damage_flag_8)
    GotoIfFlagEnabled(Label.L17, flag=damage_flag_7)
    GotoIfFlagEnabled(Label.L16, flag=damage_flag_6)
    GotoIfFlagEnabled(Label.L15, flag=damage_flag_5)
    GotoIfFlagEnabled(Label.L14, flag=damage_flag_4)
    GotoIfFlagEnabled(Label.L13, flag=damage_flag_3)
    GotoIfFlagEnabled(Label.L12, flag=damage_flag_2)
    GotoIfFlagEnabled(Label.L11, flag=damage_flag_1)
    GotoIfFlagEnabled(Label.L10, flag=damage_flag_0)
    OR_10.Add(CharacterPartHealth(fire_giant, npc_part_id=8) <= value_0)
    
    MAIN.Await(OR_10)
    
    EnableNetworkFlag(damage_flag_0)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 10 --- #
    DefineLabel(10)
    AddSpecialEffect(fire_giant, 12740)
    OR_11.Add(CharacterPartHealth(fire_giant, npc_part_id=8) <= value_1)
    
    MAIN.Await(OR_11)
    
    EnableNetworkFlag(damage_flag_1)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 11 --- #
    DefineLabel(11)
    AddSpecialEffect(fire_giant, 12741)
    OR_12.Add(CharacterPartHealth(fire_giant, npc_part_id=8) <= value_2)
    
    MAIN.Await(OR_12)
    
    EnableNetworkFlag(damage_flag_2)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 12 --- #
    DefineLabel(12)
    AddSpecialEffect(fire_giant, 12742)
    OR_13.Add(CharacterPartHealth(fire_giant, npc_part_id=8) <= value_3)
    
    MAIN.Await(OR_13)
    
    EnableNetworkFlag(damage_flag_3)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 13 --- #
    DefineLabel(13)
    AddSpecialEffect(fire_giant, 12743)
    OR_14.Add(CharacterPartHealth(fire_giant, npc_part_id=8) <= value_4)
    
    MAIN.Await(OR_14)
    
    EnableNetworkFlag(damage_flag_4)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 14 --- #
    DefineLabel(14)
    AddSpecialEffect(fire_giant, 12744)
    OR_15.Add(CharacterPartHealth(fire_giant, npc_part_id=8) <= value_5)
    
    MAIN.Await(OR_15)
    
    EnableNetworkFlag(damage_flag_5)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 15 --- #
    DefineLabel(15)
    AddSpecialEffect(fire_giant, 12745)
    AND_10.Add(CharacterPartHealth(fire_giant, npc_part_id=8) <= value_6)
    
    MAIN.Await(AND_10)
    
    EnableNetworkFlag(damage_flag_6)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 16 --- #
    DefineLabel(16)
    AddSpecialEffect(fire_giant, 12746)
    AND_11.Add(CharacterPartHealth(fire_giant, npc_part_id=8) <= value_7)
    
    MAIN.Await(AND_11)
    
    EnableNetworkFlag(damage_flag_7)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 17 --- #
    DefineLabel(17)
    AddSpecialEffect(fire_giant, 12747)
    AND_12.Add(CharacterPartHealth(fire_giant, npc_part_id=8) <= value_8)
    
    MAIN.Await(AND_12)
    
    EnableNetworkFlag(damage_flag_8)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=fire_giant,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 18 --- #
    DefineLabel(18)
    AddSpecialEffect(fire_giant, 12748)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    if CharacterHasSpecialEffect(character=fire_giant, special_effect=12752):
        return
    AddSpecialEffect(fire_giant, 12750)


@RestartOnRest(1052522817)
def FireGiantRegenerate(_, fire_giant: uint):
    """Event 1052522817"""
    if FlagEnabled(Flags.FireGiantDead):
        return
    OR_1.Add(CharacterHasSpecialEffect(fire_giant, 12752))
    
    MAIN.Await(OR_1)
    
    SetNPCPartHealth(fire_giant, npc_part_id=8, desired_health=0, overwrite_max=False)
    SetNPCPartHealth(fire_giant, npc_part_id=9, desired_health=0, overwrite_max=False)
    WaitFrames(frames=1)
    CreateNPCPart(
        fire_giant,
        npc_part_id=8,
        part_index=NPCPartType.Part8,
        part_health=99999,
        body_damage_correction=2.0,
    )
    CreateNPCPart(
        fire_giant,
        npc_part_id=9,
        part_index=NPCPartType.Part9,
        part_health=99999,
        body_damage_correction=2.0,
    )


@RestartOnRest(1052522849)
def FireGiantCommonEvents():
    """Event 1052522849"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.FireGiantDead,
        fog_asset=m60_52_Assets.AEG099_002_9000,
        fog_region=1052532800,
        host_entered_fog_flag=1252522805,
        boss_characters=CharacterGroups.FireGiantBoss,
        action_button_id=10000,
        first_time_done_flag=Flags.FireGiantFirstTimeDone,
        first_time_trigger_region=0,
    )
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.FireGiantDead,
        fog_asset=m60_52_Assets.AEG099_003_9001,
        fog_region=1052532801,
        host_entered_fog_flag=1252522805,
        boss_characters=CharacterGroups.FireGiantBoss,
        action_button_id=10000,
        first_time_done_flag=Flags.FireGiantFirstTimeDone,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.FireGiantDead,
        fog_asset=m60_52_Assets.AEG099_002_9000,
        fog_region=1052532800,
        host_entered_fog_flag=1252522805,
        summon_entered_fog_flag=1252522806,
        action_button_id=10000,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.FireGiantDead,
        fog_asset=m60_52_Assets.AEG099_003_9001,
        fog_region=1052532801,
        host_entered_fog_flag=1252522805,
        summon_entered_fog_flag=1252522806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(
        0,
        boss_dead_flag=Flags.FireGiantDead,
        fog_asset=m60_52_Assets.AEG099_002_9000,
        model_point=9,
        required_flag=Flags.EnableFireGiantFog,
    )
    CommonFunc_ControlBossFog(
        0,
        boss_dead_flag=Flags.FireGiantDead,
        fog_asset=m60_52_Assets.AEG099_003_9001,
        model_point=10,
        required_flag=Flags.EnableFireGiantFog,
    )
    CommonFunc_ControlBossFog(
        0,
        boss_dead_flag=Flags.FireGiantDead,
        fog_asset=Assets.AEG099_019_1000,
        model_point=0,
        required_flag=Flags.EnableFireGiantFog,
    )
    CommonFunc_ControlBossFog(
        0,
        boss_dead_flag=Flags.FireGiantDead,
        fog_asset=m60_52_Assets.AEG099_017_1000,
        model_point=0,
        required_flag=Flags.EnableFireGiantFog,
    )
    CommonFunc_ControlBossMusic(
        0,
        Flags.FireGiantDead,
        476000,
        1252522805,
        1252522806,
        0,
        Flags.FireGiantInPhaseThree,
        1,
        1,
    )
