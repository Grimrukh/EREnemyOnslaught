"""DONE
Crumbling Farum Azula

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
from .entities.m13_00_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=13000003, asset=Assets.AEG099_060_9003)
    RegisterGrace(grace_flag=13000004, asset=Assets.AEG099_060_9004)
    RegisterGrace(grace_flag=13000005, asset=Assets.AEG099_060_9005)
    RegisterGrace(grace_flag=13000006, asset=Assets.AEG099_060_9006)
    RegisterGrace(grace_flag=13000007, asset=Assets.AEG099_060_9007)
    RegisterGrace(grace_flag=13000008, asset=Assets.AEG099_060_9008)
    RegisterGrace(grace_flag=13000009, asset=Assets.AEG099_060_9009)
    RegisterGrace(grace_flag=13000010, asset=Assets.AEG099_060_9010)
    ControlMalikethGrace()
    CommonFunc_RegisterGraceIfFlagEnabled(
        0,
        flag=Flags.DragonlodPlacidusaxDead,
        grace_flag=13000001,
        character=Characters.TalkDummy1,
        asset=Assets.AEG099_060_9001,
        enemy_block_distance=5.0,
    )
    CommonFunc_RegisterGraceIfFlagEnabled(
        0,
        flag=Flags.GodskinDuoDead,
        grace_flag=13000002,
        character=Characters.TalkDummy2,
        asset=Assets.AEG099_060_9002,
        enemy_block_distance=5.0,
    )
    Event_13002500()

    # MALIKETH, THE BLACK BLADE
    # TODO: Clone event instances. Harder to find free event IDs here.
    MalikethDies()
    MalikethBattleTrigger()
    MalikethPhaseTwoTransition(
        0,
        maliketh_phase_one=Characters.MalikethPhaseOne,
        maliketh_phase_two=Characters.MalikethPhaseTwo,
        boss_name=NameText.MalikethTheBlackBlade,
        bar_slot=1,
    )
    MalikethPhaseTwoTransition(
        1,
        maliketh_phase_one=Characters.CLONE_MalikethPhaseOne,
        maliketh_phase_two=Characters.CLONE_MalikethPhaseTwo,
        boss_name=NameText.CLONE_MalikethTheBlackBlade,
        bar_slot=0,
    )
    MalikethCommonEvents()
    # SetMalikethPhaseTwoEventPoint()  # TODO: weird buggy/useless event that will keep restarting
    MalikethEntersSpecialRegions(
        0, maliketh=Characters.MalikethPhaseTwo, in_regions_flag=Flags.MalikethInSpecialRegions
    )
    MalikethEntersSpecialRegions(
        1, maliketh=Characters.CLONE_MalikethPhaseTwo, in_regions_flag=Flags.CLONE_MalikethInSpecialRegions
    )
    MalikethLeavesSpecialRegions(
        0, maliketh=Characters.MalikethPhaseTwo, in_regions_flag=Flags.MalikethInSpecialRegions
    )
    MalikethLeavesSpecialRegions(
        1, maliketh=Characters.CLONE_MalikethPhaseTwo, in_regions_flag=Flags.CLONE_MalikethInSpecialRegions
    )
    MoveMalikethPhaseTwo(0, maliketh=Characters.MalikethPhaseTwo)
    MoveMalikethPhaseTwo(1, maliketh=Characters.CLONE_MalikethPhaseTwo)

    # DRAGONLORD PLACIDUSAX
    DragonlordPlacidusaxDies()
    PlayerTravelsToDragonlord()
    DragonlordPlacidusaxBattleTrigger()
    DragonlordPlacidusaxPhaseTwoTransition()
    DragonlordPlacidusaxCameraControl()
    DragonlordPlacidusaxCommonEvents()

    # GODSKIN DUO (now QUARTET)
    GodskinDuoDies()
    StopGodskinDuoRespawning(  # 13002760
        0,
        godskin_health_pool=Characters.GodskinDuoHealthPool,
        apostle=Characters.GodskinDuoApostle,
        noble=Characters.GodskinDuoNoble,
        stop_respawning_flag=Flags.StopGodskinDuoRespawning,
    )
    StopGodskinDuoRespawning(  # 13002761
        1,
        godskin_health_pool=Characters.CLONE_GodskinDuoHealthPool,
        apostle=Characters.CLONE_GodskinDuoApostle,
        noble=Characters.CLONE_GodskinDuoNoble,
        stop_respawning_flag=Flags.CLONE_StopGodskinDuoRespawning,
    )
    GodskinDuoBattleTrigger()
    GodskinDuoPhaseTwoTransition()
    GodskinDuoCommonEvents()
    FirstGodskinDies(
        0,
        solo_godskin_flag=Flags.NobleSoloFlag,
        dead_godskin=Characters.GodskinDuoApostle,
        remaining_godskin=Characters.GodskinDuoNoble,
        remaining_godskin_special_effect=Effects.GodskinNobleSolo,
    )
    GodskinRespawns(
        0,
        solo_godskin_flag=Flags.NobleSoloFlag,
        spawner=Spawners.ApostleSpawner,
        remaining_godskin=Characters.GodskinDuoNoble,
        revival_special_effect=Effects.GodskinNobleRevivingApostle,
        respawned_godskin=Characters.GodskinDuoApostle,
        respawned_flag=Flags.GodskinApostleHasRespawned,
    )
    FirstGodskinDies(
        1,
        solo_godskin_flag=Flags.ApostleSoloFlag,
        dead_godskin=Characters.GodskinDuoNoble,
        remaining_godskin=Characters.GodskinDuoApostle,
        remaining_godskin_special_effect=Effects.GodskinApostleSolo,
    )
    GodskinRespawns(
        1,
        solo_godskin_flag=Flags.ApostleSoloFlag,
        spawner=Spawners.NobleSpawner,
        remaining_godskin=Characters.GodskinDuoApostle,
        revival_special_effect=Effects.GodskinApostleRevivingNoble,
        respawned_godskin=Characters.GodskinDuoNoble,
        respawned_flag=Flags.GodskinNobleHasRespawned,
    )
    RespawnRandomGodskinDuoMember(
        0,
        apostle=Characters.GodskinDuoApostle,
        noble=Characters.GodskinDuoNoble,
        apostle_spawner=Spawners.ApostleSpawner,
        noble_spawner=Spawners.NobleSpawner,
        apostle_respawned_flag=Flags.GodskinApostleHasRespawned,
        noble_respawned_flag=Flags.GodskinNobleHasRespawned,
        random_flag_1=Flags.RandomApostleFlag,
        random_flag_2=Flags.RandomNobleFlag,
    )
    RespawnRandomGodskinDuoMember(
        0,
        apostle=Characters.GodskinDuoApostle,
        noble=Characters.GodskinDuoNoble,
        apostle_spawner=Spawners.ApostleSpawner,
        noble_spawner=Spawners.NobleSpawner,
        apostle_respawned_flag=Flags.GodskinApostleHasRespawned,
        noble_respawned_flag=Flags.GodskinNobleHasRespawned,
        random_flag_1=Flags.RandomApostleFlag,
        random_flag_2=Flags.RandomNobleFlag,
    )

    # CLONE RESPAWNING
    FirstGodskinDies(  # 13002895
        5,
        solo_godskin_flag=Flags.CLONE_NobleSoloFlag,
        dead_godskin=Characters.CLONE_GodskinDuoApostle,
        remaining_godskin=Characters.CLONE_GodskinDuoNoble,
        remaining_godskin_special_effect=Effects.GodskinNobleSolo,
    )
    GodskinRespawns(  # 13002896
        5,
        solo_godskin_flag=Flags.CLONE_NobleSoloFlag,
        spawner=Spawners.CLONE_ApostleSpawner,
        remaining_godskin=Characters.CLONE_GodskinDuoNoble,
        revival_special_effect=Effects.GodskinNobleRevivingApostle,
        respawned_godskin=Characters.CLONE_GodskinDuoApostle,
        respawned_flag=Flags.GodskinApostleHasRespawned,
    )
    FirstGodskinDies(  # 13002896 (repeat doesn't matter)
        6,
        solo_godskin_flag=Flags.CLONE_ApostleSoloFlag,
        dead_godskin=Characters.CLONE_GodskinDuoNoble,
        remaining_godskin=Characters.CLONE_GodskinDuoApostle,
        remaining_godskin_special_effect=Effects.GodskinApostleSolo,
    )
    GodskinRespawns(  # 13002897
        6,
        solo_godskin_flag=Flags.CLONE_ApostleSoloFlag,
        spawner=Spawners.CLONE_NobleSpawner,
        remaining_godskin=Characters.CLONE_GodskinDuoApostle,
        revival_special_effect=Effects.GodskinApostleRevivingNoble,
        respawned_godskin=Characters.CLONE_GodskinDuoNoble,
        respawned_flag=Flags.GodskinNobleHasRespawned,
    )
    RespawnRandomGodskinDuoMember(  # 13002893
        1,
        apostle=Characters.CLONE_GodskinDuoApostle,
        noble=Characters.CLONE_GodskinDuoNoble,
        apostle_spawner=Spawners.CLONE_ApostleSpawner,
        noble_spawner=Spawners.CLONE_NobleSpawner,
        apostle_respawned_flag=Flags.GodskinApostleHasRespawned,
        noble_respawned_flag=Flags.GodskinNobleHasRespawned,
        random_flag_1=Flags.CLONE_RandomApostleFlag,
        random_flag_2=Flags.CLONE_RandomNobleFlag,
    )

    Event_13002236(0, region=13002314, character=Characters.BeastmanofFarumAzula29)
    CommonFunc_NonRespawningWithReward(
        0, dead_flag=13000340, character=13000340, item_lot=40770, reward_delay=0.0, skip_reward=0, clone=0,
    )
    CommonFunc_NonRespawningWithReward(
        0, dead_flag=13000341, character=Characters.Scarab, item_lot=40772, reward_delay=0.0, skip_reward=0,
        clone=0,
    )
    CommonFunc_NonRespawningWithReward(
        0, dead_flag=13000342, character=13000342, item_lot=40774, reward_delay=0.0, skip_reward=0, clone=0,
    )
    CommonFunc_NonRespawningWithReward(
        0, dead_flag=13000343, character=13000343, item_lot=40776, reward_delay=0.0, skip_reward=0, clone=0,
    )
    CommonFunc_NonRespawningWithReward(
        0, dead_flag=13000369, character=Characters.WormfaceLarge, item_lot=0, reward_delay=0.0, skip_reward=0,
        clone=Characters.CLONE_WormfaceLarge,
    )
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=13000490,
        character=Characters.AncientDragonUpperCurve,
        item_lot=13002091,
        reward_delay=0.0,
        skip_reward=0,
        clone=Characters.CLONE_AncientDragonUpperCurve,
    )
    ApplyAncientDragonEffect(0, dragon=Characters.AncientDragonUpperCurve, region=13002641, region_1=13002640)
    ApplyAncientDragonEffect(1, dragon=Characters.CLONE_AncientDragonUpperCurve, region=13002641, region_1=13002640)

    AncientDragonVanishes(
        0, dead_flag=13000492, do_not_vanish_region=13002492, dragon=Characters.AncientDragonRespawning, delay=10.0
    )

    CommonFunc_NonRespawningWithReward(
        0, dead_flag=13000494, character=Characters.AncientDragonSidePlatform, item_lot=0, reward_delay=0.0,
        skip_reward=0,
        clone=Characters.CLONE_AncientDragonSidePlatform,
    )
    ApplyAncientDragonEffect(2, dragon=Characters.AncientDragonSidePlatform, region=13002645, region_1=13002494)
    ApplyAncientDragonEffect(3, dragon=Characters.CLONE_AncientDragonSidePlatform, region=13002645, region_1=13002494)
    AncientDragonVanishes(
        1, dead_flag=13000494, do_not_vanish_region=13002646, dragon=Characters.AncientDragonSidePlatform, delay=10.0
    )

    AncientDragonLowerLightning(0, dragon=Characters.AncientDragonLowerPlatform)
    AncientDragonLowerLightning(1, dragon=Characters.CLONE_AncientDragonLowerPlatform)
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=Flags.AncientDragonLowerPlatformDead,
        character=Characters.AncientDragonLowerPlatform,
        item_lot=13002093,
        reward_delay=0.0,
        skip_reward=0,
        clone=Characters.CLONE_AncientDragonLowerPlatform,
    )
    AncientDragonVanishes(
        2, dead_flag=Flags.AncientDragonLowerPlatformDead, do_not_vanish_region=13002495,
        dragon=Characters.AncientDragonLowerPlatform, delay=1.0
    )
    CommonFunc_NonRespawningWithReward(
        0, dead_flag=13000701, character=Characters.AncientDragon4, item_lot=0, reward_delay=0.0, skip_reward=0,
        clone=0,
    )
    CommonFunc_NonRespawningWithReward(
        0, dead_flag=13000702, character=Characters.AncientDragon5, item_lot=0, reward_delay=0.0, skip_reward=0,
        clone=0,
    )
    ApplyAncientDragonEffect(4, dragon=Characters.AncientDragon5, region=13002497, region_1=13002493)  # no clone

    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=13000295,
        character=Characters.CrucibleKnight0,
        item_lot=0,
        reward_delay=0.0,
        skip_reward=0,
        clone=Characters.CLONE_CrucibleKnight0,
    )
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=13000296,
        character=Characters.CrucibleKnight1,
        item_lot=0,
        reward_delay=0.0,
        skip_reward=0,
        clone=Characters.CLONE_CrucibleKnight1,
    )
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=13000496,
        character=Characters.DraconicTreeSentinel,
        item_lot=13002095,
        reward_delay=2.0,
        skip_reward=0,
        clone=Characters.CLONE_DraconicTreeSentinel,
    )
    Event_13002580()
    Event_13002510()
    CommonFunc_90005501(
        0,
        flag=13000510,
        flag_1=13000511,
        left=0,
        asset=Assets.AEG247_002_0500,
        asset_1=Assets.AEG247_003_0500,
        asset_2=Assets.AEG247_003_0501,
        flag_2=13000512,
    )
    CommonFunc_90005501(
        0,
        flag=13000515,
        flag_1=13000516,
        left=0,
        asset=Assets.AEG247_045_0500,
        asset_1=Assets.AEG247_003_0505,
        asset_2=Assets.AEG247_003_0504,
        flag_2=13000517,
    )
    CommonFunc_90005501(
        0,
        flag=13000520,
        flag_1=13000521,
        left=0,
        asset=Assets.AEG247_004_0500,
        asset_1=Assets.AEG247_003_0502,
        asset_2=Assets.AEG247_003_0503,
        flag_2=13000522,
    )
    CommonFunc_90005501(
        0,
        flag=13000525,
        flag_1=13000526,
        left=1,
        asset=Assets.AEG247_005_0501,
        asset_1=Assets.AEG247_003_0506,
        asset_2=Assets.AEG247_003_0507,
        flag_2=13000527,
    )
    CommonFunc_90005501(
        0,
        flag=13000530,
        flag_1=13000531,
        left=2,
        asset=Assets.AEG247_005_0502,
        asset_1=Assets.AEG247_003_0509,
        asset_2=Assets.AEG247_003_0508,
        flag_2=13000532,
    )
    Event_13002600(0, entity=Characters.Dummy0, region=13002600, anchor_entity=13002120, seconds=0.0)
    Event_13002600(1, entity=Characters.Dummy0, region=13002600, anchor_entity=13002121, seconds=1.0)
    Event_13002600(2, entity=Characters.Dummy0, region=13002600, anchor_entity=13002122, seconds=3.0)
    Event_13002600(3, entity=Characters.Dummy0, region=13002600, anchor_entity=13002123, seconds=5.0)
    Event_13002600(4, entity=Characters.Dummy0, region=13002600, anchor_entity=13002124, seconds=6.0)
    Event_13002600(5, entity=Characters.Dummy0, region=13002600, anchor_entity=13002125, seconds=9.0)
    Event_13002600(6, entity=Characters.Dummy0, region=13002600, anchor_entity=13002126, seconds=1.0)
    Event_13002600(7, entity=Characters.Dummy0, region=13002600, anchor_entity=13002127, seconds=2.5)
    Event_13002600(8, entity=Characters.Dummy0, region=13002600, anchor_entity=13002128, seconds=7.0)
    CommonFunc_90005620(
        0,
        flag=13000570,
        asset=Assets.AEG027_078_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=Assets.AEG027_217_9000,
        left_flag=13002570,
        cancel_flag__right_flag=13002571,
        right=13002572,
    )
    CommonFunc_90005621(0, flag=13000570, asset=Assets.AEG099_270_9000)
    CommonFunc_90005780(
        0,
        flag=Flags.GodskinDuoDead,
        summon_flag=13002160,
        dismissal_flag=13002161,
        character=Characters.RecusantBernahl1,
        sign_type=20,
        region=13002721,
        right=13002720,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(
        0, flag=Flags.GodskinDuoDead, flag_1=13002160, flag_2=13002161, character=Characters.RecusantBernahl1
    )
    Event_13002859()
    CommonFunc_90005780(
        0,
        flag=Flags.GodskinDuoDead,
        summon_flag=13002164,
        dismissal_flag=13002165,
        character=Characters.RecusantBernahl2,
        sign_type=20,
        region=13002726,
        right=13002721,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(
        0, flag=Flags.GodskinDuoDead, flag_1=13002164, flag_2=13002165, character=Characters.RecusantBernahl2
    )
    CommonFunc_90005782(
        0,
        flag=13002164,
        region=13002855,
        character=Characters.RecusantBernahl2,
        target_entity=13002853,
        region_1=13002869,
        animation=0,
    )
    CommonFunc_NPCInvaderSummonSign(
        0,
        right=0,
        dead_flag=13000180,
        summon_flag=13002181,
        dismissal_flag=13002182,
        character=Characters.RecusantBernahl0,
        sign_type=22,
        region=13002180,
        region_1=13002181,
        seconds=0.0,
        right_1=13009300,
        unknown=0,
        right_2=0,
    )
    CommonFunc_NPCInvaderAppearance(0, dead_flag=13000180, summon_flag=13002181, dismissal_flag=13002182, npc=Characters.RecusantBernahl0)
    CommonFunc_NPCInvaderDies(
        0,
        dead_flag=13000180,
        summon_flag=13002181,
        dismissal_flag=13002182,
        npc=Characters.RecusantBernahl0,
        item_lot=102920,
        seconds=0.0,
    )
    RunCommonEvent(
        13002660,
        slot=0,
        args=(13000180, 13002181, 13002182, 13000710, 13002180, 13002183, 0),
        arg_types="IIIIIIi",
    )
    Event_13003700()
    CommonFunc_90005704(0, attacked_entity=Characters.Alexander, flag=13009256, flag_1=3660, flag_2=13009251, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Alexander,
        flag=3661,
        flag_1=3662,
        flag_2=13009251,
        flag_3=13009256,
        first_flag=3660,
        last_flag=3663,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Alexander, flag=3663, first_flag=3660, last_flag=3663)
    Event_13003710(0, character=Characters.Alexander)
    Event_13003711(0, character=Characters.Alexander)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9009,
        action_button_id=4110,
        item_lot=101740,
        first_flag=400174,
        last_flag=400174,
        flag=13009254,
        model_point=0,
    )
    Event_13003720()
    Event_13003721()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_13000519()
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.BeastmanofFarumAzula0,
        inactive_animation=30003,
        active_animation=20003,
        radius=2.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.BeastmanofFarumAzula1,
        inactive_animation=30003,
        active_animation=20003,
        radius=2.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.BeastmanofFarumAzula2,
        inactive_animation=30003,
        active_animation=20003,
        radius=2.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.BeastmanofFarumAzula35,
        inactive_animation=30003,
        active_animation=20003,
        radius=2.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.BeastmanofFarumAzula3,
        region=13002203,
        radius=20.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula4, region=13002201, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula33, region=13002201, seconds=3.5, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula15, region=13002217, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BeastmanofFarumAzula16,
        inactive_animation=30004,
        active_animation=20004,
        trigger_region=13002217,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.BeastmanofFarumAzula5,
        region=13002205,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.BeastmanofFarumAzula7,
        region=13002209,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.BeastmanofFarumAzula6,
        animation_id=30003,
        animation_id_1=20003,
        region=13002207,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula8, region=13002210, seconds=0.0, animation_id=3001
    )
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.BeastmanofFarumAzula8, radius=3.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula9, region=13002207, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula10, region=13002207, seconds=1.0, animation_id=-1
    )
    CommonFunc_90005271(0, character=Characters.BeastmanofFarumAzula10, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula11, region=13002212, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula12, region=13002215, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula13, region=13002215, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula14, region=13002215, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula17, region=13002214, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula34, region=13002214, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula18, region=13002220, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula19, region=13002222, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula20, region=13002223, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.BeastmanofFarumAzula21,
        region=13002225,
        radius=20.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionAndRadius(
        0,
        character=Characters.BeastmanofFarumAzula22,
        animation_id=30004,
        animation_id_1=20004,
        region=13002227,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula23, region=13002228, seconds=0.0, animation_id=3002
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula24, region=13002230, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BeastmanofFarumAzula25,
        inactive_animation=30004,
        active_animation=20004,
        trigger_region=13002231,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula26, region=13002230, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula28, region=13002234, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BeastmanofFarumAzula27,
        inactive_animation=30003,
        active_animation=20003,
        trigger_region=13002233,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.BeastmanofFarumAzula29,
        region=13002235,
        radius=20.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.BeastmanofFarumAzula30, radius=5.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.BeastmanofFarumAzula31,
        inactive_animation=30004,
        active_animation=20004,
        radius=5.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula32, region=13002245, seconds=0.0, animation_id=-1
    )
    CommonFunc_90005221(
        0,
        character=Characters.BeastmanofFarumAzula39,
        animation_id=30004,
        animation_id_1=20004,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.BeastmanofFarumAzula40,
        animation_id=30004,
        animation_id_1=20004,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.BeastmanofFarumAzula41,
        animation_id=30004,
        animation_id_1=20004,
        seconds=0.0,
        left=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BeastmanofFarumAzula42,
        inactive_animation=30004,
        active_animation=20004,
        trigger_region=13002269,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.BeastmanofFarumAzula43, radius=40.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula36, region=13002296, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula37, region=13002296, seconds=1.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula38, region=13002296, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.BeastmanofFarumAzula47,
        region=13002278,
        radius=30.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula44, region=13002277, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula45, region=13002277, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BeastmanofFarumAzula46, region=13002277, seconds=0.0, animation_id=-1
    )
    CommonFunc_90005221(
        0,
        character=Characters.BeastmanofFarumAzula48,
        animation_id=30004,
        animation_id_1=20004,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.BeastmanofFarumAzula49,
        animation_id=30004,
        animation_id_1=20004,
        seconds=0.0,
        left=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BeastmanofFarumAzula50,
        inactive_animation=30004,
        active_animation=20004,
        trigger_region=13002289,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BeastmanofFarumAzula51,
        inactive_animation=30004,
        active_animation=20004,
        trigger_region=13002289,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BeastmanofFarumAzula52,
        inactive_animation=30004,
        active_animation=20004,
        trigger_region=13002289,
        trigger_delay=0.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.Skeleton5, region=13002412, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.Skeleton7, region=13002412, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.Skeleton0, region=13002412, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.Skeleton4, region=13002408, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Skeleton2,
        inactive_animation=30017,
        active_animation=20017,
        trigger_region=13002412,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Skeleton3,
        inactive_animation=30017,
        active_animation=20017,
        trigger_region=13002412,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.Skeleton8, region=13002416, seconds=0.0, animation_id=3014
    )
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Skeleton9, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=13000418, region=13002418, seconds=0.0, animation_id=3003)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=13000419, region=13002418, seconds=0.5, animation_id=3003)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0, character=Characters.Skeleton10, region=13002420, radius=10.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Skeleton11,
        inactive_animation=30018,
        active_animation=20018,
        trigger_region=13002421,
        trigger_delay=5.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Skeleton12,
        inactive_animation=30018,
        active_animation=20018,
        trigger_region=13002421,
        trigger_delay=7.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Skeleton13,
        inactive_animation=30018,
        active_animation=20018,
        trigger_region=13002421,
        trigger_delay=8.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Skeleton14,
        inactive_animation=30017,
        active_animation=20017,
        trigger_region=13002435,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.Skeleton15, region=13002435, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Skeleton17,
        inactive_animation=30017,
        active_animation=20017,
        trigger_region=13002446,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Skeleton22,
        inactive_animation=30014,
        active_animation=20014,
        trigger_region=13002446,
        trigger_delay=3.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Skeleton23,
        inactive_animation=30014,
        active_animation=20014,
        trigger_region=13002446,
        trigger_delay=1.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0, character=Characters.Dummy1, region=13002323, radius=35.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0, character=Characters.Dummy2, region=13002323, radius=35.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Skeleton24,
        inactive_animation=30017,
        active_animation=20017,
        trigger_region=13002456,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Skeleton25,
        inactive_animation=30018,
        active_animation=20018,
        trigger_region=13002459,
        trigger_delay=1.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Skeleton26,
        inactive_animation=30018,
        active_animation=20018,
        trigger_region=13002459,
        trigger_delay=2.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Skeleton27,
        animation_id=30018,
        animation_id_1=20018,
        seconds=0.0,
        left=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Skeleton29,
        inactive_animation=30018,
        active_animation=20018,
        trigger_region=13002459,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Skeleton32,
        animation_id=30018,
        animation_id_1=20018,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Skeleton33,
        animation_id=30018,
        animation_id_1=20018,
        seconds=0.0,
        left=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Skeleton30,
        inactive_animation=30018,
        active_animation=20018,
        trigger_region=13002463,
        trigger_delay=3.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Skeleton31,
        inactive_animation=30018,
        active_animation=20018,
        trigger_region=13002463,
        trigger_delay=4.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Skeleton34,
        animation_id=30018,
        animation_id_1=20018,
        seconds=0.0,
        left=0,
    )
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Skeleton28, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.UndeadAzulaBeastman1, region=13002481, seconds=0.0, animation_id=3003
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.UndeadAzulaBeastman2, region=13002418, seconds=0.5, animation_id=3003
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.UndeadAzulaBeastman3,
        inactive_animation=30017,
        active_animation=20017,
        trigger_region=13002435,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.UndeadAzulaBeastman5,
        inactive_animation=30017,
        active_animation=20017,
        trigger_region=13002435,
        trigger_delay=3.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.UndeadAzulaBeastman6,
        inactive_animation=30017,
        active_animation=20017,
        trigger_region=13002488,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.UndeadAzulaBeastman7,
        region=13002488,
        radius=2.0,
        seconds=0.5,
        animation_id=-1,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.FarumAzulaDog2_0,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=13002300,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.FarumAzulaDog2_1,
        inactive_animation=30000,
        active_animation=20000,
        radius=10.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.FarumAzulaDog2_2,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=13002311,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.FarumAzulaDog2_3,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=13002311,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.FarumAzulaDog2_4,
        region=13002314,
        radius=20.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.FarumAzulaDog2_5,
        inactive_animation=30000,
        active_animation=20000,
        radius=20.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.FarumAzulaDog2_5,
        inactive_animation=30000,
        active_animation=20000,
        radius=15.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.FarumAzulaDog2_6,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=13002456,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=13000330, region=13002355, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=13000331, region=13002355, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BladedTalonEagle0,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=13002350,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BladedTalonEagle1,
        inactive_animation=30000,
        active_animation=3009,
        trigger_region=13002350,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BladedTalonEagle2, region=13002352, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BladedTalonEagle2,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=13002352,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BladedTalonEagle3,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=13002355,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BladedTalonEagle4,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=13002355,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionAndRadius(
        0,
        character=Characters.BladedTalonEagle5,
        animation_id=30000,
        animation_id_1=20000,
        region=13002356,
        radius=9.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionAndRadius(
        0,
        character=Characters.BladedTalonEagle6,
        animation_id=30000,
        animation_id_1=20000,
        region=13002356,
        radius=9.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionAndRadius(
        0,
        character=Characters.BladedTalonEagle7,
        animation_id=30000,
        animation_id_1=20000,
        region=13002356,
        radius=9.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BladedTalonEagle8,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=13002356,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BladedTalonEagle9,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=13002356,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BladedTalonEagle10,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=13002362,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BladedTalonEagle11,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=13002362,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BladedTalonEagle12,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=13002362,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.BladedTalonEagle13,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=13002365,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.BladedTalonEagle14,
        inactive_animation=30000,
        active_animation=20000,
        radius=1.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BanishedKnight0, region=13002381, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BanishedKnight1, region=13002382, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BanishedKnight2, region=13002384, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.BanishedKnight3, radius=10.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=13000380, region=13002380, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=13000383, region=13002380, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BanishedKnight8, region=13002390, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRadius(
        0, character=Characters.BanishedKnight4, radius=55.0, seconds=6.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BanishedKnight6, region=13002388, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BanishedKnight7, region=13002389, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BanishedKnight10, region=13002392, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BanishedKnight11, region=13002395, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=13000396, region=13002396, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.BanishedKnight13, region=13002398, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Wormface1,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=13002372,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Wormface2,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=13002372,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Wormface3,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=13002300,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Wormface6,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=13002372,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0, character=Characters.Wormface4, region=13002374, radius=3.0, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Wormface5,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=13002375,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.Wormface7, region=13002377, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Wormface8,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=13002369,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Wormface9,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=13002369,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.WormfaceLarge,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=13002369,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.AncientDragonUpperCurve,
        inactive_animation=30019,
        active_animation=20019,
        trigger_region=13002490,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.AncientDragonSidePlatform,
        inactive_animation=30019,
        active_animation=20019,
        trigger_region=13002494,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.AncientDragonLowerPlatform, region=13002495, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.AncientDragon5,
        inactive_animation=30010,
        active_animation=20010,
        trigger_region=13002498,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.CrucibleKnight0, region=13002295, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegion(
        0, character=Characters.CrucibleKnight1, region=13002296, seconds=0.0, animation_id=-1
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, 13000496, 13002496, 40.0, 0.0, -1)


@ContinueOnRest(13002500)
def Event_13002500():
    """Event 13002500"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(13000500):
        return
    AND_1.Add(InsideMap(game_map=CRUMBLING_FARUM_AZULA))
    AND_1.Add(FlagEnabled(110))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=13002502))

    MAIN.Await(AND_1)

    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(9000))

    MAIN.Await(AND_2)

    EnableFlag(13000500)
    AddSpecialEffect(PLAYER, 4281)
    AddSpecialEffect(PLAYER, 4283)


