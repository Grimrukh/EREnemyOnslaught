"""
Volcano Manor

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
from .entities.m16_00_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=16000002, asset=Assets.AEG099_060_9002)
    RegisterGrace(grace_flag=16000003, asset=Assets.AEG099_060_9003)
    RegisterGrace(grace_flag=16000004, asset=Assets.AEG099_060_9004)
    RegisterGrace(grace_flag=16000005, asset=Assets.AEG099_060_9005)
    RegisterGrace(grace_flag=16000007, asset=Assets.AEG099_060_9007)
    CommonFunc_RegisterGraceIfFlagEnabled(
        0,
        flag=Flags.RykardDead,
        grace_flag=16000000,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=20.0,
    )
    CommonFunc_RegisterGraceIfFlagEnabled(
        1,
        flag=Flags.GodskinNobleDead,
        grace_flag=16000001,
        character=Characters.TalkDummy1,
        asset=Assets.AEG099_060_9001,
        enemy_block_distance=8.0,
    )
    CommonFunc_RegisterGraceIfFlagEnabled(
        2,
        flag=Flags.IronVirginsDead,
        grace_flag=16000006,
        character=Characters.TalkDummy7,
        asset=Assets.AEG099_060_9006,
        enemy_block_distance=8.0,
    )

    # RYKARD
    RykardBattleTrigger()
    RykardDies()
    RykardPhaseTwoTransition()
    RykardPhaseTwoHalfHealthEffect(0, rykard=Characters.RykardPhaseTwo)
    RykardPhaseTwoHalfHealthEffect(1, rykard=Characters.CLONE_RykardPhaseTwo)  # 16002813
    RykardPhaseTwoEffect11930(0, rykard=Characters.RykardPhaseTwo)
    RykardPhaseTwoEffect11930(1, rykard=Characters.CLONE_RykardPhaseTwo)  # 16002823
    RykardPhaseTwoEffect11931(0, rykard=Characters.RykardPhaseTwo)
    RykardPhaseTwoEffect11931(1, rykard=Characters.CLONE_RykardPhaseTwo)  # 16002825
    RykardPhaseTwoEffect11941(0, rykard=Characters.RykardPhaseTwo)
    RykardPhaseTwoEffect11941(1, rykard=Characters.CLONE_RykardPhaseTwo)  # 16002827
    RykardPhaseTwoEffect11945(0, rykard=Characters.RykardPhaseTwo)
    RykardPhaseTwoEffect11945(1, rykard=Characters.CLONE_RykardPhaseTwo)  # 16002831
    RykardPhaseTwoEffectsClear(0, rykard=Characters.RykardPhaseTwo)
    RykardPhaseTwoEffectsClear(1, rykard=Characters.CLONE_RykardPhaseTwo)  # 16002833
    RykardCameraTrigger1()
    RykardCameraTrigger2()
    RykardSpiritAshesCheck()
    RykardCoopBuffs(0, rykard=Characters.RykardPhaseTwo)
    RykardCoopBuffs(1, rykard=Characters.RykardPhaseOne)
    RykardCoopBuffs(2, rykard=Characters.CLONE_RykardPhaseTwo)
    RykardCoopBuffs(3, rykard=Characters.CLONE_RykardPhaseOne)
    RykardFogGateEvents()

    # GODSKIN NOBLE
    GodskinNobleBattleTrigger()
    GodskinNobleDies()
    GodskinNobleFogGateEvents()

    # IRON VIRGINS
    IronVirginsBattleTrigger()
    IronVirginsDie()
    IronVirginsFogGateEvents()

    MonitorSerpentHunterPossession()

    Event_16002690(0, flag=16002696, asset=Assets.AEG099_340_9000, asset_1=Assets.AEG099_090_9005)
    Event_16002691(0, asset=Assets.AEG099_340_9000, asset_1=Assets.AEG099_090_9005, destination=16002690)
    Event_16002620(0, flag=16000622, asset=Assets.AEG277_011_0501)
    Event_16002620(1, flag=16000624, asset=Assets.AEG277_011_0503)
    Event_16002625()
    Event_16002500()
    Event_16002650()
    CommonFunc_90005515(0, flag=16008544, anchor_entity=Assets.AEG277_013_0500)
    CommonFunc_90005515(0, flag=16008546, anchor_entity=Assets.AEG277_016_0500)
    CommonFunc_90005515(0, flag=16008548, anchor_entity=Assets.AEG277_014_0500)
    CommonFunc_90005515(0, flag=16008542, anchor_entity=Assets.AEG277_015_0500)
    CommonFunc_90005515(0, flag=16008552, anchor_entity=Assets.AEG277_018_0500)
    CommonFunc_90005515(0, flag=16008556, anchor_entity=Assets.AEG277_018_0501)
    CommonFunc_90005515(0, flag=16008554, anchor_entity=Assets.AEG277_010_0500)
    CommonFunc_90005510(
        0,
        flag=16000552,
        asset=Assets.AEG277_018_0500,
        obj_act_id=16003552,
        obj_act_id_1=1277018,
        text=208134,
        left=0,
    )
    CommonFunc_90005510(
        0,
        flag=16000564,
        asset=Assets.AEG277_018_0505,
        obj_act_id=16003564,
        obj_act_id_1=1277018,
        text=208134,
        left=0,
    )
    CommonFunc_90005510(
        0,
        flag=16000560,
        asset=Assets.AEG277_018_0503,
        obj_act_id=16003560,
        obj_act_id_1=1277018,
        text=208134,
        left=0,
    )
    CommonFunc_90005510(
        0,
        flag=16000562,
        asset=Assets.AEG277_018_0504,
        obj_act_id=16003562,
        obj_act_id_1=1277018,
        text=208134,
        left=0,
    )
    Event_16002580()
    Event_16002510()
    CommonFunc_90005501(
        0,
        flag=16000510,
        flag_1=16001510,
        left=0,
        asset=Assets.AEG277_003_0500,
        asset_1=Assets.AEG277_000_0502,
        asset_2=Assets.AEG277_000_0503,
        flag_2=16000511,
    )
    CommonFunc_90005501(
        0,
        flag=16000520,
        flag_1=16001520,
        left=0,
        asset=Assets.AEG277_005_0500,
        asset_1=Assets.AEG277_021_0500,
        asset_2=Assets.AEG277_021_0501,
        flag_2=16000521,
    )
    CommonFunc_90005504(0, flag=16000525, flag_1=16001525, left=0, entity=Assets.AEG277_020_0500, flag_2=16000526)
    CommonFunc_90005504(0, flag=16000530, flag_1=16001530, left=1, entity=Assets.AEG277_020_0501, flag_2=16000531)
    Event_16002640()
    Event_16002570(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=16,
        block_id=0,
        cc_id=0,
        dd_id=0,
        player_start=16002570,
        unk_8_12=0,
        flag=16002574,
        left_flag=16002572,
        cancel_flag__right_flag=16002573,
    )
    Event_16002579()
    Event_16002689()
    Event_16002670()
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9003, vfx_id=100, model_point=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9004, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005502(0, flag=16000514, asset=Assets.AEG277_000_0503, region=16002511)
    Event_16002590()
    CommonFunc_90005694(
        0,
        asset_flag=16001651,
        asset=Assets.AEG270_034_2000,
        model_point_start=201,
        model_point_end=0,
        behavior_param_id__behaviour_id=200400,
        radius=0.75,
        life=0.0,
        repetition_time=1.0,
    )
    Event_16002505()
    CommonFunc_90005620(
        0,
        flag=16000575,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=16002575,
        cancel_flag__right_flag=16002576,
        right=16002577,
    )
    CommonFunc_90005621(0, flag=16000575, asset=Assets.AEG099_272_9000)
    CommonFunc_90005620(
        0,
        flag=16000565,
        asset=Assets.AEG027_078_9000,
        asset_1=Assets.AEG027_216_9001,
        asset_2=Assets.AEG027_217_9000,
        left_flag=16002565,
        cancel_flag__right_flag=16002566,
        right=16002567,
    )
    CommonFunc_90005621(0, flag=16000565, asset=Assets.AEG099_272_9001)
    CommonFunc_90005790(
        0,
        right=0,
        flag=16000180,
        summon_flag=16002181,
        dismissal_flag=16002182,
        character=Characters.InquisitorGhiza,
        sign_type=23,
        region=16002180,
        region_1=16002181,
        seconds=0.0,
        right_1=0,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=16000180, flag_1=16002181, flag_2=16002182, character=Characters.InquisitorGhiza)
    CommonFunc_90005792(
        0,
        flag=16000180,
        flag_1=16002181,
        flag_2=16002182,
        character=Characters.InquisitorGhiza,
        item_lot=16000940,
        seconds=0.0,
    )
    Event_16002185(
        0,
        character=Characters.InquisitorGhiza,
        flag=16002181,
        flag_1=16002182,
        flag_2=16000180,
        flag_3=16002180,
        region=16002182,
    )
    CommonFunc_90005702(0, character=Characters.Tanith1, flag=3103, first_flag=3100, last_flag=3104)
    Event_16003700(0, character=Characters.Tanith0, destination=16002700, character_1=Characters.CrucibleKnight0)
    Event_16003701(0, character=Characters.Tanith1, character_1=Characters.WrithingMass, asset=Assets.AEG099_990_9004)
    Event_16003702(0, flag=400073)
    Event_16003703(0, asset=Assets.AEG277_037_6001, asset_1=Assets.AEG277_037_6000, asset_2=Assets.AEG277_030_6090)
    Event_16003704(0, flag=7602, flag_1=7603, flag_2=7604)
    Event_16003707(0, character=Characters.Tanith0, flag=16009270)
    Event_16003705(0, character=Characters.CrucibleKnight1, character_1=Characters.Tanith1)
    Event_16003706(0, character=Characters.CrucibleKnight1, character_1=Characters.Tanith1)
    Event_16003708()
    Event_16003709()
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9000,
        action_button_id=4350,
        item_lot=100730,
        first_flag=400073,
        last_flag=400073,
        flag=16009208,
        model_point=6101,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9001,
        action_button_id=4350,
        item_lot=100740,
        first_flag=400074,
        last_flag=400074,
        flag=16009216,
        model_point=6101,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9002,
        action_button_id=4350,
        item_lot=100750,
        first_flag=400075,
        last_flag=400075,
        flag=16009217,
        model_point=6101,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9003,
        action_button_id=4350,
        item_lot=100725,
        first_flag=400070,
        last_flag=400072,
        flag=16009270,
        model_point=6101,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9004,
        action_button_id=4350,
        item_lot=100710,
        first_flag=400071,
        last_flag=400071,
        flag=16009266,
        model_point=6101,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9000,
        action_button_id=4350,
        item_lot=100760,
        first_flag=400076,
        last_flag=400076,
        flag=16009267,
        model_point=6101,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9001,
        action_button_id=4350,
        item_lot=100770,
        first_flag=400077,
        last_flag=400077,
        flag=16009268,
        model_point=6101,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9002,
        action_button_id=4350,
        item_lot=100780,
        first_flag=400078,
        last_flag=400078,
        flag=16009269,
        model_point=6101,
    )
    CommonFunc_90005775(0, world_map_point_param_id=80110000, flag=400290, distance=-1.0)
    CommonFunc_90005775(0, world_map_point_param_id=80392000, flag=400180, distance=-1.0)
    CommonFunc_90005775(0, world_map_point_param_id=81423900, flag=400073, distance=-1.0)
    CommonFunc_90005775(0, world_map_point_param_id=83395300, flag=400074, distance=-1.0)
    CommonFunc_90005775(0, world_map_point_param_id=85505600, flag=400075, distance=-1.0)
    Event_16003710(0, character=Characters.Patches)
    Event_16003712()
    CommonFunc_90005702(0, character=Characters.RyatheScout1, flag=3423, first_flag=3420, last_flag=3424)
    Event_16003720(0, character=Characters.RyatheScout0, character_1=Characters.ManSerpent4)
    Event_16003722(0, character=Characters.RyatheScout1, character_1=Characters.ManSerpent5)
    Event_16003721(0, flag=16009208)
    Event_16003723(0, character=Characters.RyatheScout1, character_1=Characters.ManSerpent5)
    Event_16003724()
    Event_16003725()
    Event_16003726()
    Event_16003727()
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9007,
        action_button_id=4350,
        item_lot=100910,
        first_flag=400091,
        last_flag=400091,
        flag=16009337,
        model_point=0,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9009,
        action_button_id=4350,
        item_lot=100911,
        first_flag=400091,
        last_flag=400091,
        flag=16009338,
        model_point=0,
    )
    Event_16003730(0, character=Characters.KnightDiallos)
    Event_16003731(0, flag=16009417, flag_1=16002731, flag_2=16009400)
    Event_16003740(0, character=Characters.RecusantBernahl, asset=Assets.AEG277_030_9001, destination=16002710)
    Event_16003742(0, character=Characters.TalkDummy13, asset=Assets.AEG270_900_9000, asset_1=Assets.AEG277_030_9001)
    Event_16003741(0, flag=16009450)
    Event_16003743()
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9008,
        action_button_id=4350,
        item_lot=102910,
        first_flag=400291,
        last_flag=400291,
        flag=16009463,
        model_point=0,
    )
    SetRykardTalkRange(
        0,
        rykard_phase_one=Characters.RykardPhaseOne,
        rykard_phase_two=Characters.RykardPhaseTwo,
        flag=9122,
        flag_1=16002805,
        distance=195.0,
    )
    Event_16003760(0, asset__character=16000770)
    Event_16003761(0, character=Characters.RykardHatingSpirit)
    Event_16003762(
        0,
        asset=Assets.AEG099_090_9006,
        action_button_id=4110,
        gesture_param_id=2,
        first_flag=60802,
        last_flag=60802,
        flag=9122,
        model_point=0,
    )
    Event_16003763()
    Event_16003764()
    Event_16003765()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Tanith0)
    DisableBackread(Characters.Tanith1)
    DisableBackread(Characters.Patches)
    DisableBackread(Characters.RyatheScout0)
    DisableBackread(Characters.ManSerpent4)
    DisableBackread(Characters.RyatheScout1)
    DisableBackread(Characters.ManSerpent5)
    DisableBackread(Characters.KnightDiallos)
    DisableBackread(Characters.CrucibleKnight0)
    DisableBackread(Characters.CrucibleKnight1)
    DisableBackread(Characters.RecusantBernahl)
    DisableBackread(Characters.TalkDummy13)
    DisableBackread(Characters.WrithingMass)
    DisableBackread(Characters.RykardHatingSpirit)
    EnableAssetInvulnerability(Assets.AEG277_030_6090)
    EnableAssetInvulnerability(Assets.AEG277_037_6001)
    EnableAssetInvulnerability(Assets.AEG277_030_9001)
    EnableAssetInvulnerability(Assets.AEG277_037_6000)
    Event_16000519()
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Snail2, region=16002345, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Snail3, region=16002345, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Snail4, region=16002345, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Snail8, region=16002355, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Snail1, region=16002344, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Snail0, region=16002343, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Snail5, region=16002343, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Snail6, region=16002343, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Snail7, region=16002343, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.BloodhoundKnight, radius=8.0, seconds=0.0,
                                         animation_id=-1)
    RunCommonEvent(16002310, slot=0, args=(16000316, 18.0, 0.0, -1), arg_types="Iffi")
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.ManSerpent2, radius=25.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Commoner13, radius=8.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Commoner14, region=16002225, radius=5.0,
                                                 seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Commoner15, region=16002225, radius=5.0,
                                                 seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Commoner7, region=16002225, radius=8.0,
                                                 seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Commoner16, region=16002227, radius=10.0,
                                                 seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Commoner9, radius=13.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=16000210, radius=20.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Commoner10, radius=8.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Commoner11, radius=8.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.SmallerDog0, region=16002410, seconds=0.0,
                                         animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.SmallerDog1, region=16002410, seconds=0.0,
                                         animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.IronVirgin0, region=16002460, seconds=0.0,
                                         animation_id=3012)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Omenkiller, region=16002500, seconds=0.0,
                                         animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.IronVirgin2, region=16002462, seconds=0.0,
                                         animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Commoner1, region=16002203, seconds=0.0,
                                         animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Commoner2, region=16002203, seconds=0.0,
                                         animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Commoner3, region=16002203, seconds=0.0,
                                         animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Commoner4, region=16002203, seconds=0.0,
                                         animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Commoner5, region=16002203, seconds=0.0,
                                         animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.ManSerpent3, radius=20.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.ManSerpent0, region=16002314, radius=5.0,
                                                 seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.AlbinauricLookout0, radius=5.0, seconds=0.0,
                                         animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.AlbinauricLookout1, radius=6.0, seconds=0.0,
                                         animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=16000272, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.AlbinauricLookout2, radius=6.0, seconds=0.0,
                                         animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.AlbinauricLookout3, radius=3.0, seconds=0.0,
                                         animation_id=3015)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.AlbinauricLookout5, radius=6.0, seconds=1.0,
                                         animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.AlbinauricLookout6, radius=3.0, seconds=0.0,
                                         animation_id=3015)
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.AlbinauricLookout4,
        animation_id=30001,
        animation_id_1=20020,
        region=16002277,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.AlbinauricLookout7,
        region=16002278,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.AlbinauricLookout8,
        region=16002278,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.AlbinauricLookout9,
        region=16002278,
        radius=3.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.AlbinauricLookout10,
        region=16002278,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.AlbinauricLookout11,
        region=16002278,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=16000283, region=16002278, radius=5.0, seconds=0.0,
                                                 animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Commoner22, radius=14.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Commoner24, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=16000236, radius=12.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Commoner23, radius=5.0, seconds=0.0, animation_id=3002)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Commoner26, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.MagmaWyrm,
        animation_id=30001,
        animation_id_1=20001,
        region=16002510,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=Flags.MagmaWyrmDead,
        character=Characters.MagmaWyrm,
        item_lot=16002000,
        reward_delay=0.0,
        skip_reward=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.IronVirgin1, region=16002461, radius=10.0,
                                                 seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.ManSerpent8, region=16002338, radius=10.0,
                                                 seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.ManSerpent7, region=16002339, radius=5.0,
                                                 seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.ManSerpent9, region=16002339, radius=3.0,
                                                 seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.WanderingNoble0, radius=3.0, seconds=0.0,
                                         animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.WanderingNoble1, radius=3.0, seconds=0.0,
                                         animation_id=-1)
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=16000443,
        inactive_animation=30011,
        active_animation=20,
        radius=5.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.WanderingNoble2,
        inactive_animation=30011,
        active_animation=20,
        radius=5.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.WanderingNoble3,
        animation_id=30011,
        animation_id_1=20,
        region=16002446,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.ManSerpent6,
        region=16002327,
        radius=3.0,
        seconds=0.0,
        animation_id=3007,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.WanderingNoble4,
        inactive_animation=30011,
        active_animation=20,
        radius=1.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.WanderingNoble5,
        inactive_animation=30011,
        active_animation=20,
        radius=3.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    Event_16009000()
    CommonFunc_NonRespawningWithReward(0, dead_flag=16000420, character=Characters.Scarab0, item_lot=40590,
                                       reward_delay=0.0, skip_reward=0)
    CommonFunc_NonRespawningWithReward(0, 16000421, 16000421, 40592, 0.0, 0)


@RestartOnRest(16002185)
def Event_16002185(_, character: uint, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint, region: uint):
    """Event 16002185"""
    if FlagEnabled(character):
        return
    AND_1.Add(FlagEnabled(character))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    OR_10.Add(AND_1)
    OR_10.Add(AND_2)

    MAIN.Await(OR_10)

    if FlagEnabled(character):
        return
    SendNPCSummonHome(character=character)
    End()
    OR_11.Add(FlagDisabled(flag_1))
    OR_11.Add(FlagDisabled(flag_2))
    OR_11.Add(FlagDisabled(flag_3))


@RestartOnRest(16002310)
def Event_16002310(_, character: uint, radius: float, seconds: float, animation_id: int):
    """Event 16002310"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)

    MAIN.Await(OR_2)

    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    RotateToFaceEntity(character, 16002310, wait_for_completion=True)
    EnableAI(character)