@RestartOnRest(13002580)
def Event_13002580():
    """Event 13002580"""
    RegisterLadder(start_climbing_flag=13000580, stop_climbing_flag=13000581, asset=Assets.AEG247_001_0500)
    RegisterLadder(start_climbing_flag=13000582, stop_climbing_flag=13000583, asset=Assets.AEG247_000_0500)
    RegisterLadder(start_climbing_flag=13000584, stop_climbing_flag=13000585, asset=Assets.AEG247_008_0500)
    RegisterLadder(start_climbing_flag=13000586, stop_climbing_flag=13000587, asset=Assets.AEG247_006_0500)
    RegisterLadder(start_climbing_flag=13000588, stop_climbing_flag=13000589, asset=Assets.AEG247_007_0500)
    RegisterLadder(start_climbing_flag=13000590, stop_climbing_flag=13000591, asset=Assets.AEG247_011_0500)


@ContinueOnRest(13002510)
def Event_13002510():
    """Event 13002510"""
    CommonFunc_90005500(
        0,
        flag=13000510,
        flag_1=13000511,
        left=0,
        asset=Assets.AEG247_002_0500,
        asset_1=Assets.AEG247_003_0500,
        obj_act_id=13003511,
        asset_2=Assets.AEG247_003_0501,
        obj_act_id_1=13003512,
        region=13002511,
        region_1=13002512,
        flag_2=13000512,
        flag_3=13000513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=13000515,
        flag_1=13000516,
        left=0,
        asset=Assets.AEG247_045_0500,
        asset_1=Assets.AEG247_003_0505,
        obj_act_id=13003516,
        asset_2=Assets.AEG247_003_0504,
        obj_act_id_1=13003517,
        region=13002516,
        region_1=13002517,
        flag_2=13000517,
        flag_3=13000518,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=13000520,
        flag_1=13000521,
        left=0,
        asset=Assets.AEG247_004_0500,
        asset_1=Assets.AEG247_003_0502,
        obj_act_id=13003521,
        asset_2=Assets.AEG247_003_0503,
        obj_act_id_1=13003522,
        region=13002521,
        region_1=13002522,
        flag_2=13000522,
        flag_3=13000523,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=13000525,
        flag_1=13000526,
        left=1,
        asset=Assets.AEG247_005_0501,
        asset_1=Assets.AEG247_003_0506,
        obj_act_id=13003526,
        asset_2=Assets.AEG247_003_0507,
        obj_act_id_1=13003527,
        region=13002526,
        region_1=13002527,
        flag_2=13000527,
        flag_3=13000528,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        13000530,
        13000531,
        2,
        13001530,
        13001531,
        13003531,
        13001532,
        13003532,
        13002531,
        13002532,
        13000532,
        13000533,
        0,
    )