@ContinueOnRest(16002500)
def Event_16002500():
    """Event 16002500"""
    GotoIfFlagDisabled(Label.L0, flag=16000500)
    EndOfAnimation(asset=Assets.AEG277_019_0500, animation_id=20)
    EndOfAnimation(asset=Assets.AEG277_081_0500, animation_id=1)
    DisableAssetActivation(Assets.AEG277_081_0500, obj_act_id=-1)
    DisableAsset(Assets.AEG270_459_2000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_8.Add(MultiplayerPending())
    AND_7.Add(Multiplayer())
    AND_8.Add(not AND_7)
    GotoIfConditionTrue(Label.L1, input_condition=AND_8)
    EnableAssetActivation(Assets.AEG277_081_0500, obj_act_id=277081)
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(AssetActivated(obj_act_id=16003501))
    AND_2.Add(MultiplayerPending())
    AND_3.Add(Multiplayer())
    AND_2.Add(not AND_3)
    OR_1.Add(AND_2)
    AND_1.Add(OR_1)

    MAIN.Await(AND_1)

    AND_6.Add(MultiplayerPending())
    AND_5.Add(Multiplayer())
    AND_6.Add(not AND_5)
    GotoIfConditionTrue(Label.L1, input_condition=AND_6)
    EnableNetworkFlag(16000500)
    EnableNetworkFlag(9021)
    PlayCutscene(16000000, cutscene_flags=0, player_id=PLAYER)
    WaitFramesAfterCutscene(frames=1)
    EndOfAnimation(asset=Assets.AEG277_019_0500, animation_id=20)
    DisableAsset(Assets.AEG270_459_2000)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAssetActivation(Assets.AEG277_081_0500, obj_act_id=277081)
    Wait(1.0)
    Restart()


@ContinueOnRest(16002505)
def Event_16002505():
    """Event 16002505"""
    DisableAsset(Assets.AEG007_434_9000)


@ContinueOnRest(16002510)
def Event_16002510():
    """Event 16002510"""
    CommonFunc_90005500(
        0,
        flag=16000510,
        flag_1=16001510,
        left=0,
        asset=Assets.AEG277_003_0500,
        asset_1=Assets.AEG277_000_0502,
        obj_act_id=16003511,
        asset_2=Assets.AEG277_000_0503,
        obj_act_id_1=16003512,
        region=16002511,
        region_1=16002512,
        flag_2=16000511,
        flag_3=16002512,
        left_1=16000514,
    )
    CommonFunc_90005500(
        0,
        flag=16000520,
        flag_1=16001520,
        left=0,
        asset=Assets.AEG277_005_0500,
        asset_1=Assets.AEG277_021_0500,
        obj_act_id=16003521,
        asset_2=Assets.AEG277_021_0501,
        obj_act_id_1=16003522,
        region=16002521,
        region_1=16002522,
        flag_2=16000521,
        flag_3=16002522,
        left_1=Flags.GodskinNobleDead,
    )
    CommonFunc_90005503(
        0,
        flag=16000525,
        flag_1=16001525,
        left=0,
        asset=Assets.AEG277_020_0500,
        asset__region=16002526,
        region=16002527,
        region_1=16002528,
        region_2=16002529,
        flag_2=16000526,
        flag_3=16002527,
        left_1=0,
    )
    CommonFunc_90005503(
        0,
        16000530,
        16001530,
        1,
        16001530,
        16002531,
        16002532,
        16002533,
        16002534,
        16000531,
        16002532,
        0,
    )


@ContinueOnRest(16000519)
def Event_16000519():
    """Event 16000519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(16000510)
    EnableFlag(16000515)
    DisableFlag(16000520)
    EnableFlag(16000525)


@RestartOnRest(16002650)
def Event_16002650():
    """Event 16002650"""
    if FlagDisabled(16000540):
        return
    if PlayerNotInOwnWorld():
        return
    EnableFlag(9080)
    DisableFlag(16000540)


@RestartOnRest(16002570)
def Event_16002570(
        _,
        asset: uint,
        area_id: uchar,
        block_id: uchar,
        cc_id: char,
        dd_id: char,
        player_start: uint,
        unk_8_12: int,
        flag: uint,
        left_flag: uint,
        cancel_flag__right_flag: uint,
):
    """Event 16002570"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, vfx_id=200, model_point=806870)
    AND_1.Add(PlayerInOwnWorld())
    AND_2.Add(MultiplayerPending())
    AND_1.Add(not AND_2)
    AND_1.Add(ActionButtonParamActivated(action_button_id=9140, entity=asset))
    AND_4.Add(MultiplayerPending())
    AND_5.Add(Multiplayer())
    AND_4.Add(not AND_5)
    AND_7.Add(PlayerInOwnWorld())
    AND_7.Add(MultiplayerPending())
    AND_7.Add(Multiplayer())
    AND_7.Add(ActionButtonParamActivated(action_button_id=9140, entity=asset))
    OR_2.Add(InvasionPending())
    OR_2.Add(Invasion())
    AND_8.Add(OR_2)
    OR_14.Add(AND_1)
    OR_14.Add(AND_4)
    OR_14.Add(AND_7)
    OR_14.Add(AND_8)

    MAIN.Await(OR_14)

    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_1)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_7)
    DeleteAssetVFX(asset)
    Wait(1.0)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisplayDialogAndSetFlags(
        message=4300,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=asset,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L6, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    AND_10.Add(MultiplayerPending())
    AND_10.Add(Multiplayer())
    OR_15.Add(AND_10)
    AND_11.Add(MultiplayerPending())
    AND_12.Add(not AND_11)
    AND_13.Add(Multiplayer())
    AND_12.Add(not AND_13)
    OR_15.Add(AND_12)
    SkipLinesIfConditionTrue(1, OR_15)
    Restart()
    OR_4.Add(InvasionPending())
    OR_4.Add(Invasion())
    if OR_4:
        return RESTART
    RotateToFaceEntity(PLAYER, asset, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490)
    Wait(3.0)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=player_start,
        model_point=10,
        copy_draw_parent=PLAYER,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    EnableNetworkFlag(16002578)
    Restart()
    SkipLines(1)
    DisableFlag(flag)
    SkipLines(1)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start, unk_8_12=unk_8_12)


@RestartOnRest(16002579)
def Event_16002579():
    """Event 16002579"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        return

    MAIN.Await(FlagEnabled(16002578))

    MoveCharacterAndCopyDrawParentWithFadeout(
        character=20000,
        destination_type=CoordEntityType.Region,
        destination=16002575,
        model_point=10,
        copy_draw_parent=20000,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    End()


@RestartOnRest(16002580)
def Event_16002580():
    """Event 16002580"""
    RegisterLadder(start_climbing_flag=16000580, stop_climbing_flag=16000581, asset=Assets.AEG277_001_0500)
    RegisterLadder(start_climbing_flag=16000582, stop_climbing_flag=16000583, asset=Assets.AEG277_002_0500)
    RegisterLadder(start_climbing_flag=16000590, stop_climbing_flag=16000591, asset=Assets.AEG277_006_0500)
    RegisterLadder(start_climbing_flag=16000592, stop_climbing_flag=16000593, asset=Assets.AEG277_007_0500)
    RegisterLadder(start_climbing_flag=16000594, stop_climbing_flag=16000595, asset=Assets.AEG277_008_0500)


@RestartOnRest(16002590)
def Event_16002590():
    """Event 16002590"""
    if FlagEnabled(16000520):
        EnableAssetActivation(Assets.AEG277_021_0501, obj_act_id=277021)
    if FlagEnabled(Flags.GodskinNobleDead):
        return
    ForceAnimation(Assets.AEG277_005_0500, 20, loop=True)
    EnableFlag(16000520)
    EnableFlag(16001520)
    Wait(2.5)
    DisableAssetActivation(Assets.AEG277_021_0501, obj_act_id=277021)

    MAIN.Await(FlagEnabled(Flags.GodskinNobleDead))

    Wait(4.0)
    DisableFlag(16001520)
    DisableFlag(16000520)


@RestartOnRest(16002620)
def Event_16002620(_, flag: uint, asset: uint):
    """Event 16002620"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(AttackedWithDamageType(attacked_entity=asset, attacker=20000))
    OR_1.Add(EntityWithinDistance(entity=asset, other_entity=PLAYER, radius=1.0))
    AND_1.Add(OR_1)

    MAIN.Await(AND_1)

    EnableNetworkFlag(flag)
    ForceAnimation(asset, 1, wait_for_completion=True)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(asset)


@RestartOnRest(16002625)
def Event_16002625():
    """Event 16002625"""
    EnableAssetInvulnerability(Assets.AEG277_011_0500)
    EnableAssetInvulnerability(Assets.AEG277_012_0500)


@RestartOnRest(16002640)
def Event_16002640():
    """Event 16002640"""
    GotoIfFlagDisabled(Label.L0, flag=16000640)
    DisableAsset(Assets.AEG270_619_2000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=16002640))

    MAIN.Await(AND_1)

    DestroyAsset(Assets.AEG270_619_2000)
    EnableFlag(16000640)


@RestartOnRest(16002670)
def Event_16002670():
    """Event 16002670"""
    DisableNetworkSync()
    AND_2.Add(CharacterInsideRegion(character=20000, region=16002670))

    MAIN.Await(AND_2)

    AddSpecialEffect(20000, 9621)
    Wait(0.10000000149011612)
    AND_3.Add(CharacterOutsideRegion(character=20000, region=16002670))

    MAIN.Await(AND_3)

    Wait(0.10000000149011612)
    RemoveSpecialEffect(20000, 9621)
    Restart()


@RestartOnRest(16002689)
def Event_16002689():
    """Event 16002689"""
    DisableNetworkSync()
    if ThisEventSlotFlagDisabled():
        DeleteVFX(16003680, erase_root_only=False)
    AND_1.Add(InsideMap(game_map=VOLCANO_MANOR))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=16002680))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=16002681))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=16002682))

    MAIN.Await(AND_1)

    CreateVFX(16003680)
    Wait(1.0)
    OR_1.Add(OutsideMap(game_map=VOLCANO_MANOR))
    OR_1.Add(CharacterOutsideRegion(character=PLAYER, region=16002680))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=16002681))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=16002682))

    MAIN.Await(OR_1)

    DeleteVFX(16003680)
    Wait(1.0)
    Restart()


@RestartOnRest(16002690)
def Event_16002690(_, flag: uint, asset: uint, asset_1: uint):
    """Event 16002690"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(Flags.RykardDead):
        return
    EnableAsset(asset)
    ForceAnimation(asset, 0)

    MAIN.Await(FlagEnabled(16002695))

    AND_1.Add(FlagEnabled(flag))
    SkipLinesIfConditionTrue(3, AND_1)
    DisableAsset(asset)
    DeleteAssetVFX(asset_1)
    End()
    CreateAssetVFX(asset_1, vfx_id=90, model_point=6102)
    ForceAnimation(asset, 0)
    EnableAssetActivation(asset, obj_act_id=99340)
    DisableFlag(16007690)


@RestartOnRest(16002691)
def Event_16002691(_, asset: uint, asset_1: uint, destination: uint):
    """Event 16002691"""
    OR_15.Add(FlagEnabled(Flags.RykardDead))
    OR_15.Add(PlayerNotInOwnWorld())
    if OR_15:
        return
    AND_2.Add(ActionButtonParamActivated(action_button_id=9532, entity=asset_1))
    AND_2.Add(FlagEnabled(16002696))
    AwaitConditionTrue(AND_2)
    DeleteAssetVFX(asset_1)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 60530)
    ForceAnimation(asset, 1)
    Wait(2.799999952316284)
    DisableAsset(asset)
    Wait(0.10000000149011612)
    AwardItemLot(16000690, host_only=False)


@RestartOnRest(16002695)
def MonitorSerpentHunterPossession():
    """Event 16002695"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(Flags.RykardDead):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=16002165))

    MAIN.Await(AND_1)

    OR_4.Add(PlayerHasWeapon(17030000, including_storage=True))
    OR_4.Add(PlayerHasWeapon(17030001, including_storage=True))
    OR_4.Add(PlayerHasWeapon(17030002, including_storage=True))
    OR_4.Add(PlayerHasWeapon(17030003, including_storage=True))
    OR_4.Add(PlayerHasWeapon(17030004, including_storage=True))
    OR_4.Add(PlayerHasWeapon(17030005, including_storage=True))
    OR_4.Add(PlayerHasWeapon(17030006, including_storage=True))
    OR_4.Add(PlayerHasWeapon(17030007, including_storage=True))
    OR_4.Add(PlayerHasWeapon(17030008, including_storage=True))
    OR_4.Add(PlayerHasWeapon(17030009, including_storage=True))
    OR_4.Add(PlayerHasWeapon(17030010, including_storage=True))
    SkipLinesIfConditionTrue(1, OR_4)
    EnableFlag(16002696)