@ContinueOnRest(13000519)
def Event_13000519():
    """Event 13000519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(13000510)
    EnableThisSlotFlag()


@RestartOnRest(13002236)
def Event_13002236(_, region: uint, character: uint):
    """Event 13002236"""
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))

    MAIN.Await(AND_1)

    ClearTargetList(character)
    Restart()


@RestartOnRest(13002490)
def Event_13002490(_, character: uint, region: uint, animation_id: int, flag: uint):
    """Event 13002490"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableAnimations(character)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))

    MAIN.Await(AND_1)

    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, animation_id)


@RestartOnRest(13002493)
def ApplyAncientDragonEffect(_, dragon: uint, region: uint, region_1: uint):
    """Event 13002493"""
    RemoveSpecialEffect(dragon, 18941)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterInsideRegion(character=dragon, region=region_1))

    MAIN.Await(AND_1)

    AddSpecialEffect(dragon, 18941)
    Wait(4.0)
    Restart()


@RestartOnRest(13002646)
def AncientDragonVanishes(_, dead_flag: uint, do_not_vanish_region: uint, dragon: uint, delay: float):
    """Event 13002646"""
    if FlagEnabled(dead_flag):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=do_not_vanish_region))
    AND_1.Add(HasAIStatus(dragon, ai_status=AIStatusType.Battle))

    MAIN.Await(AND_1)

    Wait(delay)
    ForceAnimation(dragon, 20001)
    Wait(6.0)
    DisableCharacter(dragon)
    EnableThisSlotFlag()


@RestartOnRest(13002660)
def Event_13002660(
    _,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    character: uint,
    other_entity: uint,
    region: uint,
    left: int,
):
    """Event 13002660"""
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(FlagEnabled(flag_1))
    if UnsignedEqual(left=region, right=0):
        AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=110.0))
    else:
        AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_3.Add(FlagEnabled(flag_1))
    SkipLinesIfValueEqual(5, left=left, right=2)
    SkipLinesIfValueEqual(2, left=left, right=1)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=180.0))
    SkipLines(3)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=360.0))
    SkipLines(1)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=720.0))
    OR_10.Add(AND_1)
    OR_10.Add(AND_2)
    OR_10.Add(AND_3)

    MAIN.Await(OR_10)

    if FlagEnabled(flag):
        return
    SendNPCSummonHome(character=character)
    End()
    OR_11.Add(FlagDisabled(flag_2))


@RestartOnRest(13002800)
def MalikethDies():
    """Event 13002800"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.MalikethDead)
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L1, flag=118)
    End()

    # --- Label 0 --- #
    DefineLabel(0)

    # TODO: Maliketh's death dialogue should only play when BOTH die.
    AND_1.Add(HealthValue(Characters.MalikethPhaseTwo) <= 0)
    AND_1.Add(HealthValue(Characters.CLONE_MalikethPhaseTwo) <= 0)
    MAIN.Await(AND_1)

    Kill(Characters.MalikethPhaseOne)
    Kill(Characters.CLONE_MalikethPhaseOne)
    Kill(Characters.MalikethPhaseTwo)
    Kill(Characters.CLONE_MalikethPhaseTwo)
    Wait(4.0)
    PlaySoundEffect(13008000, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(Characters.MalikethPhaseTwo))
    AND_2.Add(CharacterDead(Characters.CLONE_MalikethPhaseTwo))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(Flags.MalikethDead))

    MAIN.Await(OR_2)

    SetBackreadStateAlternate(Characters.MalikethPhaseTwo, True)
    SetBackreadStateAlternate(Characters.CLONE_MalikethPhaseTwo, True)
    KillBossAndDisplayBanner(character=Characters.MalikethPhaseTwo, banner_type=BannerType.LegendFelled)
    EnableNetworkFlag(Flags.MalikethDead)
    EnableFlag(9116)
    if PlayerInOwnWorld():
        EnableFlag(61116)
    if PlayerNotInOwnWorld():
        return
    if PlayerInOwnWorld():
        return


@RestartOnRest(13002805)
def ControlMalikethGrace():
    """Event 13002805"""
    GotoIfFlagEnabled(Label.L0, flag=Flags.MalikethDead)
    DisableCharacter(Characters.TalkDummy0)
    DisableAsset(Assets.AEG099_060_9000)
    Wait(1.0)

    MAIN.Await(FlagEnabled(Flags.MalikethDead))

    Wait(4.0)
    Wait(7.800000190734863)
    CreateTemporaryVFX(
        vfx_id=1060,
        anchor_entity=Assets.AEG099_060_9000,
        model_point=200,
        anchor_type=CoordEntityType.Asset,
    )
    Wait(0.5)
    EnableCharacter(Characters.TalkDummy0)
    EnableAsset(Assets.AEG099_060_9000)

    # --- Label 0 --- #
    DefineLabel(0)
    RegisterGrace(grace_flag=13000000, asset=Assets.AEG099_060_9000, reaction_distance=5.0, reaction_angle=180.0)


@RestartOnRest(13002810)
def MalikethBattleTrigger():
    """Event 13002810"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.MalikethDead)
    DisableCharacter(Characters.MalikethPhaseTwo)
    DisableCharacter(Characters.MalikethPhaseOne)
    DisableAnimations(Characters.MalikethPhaseTwo)
    DisableAnimations(Characters.MalikethPhaseOne)
    Kill(Characters.MalikethPhaseTwo)
    Kill(Characters.MalikethPhaseOne)
    DisableCharacter(Characters.CLONE_MalikethPhaseTwo)
    DisableCharacter(Characters.CLONE_MalikethPhaseOne)
    DisableAnimations(Characters.CLONE_MalikethPhaseTwo)
    DisableAnimations(Characters.CLONE_MalikethPhaseOne)
    Kill(Characters.CLONE_MalikethPhaseTwo)
    Kill(Characters.CLONE_MalikethPhaseOne)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.MalikethPhaseOne)
    DisableAI(Characters.MalikethPhaseTwo)
    DisableHealthBar(Characters.MalikethPhaseTwo)
    DisableCharacter(Characters.MalikethPhaseTwo)
    DisableGravity(Characters.MalikethPhaseTwo)
    DisableAnimations(Characters.MalikethPhaseTwo)

    DisableAI(Characters.CLONE_MalikethPhaseOne)
    DisableAI(Characters.CLONE_MalikethPhaseTwo)
    DisableHealthBar(Characters.CLONE_MalikethPhaseTwo)
    DisableCharacter(Characters.CLONE_MalikethPhaseTwo)
    DisableGravity(Characters.CLONE_MalikethPhaseTwo)
    DisableAnimations(Characters.CLONE_MalikethPhaseTwo)

    GotoIfFlagEnabled(Label.L1, flag=Flags.MalikethFirstTimeDone)

    ForceAnimation(Characters.MalikethPhaseOne, 30018, loop=True)
    ForceAnimation(Characters.CLONE_MalikethPhaseOne, 30018, loop=True)
    AND_1.Add(FlagEnabled(13002805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=13002800))

    MAIN.Await(AND_1)

    Wait(3.0)
    ForceAnimation(Characters.MalikethPhaseOne, 20038, loop=True)
    ForceAnimation(Characters.CLONE_MalikethPhaseOne, 20038, loop=True)
    EnableNetworkFlag(Flags.MalikethFirstTimeDone)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(13002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=13002800))

    MAIN.Await(AND_2)

    EnableFlag(13002803)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(Characters.MalikethPhaseTwo)
    EnableCharacter(Characters.CLONE_MalikethPhaseTwo)
    ReferDamageToEntity(Characters.MalikethPhaseOne, target_entity=Characters.MalikethPhaseTwo)
    ReferDamageToEntity(Characters.CLONE_MalikethPhaseOne, target_entity=Characters.CLONE_MalikethPhaseTwo)
    EnableAI(Characters.MalikethPhaseOne)
    EnableAI(Characters.CLONE_MalikethPhaseOne)
    SetNetworkUpdateRate(Characters.MalikethPhaseOne, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.MalikethPhaseTwo, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_MalikethPhaseOne, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_MalikethPhaseTwo, is_fixed=True, update_rate=CharacterUpdateRate.Always)

    EnableBossHealthBar(Characters.MalikethPhaseOne, name=NameText.BeastClergyman, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_MalikethPhaseOne, name=NameText.CLONE_BeastClergyman, bar_slot=0)