@RestartOnRest(16002800)
def RykardDies():
    """Event 16002800"""
    if FlagEnabled(Flags.RykardDead):
        return

    MAIN.Await(HealthValue(Characters.RykardPhaseTwo) <= 0)

    Wait(4.0)
    PlaySoundEffect(16008000, 888880000, sound_type=SoundType.s_SFX)

    MAIN.Await(CharacterDead(Characters.RykardPhaseTwo))

    KillBossAndDisplayBanner(character=Characters.RykardPhaseTwo, banner_type=BannerType.DemigodFelled)
    if PlayerInOwnWorld():
        TriggerMultiplayerEvent(event_id=0)
    EnableFlag(Flags.RykardDead)
    EnableFlag(9122)
    if PlayerInOwnWorld():
        EnableFlag(61122)
    RemoveSpecialEffect(PLAYER, 1908)
    DeleteVFX(16002810)
    DeleteVFX(16002811)
    DeleteVFX(16002812)
    DeleteVFX(16002813)
    DeleteVFX(16002814)
    ChangeCamera(normal_camera_id=0, locked_camera_id=0)


@RestartOnRest(16002810)
def RykardBattleTrigger():
    """Event 16002810"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.RykardDead)
    DisableCharacter(CharacterGroups.RykardBoss)
    DisableAnimations(CharacterGroups.RykardBoss)
    Kill(CharacterGroups.RykardBoss)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(CharacterGroups.RykardBoss)
    DisableCharacter(Characters.RykardPhaseTwo)
    DisableAnimations(Characters.RykardPhaseTwo)
    DisableCharacter(Characters.CLONE_RykardPhaseTwo)
    DisableAnimations(Characters.CLONE_RykardPhaseTwo)
    SetCharacterFadeOnEnable(character=Characters.RykardPhaseTwo, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RykardPhaseTwo, state=False)
    AND_1.Add(PlayerInOwnWorld())
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.RykardPhaseOne, radius=40.0))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.CLONE_RykardPhaseOne, radius=40.0))
    AND_1.Add(OR_2)
    OR_1.Add(AND_1)
    # TODO: Interesting - how would Rykard Phase Two be interacted with here?
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.RykardPhaseTwo, attacker=PLAYER))
    OR_1.Add(CharacterHasStateInfo(character=Characters.RykardPhaseTwo, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.RykardPhaseTwo, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.RykardPhaseTwo, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.RykardPhaseTwo, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.RykardPhaseTwo, state_info=260))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.CLONE_RykardPhaseTwo, attacker=PLAYER))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_RykardPhaseTwo, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_RykardPhaseTwo, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_RykardPhaseTwo, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_RykardPhaseTwo, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_RykardPhaseTwo, state_info=260))

    MAIN.Await(OR_1)

    EnableNetworkFlag(16000801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(16002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=16002800))

    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(PLAYER, 1908)
    EnableAI(Characters.RykardPhaseOne)
    EnableAI(Characters.CLONE_RykardPhaseOne)
    SetNetworkUpdateRate(Characters.RykardPhaseOne, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_RykardPhaseOne, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.RykardPhaseOne, name=NameText.GodDevouringSerpent, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_RykardPhaseOne, name=NameText.CLONE_GodDevouringSerpent, bar_slot=0)
    EnableFlag(16002803)
    SetLockOnPoint(character=Characters.RykardPhaseOne, lock_on_model_point=220, state=True)
    SetLockOnPoint(character=Characters.RykardPhaseOne, lock_on_model_point=221, state=False)
    SetLockOnPoint(character=Characters.CLONE_RykardPhaseOne, lock_on_model_point=220, state=True)
    SetLockOnPoint(character=Characters.CLONE_RykardPhaseOne, lock_on_model_point=221, state=False)
    EnableFlag(16002801)
    ForceAnimation(Characters.RykardPhaseOne, 20002)
    Wait(0.2)
    ForceAnimation(Characters.CLONE_RykardPhaseOne, 20002)


@RestartOnRest(16002811)
def RykardPhaseTwoTransition():
    """Event 16002811"""
    if FlagEnabled(Flags.RykardDead):
        return
    AND_1.Add(PlayerInOwnWorld())
    # TODO: Is Rykard immortal? Could have them share a health bar.
    AND_1.Add(HealthRatio(Characters.RykardPhaseOne) <= 0.01)
    AND_1.Add(HealthRatio(Characters.CLONE_RykardPhaseOne) <= 0.01)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.RykardPhaseOne, 11955))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.CLONE_RykardPhaseOne, 11955))

    MAIN.Await(AND_1)

    Wait(0.1)

    # Restart if EITHER Rykard has effect 11955.
    SkipLinesIfCharacterHasSpecialEffect(1, Characters.CLONE_RykardPhaseOne, 11955)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(1, Characters.RykardPhaseOne, 11955)
    Restart()

    ForceAnimation(Characters.RykardPhaseOne, 20001)
    ForceAnimation(Characters.CLONE_RykardPhaseOne, 20001)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterAlive(PLAYER))
    AND_2.Add(CharacterHasSpecialEffect(Characters.RykardPhaseOne, 11920))  # only monitor one (short duration)

    MAIN.Await(AND_2)

    ForceAnimation(Characters.RykardPhaseOne, 30001, loop=True)
    ForceAnimation(Characters.CLONE_RykardPhaseOne, 30001, loop=True)
    RemoveSpecialEffect(Characters.RykardPhaseOne, 11943)
    RemoveSpecialEffect(Characters.RykardPhaseOne, 11948)
    RemoveSpecialEffect(Characters.CLONE_RykardPhaseOne, 11943)
    RemoveSpecialEffect(Characters.CLONE_RykardPhaseOne, 11948)
    OR_9.Add(HealthRatio(PLAYER) == 0.0)
    OR_9.Add(CharacterDead(PLAYER))
    if OR_9:
        return
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=16000020,
            cutscene_flags=0,
            move_to_region=16002830,
            map_id=16,
            player_id=PLAYER,
            unk_20_24=16,
            unk_24_25=False,
        )
    else:
        PlayCutscene(16000020, cutscene_flags=0, player_id=PLAYER)
    WaitFramesAfterCutscene(frames=1)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=-4.0, y_angle=0.0)
    EnableFlag(16002802)
    AddSpecialEffect(Characters.RykardPhaseTwo, 11901)
    AddSpecialEffect(Characters.CLONE_RykardPhaseTwo, 11901)
    DisableCharacter(Characters.RykardPhaseOne)
    DisableAnimations(Characters.RykardPhaseOne)
    DisableCharacter(Characters.CLONE_RykardPhaseOne)
    DisableAnimations(Characters.CLONE_RykardPhaseOne)
    EnableCharacter(Characters.RykardPhaseTwo)
    EnableCharacter(Characters.CLONE_RykardPhaseTwo)
    SetNetworkUpdateRate(Characters.RykardPhaseTwo, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_RykardPhaseTwo, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    CreateVFX(16002814)
    Move(
        Characters.RykardPhaseTwo,
        destination=RegionPoints.RykardPhaseTwoStart,
        destination_type=CoordEntityType.Region,
        model_point=0,
        copy_draw_parent=Characters.RykardPhaseOne,
    )
    Move(
        Characters.CLONE_RykardPhaseTwo,
        destination=RegionPoints.CLONE_RykardPhaseTwoStart,
        destination_type=CoordEntityType.Region,
        model_point=0,
        copy_draw_parent=Characters.CLONE_RykardPhaseOne,  # why not
    )
    WaitFrames(frames=1)
    EnableAnimations(Characters.RykardPhaseTwo)
    EnableAnimations(Characters.CLONE_RykardPhaseTwo)
    EnableAI(Characters.RykardPhaseTwo)
    EnableAI(Characters.CLONE_RykardPhaseTwo)
    EnableBossHealthBar(Characters.RykardPhaseTwo, name=NameText.RykardLordOfBlasphemy, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_RykardPhaseTwo, name=NameText.CLONE_RykardLordOfBlasphemy, bar_slot=0)
    SetLockOnPoint(character=Characters.RykardPhaseTwo, lock_on_model_point=220, state=False)
    SetLockOnPoint(character=Characters.RykardPhaseTwo, lock_on_model_point=221, state=True)
    SetLockOnPoint(character=Characters.CLONE_RykardPhaseTwo, lock_on_model_point=220, state=False)
    SetLockOnPoint(character=Characters.CLONE_RykardPhaseTwo, lock_on_model_point=221, state=True)
    ForceAnimation(Characters.RykardPhaseTwo, 20002, wait_for_completion=False)
    Wait(0.2)  # to avoid animation sync
    ForceAnimation(Characters.CLONE_RykardPhaseTwo, 20002, wait_for_completion=True)


@RestartOnRest(16002812)
def RykardPhaseTwoHalfHealthEffect(_, rykard: uint):
    """Event 16002812"""
    if FlagEnabled(Flags.RykardDead):
        return
    AND_1.Add(HealthRatio(rykard) <= 0.5)

    MAIN.Await(AND_1)

    AddSpecialEffect(rykard, 11902)


@RestartOnRest(16002822)
def RykardPhaseTwoEffect11930(_, rykard: uint):
    """Event 16002822"""
    AND_1.Add(CharacterBackreadEnabled(rykard))
    OR_1.Add(CharacterHasSpecialEffect(rykard, 11901))
    OR_1.Add(CharacterHasSpecialEffect(rykard, 11902))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterHasSpecialEffect(rykard, 11940))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(rykard, 11930))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(rykard, 11931))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(rykard, 11941))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(rykard, 11946))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(rykard, 11947))

    MAIN.Await(AND_1)

    Wait(3.0)
    CreateVFX(16002810)
    AddSpecialEffect(rykard, 11930)
    Wait(1.0)
    Restart()


@RestartOnRest(16002824)
def RykardPhaseTwoEffect11931(_, rykard: uint):
    """Event 16002824"""
    AND_1.Add(CharacterBackreadEnabled(rykard))
    OR_1.Add(CharacterHasSpecialEffect(rykard, 11901))
    OR_1.Add(CharacterHasSpecialEffect(rykard, 11902))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterHasSpecialEffect(rykard, 11940))
    AND_1.Add(CharacterHasSpecialEffect(rykard, 11930))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(rykard, 11931))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(rykard, 11941))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(rykard, 11946))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(rykard, 11947))

    MAIN.Await(AND_1)

    Wait(3.0)
    CreateVFX(16002811)
    DeleteVFX(16002810)
    AddSpecialEffect(rykard, 11931)
    RemoveSpecialEffect(rykard, 11930)
    Wait(1.0)
    Restart()


@RestartOnRest(16002826)
def RykardPhaseTwoEffect11941(_, rykard: uint):
    """Event 16002826"""
    AND_1.Add(CharacterBackreadEnabled(rykard))
    OR_1.Add(CharacterHasSpecialEffect(rykard, 11901))
    OR_1.Add(CharacterHasSpecialEffect(rykard, 11902))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterHasSpecialEffect(rykard, 11940))
    AND_1.Add(CharacterHasSpecialEffect(rykard, 11931))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(rykard, 11930))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(rykard, 11941))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(rykard, 11946))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(rykard, 11947))

    MAIN.Await(AND_1)

    Wait(3.0)
    CreateVFX(16002812)
    DeleteVFX(16002811)
    AddSpecialEffect(rykard, 11941)
    RemoveSpecialEffect(rykard, 11931)
    Wait(1.0)
    Restart()


@RestartOnRest(16002830)
def RykardPhaseTwoEffect11945(_, rykard: uint):
    """Event 16002830"""
    if FlagEnabled(Flags.RykardDead):
        return

    MAIN.Await(CharacterHasSpecialEffect(rykard, 11942))

    CreateVFX(16002813)
    RemoveSpecialEffect(rykard, 11941)
    AddSpecialEffect(rykard, 11947)
    ShootProjectile(
        owner_entity=rykard,
        source_entity=Assets.AEG003_316_9002,
        model_point=100,
        behavior_id=247100510,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=rykard,
        source_entity=Assets.AEG003_316_9002,
        model_point=100,
        behavior_id=247100810,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=rykard,
        source_entity=Assets.AEG003_316_9002,
        model_point=100,
        behavior_id=247100820,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=rykard,
        source_entity=Assets.AEG003_316_9002,
        model_point=100,
        behavior_id=247100830,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(25.0)
    AddSpecialEffect(rykard, 11945)
    Wait(1.0)
    Restart()


@RestartOnRest(16002832)
def RykardPhaseTwoEffectsClear(_, rykard: uint):
    """Event 16002832"""
    MAIN.Await(CharacterHasSpecialEffect(rykard, 11946))

    DeleteVFX(16002810)
    DeleteVFX(16002811)
    DeleteVFX(16002812)
    DeleteVFX(16002813)
    RemoveSpecialEffect(rykard, 11941)
    RemoveSpecialEffect(rykard, 11945)
    RemoveSpecialEffect(rykard, 11947)
    RemoveSpecialEffect(rykard, 11946)
    Wait(1.0)
    Restart()


@RestartOnRest(16002836)
def RykardCameraTrigger1():
    """Event 16002836"""
    DisableNetworkSync()
    if FlagEnabled(Flags.RykardDead):
        return
    if FlagEnabled(16002802):
        return
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AND_1.Add(FlagDisabled(16002802))
    AND_1.Add(FlagEnabled(16002801))
    AND_1.Add(FlagEnabled(16002805))

    MAIN.Await(AND_1)

    ChangeCamera(normal_camera_id=4710, locked_camera_id=4712)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(16002802))
    AND_2.Add(FlagEnabled(16002806))
    AND_2.Add(FlagEnabled(16002801))

    MAIN.Await(AND_2)

    ChangeCamera(normal_camera_id=4710, locked_camera_id=4712)


@RestartOnRest(16002838)
def RykardCameraTrigger2():
    """Event 16002838"""
    DisableNetworkSync()
    if FlagEnabled(Flags.RykardDead):
        return
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AND_1.Add(FlagEnabled(16002802))
    AND_1.Add(FlagEnabled(16002805))

    MAIN.Await(AND_1)

    ChangeCamera(normal_camera_id=4710, locked_camera_id=4711)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagEnabled(16002802))
    AND_2.Add(FlagEnabled(16002806))

    MAIN.Await(AND_2)

    ChangeCamera(normal_camera_id=4710, locked_camera_id=4711)


@RestartOnRest(16002840)
def RykardSpiritAshesCheck():
    """Event 16002840"""
    DisableNetworkSync()
    if FlagEnabled(Flags.RykardDead):
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=16002164))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 1908)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(1.0)
    Restart()


@RestartOnRest(16002842)
def RykardCoopBuffs(_, rykard: uint):
    """Event 16002842"""
    if FlagEnabled(Flags.RykardDead):
        return
    OR_10.Add(CharacterHasSpecialEffect(rykard, 1929))
    OR_10.Add(CharacterHasSpecialEffect(rykard, 1930))
    OR_10.Add(CharacterHasSpecialEffect(rykard, 1931))
    OR_10.Add(CharacterHasSpecialEffect(rykard, 1932))

    MAIN.Await(OR_10)

    GotoIfCharacterHasSpecialEffect(Label.L0, character=rykard, special_effect=1929)
    GotoIfCharacterHasSpecialEffect(Label.L1, character=rykard, special_effect=1930)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=rykard, special_effect=1931)
    GotoIfCharacterHasSpecialEffect(Label.L3, character=rykard, special_effect=1932)

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfCoopClientCountComparison(2, comparison_type=ComparisonType.Equal, value=0)
    SkipLinesIfCoopClientCountComparison(3, comparison_type=ComparisonType.Equal, value=1)
    SkipLinesIfCoopClientCountComparison(4, comparison_type=ComparisonType.Equal, value=2)
    AddSpecialEffect(rykard, 19450)
    Goto(Label.L10)
    AddSpecialEffect(rykard, 19451)
    Goto(Label.L10)
    AddSpecialEffect(rykard, 19452)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfCoopClientCountComparison(2, comparison_type=ComparisonType.Equal, value=0)
    SkipLinesIfCoopClientCountComparison(3, comparison_type=ComparisonType.Equal, value=1)
    SkipLinesIfCoopClientCountComparison(4, comparison_type=ComparisonType.Equal, value=2)
    AddSpecialEffect(rykard, 19455)
    Goto(Label.L10)
    AddSpecialEffect(rykard, 19456)
    Goto(Label.L10)
    AddSpecialEffect(rykard, 19457)
    Goto(Label.L10)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfCoopClientCountComparison(2, comparison_type=ComparisonType.Equal, value=0)
    SkipLinesIfCoopClientCountComparison(3, comparison_type=ComparisonType.Equal, value=1)
    SkipLinesIfCoopClientCountComparison(4, comparison_type=ComparisonType.Equal, value=2)
    AddSpecialEffect(rykard, 19460)
    Goto(Label.L10)
    AddSpecialEffect(rykard, 19461)
    Goto(Label.L10)
    AddSpecialEffect(rykard, 19462)
    Goto(Label.L10)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfCoopClientCountComparison(2, comparison_type=ComparisonType.Equal, value=0)
    SkipLinesIfCoopClientCountComparison(3, comparison_type=ComparisonType.Equal, value=1)
    SkipLinesIfCoopClientCountComparison(4, comparison_type=ComparisonType.Equal, value=2)
    AddSpecialEffect(rykard, 19465)
    Goto(Label.L10)
    AddSpecialEffect(rykard, 19466)
    Goto(Label.L10)
    AddSpecialEffect(rykard, 19467)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    WaitFrames(frames=15)
    Restart()


@RestartOnRest(16002846)
def Event_16002846(
        _,
        flag: uint,
        entity: uint,
        region: uint,
        flag_1: uint,
        character: uint,
        action_button_id: int,
        left: uint,
        region_1: uint,
):
    """Event 16002846"""
    GotoIfFlagEnabled(Label.L10, flag=flag)
    WaitFrames(frames=1)
    GotoIfUnsignedEqual(Label.L0, left=left, right=0)
    GotoIfFlagEnabled(Label.L0, flag=left)
    if UnsignedNotEqual(left=region_1, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_1.Add(FlagEnabled(left))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(flag))

    MAIN.Await(OR_2)

    if FlagEnabled(flag):
        return RESTART
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagDisabled(flag))
    AND_3.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    OR_3.Add(FlagEnabled(flag))
    OR_3.Add(AND_3)

    MAIN.Await(OR_3)

    GotoIfPlayerNotInOwnWorld(Label.L2)
    if FlagEnabled(flag):
        return RESTART
    SuppressSoundForFogGate(duration=5.0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=PLAYER, special_effect=4250)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    SkipLines(1)
    RotateToFaceEntity(PLAYER, region, animation=60060)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_5.Add(OR_4)
    AND_4.Add(OR_5)
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(FlagDisabled(flag))
    OR_6.Add(AND_4)
    OR_6.Add(FlagEnabled(flag))

    MAIN.Await(OR_6)

    if FlagEnabled(flag):
        return RESTART
    RestartIfFinishedConditionTrue(input_condition=OR_4)
    AND_8.Add(PlayerInOwnWorld())
    AND_8.Add(EntityWithinDistance(entity=Characters.RykardPhaseOne, other_entity=PLAYER, radius=40.0))

    MAIN.Await(AND_8)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(character)
    EnableNetworkFlag(flag_1)
    if PlayerNotInOwnWorld():
        return
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(PlayerInOwnWorld())
    AND_10.Add(FlagEnabled(flag))
    OR_10.Add(Invasion())
    OR_10.Add(InvasionPending())
    AND_10.Add(OR_10)
    AND_10.Add(ActionButtonParamActivated(action_button_id=10000, entity=entity))

    MAIN.Await(AND_10)

    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()


@RestartOnRest(16002849)
def RykardFogGateEvents():
    """Event 16002849"""
    Event_16002846(
        0,
        flag=Flags.RykardDead,
        entity=Assets.AEG099_003_9000,
        region=16002801,
        flag_1=16002805,
        character=CharacterGroups.RykardBoss,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.RykardDead,
        fog_asset=Assets.AEG099_003_9000,
        fog_region=16002801,
        host_entered_fog_flag=16002805,
        summon_entered_fog_flag=16002806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.RykardDead, fog_asset=Assets.AEG099_003_9000, model_point=3, required_flag=0)
    CommonFunc_ControlBossMusic(0, Flags.RykardDead, 471000, 16002805, 16002806, 16002803, 16002802, 0, 0)


@RestartOnRest(16002850)
def GodskinNobleDies():
    """Event 16002850"""
    if FlagEnabled(Flags.GodskinNobleDead):
        return

    MAIN.Await(HealthValue(Characters.GodskinNoble) <= 0)

    Wait(4.0)
    PlaySoundEffect(16008000, 888880000, sound_type=SoundType.s_SFX)

    MAIN.Await(CharacterDead(Characters.GodskinNoble))

    KillBossAndDisplayBanner(character=Characters.GodskinNoble, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(Flags.GodskinNobleDead)
    EnableFlag(9121)
    if PlayerInOwnWorld():
        EnableFlag(61121)
    EnableTreasure(asset=Assets.AEG099_990_9001)
    DeleteAssetVFX(Assets.AEG099_990_9002)


@RestartOnRest(16002855)
def GodskinNobleBattleTrigger():
    """Event 16002855"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.GodskinNobleDead)
    DisableCharacter(Characters.GodskinNoble)
    DisableAnimations(Characters.GodskinNoble)
    Kill(Characters.GodskinNoble)
    DisableCharacter(Characters.CLONE_GodskinNoble)
    DisableAnimations(Characters.CLONE_GodskinNoble)
    Kill(Characters.CLONE_GodskinNoble)
    DeleteAssetVFX(Assets.AEG099_990_9002)
    if FlagDisabled(16007710):
        EnableTreasure(asset=Assets.AEG099_990_9001)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableTreasure(asset=Assets.AEG099_990_9001)
    CreateAssetVFX(Assets.AEG099_990_9002, vfx_id=90, model_point=6101)
    DisableAI(Characters.GodskinNoble)
    DisableAI(Characters.CLONE_GodskinNoble)
    GotoIfFlagEnabled(Label.L1, flag=16000851)
    DisableCharacter(Characters.GodskinNoble)
    DisableAnimations(Characters.GodskinNoble)
    DisableCharacter(Characters.CLONE_GodskinNoble)
    DisableAnimations(Characters.CLONE_GodskinNoble)
    ForceAnimation(Characters.GodskinNoble, 30001, loop=True)
    ForceAnimation(Characters.CLONE_GodskinNoble, 30001, loop=True)
    AND_1.Add(PlayerInOwnWorld())
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.GodskinNoble, radius=26.0))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.CLONE_GodskinNoble, radius=26.0))
    AND_1.Add(OR_2)
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.GodskinNoble, attacker=PLAYER))
    OR_1.Add(CharacterHasStateInfo(character=Characters.GodskinNoble, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.GodskinNoble, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.GodskinNoble, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.GodskinNoble, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.GodskinNoble, state_info=260))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.CLONE_GodskinNoble, attacker=PLAYER))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_GodskinNoble, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_GodskinNoble, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_GodskinNoble, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_GodskinNoble, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.CLONE_GodskinNoble, state_info=260))

    MAIN.Await(OR_1)

    EnableNetworkFlag(16000851)
    EnableCharacter(Characters.GodskinNoble)
    EnableAnimations(Characters.GodskinNoble)
    EnableAI(Characters.GodskinNoble)
    EnableCharacter(Characters.CLONE_GodskinNoble)
    EnableAnimations(Characters.CLONE_GodskinNoble)
    EnableAI(Characters.CLONE_GodskinNoble)
    ForceAnimation(Characters.GodskinNoble, 20001, wait_for_completion=False)
    ForceAnimation(Characters.CLONE_GodskinNoble, 20001, wait_for_completion=True)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(16002855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=16002850))

    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.GodskinNoble)
    EnableAI(Characters.CLONE_GodskinNoble)
    SetNetworkUpdateRate(Characters.GodskinNoble, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_GodskinNoble, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.GodskinNoble, name=NameText.GodskinNoble, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_GodskinNoble, name=NameText.CLONE_GodskinNoble, bar_slot=0)