@RestartOnRest(13002750)  # renumbered for more free slots
def MalikethPhaseTwoTransition(_, maliketh_phase_one: uint, maliketh_phase_two: uint, boss_name: int, bar_slot: short):
    """Separate for each clone."""
    if FlagEnabled(Flags.MalikethDead):
        return
    AND_1.Add(HealthRatio(maliketh_phase_one) <= 0.550000011920929)

    MAIN.Await(AND_1)

    OR_15.Add(HealthValue(PLAYER) <= 0)
    OR_15.Add(CharacterInsideRegion(character=PLAYER, region=13002815))
    if OR_15:
        return
    SetCharacterFadeOnEnable(character=maliketh_phase_two, state=False)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=13000040,
            cutscene_flags=0,
            move_to_region=13002820,
            map_id=13000000,
            player_id=PLAYER,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(13000040, cutscene_flags=0, player_id=PLAYER)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(13002802)
    DisableCharacter(maliketh_phase_one)
    SetNetworkUpdateRate(maliketh_phase_one, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    DisableAI(maliketh_phase_one)
    ForceAnimation(maliketh_phase_two, 20015)
    Move(
        maliketh_phase_two,
        destination=13002825,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=maliketh_phase_two,
    )
    EnableGravity(maliketh_phase_two)
    EnableAnimations(maliketh_phase_two)
    EnableAI(maliketh_phase_two)
    SetNetworkUpdateRate(maliketh_phase_two, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(maliketh_phase_two, name=boss_name, bar_slot=bar_slot)


@RestartOnRest(13002756)  # new ID
def MoveMalikethPhaseTwo(_, maliketh: uint):
    """Event 13002819"""
    MAIN.Await(CharacterHasSpecialEffect(maliketh, 15272))

    Move(
        maliketh,
        destination=13002825,  # TODO: clone and move slightly?
        destination_type=CoordEntityType.Region,
        copy_draw_parent=maliketh,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(13002820)
def SetMalikethPhaseTwoEventPoint():
    """Event 13002820"""
    # TODO: This AND_1 condition isn't even used and flag 13002821 doesn't seem to be enabled anywhere.
    #  In fact, none of these flags are enabled anywhere. Ignoring and disabling this event for now.
    AND_1.Add(HealthRatio(Characters.MalikethPhaseTwo) != 0.0)
    AND_1.Add(FlagEnabled(13002821))
    if FlagEnabled(13002822):
        SetEventPoint(Characters.MalikethPhaseTwo, region=13002810, reaction_range=200.0)
    if FlagEnabled(13002823):
        SetEventPoint(Characters.MalikethPhaseTwo, region=13002811, reaction_range=200.0)
    if FlagEnabled(13002824):
        SetEventPoint(Characters.MalikethPhaseTwo, region=13002812, reaction_range=200.0)
    DisableFlag(13002821)
    Restart()


@RestartOnRest(13002752)  # new ID
def MalikethEntersSpecialRegions(_, maliketh: uint, in_regions_flag: int):
    """Gives effect 15270 to Maliketh when he is in one of three regions."""
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(maliketh, 15270))
    AND_1.Add(FlagDisabled(in_regions_flag))
    OR_1.Add(CharacterInsideRegion(character=maliketh, region=13002840))
    OR_1.Add(CharacterInsideRegion(character=maliketh, region=13002841))
    OR_1.Add(CharacterInsideRegion(character=maliketh, region=13002842))
    AND_1.Add(OR_1)

    MAIN.Await(AND_1)

    AddSpecialEffect(maliketh, 15270)
    EnableFlag(in_regions_flag)
    Restart()


@RestartOnRest(13002754)  # new ID
def MalikethLeavesSpecialRegions(_, maliketh: uint, in_regions_flag: int):
    """Removes effect 15270 from Maliketh once he leaves these three regions (see above)."""
    AND_1.Add(FlagEnabled(in_regions_flag))
    AND_1.Add(CharacterOutsideRegion(character=maliketh, region=13002840))
    AND_1.Add(CharacterOutsideRegion(character=maliketh, region=13002841))
    AND_1.Add(CharacterOutsideRegion(character=maliketh, region=13002842))

    MAIN.Await(AND_1)

    DisableFlag(in_regions_flag)
    Restart()


@RestartOnRest(13002829)
def MalikethCommonEvents():
    """Event 13002829"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.MalikethDead,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=13002800,
        host_entered_fog_flag=13002805,
        boss_characters=13005800,
        action_button_id=10000,
        first_time_done_flag=0,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.MalikethDead,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=13002800,
        host_entered_fog_flag=13002805,
        summon_entered_fog_flag=13002806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(
        0, boss_dead_flag=Flags.MalikethDead, fog_asset=Assets.AEG099_002_9000, model_point=4, required_flag=0
    )
    CommonFunc_ControlBossMusic(0, Flags.MalikethDead, 211000, 13002805, 13002806, 0, 13002802, 1, 1)


@RestartOnRest(13002830)
def DragonlordPlacidusaxDies():
    """Event 13002830"""
    if FlagEnabled(Flags.DragonlodPlacidusaxDead):
        return

    AND_1.Add(HealthValue(Characters.DragonlordPlacidusax) <= 0)
    AND_1.Add(HealthValue(Characters.CLONE_DragonlordPlacidusax) <= 0)
    MAIN.Await(AND_1)

    Kill(Characters.DragonlordPlacidusax)
    Kill(Characters.CLONE_DragonlordPlacidusax)
    Wait(4.0)
    PlaySoundEffect(13008000, 888880000, sound_type=SoundType.s_SFX)

    AND_2.Add(CharacterDead(Characters.DragonlordPlacidusax))
    AND_2.Add(CharacterDead(Characters.CLONE_DragonlordPlacidusax))
    MAIN.Await(AND_2)

    KillBossAndDisplayBanner(character=Characters.DragonlordPlacidusax, banner_type=BannerType.LegendFelled)
    SetWeather(weather=Weather.Default, duration=-1.0, immediate_change=False)
    EnableFlag(Flags.DragonlodPlacidusaxDead)
    EnableFlag(9115)
    if PlayerInOwnWorld():
        EnableFlag(61115)
    if PlayerInOwnWorld():
        EnableFlag(71301)


@RestartOnRest(13002834)
def PlayerTravelsToDragonlord():
    """Event 13002834"""
    if FlagEnabled(Flags.DragonlodPlacidusaxDead):
        return
    GotoIfPlayerInOwnWorld(Label.L0)
    GotoIfFlagDisabled(Label.L0, flag=13002834)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=20000,
        destination_type=CoordEntityType.Region,
        destination=13002836,
        model_point=-1,
        copy_draw_parent=20000,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    ChangeCamera(normal_camera_id=4525, locked_camera_id=4520)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.Invader))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.Invader2))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.Invader3))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    if OR_15:
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9740, entity=Assets.AEG099_090_9006))

    MAIN.Await(AND_1)

    Move(
        PLAYER,
        destination=Assets.AEG099_090_9006,
        destination_type=CoordEntityType.Asset,
        model_point=100,
        short_move=True,
    )
    ForceAnimation(PLAYER, 67010)
    Wait(3.0)
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarpWithWeatherAndTime(
            cutscene_id=13000010,
            cutscene_flags=0,
            move_to_region=13002834,
            map_id=13000000,
            player_id=PLAYER,
            unk_20_24=0,
            unk_24_25=False,
            change_weather=True,
            weather=Weather.FlatClouds,
        )
    else:
        PlayCutsceneToPlayerAndWarpWithWeatherAndTime(
            cutscene_id=13000010,
            cutscene_flags=CutsceneFlags.Unskippable,
            move_to_region=13002836,
            map_id=13000000,
            player_id=PLAYER,
            unk_20_24=0,
            unk_24_25=False,
            change_weather=True,
            weather=Weather.FlatClouds,
        )
    WaitFramesAfterCutscene(frames=1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    ChangeCamera(normal_camera_id=4525, locked_camera_id=4520)


@RestartOnRest(13002835)
def DragonlordPlacidusaxBattleTrigger():
    """Event 13002835"""
    GotoIfFlagDisabled(Label.L3, flag=Flags.DragonlodPlacidusaxDead)
    DisableCharacter(CharacterGroups.DragonlordPlacidusaxBoss)
    DisableAnimations(CharacterGroups.DragonlordPlacidusaxBoss)
    Kill(CharacterGroups.DragonlordPlacidusaxBoss)
    EnableFlag(71301)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableAI(Characters.DragonlordPlacidusax)
    CreateNPCPart(Characters.DragonlordPlacidusax, npc_part_id=0, part_index=NPCPartType.Part1, part_health=9999)
    CreateNPCPart(Characters.DragonlordPlacidusax, npc_part_id=1, part_index=NPCPartType.Part2, part_health=9999)
    SetNPCPartEffects(
        Characters.DragonlordPlacidusax,
        npc_part_id=0,
        material_sfx_id=173,
        material_vfx_id=173,
        unk_16_20=139,
        unk_20_24=139,
        unk_24_28=0,
    )
    SetNPCPartEffects(
        Characters.DragonlordPlacidusax,
        npc_part_id=1,
        material_sfx_id=173,
        material_vfx_id=173,
        unk_16_20=139,
        unk_20_24=139,
        unk_24_28=0,
    )
    SetLockOnPoint(character=Characters.DragonlordPlacidusax, lock_on_model_point=222, state=False)
    SetLockOnPoint(character=Characters.DragonlordPlacidusax, lock_on_model_point=223, state=False)
    SetLockOnPoint(character=Characters.DragonlordPlacidusax, lock_on_model_point=224, state=False)
    SetLockOnPoint(character=Characters.DragonlordPlacidusax, lock_on_model_point=225, state=False)
    SetCharacterEventTarget(Characters.DragonlordPlacidusax, entity=13000840)
    SetBackreadStateAlternate(Characters.DragonlordPlacidusax, True)
    ForceAnimation(Characters.DragonlordPlacidusax, 30000, loop=True)

    # CLONE
    DisableAI(Characters.CLONE_DragonlordPlacidusax)
    CreateNPCPart(Characters.CLONE_DragonlordPlacidusax, npc_part_id=0, part_index=NPCPartType.Part1, part_health=9999)
    CreateNPCPart(Characters.CLONE_DragonlordPlacidusax, npc_part_id=1, part_index=NPCPartType.Part2, part_health=9999)
    SetNPCPartEffects(
        Characters.CLONE_DragonlordPlacidusax,
        npc_part_id=0,
        material_sfx_id=173,
        material_vfx_id=173,
        unk_16_20=139,
        unk_20_24=139,
        unk_24_28=0,
    )
    SetNPCPartEffects(
        Characters.CLONE_DragonlordPlacidusax,
        npc_part_id=1,
        material_sfx_id=173,
        material_vfx_id=173,
        unk_16_20=139,
        unk_20_24=139,
        unk_24_28=0,
    )
    SetLockOnPoint(character=Characters.CLONE_DragonlordPlacidusax, lock_on_model_point=222, state=False)
    SetLockOnPoint(character=Characters.CLONE_DragonlordPlacidusax, lock_on_model_point=223, state=False)
    SetLockOnPoint(character=Characters.CLONE_DragonlordPlacidusax, lock_on_model_point=224, state=False)
    SetLockOnPoint(character=Characters.CLONE_DragonlordPlacidusax, lock_on_model_point=225, state=False)
    SetCharacterEventTarget(Characters.CLONE_DragonlordPlacidusax, entity=13000840)
    SetBackreadStateAlternate(Characters.CLONE_DragonlordPlacidusax, True)
    ForceAnimation(Characters.CLONE_DragonlordPlacidusax, 30000, loop=True)

    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=13002831))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DragonlordPlacidusax))
    OR_1.Add(CharacterHasStateInfo(character=Characters.DragonlordPlacidusax, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.DragonlordPlacidusax, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.DragonlordPlacidusax, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.DragonlordPlacidusax, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.DragonlordPlacidusax, state_info=260))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.CLONE_DragonlordPlacidusax))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_DragonlordPlacidusax, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_DragonlordPlacidusax, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_DragonlordPlacidusax, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_DragonlordPlacidusax, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_DragonlordPlacidusax, state_info=260))

    MAIN.Await(OR_1)

    ForceAnimation(Characters.DragonlordPlacidusax, 20000)
    EnableAI(Characters.DragonlordPlacidusax)
    SetNetworkUpdateRate(Characters.DragonlordPlacidusax, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(Characters.DragonlordPlacidusax, 20000)
    EnableAI(Characters.DragonlordPlacidusax)
    SetNetworkUpdateRate(Characters.DragonlordPlacidusax, is_fixed=True, update_rate=CharacterUpdateRate.Always)

    ForceAnimation(Characters.CLONE_DragonlordPlacidusax, 20000)
    EnableAI(Characters.CLONE_DragonlordPlacidusax)
    SetNetworkUpdateRate(Characters.CLONE_DragonlordPlacidusax, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(Characters.CLONE_DragonlordPlacidusax, 20000)
    EnableAI(Characters.CLONE_DragonlordPlacidusax)
    SetNetworkUpdateRate(Characters.CLONE_DragonlordPlacidusax, is_fixed=True, update_rate=CharacterUpdateRate.Always)

    ActivateMultiplayerBuffs(CharacterGroups.DragonlordPlacidusaxBoss)
    EnableBossHealthBar(Characters.DragonlordPlacidusax, name=NameText.DragonlordPlacidusax, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_DragonlordPlacidusax, name=NameText.CLONE_DragonlordPlacidusax, bar_slot=0)

    if PlayerNotInOwnWorld():
        return
    EnableNetworkFlag(13002835)
    SetNetworkUpdateAuthority(CharacterGroups.DragonlordPlacidusaxBoss, authority_level=UpdateAuthority.Forced)
    NotifyBossBattleStart()


@RestartOnRest(13002840)
def DragonlordPlacidusaxPhaseTwoTransition():
    """Event 13002840"""
    if FlagEnabled(Flags.DragonlodPlacidusaxDead):
        return
    OR_1.Add(CharacterHasSpecialEffect(Characters.DragonlordPlacidusax, 5029))
    OR_1.Add(CharacterHasSpecialEffect(Characters.CLONE_DragonlordPlacidusax, 5029))

    MAIN.Await(OR_1)

    SetWeather(weather=Weather.WindyRain, duration=-1.0, immediate_change=False)
    EnableFlag(Flags.DragonlordPlacidusaxInPhaseTwo)


@RestartOnRest(13002841)
def DragonlordPlacidusaxCameraControl():
    """Event 13002841"""
    if FlagEnabled(Flags.DragonlodPlacidusaxDead):
        return
    DisableNetworkSync()

    OR_1.Add(CharacterHasSpecialEffect(Characters.DragonlordPlacidusax, 5025))
    OR_1.Add(CharacterHasSpecialEffect(Characters.CLONE_DragonlordPlacidusax, 5025))

    MAIN.Await(OR_1)

    ChangeCamera(normal_camera_id=4525, locked_camera_id=4521)
    Wait(1.0)

    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.DragonlordPlacidusax, 5025))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.CLONE_DragonlordPlacidusax, 5025))
    MAIN.Await(AND_1)

    ChangeCamera(normal_camera_id=4525, locked_camera_id=4520)
    Wait(1.0)
    Restart()


@RestartOnRest(13002846)
def Event_13002846(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 13002846"""
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))

    MAIN.Await(AND_1)

    EnableFlag(flag_2)
    Restart()


@RestartOnRest(13002849)
def DragonlordPlacidusaxCommonEvents():
    """Event 13002849"""
    Event_13002846(0, flag=Flags.DragonlodPlacidusaxDead, flag_1=13002835, flag_2=13002836)
    CommonFunc_ControlBossMusic(
        0, Flags.DragonlodPlacidusaxDead, 452000, 13002835, 13002836, 0, Flags.DragonlordPlacidusaxInPhaseTwo, 0, 1
    )


@RestartOnRest(13002850)
def GodskinDuoDies():
    """Event 13002850"""
    if FlagEnabled(Flags.GodskinDuoDead):
        return

    AND_1.Add(HealthValue(Characters.GodskinDuoHealthPool) <= 0)
    AND_1.Add(HealthValue(Characters.CLONE_GodskinDuoHealthPool) <= 0)
    MAIN.Await(AND_1)

    # Spawns killed and respawns stopped in new separate event.
    Wait(4.0)
    PlaySoundEffect(Characters.GodskinDuoHealthPool, 888880000, sound_type=SoundType.s_SFX)

    AND_2.Add(CharacterDead(Characters.GodskinDuoHealthPool))
    AND_2.Add(CharacterDead(Characters.CLONE_GodskinDuoHealthPool))
    MAIN.Await(AND_2)

    KillBossAndDisplayBanner(character=Characters.GodskinDuoHealthPool, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(Flags.GodskinDuoDead)
    EnableFlag(9114)
    if PlayerInOwnWorld():
        EnableFlag(61114)


@RestartOnRest(13002760)
def StopGodskinDuoRespawning(_, godskin_health_pool: uint, apostle: uint, noble: uint, stop_respawning_flag: int):
    if FlagEnabled(Flags.GodskinDuoDead):
        return
    MAIN.Await(HealthValue(godskin_health_pool) <= 0)
    Kill(apostle)
    Kill(noble)
    EnableFlag(stop_respawning_flag)


@ContinueOnRest(13002859)
def Event_13002859():
    """Event 13002859"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(13002160))
    AND_1.Add(FlagEnabled(13002855))

    MAIN.Await(AND_1)

    GotoIfCharacterInsideRegion(Label.L0, character=PLAYER, region=13002852)
    AICommand(Characters.RecusantBernahl1, command_id=10, command_slot=0)
    ReplanAI(Characters.RecusantBernahl1)
    SetEventPoint(Characters.RecusantBernahl1, region=13002850, reaction_range=0.0)

    MAIN.Await(CharacterInsideRegion(character=Characters.RecusantBernahl1, region=13002859))

    RotateToFaceEntity(Characters.RecusantBernahl1, 13002850, animation=60060, wait_for_completion=True)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(OR_4)
    OR_5.Add(CharacterInsideRegion(character=Characters.RecusantBernahl1, region=13002850))

    MAIN.Await(OR_5)

    RestartIfFinishedConditionTrue(input_condition=OR_4)
    AICommand(Characters.RecusantBernahl1, command_id=-1, command_slot=0)
    ReplanAI(Characters.RecusantBernahl1)
    SetNetworkUpdateRate(Characters.RecusantBernahl1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(Characters.RecusantBernahl1, command_id=10, command_slot=0)
    ReplanAI(Characters.RecusantBernahl1)
    SetEventPoint(Characters.RecusantBernahl1, region=13002852, reaction_range=0.0)

    MAIN.Await(CharacterInsideRegion(character=Characters.RecusantBernahl1, region=13002859))

    RotateToFaceEntity(Characters.RecusantBernahl1, 13002852, animation=60060, wait_for_completion=True)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(OR_4)
    OR_5.Add(CharacterInsideRegion(character=Characters.RecusantBernahl1, region=13002852))

    MAIN.Await(OR_5)

    RestartIfFinishedConditionTrue(input_condition=OR_4)
    AICommand(Characters.RecusantBernahl1, command_id=-1, command_slot=0)
    ReplanAI(Characters.RecusantBernahl1)
    SetNetworkUpdateRate(Characters.RecusantBernahl1, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(13002860)
def GodskinDuoBattleTrigger():
    """Event 13002860"""
    GotoIfFlagDisabled(Label.L6, flag=Flags.GodskinDuoDead)
    DisableCharacter(Characters.GodskinDuoHealthPool)
    DisableCharacter(Characters.GodskinDuoApostle)
    DisableCharacter(Characters.GodskinDuoNoble)
    DisableAnimations(Characters.GodskinDuoHealthPool)
    DisableAnimations(Characters.GodskinDuoApostle)
    DisableAnimations(Characters.GodskinDuoNoble)
    Kill(Characters.GodskinDuoHealthPool)
    Kill(Characters.GodskinDuoApostle)
    Kill(Characters.GodskinDuoNoble)
    DisableCharacter(Characters.CLONE_GodskinDuoHealthPool)
    DisableCharacter(Characters.CLONE_GodskinDuoApostle)
    DisableCharacter(Characters.CLONE_GodskinDuoNoble)
    DisableAnimations(Characters.CLONE_GodskinDuoHealthPool)
    DisableAnimations(Characters.CLONE_GodskinDuoApostle)
    DisableAnimations(Characters.CLONE_GodskinDuoNoble)
    Kill(Characters.CLONE_GodskinDuoHealthPool)
    Kill(Characters.CLONE_GodskinDuoApostle)
    Kill(Characters.CLONE_GodskinDuoNoble)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    DisableAI(Characters.GodskinDuoApostle)
    DisableAI(Characters.GodskinDuoNoble)
    DisableCharacter(Characters.GodskinDuoHealthPool)
    DisableGravity(Characters.GodskinDuoHealthPool)
    DisableAnimations(Characters.GodskinDuoHealthPool)

    DisableAI(Characters.CLONE_GodskinDuoApostle)
    DisableAI(Characters.CLONE_GodskinDuoNoble)
    DisableCharacter(Characters.CLONE_GodskinDuoHealthPool)
    DisableGravity(Characters.CLONE_GodskinDuoHealthPool)
    DisableAnimations(Characters.CLONE_GodskinDuoHealthPool)

    GotoIfFlagEnabled(Label.L7, flag=Flags.GodskinDuoFirstTimeDone)

    DisableCharacter(Characters.GodskinDuoApostle)
    DisableCharacter(Characters.GodskinDuoNoble)
    ForceAnimation(Characters.GodskinDuoApostle, 30001, loop=True)
    ForceAnimation(Characters.GodskinDuoNoble, 30001, loop=True)
    DisableCharacter(Characters.CLONE_GodskinDuoApostle)
    DisableCharacter(Characters.CLONE_GodskinDuoNoble)
    ForceAnimation(Characters.CLONE_GodskinDuoApostle, 30001, loop=True)
    ForceAnimation(Characters.CLONE_GodskinDuoNoble, 30001, loop=True)

    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=13002851))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.GodskinDuoApostle, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.GodskinDuoNoble, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.CLONE_GodskinDuoApostle, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.CLONE_GodskinDuoNoble, attacker=PLAYER))

    MAIN.Await(OR_1)

    EnableNetworkFlag(Flags.GodskinDuoFirstTimeDone)
    EnableCharacter(Characters.GodskinDuoApostle)
    EnableCharacter(Characters.GodskinDuoNoble)
    ForceAnimation(Characters.GodskinDuoApostle, 20001)
    ForceAnimation(Characters.GodskinDuoNoble, 20001)
    EnableCharacter(Characters.CLONE_GodskinDuoApostle)
    EnableCharacter(Characters.CLONE_GodskinDuoNoble)
    ForceAnimation(Characters.CLONE_GodskinDuoApostle, 20001)
    ForceAnimation(Characters.CLONE_GodskinDuoNoble, 20001)
    Goto(Label.L8)

    # --- Label 7 --- #
    DefineLabel(7)
    OR_2.Add(FlagEnabled(13002855))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=13002850))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=13002852))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=13002853))

    MAIN.Await(OR_2)

    # --- Label 8 --- #
    DefineLabel(8)
    EnableCharacter(Characters.GodskinDuoHealthPool)
    DisableAI(Characters.GodskinDuoHealthPool)
    EnableAI(Characters.GodskinDuoApostle)
    EnableAI(Characters.GodskinDuoNoble)
    SetNetworkUpdateRate(Characters.GodskinDuoHealthPool, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.GodskinDuoApostle, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.GodskinDuoNoble, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ReferDamageToEntity(CharacterGroups.GodskinDuoBoss, target_entity=Characters.GodskinDuoHealthPool)

    EnableCharacter(Characters.CLONE_GodskinDuoHealthPool)
    DisableAI(Characters.CLONE_GodskinDuoHealthPool)
    EnableAI(Characters.CLONE_GodskinDuoApostle)
    EnableAI(Characters.CLONE_GodskinDuoNoble)
    SetNetworkUpdateRate(Characters.CLONE_GodskinDuoHealthPool, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_GodskinDuoApostle, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_GodskinDuoNoble, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ReferDamageToEntity(CharacterGroups.CLONE_GodskinDuoBoss, target_entity=Characters.CLONE_GodskinDuoHealthPool)

    EnableBossHealthBar(Characters.GodskinDuoHealthPool, name=NameText.GodskinDuo, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_GodskinDuoHealthPool, name=NameText.CLONE_GodskinDuo, bar_slot=0)


@RestartOnRest(13002861)
def GodskinDuoPhaseTwoTransition():
    """Only changes music. Either Duo can trigger it."""
    if FlagEnabled(Flags.GodskinDuoDead):
        return
    OR_1.Add(HealthRatio(Characters.GodskinDuoHealthPool) <= 0.5)
    OR_1.Add(HealthRatio(Characters.CLONE_GodskinDuoHealthPool) <= 0.5)
    OR_1.Add(FlagEnabled(Flags.GodskinApostleHasRespawned))
    OR_1.Add(FlagEnabled(Flags.GodskinNobleHasRespawned))

    MAIN.Await(OR_1)

    EnableFlag(Flags.GodskinDuoInPhaseTwo)


@RestartOnRest(13002890)
def FirstGodskinDies(
    _, solo_godskin_flag: uint, dead_godskin: uint, remaining_godskin: uint, remaining_godskin_special_effect: int
):
    """Event 13002890"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(Flags.GodskinDuoDead):
        return
    if FlagEnabled(Flags.StopGodskinDuoRespawning):
        return
    AND_1.Add(FlagDisabled(solo_godskin_flag))
    AND_1.Add(CharacterDead(dead_godskin))

    MAIN.Await(AND_1)

    Wait(20.0)
    OR_1.Add(HealthValue(remaining_godskin) > 0)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(remaining_godskin, remaining_godskin_special_effect)
    EnableNetworkFlag(solo_godskin_flag)
    Restart()


@RestartOnRest(13002891)
def GodskinRespawns(
    _,
    solo_godskin_flag: uint,
    spawner: uint,
    remaining_godskin: uint,
    revival_special_effect: int,
    respawned_godskin: uint,
    respawned_flag: uint,
):
    """Event 13002891"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(Flags.GodskinDuoDead):
        return
    if FlagEnabled(Flags.StopGodskinDuoRespawning):
        return
    OR_1.Add(CharacterHasSpecialEffect(remaining_godskin, revival_special_effect))
    OR_1.Add(CharacterDead(remaining_godskin))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(solo_godskin_flag))

    MAIN.Await(AND_1)

    if FlagEnabled(Flags.GodskinDuoDead):
        return
    if FlagEnabled(Flags.StopGodskinDuoRespawning):
        return
    ForceSpawnerToSpawn(spawner=spawner)
    DisableNetworkFlag(solo_godskin_flag)
    EnableNetworkFlag(respawned_flag)
    SetNetworkUpdateRate(respawned_godskin, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()


@RestartOnRest(13002892)
def RespawnRandomGodskinDuoMember(
    _,
    apostle: uint,
    noble: uint,
    apostle_spawner: int,
    noble_spawner: int,
    apostle_respawned_flag: int,
    noble_respawned_flag: int,
    random_flag_1: int,
    random_flag_2: int,
):
    """Event 13002892"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(Flags.GodskinDuoDead):
        return
    if FlagEnabled(Flags.StopGodskinDuoRespawning):
        return
    AND_1.Add(CharacterDead(apostle))
    AND_1.Add(CharacterDead(noble))
    AND_1.Add(FlagDisabled(Flags.NobleSoloFlag))
    AND_1.Add(FlagDisabled(Flags.ApostleSoloFlag))

    MAIN.Await(AND_1)

    if FlagEnabled(Flags.GodskinDuoDead):
        return
    Wait(10.0)
    if FlagEnabled(Flags.GodskinDuoDead):
        return
    if FlagEnabled(Flags.StopGodskinDuoRespawning):
        return

    EnableRandomFlagInRange(flag_range=(random_flag_1, random_flag_2))
    GotoIfFlagEnabled(Label.L0, flag=random_flag_1)
    GotoIfFlagEnabled(Label.L1, flag=random_flag_2)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceSpawnerToSpawn(spawner=apostle_spawner)
    EnableFlag(apostle_respawned_flag)
    DisableFlag(random_flag_1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    ForceSpawnerToSpawn(spawner=noble_spawner)
    EnableFlag(noble_respawned_flag)
    DisableFlag(random_flag_2)
    Restart()


@RestartOnRest(13002865)
def GodskinDuoCommonEvents():
    """Event 13002865"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.GodskinDuoDead,
        fog_asset=Assets.AEG099_001_9000,
        fog_region=13002850,
        host_entered_fog_flag=13002855,
        boss_characters=13005850,
        action_button_id=10000,
        first_time_done_flag=Flags.GodskinDuoFirstTimeDone,
        first_time_trigger_region=13002851,
    )
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.GodskinDuoDead,
        fog_asset=Assets.AEG099_001_9003,
        fog_region=13002852,
        host_entered_fog_flag=13002855,
        boss_characters=13005850,
        action_button_id=10000,
        first_time_done_flag=Flags.GodskinDuoFirstTimeDone,
        first_time_trigger_region=13002851,
    )
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.GodskinDuoDead,
        fog_asset=Assets.AEG099_001_9002,
        fog_region=13002853,
        host_entered_fog_flag=13002855,
        boss_characters=13005850,
        action_button_id=10000,
        first_time_done_flag=Flags.GodskinDuoFirstTimeDone,
        first_time_trigger_region=13002851,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.GodskinDuoDead,
        fog_asset=Assets.AEG099_001_9000,
        fog_region=13002850,
        host_entered_fog_flag=13002855,
        summon_entered_fog_flag=13002856,
        action_button_id=10000,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.GodskinDuoDead,
        fog_asset=Assets.AEG099_001_9003,
        fog_region=13002852,
        host_entered_fog_flag=13002855,
        summon_entered_fog_flag=13002856,
        action_button_id=10000,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.GodskinDuoDead,
        fog_asset=Assets.AEG099_001_9002,
        fog_region=13002853,
        host_entered_fog_flag=13002855,
        summon_entered_fog_flag=13002856,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(
        0, boss_dead_flag=Flags.GodskinDuoDead, fog_asset=Assets.AEG099_001_9000, model_point=5,
        required_flag=Flags.GodskinDuoFirstTimeDone
    )
    CommonFunc_ControlBossFog(
        0, boss_dead_flag=Flags.GodskinDuoDead, fog_asset=Assets.AEG099_001_9003, model_point=5,
        required_flag=Flags.GodskinDuoFirstTimeDone
    )
    CommonFunc_ControlBossFog(
        0, boss_dead_flag=Flags.GodskinDuoDead, fog_asset=Assets.AEG099_001_9002, model_point=5,
        required_flag=Flags.GodskinDuoFirstTimeDone
    )
    CommonFunc_ControlBossFog(
        0, boss_dead_flag=Flags.GodskinDuoDead, fog_asset=Assets.AEG099_001_9001, model_point=5,
        required_flag=Flags.GodskinDuoFirstTimeDone
    )
    CommonFunc_ControlBossFog(
        0, boss_dead_flag=Flags.GodskinDuoDead, fog_asset=Assets.AEG099_001_9004, model_point=5,
        required_flag=Flags.GodskinDuoFirstTimeDone
    )
    CommonFunc_ControlBossMusic(
        0, Flags.GodskinDuoDead, 356000, 13002855, 13002856, 0, Flags.GodskinDuoInPhaseTwo, 0, 0
    )


@RestartOnRest(13002600)
def Event_13002600(_, entity: uint, region: uint, anchor_entity: uint, seconds: float):
    """Event 13002600"""
    if FlagEnabled(13000490):
        return
    CreateProjectileOwner(entity=entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))

    MAIN.Await(AND_1)

    Wait(0.10000000149011612)
    Wait(seconds)
    CreateTemporaryVFX(vfx_id=813600, anchor_entity=anchor_entity, anchor_type=CoordEntityType.Region)
    Wait(5.0)
    Restart()


@RestartOnRest(13002610)
def AncientDragonLowerLightning(_, dragon: uint):
    """Event 13002610"""
    ForceAnimation(dragon, 0)
    OR_15.Add(HasAIStatus(dragon, ai_status=AIStatusType.Battle))
    if OR_15:
        return
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_2.Add(FlagEnabled(Flags.AncientDragonLowerPlatformDead))
    if OR_2:
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=13002619))
    AND_1.Add(OR_1)

    MAIN.Await(AND_1)

    if ThisEventSlotFlagDisabled():
        ForceAnimation(dragon, 3029)
    else:
        ForceAnimation(dragon, 20002)
    EnableThisSlotFlag()
    Wait(2.0)
    OR_10.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_10.Add(FlagEnabled(Flags.AncientDragonLowerPlatformDead))
    if OR_10:
        return
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.5)
    OR_11.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_11.Add(FlagEnabled(Flags.AncientDragonLowerPlatformDead))
    if OR_11:
        return
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.5)
    OR_12.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_12.Add(FlagEnabled(Flags.AncientDragonLowerPlatformDead))
    if OR_12:
        return
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(0.8999999761581421)
    OR_13.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_13.Add(FlagEnabled(Flags.AncientDragonLowerPlatformDead))
    if OR_13:
        return
    ForceAnimation(dragon, 30000)
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_3.Add(FlagEnabled(Flags.AncientDragonLowerPlatformDead))
    GotoIfConditionTrue(Label.L0, input_condition=OR_3)
    Wait(1.0)
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_4.Add(FlagEnabled(Flags.AncientDragonLowerPlatformDead))
    GotoIfConditionTrue(Label.L0, input_condition=OR_4)
    Wait(1.0)
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_5.Add(FlagEnabled(Flags.AncientDragonLowerPlatformDead))
    GotoIfConditionTrue(Label.L0, input_condition=OR_5)
    Wait(1.0)
    OR_6.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_6.Add(FlagEnabled(Flags.AncientDragonLowerPlatformDead))
    GotoIfConditionTrue(Label.L0, input_condition=OR_6)
    Wait(1.0)
    OR_7.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_7.Add(FlagEnabled(Flags.AncientDragonLowerPlatformDead))
    GotoIfConditionTrue(Label.L0, input_condition=OR_7)
    Wait(1.0)
    OR_8.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_8.Add(FlagEnabled(Flags.AncientDragonLowerPlatformDead))
    Wait(1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(13003700)
def Event_13003700():
    """Event 13003700"""
    if PlayerNotInOwnWorld():
        return

    MAIN.Await(FlagEnabled(13002805))

    SetCharacterTalkRange(character=Characters.MalikethPhaseOne, distance=100.0)
    SetCharacterTalkRange(character=Characters.MalikethPhaseTwo, distance=100.0)
    End()


@RestartOnRest(13003710)
def Event_13003710(_, character: uint):
    """Event 13003710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3660):
        DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3671)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(Characters.AncientDragon4)
    EnableCharacter(Characters.AncientDragon5)
    if FlagEnabled(13000702):
        DisableCharacter(Characters.AncientDragon5)

    MAIN.Await(FlagEnabled(3671))

    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableFlag(13002710)
    GotoIfFlagEnabled(Label.L4, flag=13009257)
    GotoIfFlagEnabled(Label.L1, flag=3660)
    GotoIfFlagEnabled(Label.L2, flag=3661)
    GotoIfFlagEnabled(Label.L4, flag=3663)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930010)
    if FlagEnabled(13009258):
        ForceAnimation(character, 930014)
    DisableCharacter(Characters.AncientDragon4)
    ForceAnimation(Characters.AncientDragon4, 10001)
    DisableCharacter(Characters.AncientDragon5)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    DisableCharacter(Characters.AncientDragon4)
    DisableCharacter(Characters.AncientDragon5)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(Characters.AncientDragon4)
    DisableCharacter(Characters.AncientDragon5)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)

    MAIN.Await(FlagDisabled(3671))

    Restart()