@RestartOnRest(16002860)
def IronVirginsDie():
    """Event 16002860"""
    if FlagEnabled(Flags.IronVirginsDead):
        return
    AND_1.Add(CharacterDead(Characters.IronVirginBoss1))
    AND_1.Add(CharacterDead(Characters.IronVirginBoss0))
    AND_1.Add(CharacterDead(Characters.CLONE_IronVirginBoss1))
    AND_1.Add(CharacterDead(Characters.CLONE_IronVirginBoss0))

    MAIN.Await(AND_1)

    KillBossAndDisplayBanner(character=Characters.IronVirginBoss1, banner_type=BannerType.EnemyFelled)
    EnableFlag(Flags.IronVirginsDead)
    EnableFlag(9129)
    if PlayerInOwnWorld():
        EnableFlag(61129)


@RestartOnRest(16002865)
def IronVirginsBattleTrigger():
    """Event 16002865"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.IronVirginsDead)
    DisableCharacter(Characters.IronVirginBoss1)
    DisableAnimations(Characters.IronVirginBoss1)
    Kill(Characters.IronVirginBoss1)
    DisableCharacter(Characters.IronVirginBoss0)
    DisableAnimations(Characters.IronVirginBoss0)
    Kill(Characters.IronVirginBoss0)
    DisableCharacter(Characters.CLONE_IronVirginBoss1)
    DisableAnimations(Characters.CLONE_IronVirginBoss1)
    Kill(Characters.CLONE_IronVirginBoss1)
    DisableCharacter(Characters.CLONE_IronVirginBoss0)
    DisableAnimations(Characters.CLONE_IronVirginBoss0)
    Kill(Characters.CLONE_IronVirginBoss0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.IronVirginBoss1)
    DisableAI(Characters.IronVirginBoss0)
    DisableAI(Characters.CLONE_IronVirginBoss1)
    DisableAI(Characters.CLONE_IronVirginBoss0)
    AND_2.Add(FlagEnabled(16002865))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=16002860))

    MAIN.Await(AND_2)

    EnableAI(Characters.IronVirginBoss1)
    EnableAI(Characters.IronVirginBoss0)
    EnableAI(Characters.CLONE_IronVirginBoss1)
    EnableAI(Characters.CLONE_IronVirginBoss0)
    SetNetworkUpdateRate(Characters.IronVirginBoss1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.IronVirginBoss0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_IronVirginBoss1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_IronVirginBoss0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    # TODO: Can't use four bar slots, so I'd rather two than three.
    EnableBossHealthBar(Characters.IronVirginBoss1, name=904470000)
    EnableBossHealthBar(Characters.IronVirginBoss0, name=904470001, bar_slot=1)


@ContinueOnRest(16002889)
def IronVirginsFogGateEvents():
    """Event 16002889"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.IronVirginsDead,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=16002860,
        host_entered_fog_flag=16002865,
        boss_characters=16005860,
        action_button_id=10000,
        first_time_done_flag=0,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.IronVirginsDead,
        fog_asset=Assets.AEG099_002_9000,
        fog_region=16002860,
        host_entered_fog_flag=16002865,
        summon_entered_fog_flag=16002866,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.IronVirginsDead, fog_asset=Assets.AEG099_002_9000, model_point=4, required_flag=0)
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.IronVirginsDead, fog_asset=Assets.AEG099_002_9001, model_point=5, required_flag=0)
    CommonFunc_ControlBossMusic(0, Flags.IronVirginsDead, 931000, 16002865, 16002866, 0, 16002862, 0, 0)