@RestartOnRest(13003711)
def Event_13003711(_, character: uint):
    """Event 13003711"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(3671))
    AND_1.Add(FlagEnabled(13009256))

    MAIN.Await(AND_1)

    SetCharacterTalkRange(character=character, distance=200.0)
    GotoIfFlagDisabled(Label.L1, flag=13009258)
    AND_2.Add(FlagEnabled(13009258))
    AND_2.Add(FlagDisabled(13009257))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    AND_3.Add(FlagEnabled(13009258))
    AND_3.Add(FlagEnabled(13009257))
    GotoIfConditionTrue(Label.L3, input_condition=AND_3)

    # --- Label 1 --- #
    DefineLabel(1)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAI(character)
    EnableImmortality(character)
    DisableNetworkConnectedFlagRange(flag_range=(3660, 3663))
    EnableNetworkFlag(3662)
    EnableFlag(400175)
    AND_2.Add(HealthValue(character) == 1)
    AwaitConditionTrue(AND_2)
    EnableNetworkFlag(13002712)
    ForceAnimation(character, 20035)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableAI(character)
    DisableNetworkConnectedFlagRange(flag_range=(3660, 3663))
    EnableNetworkFlag(3660)
    SetTeamType(character, TeamType.NoTeam)
    AND_3.Add(FlagEnabled(13009257))
    AwaitConditionTrue(AND_3)
    SetTeamType(character, TeamType.FriendlyNPC)
    DisableImmortality(character)
    OR_1.Add(FlagEnabled(13009260))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(CharacterDead(character))
    AwaitConditionTrue(OR_1)
    AND_4.Add(CharacterDead(character))
    SkipLinesIfConditionTrue(1, AND_4)
    Kill(character, award_runes=True)
    AwardItemLot(101740, host_only=False)

    # --- Label 3 --- #
    DefineLabel(3)
    if FlagDisabled(400174):
        EnableFlag(13009254)
    DisableNetworkConnectedFlagRange(flag_range=(3660, 3663))
    EnableNetworkFlag(3663)
    End()


@RestartOnRest(13003720)
def Event_13003720():
    """Event 13003720"""
    WaitFrames(frames=1)
    DisableFlag(13009300)
    AND_1.Add(FlagDisabled(16009460))
    AND_1.Add(FlagDisabled(3883))
    if AND_1:
        return
    EnableFlag(13009300)
    End()


@ContinueOnRest(13003721)
def Event_13003721():
    """Event 13003721"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    OR_4.Add(FlagEnabled(13002720))
    OR_4.Add(FlagEnabled(13002721))
    if OR_4:
        return
    if FlagEnabled(Flags.GodskinDuoDead):
        return
    if FlagDisabled(3880):
        return
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=13002721, radius=10.0))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=13002726, radius=10.0))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)

    MAIN.Await(OR_3)

    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_1)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(13002720)
    DisableFlag(13002721)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableFlag(13002720)
    EnableFlag(13002721)
    End()