@ContinueOnRest(16002899)
def GodskinNobleFogGateEvents():
    """Event 16002899"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.GodskinNobleDead,
        fog_asset=Assets.AEG099_003_0500,
        fog_region=16002850,
        host_entered_fog_flag=16002855,
        boss_characters=16005850,
        action_button_id=10000,
        first_time_done_flag=16000851,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.GodskinNobleDead,
        fog_asset=Assets.AEG099_003_0500,
        fog_region=16002850,
        host_entered_fog_flag=16002855,
        summon_entered_fog_flag=16002856,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.GodskinNobleDead, fog_asset=Assets.AEG099_003_0500, model_point=4, required_flag=16000851)
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.GodskinNobleDead, fog_asset=Assets.AEG099_003_0501, model_point=3, required_flag=0)
    CommonFunc_ControlBossMusic(0, Flags.GodskinNobleDead, 356000, 16002855, 16002856, 0, 16002852, 0, 0)


@RestartOnRest(16009000)
def Event_16009000():
    """Event 16009000"""
    AwaitFlagEnabled(flag=16009213)

    MAIN.Await(CharacterBackreadEnabled(PLAYER))

    PlayCutsceneToPlayerAndWarp(
        cutscene_id=16000010,
        cutscene_flags=0,
        move_to_region=16002840,
        map_id=16000000,
        player_id=PLAYER,
        unk_20_24=0,
        unk_24_25=False,
    )
    WaitFramesAfterCutscene(frames=1)
    DisableFlag(16009213)
    ForceAnimation(20000, 60451)


@RestartOnRest(16002900)
def Event_16002900():
    """Event 16002900"""
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=Characters.RykardPhaseOne, radius=30.0))

    SetLockedCameraSlot(area_id=16, block_id=0, camera_slot=1)

    MAIN.Await(EntityBeyondDistance(entity=PLAYER, other_entity=Characters.RykardPhaseOne, radius=30.0))

    SetLockedCameraSlot(area_id=16, block_id=0, camera_slot=0)
    Restart()


@RestartOnRest(16003700)
def Event_16003700(_, character: uint, destination: uint, character_1: uint):
    """Event 16003700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3100):
        DisableFlag(16009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3105)
    GotoIfFlagEnabled(Label.L5, flag=3106)
    GotoIfFlagEnabled(Label.L5, flag=3107)
    GotoIfFlagEnabled(Label.L5, flag=3108)
    DisableCharacter(character)
    DisableBackread(character)
    EnableGravity(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    OR_3.Add(FlagEnabled(3105))
    OR_3.Add(FlagEnabled(3106))
    OR_3.Add(FlagEnabled(3107))
    OR_3.Add(FlagEnabled(3108))

    MAIN.Await(OR_3)

    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3100)
    GotoIfFlagEnabled(Label.L2, flag=3101)
    GotoIfFlagEnabled(Label.L3, flag=3102)
    GotoIfFlagEnabled(Label.L4, flag=3103)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    DisableGravity(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character, 90100)
    ForceAnimation(character_1, 930010)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

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
    OR_4.Add(FlagEnabled(3105))
    OR_4.Add(FlagEnabled(3106))
    OR_4.Add(FlagEnabled(3107))
    OR_4.Add(FlagEnabled(3108))

    MAIN.Await(not OR_4)

    Restart()


@RestartOnRest(16003701)
def Event_16003701(_, character: uint, character_1: uint, asset: uint):
    """Event 16003701"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3100):
        DisableFlag(16009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3109)
    GotoIfFlagEnabled(Label.L5, flag=3110)
    GotoIfFlagEnabled(Label.L5, flag=3111)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    OR_3.Add(FlagEnabled(3109))
    OR_3.Add(FlagEnabled(3110))
    OR_3.Add(FlagEnabled(3111))

    MAIN.Await(OR_3)

    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    MoveAssetToCharacter(asset, character=character)
    GotoIfFlagEnabled(Label.L1, flag=3100)
    GotoIfFlagEnabled(Label.L2, flag=3101)
    GotoIfFlagEnabled(Label.L3, flag=3102)
    GotoIfFlagEnabled(Label.L4, flag=3103)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90101)
    if FlagEnabled(3110):
        ForceAnimation(character, 90102)
        DisableAnimations(character)
    if FlagEnabled(3111):
        DisableCharacter(character)
        DisableBackread(character)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    if FlagEnabled(3111):
        DisableCharacter(character)
        DisableBackread(character)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    if FlagEnabled(3111):
        DisableCharacter(character)
        DisableBackread(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    if FlagEnabled(3111):
        DisableCharacter(character)
        DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3109))
    OR_4.Add(FlagEnabled(3110))
    OR_4.Add(FlagEnabled(3111))

    MAIN.Await(not OR_4)

    Restart()


@RestartOnRest(16003702)
def Event_16003702(_, flag: uint):
    """Event 16003702"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3105):
        return

    MAIN.Await(FlagEnabled(flag))

    EnableFlag(3118)
    End()


@RestartOnRest(16003703)
def Event_16003703(_, asset: uint, asset_1: uint, asset_2: uint):
    """Event 16003703"""
    RestoreAsset(asset)
    EnableAssetInvulnerability(asset)
    RestoreAsset(asset_1)
    EnableAssetInvulnerability(asset_1)
    RestoreAsset(asset_2)
    EnableAssetInvulnerability(asset_2)
    End()


@RestartOnRest(16003704)
def Event_16003704(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 16003704"""
    AND_1.Add(EventValue(flag=16009260, bit_count=3) >= 3)
    if AND_1:
        return
    if FlagEnabled(3109):
        return
    if FlagEnabled(3110):
        return
    if FlagEnabled(3111):
        return
    ClearEventValue(16009260, bit_count=3)
    if FlagDisabled(flag):
        return
    IncrementEventValue(16009260, bit_count=3, max_value=3)
    if FlagDisabled(flag_1):
        return
    IncrementEventValue(16009260, bit_count=3, max_value=3)
    EnableFlag(3438)
    if FlagDisabled(flag_2):
        return
    IncrementEventValue(16009260, bit_count=3, max_value=3)
    EnableFlag(3118)
    End()


@RestartOnRest(16003705)
def Event_16003705(_, character: uint, character_1: uint):
    """Event 16003705"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    DisableCharacter(character)
    DisableBackread(character)
    DisableImmortality(character_1)
    AND_1.Add(FlagEnabled(16009265))
    AND_1.Add(FlagDisabled(16009264))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    if FlagEnabled(16009264):
        return
    if FlagDisabled(3109):
        return
    DisableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character_1)
    SetCharacterTalkRange(character=character_1, distance=50.0)
    AND_2.Add(AttackedWithDamageType(attacked_entity=character_1, attacker=PLAYER))
    AND_2.Add(FlagDisabled(9000))

    MAIN.Await(AND_2)

    EnableFlag(16009265)
    ForceAnimation(character_1, 90201)
    SetCharacterTalkRange(character=character_1, distance=17.0)
    Wait(7.0)
    EnableCharacter(character)
    ForceAnimation(character, 20021)
    DisplayFlashingMessageWithPriority(text=80020, priority=0, should_interrupt=False)
    Wait(1.0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    EnableBackread(character)
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character_1, radius=10.0))
    AND_3.Add(FlagDisabled(9000))

    MAIN.Await(AND_3)

    DisableBackread(character_1)
    Wait(2.0)
    EnableCharacter(character)
    ForceAnimation(character, 20021)
    DisplayFlashingMessageWithPriority(text=80020, priority=0, should_interrupt=False)
    Wait(1.0)
    Wait(4.0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()


@RestartOnRest(16003706)
def Event_16003706(_, character: uint, character_1: uint):
    """Event 16003706"""
    if FlagEnabled(16009264):
        return

    MAIN.Await(CharacterDead(character))

    DisplayFlashingMessageWithPriority(text=80021, priority=0, should_interrupt=False)
    EnableFlag(16009264)
    AwardItemLot(16000950, host_only=False)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    DisableAnimations(character_1)
    ForceAnimation(character_1, 90007)
    Wait(2.0)
    ForceAnimation(character_1, 90202)
    End()


@RestartOnRest(16003707)
def Event_16003707(_, character: uint, flag: uint):
    """Event 16003707"""
    if PlayerNotInOwnWorld():
        return
    AND_5.Add(FlagEnabled(400070))
    AND_5.Add(FlagEnabled(400072))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableFlag(flag)
    End()
    GotoIfFlagEnabled(Label.L1, flag=flag)
    AND_1.Add(FlagDisabled(16009208))
    AND_1.Add(FlagEnabled(Flags.RykardDead))
    AND_1.Add(CharacterBackreadDisabled(character))
    AND_2.Add(FlagDisabled(400070))
    AND_2.Add(FlagEnabled(Flags.RykardDead))
    AND_2.Add(FlagRangeAnyEnabled(flag_range=(3109, 3111)))
    AND_2.Add(CharacterBackreadDisabled(character))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)

    MAIN.Await(OR_1)

    EnableFlag(flag)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_6.Add(FlagEnabled(400070))
    AND_6.Add(FlagEnabled(400072))

    MAIN.Await(AND_6)

    DisableFlag(flag)
    End()


@RestartOnRest(16003708)
def Event_16003708():
    """Event 16003708"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(16009266):
        return
    GotoIfFlagEnabled(Label.L1, flag=16009264)

    MAIN.Await(FlagEnabled(16009264))

    Wait(3.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(16009266)
    End()


@RestartOnRest(16003709)
def Event_16003709():
    """Event 16003709"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(16009267)
    DisableFlag(16009268)
    DisableFlag(16009269)
    if FlagEnabled(400078):
        return
    if FlagDisabled(Flags.RykardDead):
        return
    if FlagDisabled(16009208):
        return
    AND_3.Add(FlagEnabled(400075))
    AND_3.Add(FlagEnabled(7604))
    AND_3.Add(FlagDisabled(400078))
    GotoIfConditionTrue(Label.L3, input_condition=AND_3)
    AND_2.Add(FlagEnabled(400074))
    AND_2.Add(FlagEnabled(7603))
    AND_2.Add(FlagDisabled(400077))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    AND_1.Add(FlagEnabled(400073))
    AND_1.Add(FlagEnabled(7602))
    AND_1.Add(FlagDisabled(400076))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(16009267)
    DisableFlag(16009268)
    DisableFlag(16009269)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableFlag(16009267)
    EnableFlag(16009268)
    DisableFlag(16009269)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableFlag(16009267)
    DisableFlag(16009268)
    EnableFlag(16009269)
    End()


@RestartOnRest(16003710)
def Event_16003710(_, character: uint):
    """Event 16003710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3680):
        DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3689)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3689))

    MAIN.Await(OR_3)

    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3681)
    GotoIfFlagEnabled(Label.L3, flag=3682)
    GotoIfFlagEnabled(Label.L4, flag=3683)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90100)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

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
    OR_4.Add(FlagEnabled(3689))

    MAIN.Await(not OR_4)

    Restart()


@RestartOnRest(16003711)
def Event_16003711(_, character: uint, flag: uint):
    """Event 16003711"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3681):
        return
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    DisableFlag(flag)
    SetTeamType(character, TeamType.NoTeam)
    EnableNetworkFlag(3698)
    End()


@RestartOnRest(16003712)
def Event_16003712():
    """Event 16003712"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(Flags.RykardDead):
        return

    MAIN.Await(FlagEnabled(Flags.RykardDead))

    if FlagEnabled(3689):
        return
    if FlagEnabled(3690):
        return
    if FlagEnabled(3691):
        return
    if FlagEnabled(3692):
        return
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3683)
    SaveRequest()
    End()


@RestartOnRest(16003720)
def Event_16003720(_, character: uint, character_1: uint):
    """Event 16003720"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3420):
        DisableFlag(1038519203)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3427)
    GotoIfFlagEnabled(Label.L5, flag=3428)
    GotoIfFlagEnabled(Label.L5, flag=3430)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    OR_3.Add(FlagEnabled(3427))
    OR_3.Add(FlagEnabled(3428))
    OR_3.Add(FlagEnabled(3430))

    MAIN.Await(OR_3)

    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3420)
    GotoIfFlagEnabled(Label.L2, flag=3421)
    GotoIfFlagEnabled(Label.L3, flag=3422)
    GotoIfFlagEnabled(Label.L4, flag=3423)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    DisableBackread(character_1)
    DisableCharacter(character_1)
    ForceAnimation(character, 90100)
    GotoIfFlagEnabled(Label.L20, flag=3430)
    AND_1.Add(FlagEnabled(16009308))
    AND_1.Add(FlagDisabled(16002710))
    SkipLinesIfConditionFalse(2, AND_1)
    Move(character, destination=16002730, destination_type=CoordEntityType.Region, short_move=True)
    Move(character_1, destination=16002730, destination_type=CoordEntityType.Region, short_move=True)
    GotoIfFlagEnabled(Label.L20, flag=3428)
    AND_2.Add(FlagEnabled(16009308))
    AND_2.Add(FlagDisabled(16002710))
    AND_2.Add(FlagDisabled(16009306))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(16002711))
    SkipLinesIfConditionFalse(5, OR_2)
    DisableBackread(character)
    DisableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    ForceAnimation(character_1, 930000)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

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
    OR_4.Add(FlagEnabled(3427))
    OR_4.Add(FlagEnabled(3428))
    OR_4.Add(FlagEnabled(3430))

    MAIN.Await(not OR_4)

    Restart()


@RestartOnRest(16003721)
def Event_16003721(_, flag: uint):
    """Event 16003721"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3420):
        return
    if FlagEnabled(flag):
        return
    if FlagEnabled(Flags.RykardDead):
        return
    AND_1.Add(FlagEnabled(flag))

    MAIN.Await(AND_1)

    EnableFlag(3438)
    End()


@RestartOnRest(16003722)
def Event_16003722(_, character: uint, character_1: uint):
    """Event 16003722"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3420):
        DisableFlag(1038519203)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3429)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    OR_3.Add(FlagEnabled(3429))

    MAIN.Await(OR_3)

    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3420)
    GotoIfFlagEnabled(Label.L2, flag=3421)
    GotoIfFlagEnabled(Label.L3, flag=3422)
    GotoIfFlagEnabled(Label.L4, flag=3423)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(16009327):
        EnableFlag(16009329)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    DisableCharacter(character_1)
    ForceAnimation(character, 90101)
    ForceAnimation(character_1, 930020)
    GotoIfFlagDisabled(Label.L20, flag=16009329)
    ForceAnimation(character, 90102)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

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
    OR_4.Add(FlagEnabled(3429))

    MAIN.Await(not OR_4)

    Restart()


@RestartOnRest(16003723)
def Event_16003723(_, character: uint, character_1: uint):
    """Event 16003723"""
    WaitFrames(frames=1)
    if FlagDisabled(3429):
        return
    if FlagEnabled(3423):
        return

    MAIN.Await(FlagEnabled(3423))

    Wait(3.5)
    EnableCharacter(character_1)
    SetTeamType(character_1, TeamType.NoTeam)
    DisableAnimations(character_1)
    Wait(5.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(16003724)
def Event_16003724():
    """Event 16003724"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(16009316):
        return

    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=16002731))

    EnableFlag(16009316)
    End()


@RestartOnRest(16003725)
def Event_16003725():
    """Event 16003725"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3431):
        return
    if FlagDisabled(16009319):
        return
    GotoIfFlagEnabled(Label.L1, flag=16009327)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(16009338)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(16009337)
    End()


@RestartOnRest(16003726)
def Event_16003726():
    """Event 16003726"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(Flags.RykardDead):
        return
    if FlagEnabled(16009208):
        return
    if FlagEnabled(16009309):
        return
    if FlagDisabled(1038519205):
        return
    WaitFrames(frames=1)
    ForceAnimation(20000, 60451)
    EnableFlag(16009309)
    End()


@RestartOnRest(16003727)
def Event_16003727():
    """Event 16003727"""
    WaitFramesAfterCutscene(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3429):
        return
    WaitFramesAfterCutscene(frames=1)
    AND_1.Add(FlagDisabled(3105))
    AND_1.Add(FlagDisabled(3106))
    AND_1.Add(FlagDisabled(3107))
    AND_1.Add(FlagDisabled(3108))
    AND_1.Add(FlagDisabled(3689))
    AND_1.Add(FlagDisabled(3448))
    AND_1.Add(FlagDisabled(3449))
    AND_1.Add(FlagDisabled(3886))
    if not AND_1:
        return
    EnableFlag(3438)
    End()


@RestartOnRest(16003730)
def Event_16003730(_, character: uint):
    """Event 16003730"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    DisableFlag(16009400)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3440):
        DisableFlag(11109405)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3448)
    AND_1.Add(FlagDisabled(16002731))
    AND_1.Add(FlagEnabled(3449))
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    AND_2.Add(FlagDisabled(16009405))
    AND_2.Add(FlagEnabled(3449))
    GotoIfConditionTrue(Label.L5, input_condition=AND_2)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3448))
    AND_3.Add(FlagDisabled(16002731))
    AND_3.Add(FlagEnabled(3449))
    OR_3.Add(AND_3)
    AND_4.Add(FlagDisabled(16009405))
    AND_4.Add(FlagEnabled(3449))
    OR_3.Add(AND_4)

    MAIN.Await(OR_3)

    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3440)
    GotoIfFlagEnabled(Label.L2, flag=3441)
    GotoIfFlagEnabled(Label.L3, flag=3442)
    GotoIfFlagEnabled(Label.L4, flag=3443)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90100)
    if FlagEnabled(3449):
        ForceAnimation(character, 90105)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

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
    OR_15.Add(FlagEnabled(3448))
    AND_10.Add(FlagDisabled(16002731))
    AND_10.Add(FlagEnabled(3449))
    OR_15.Add(AND_10)
    AND_11.Add(FlagDisabled(16009405))
    AND_11.Add(FlagEnabled(3449))
    OR_15.Add(AND_11)

    MAIN.Await(not OR_15)

    Restart()


@RestartOnRest(16003731)
def Event_16003731(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 16003731"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3449):
        return
    if FlagEnabled(flag):
        return
    EnableFlag(flag)
    EnableFlag(flag_1)
    WaitFrames(frames=1)
    EnableFlag(flag_2)
    End()


@RestartOnRest(16003740)
def Event_16003740(_, character: uint, asset: uint, destination: uint):
    """Event 16003740"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3880):
        DisableFlag(1042389253)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3886)
    DisableCharacter(character)
    DisableBackread(character)
    EnableGravity(character)
    DisableAssetInvulnerability(asset)
    OR_3.Add(FlagEnabled(3886))

    MAIN.Await(OR_3)

    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3880)
    GotoIfFlagEnabled(Label.L2, flag=3881)
    GotoIfFlagEnabled(Label.L3, flag=3882)
    GotoIfFlagEnabled(Label.L4, flag=3883)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    RestoreAsset(asset)
    EnableAssetInvulnerability(asset)
    DisableGravity(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character, 90100)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

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
    OR_4.Add(FlagEnabled(3886))

    MAIN.Await(not OR_4)

    Restart()


@RestartOnRest(16003741)
def Event_16003741(_, flag: uint):
    """Event 16003741"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3880):
        return
    if FlagEnabled(16009208):
        return
    AND_1.Add(FlagEnabled(16009208))

    MAIN.Await(AND_1)

    EnableFlag(3898)
    WaitFrames(frames=1)
    EnableFlag(flag)
    End()


@RestartOnRest(16003742)
def Event_16003742(_, character: uint, asset: uint, asset_1: uint):
    """Event 16003742"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3887)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    EnableAsset(asset_1)
    OR_3.Add(FlagEnabled(3887))

    MAIN.Await(OR_3)

    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3880)
    GotoIfFlagEnabled(Label.L2, flag=3881)
    GotoIfFlagEnabled(Label.L3, flag=3882)
    GotoIfFlagEnabled(Label.L4, flag=3883)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    EnableAsset(asset)
    DisableAsset(asset_1)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    EnableAsset(asset)
    DisableAsset(asset_1)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    EnableAsset(asset)
    DisableAsset(asset_1)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character)
    EnableBackread(character)
    EnableAsset(asset)
    DisableAsset(asset_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3887))

    MAIN.Await(not OR_4)

    Restart()


@RestartOnRest(16003743)
def Event_16003743():
    """Event 16003743"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(3887))
    AND_1.Add(FlagEnabled(7605))
    AND_1.Add(FlagDisabled(400291))
    if not AND_1:
        return
    EnableFlag(16009463)
    End()


@RestartOnRest(16003750)
def SetRykardTalkRange(_, rykard_phase_one: uint, rykard_phase_two: uint, flag: uint, flag_1: uint, distance: float):
    """Event 16003750"""
    if PlayerNotInOwnWorld():
        return
    SetCharacterTalkRange(character=rykard_phase_one, distance=17.0)
    if UnsignedNotEqual(left=0, right=rykard_phase_two):
        SetCharacterTalkRange(character=rykard_phase_two, distance=17.0)
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
    SetCharacterTalkRange(character=rykard_phase_one, distance=distance)
    if UnsignedNotEqual(left=0, right=rykard_phase_two):
        SetCharacterTalkRange(character=rykard_phase_two, distance=distance)
    End()


@RestartOnRest(16003760)
def Event_16003760(_, asset__character: uint):
    """Event 16003760"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3780))
    AND_1.Add(FlagEnabled(16009503))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(16009503)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(asset__character)
    DisableBackread(asset__character)
    AND_5.Add(FlagEnabled(3785))
    AND_5.Add(FlagEnabled(16002756))
    GotoIfConditionTrue(Label.L0, input_condition=AND_5)
    AND_6.Add(FlagEnabled(3785))
    AND_6.Add(FlagEnabled(16002756))

    MAIN.Await(AND_6)

    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SetCharacterTalkRange(character=asset__character, distance=80.0)
    GotoIfFlagEnabled(Label.L1, flag=3780)
    GotoIfFlagEnabled(Label.L2, flag=3781)
    GotoIfFlagEnabled(Label.L4, flag=3783)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(asset__character)
    EnableBackread(asset__character)
    ForceAnimation(asset__character, 90100)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(asset__character)
    EnableBackread(asset__character)
    SetTeamType(asset__character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(asset__character)
    DisableCharacter(asset__character)
    DisableBackread(asset__character)
    DisableAsset(asset__character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_15.Add(FlagEnabled(3785))
    AND_15.Add(FlagEnabled(16002756))

    MAIN.Await(not AND_15)

    Restart()


@RestartOnRest(16003761)
def Event_16003761(_, character: uint):
    """Event 16003761"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=character, radius=59.0))
    AND_1.Add(FlagEnabled(16002751))
    AND_1.Add(FlagDisabled(16009505))
    AND_1.Add(FlagEnabled(16002756))
    AwaitConditionTrue(AND_1)
    Move(character, destination=16002720, destination_type=CoordEntityType.Region, short_move=True)
    EnableFlag(16009508)
    End()


@RestartOnRest(16003762)
def Event_16003762(
        _,
        asset: uint,
        action_button_id: int,
        gesture_param_id: int,
        first_flag: uint,
        last_flag: uint,
        flag: uint,
        model_point: int,
):
    """Event 16003762"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagRangeAnyDisabled(flag_range=(first_flag, last_flag)))
    AwaitConditionTrue(AND_1)
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
    AwardGesture(gesture_param_id=gesture_param_id)
    EnableNetworkFlag(first_flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(asset)
    Restart()


@RestartOnRest(16003763)
def Event_16003763():
    """Event 16003763"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L0, flag=16009509)
    GotoIfFlagDisabled(Label.L1, flag=16009510)
    GotoIfFlagDisabled(Label.L2, flag=16009511)
    Goto(Label.L3)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNetworkFlag(16009509)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableNetworkFlag(16009510)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableNetworkFlag(16009511)
    EnableNetworkFlag(16002756)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableRandomFlagInRange(flag_range=(16002752, 16002756))
    End()


@RestartOnRest(16003764)
def Event_16003764():
    """Event 16003764"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(16009505):
        return
    AND_1.Add(FlagDisabled(16009505))
    AND_1.Add(FlagDisabled(16009508))
    AND_1.Add(FlagDisabled(16002751))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=16002721))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(16002750)
    End()


@RestartOnRest(16003765)
def Event_16003765():
    """Event 16003765"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(16009505):
        return
    AND_1.Add(FlagDisabled(16009505))
    AND_1.Add(FlagEnabled(16009508))
    AND_1.Add(FlagDisabled(16002758))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=16002722))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(16002757)
    End()
