"""
Academy of Raya Lucaria

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
from .entities.m14_00_00_00_entities import *
from .entities.m31_06_00_00_entities import Assets as m31_06_Assets
from .entities.m60_35_46_00_entities import Assets as m60_35_Assets


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=14000002, asset=Assets.AEG099_060_9002)
    RegisterGrace(grace_flag=14000003, asset=Assets.AEG099_060_9003)
    RegisterGrace(grace_flag=14000005, asset=Assets.AEG099_060_9004_NewGrace)
    CommonFunc_RegisterGraceIfFlagEnabled(
        0,
        flag=Flags.RennalaDefeated,
        grace_flag=14000000,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    CommonFunc_RegisterGraceIfFlagEnabled(
        0,
        flag=Flags.RedWolfDead,
        grace_flag=14000001,
        character=Characters.TalkDummy1,
        asset=Assets.AEG099_060_9001,
        enemy_block_distance=5.0,
    )
    Event_14002080()
    Event_14002665()
    DisableMapCollisionBackreadMask(collision=0)

    # RENNALA
    RennalaDies()
    RennalaBattleTrigger()
    RennalaPhaseTwoTransition()
    Event_14002849()
    Event_140028121()  # TODO: Rennala Phase 1 SpEffect <-> Flag communication. Not sure if it needs cloning.
    Event_140028122(0, character=Characters.RennalaPhaseTwo, special_effect=14585, special_effect_1=Effects.RennalaDragonRequest)
    Event_14002606()
    Event_14002689()
    Event_14003500(0, region=14002700, flag=Flags.RennalaDefeated)

    # RED WOLF OF RADAGON
    RedWolfDies()
    RedWolfBattleTrigger()
    RedWolfFogGateEvents()

    # RENNALA STUDENTS
    ChooseRandomGlowingStudent(
        0,
        required_flag=Flags.RennalaBarrierActive,
        rennala=Characters.RennalaPhaseOne,
        student_group=CharacterGroups.Students,
        student_2=Characters.RennalaStudent0,
        student_3=Characters.RennalaStudent1,
        student_4=Characters.RennalaStudent2,
        student_5=Characters.RennalaStudent3,
        student_6=Characters.RennalaStudent4,
        student_7=Characters.RennalaStudent5,
        student_8=Characters.RennalaStudent6,
        student_9=Characters.RennalaStudent7,
        student_10=Characters.RennalaStudent8,
        student_11=Characters.RennalaStudent9,
        student_12=Characters.RennalaStudent10,
        student_13=Characters.RennalaStudent11,
        student_14=Characters.RennalaStudent12,
        student_15=Characters.RennalaStudent13,
        student_16=Characters.RennalaStudent14,
        student_17=Characters.RennalaStudent15,
        student_18=Characters.RennalaStudent16,
        student_19=Characters.RennalaStudent17,
        student_20=Characters.RennalaStudent18,
        student_21=Characters.RennalaStudent19,
        student_22=Characters.RennalaStudent20,  # NOTE: Typo fixed.
        student_23=Characters.RennalaStudent21,
        student_24=Characters.RennalaStudent22,
        student_25=Characters.RennalaStudent23,
    )
    StudentChosenAtBattleStart(
        0, flag=Flags.RennalaBarrierActive, rennala=Characters.RennalaPhaseOne, student_group=CharacterGroups.Students
    )
    RennalaBarrierBreaks(
        0,
        required_flag=Flags.FirstGlowingStudentHit,
        rennala=Characters.RennalaPhaseOne,
        student_group=CharacterGroups.Students,
        character_2=14005811,
    )
    RennalaBarrierDamaged(0, rennala=Characters.RennalaPhaseOne, student_group=CharacterGroups.Students)
    RennalaVulnerableTimer(0, barrier_active_flag=Flags.RennalaBarrierActive, rennala=Characters.RennalaPhaseOne)
    RennalaStudentsUnknownEffect(0, student_group=CharacterGroups.Students)
    RennalaRequestsSpecialStudent(
        0,
        request_flag=Flags.RennalaSpecialStudentRequest,
        rennala=Characters.RennalaPhaseOne,
    )
    ChooseRandomSpecialStudent(
        0,
        request_flag=Flags.RennalaSpecialStudentRequest,
        student_group=CharacterGroups.Students,
        student_1=Characters.RennalaStudent0,
        student_2=Characters.RennalaStudent1,
        student_3=Characters.RennalaStudent2,
        student_4=Characters.RennalaStudent3,
        student_5=Characters.RennalaStudent4,
        student_6=Characters.RennalaStudent5,
        student_7=Characters.RennalaStudent6,
        student_8=Characters.RennalaStudent7,
        student_9=Characters.RennalaStudent8,
        student_10=Characters.RennalaStudent9,
        student_11=Characters.RennalaStudent10,
        student_12=Characters.RennalaStudent11,
        student_13=Characters.RennalaStudent12,
        student_14=Characters.RennalaStudent13,
        student_15=Characters.RennalaStudent14,
        student_16=Characters.RennalaStudent15,
        student_17=Characters.RennalaStudent16,
        student_18=Characters.RennalaStudent17,
        student_19=Characters.RennalaStudent18,
        student_20=Characters.RennalaStudent19,
        student_21=Characters.RennalaStudent20,  # NOTE: Typo fixed.
        student_22=Characters.RennalaStudent21,
        student_23=Characters.RennalaStudent22,
        student_24=Characters.RennalaStudent23,
    )
    SyncRennalaSoundDummyPosition(0, rennala=Characters.RennalaPhaseOne, rennala_sound_dummy=Characters.Dummy0)
    RennalaSoundDummyLoop(0, rennala=Characters.RennalaPhaseOne, rennala_sound_dummy=Characters.Dummy0)
    RennalaForceStudentUpdate(0, rennala=Characters.RennalaPhaseOne, student_group=CharacterGroups.Students)
    RennalaStudentsEffect14353(0, rennala=Characters.RennalaPhaseOne, student_group=CharacterGroups.Students)
    RennalaStudentsEffect14355(0, rennala=Characters.RennalaPhaseOne, student_group=CharacterGroups.Students)

    # region Rennala Phase One Clones
    CLONE_ChooseRandomGlowingStudent(
        0,
        required_flag=Flags.CLONE_RennalaBarrierActive,
        rennala=Characters.CLONE_RennalaPhaseOne,
        student_group=CharacterGroups.CLONE_Students,
        student_2=Characters.CLONE_RennalaStudent0,
        student_3=Characters.CLONE_RennalaStudent1,
        student_4=Characters.CLONE_RennalaStudent2,
        student_5=Characters.CLONE_RennalaStudent3,
        student_6=Characters.CLONE_RennalaStudent4,
        student_7=Characters.CLONE_RennalaStudent5,
        student_8=Characters.CLONE_RennalaStudent6,
        student_9=Characters.CLONE_RennalaStudent7,
        student_10=Characters.CLONE_RennalaStudent8,
        student_11=Characters.CLONE_RennalaStudent9,
        student_12=Characters.CLONE_RennalaStudent10,
        student_13=Characters.CLONE_RennalaStudent11,
        student_14=Characters.CLONE_RennalaStudent12,
        student_15=Characters.CLONE_RennalaStudent13,
        student_16=Characters.CLONE_RennalaStudent14,
        student_17=Characters.CLONE_RennalaStudent15,
        student_18=Characters.CLONE_RennalaStudent16,
        student_19=Characters.CLONE_RennalaStudent17,
        student_20=Characters.CLONE_RennalaStudent18,
        student_21=Characters.CLONE_RennalaStudent19,
        student_22=Characters.CLONE_RennalaStudent20,
        student_23=Characters.CLONE_RennalaStudent21,
        student_24=Characters.CLONE_RennalaStudent22,
        student_25=Characters.CLONE_RennalaStudent23,
    )
    CLONE_StudentChosenAtBattleStart(
        0,
        flag=Flags.CLONE_RennalaBarrierActive,
        rennala=Characters.CLONE_RennalaPhaseOne,
        student_group=CharacterGroups.CLONE_Students,
    )
    CLONE_RennalaBarrierBreaks(
        0,
        required_flag=Flags.CLONE_FirstGlowingStudentHit,
        rennala=Characters.CLONE_RennalaPhaseOne,
        student_group=CharacterGroups.CLONE_Students,
        character_2=CharacterGroups.CLONE_UnknownGroup,
    )
    CLONE_RennalaBarrierDamaged(
        0,
        rennala=Characters.CLONE_RennalaPhaseOne,
        student_group=CharacterGroups.CLONE_Students,
    )
    CLONE_RennalaVulnerableTimer(
        0,
        barrier_active_flag=Flags.CLONE_RennalaBarrierActive,
        rennala=Characters.CLONE_RennalaPhaseOne,
    )
    CLONE_RennalaStudentsUnknownEffect(0, student_group=CharacterGroups.CLONE_Students)
    CLONE_RennalaRequestsSpecialStudent(
        0,
        request_flag=Flags.CLONE_RennalaSpecialStudentRequest,
        rennala=Characters.CLONE_RennalaPhaseOne,
    )
    CLONE_ChooseRandomSpecialStudent(
        0,
        request_flag=Flags.CLONE_RennalaSpecialStudentRequest,
        student_group=CharacterGroups.CLONE_Students,
        student_1=Characters.CLONE_RennalaStudent0,
        student_2=Characters.CLONE_RennalaStudent1,
        student_3=Characters.CLONE_RennalaStudent2,
        student_4=Characters.CLONE_RennalaStudent3,
        student_5=Characters.CLONE_RennalaStudent4,
        student_6=Characters.CLONE_RennalaStudent5,
        student_7=Characters.CLONE_RennalaStudent6,
        student_8=Characters.CLONE_RennalaStudent7,
        student_9=Characters.CLONE_RennalaStudent8,
        student_10=Characters.CLONE_RennalaStudent9,
        student_11=Characters.CLONE_RennalaStudent10,
        student_12=Characters.CLONE_RennalaStudent11,
        student_13=Characters.CLONE_RennalaStudent12,
        student_14=Characters.CLONE_RennalaStudent13,
        student_15=Characters.CLONE_RennalaStudent14,
        student_16=Characters.CLONE_RennalaStudent15,
        student_17=Characters.CLONE_RennalaStudent16,
        student_18=Characters.CLONE_RennalaStudent17,
        student_19=Characters.CLONE_RennalaStudent18,
        student_20=Characters.CLONE_RennalaStudent19,
        student_21=Characters.CLONE_RennalaStudent20,
        student_22=Characters.CLONE_RennalaStudent21,
        student_23=Characters.CLONE_RennalaStudent22,
        student_24=Characters.CLONE_RennalaStudent23,
    )
    # TODO: Not cloning sound dummy.
    CLONE_RennalaForceStudentUpdate(
        0,
        rennala=Characters.CLONE_RennalaPhaseOne,
        student_group=CharacterGroups.CLONE_Students,
    )
    CLONE_RennalaStudentsEffect14353(
        0,
        rennala=Characters.CLONE_RennalaPhaseOne,
        student_group=CharacterGroups.CLONE_Students,
    )
    CLONE_RennalaStudentsEffect14355(
        0,
        rennala=Characters.CLONE_RennalaPhaseOne,
        student_group=CharacterGroups.CLONE_Students,
    )
    # endregion

    Event_14003820(0, asset=Assets.AEG250_260_9000)
    Event_14003820(1, asset=Assets.AEG250_260_5004)
    Event_14003820(2, asset=Assets.AEG250_260_5003)
    Event_14003820(3, asset=Assets.AEG250_260_9003)
    Event_14003820(5, asset=Assets.AEG250_260_9004)
    Event_14003820(6, asset=14001826)
    Event_14003820(8, asset=Assets.AEG250_260_9006)
    Event_14003820(9, asset=14001829)
    Event_14003950(0, flag=14003820, asset=Assets.AEG250_260_9000)
    Event_14003950(1, flag=14003821, asset=Assets.AEG250_260_5004)
    Event_14003950(2, flag=14003822, asset=Assets.AEG250_260_5003)
    Event_14003950(3, flag=14003823, asset=Assets.AEG250_260_9003)
    Event_14003950(4, flag=14003825, asset=Assets.AEG250_260_9004)
    Event_14003950(5, flag=14003826, asset=14001826)
    Event_14003950(6, flag=14003828, asset=Assets.AEG250_260_9006)
    Event_14003950(7, flag=14003829, asset=14001829)
    Event_14003834(0, asset=14006810)
    Event_14003834(1, asset=14006811)
    Event_14003834(2, asset=14006812)
    Event_14003834(3, asset=14006813)
    Event_14003834(4, asset=14006814)
    # TODO: Not cloning any of these student-object connections (too complicated).
    Event_14003840(
        0,
        character=Characters.RennalaStudent18,
        left=Assets.AEG250_260_5004,
        left_1=0,
        left_2=0,
        flag=14003821,
        flag_1=0,
        flag_2=0,
    )
    Event_14003840(
        1,
        character=Characters.RennalaStudent19,
        left=Assets.AEG250_260_5003,
        left_1=0,
        left_2=0,
        flag=14003822,
        flag_1=0,
        flag_2=0,
    )
    Event_14003840(
        2,
        character=Characters.RennalaStudent20,
        left=Assets.AEG250_260_9000,
        left_1=0,
        left_2=0,
        flag=14003820,
        flag_1=0,
        flag_2=0,
    )
    Event_14003840(
        3,
        character=Characters.RennalaStudent21,
        left=Assets.AEG250_260_9003,
        left_1=0,
        left_2=0,
        flag=14003823,
        flag_1=0,
        flag_2=0,
    )
    Event_14003845(
        0,
        character=Characters.RennalaStudent18,
        asset=Assets.AEG250_260_5004,
        asset_1=0,
        asset_2=0,
        asset_3=14003821,
        asset_4=0,
        asset_5=0,
    )
    Event_14003845(
        1,
        character=Characters.RennalaStudent19,
        asset=Assets.AEG250_260_5003,
        asset_1=0,
        asset_2=0,
        asset_3=14003822,
        asset_4=0,
        asset_5=0,
    )
    Event_14003845(
        2,
        character=Characters.RennalaStudent20,
        asset=Assets.AEG250_260_9000,
        asset_1=0,
        asset_2=0,
        asset_3=14003820,
        asset_4=0,
        asset_5=0,
    )
    Event_14003845(
        3,
        character=Characters.RennalaStudent21,
        asset=Assets.AEG250_260_9003,
        asset_1=0,
        asset_2=0,
        asset_3=14003823,
        asset_4=0,
        asset_5=0,
    )
    Event_14003850(
        0,
        character=Characters.RennalaStudent22,
        asset=14006810,
        asset_1=14006811,
        asset_2=14006812,
        asset_3=14006813,
        asset_4=14006814,
        flag=14003834,
        flag_1=14003835,
        flag_2=14003836,
        flag_3=14003837,
        flag_4=14003838,
        asset__asset_flag=Assets.AEG257_031_5004,
        asset__asset_flag_1=Assets.AEG257_031_5003,
        asset__asset_flag_2=Assets.AEG257_031_5002,
        asset__asset_flag_3=Assets.AEG257_031_5001,
        asset__asset_flag_4=Assets.AEG257_031_5000,
        region=14002815,
        region_1=14002816,
        region_2=14002817,
        region_3=14002818,
        region_4=14002819,
    )
    Event_14003850(
        1,
        character=Characters.RennalaStudent23,
        asset=14006810,
        asset_1=14006811,
        asset_2=14006812,
        asset_3=14006813,
        asset_4=14006814,
        flag=14003834,
        flag_1=14003835,
        flag_2=14003836,
        flag_3=14003837,
        flag_4=14003838,
        asset__asset_flag=Assets.AEG257_031_5004,
        asset__asset_flag_1=Assets.AEG257_031_5003,
        asset__asset_flag_2=Assets.AEG257_031_5002,
        asset__asset_flag_3=Assets.AEG257_031_5001,
        asset__asset_flag_4=Assets.AEG257_031_5000,
        region=14002815,
        region_1=14002816,
        region_2=14002817,
        region_3=14002818,
        region_4=14002819,
    )

    # RENNALA PHASE TWO SUMMONS
    
    # Summon order of events:
    #  - Rennala's AI enables a "summon request" SpEffect.
    #  - `RennalaSummonsCharacter` event triggers.
    #  - `RennalaSummonActive` flag is enabled.
    #  - Speculative:
    #    - Effect 14573 ("Dismissed") SpEffect is applied to summon at the end of its fake immortal "death" animation OR
    #    whatever animation it uses to "dismiss itself" after a self-timer.
    #    - Effect 14572 is added to all summons when Rennala dies, dimissing them all immediately.
    #  - Effect 14573 (and NOT the inactive effect 14574) causes the summon to heal and disable immediately.
    #  - 'Active' flag + 'Dismissed' flag + 'Dismissed' summon effect cause all three to be disabled/removed.
    #    - This presumably 'cleans up' the entire summon event AFTER Rennala is given a chance to replan her AI.
    #    - The 'Disable' event is probably expected to trigger BEFORE this event removes the request effect, but there's
    #    no synchronization that enforces this - just a lucky race condition.
    
    RennalaSummonsBloodhoundKnight(
        0,
        active_flag=Flags.RennalaBloodhoundActive,
        rennala=Characters.RennalaPhaseTwo,
        bloodhound=Characters.RennalaBloodhoundSummon,
    )
    RennalaResumesFightingAfterBloodhound(
        0,
        active_flag=Flags.RennalaBloodhoundActive,
        cleanup_flag=Flags.RennalaBloodhoundCleanup,
        bloodhound=Characters.RennalaBloodhoundSummon,
        rennala=Characters.RennalaPhaseTwo,
    )
    BloodhoundCleanup(
        0,
        active_flag=Flags.RennalaBloodhoundActive,
        cleanup_flag=Flags.RennalaBloodhoundCleanup,
        bloodhound=Characters.RennalaBloodhoundSummon,
    )
    BloodhoundSummonDefeated(
        0,
        active_flag=Flags.RennalaBloodhoundActive,
        bloodhound=Characters.RennalaBloodhoundSummon,
    )
    DisableBloodhoundSummon(0, bloodhound=Characters.RennalaBloodhoundSummon)

    RennalaSummonsTroll(
        0,
        active_flag=Flags.RennalaTrollActive,
        rennala=Characters.RennalaPhaseTwo,
        troll=Characters.RennalaTrollSummon,
    )
    RennalaResumesFightingAfterTroll(
        0,
        active_flag=Flags.RennalaTrollActive,
        cleanup_flag=Flags.RennalaTrollCleanup,
        troll=Characters.RennalaTrollSummon,
        rennala=Characters.RennalaPhaseTwo,
    )
    TrollCleanup(
        0,
        active_flag=Flags.RennalaTrollActive,
        cleanup_flag=Flags.RennalaTrollCleanup,
        troll=Characters.RennalaTrollSummon,
    )
    TrollSummonDefeated(0, active_flag=Flags.RennalaTrollActive, troll=Characters.RennalaTrollSummon)
    DisableTrollSummon(0, troll=Characters.RennalaTrollSummon)

    RennalaSummonsWolves(
        0,
        active_flag=Flags.RennalaWolvesActive,
        rennala=Characters.RennalaPhaseTwo,
        wolf_0=Characters.RennalaWolfSummon0,
        wolf_1=Characters.RennalaWolfSummon1,
        wolf_2=Characters.RennalaWolfSummon2,
        wolf_3=Characters.RennalaWolfSummon3,
    )
    RennalaResumesFightingAfterWolves(
        0,
        active_flag=Flags.RennalaWolvesActive,
        cleanup_flag=Flags.RennalaWolvesCleanup,
        wolf_0=Characters.RennalaWolfSummon0,
        wolf_1=Characters.RennalaWolfSummon1,
        wolf_2=Characters.RennalaWolfSummon2,
        wolf_3=Characters.RennalaWolfSummon3,
        rennala=Characters.RennalaPhaseTwo,
    )
    WolvesCleanup(
        0,
        active_flag=Flags.RennalaWolvesActive,
        flag_1=Flags.RennalaWolvesCleanup,
        wolf_0=Characters.RennalaWolfSummon0,
        wolf_1=Characters.RennalaWolfSummon1,
        wolf_2=Characters.RennalaWolfSummon2,
        wolf_3=Characters.RennalaWolfSummon3,
    )
    WolfSummonDefeated(0, active_flag=Flags.RennalaWolvesActive, wolf=Characters.RennalaWolfSummon0)
    WolfSummonDefeated(1, active_flag=Flags.RennalaWolvesActive, wolf=Characters.RennalaWolfSummon1)
    WolfSummonDefeated(2, active_flag=Flags.RennalaWolvesActive, wolf=Characters.RennalaWolfSummon2)
    WolfSummonDefeated(3, active_flag=Flags.RennalaWolvesActive, wolf=Characters.RennalaWolfSummon3)
    DisableWolfSummon(0, wolf=Characters.RennalaWolfSummon0)
    DisableWolfSummon(1, wolf=Characters.RennalaWolfSummon1)
    DisableWolfSummon(2, wolf=Characters.RennalaWolfSummon2)
    DisableWolfSummon(3, wolf=Characters.RennalaWolfSummon3)

    RennalaSummonsDragon(
        0,
        active_flag=Flags.RennalaDragonActive,
        rennala=Characters.RennalaPhaseTwo,
        dragon=Characters.RennalaDragonSummon,
    )
    RennalaResumesFightingAfterDragon(
        0,
        active_flag=Flags.RennalaDragonActive,
        cleanup_flag=Flags.RennalaDragonCleanup,
        dragon=Characters.RennalaDragonSummon,
        rennala=Characters.RennalaPhaseTwo,
    )
    DragonCleanup(
        0,
        active_flag=Flags.RennalaDragonActive,
        cleanup_flag=Flags.RennalaDragonCleanup,
        dragon=Characters.RennalaDragonSummon,
    )
    DragonSummonDefeated(0, active_flag=Flags.RennalaDragonActive, dragon=Characters.RennalaDragonSummon)
    DisableDragonSummon(0, dragon=Characters.RennalaDragonSummon)
    
    # region CLONED RENNALA SUMMONS

    CLONE_RennalaSummonsBloodhoundKnight(
        0,
        active_flag=Flags.CLONE_RennalaBloodhoundActive,
        rennala=Characters.CLONE_RennalaPhaseTwo,
        bloodhound=Characters.CLONE_RennalaBloodhoundSummon,
    )
    CLONE_RennalaResumesFightingAfterBloodhound(
        0,
        active_flag=Flags.CLONE_RennalaBloodhoundActive,
        cleanup_flag=Flags.CLONE_RennalaBloodhoundCleanup,
        bloodhound=Characters.CLONE_RennalaBloodhoundSummon,
        rennala=Characters.CLONE_RennalaPhaseTwo,
    )
    CLONE_BloodhoundCleanup(
        0,
        active_flag=Flags.CLONE_RennalaBloodhoundActive,
        cleanup_flag=Flags.CLONE_RennalaBloodhoundCleanup,
        bloodhound=Characters.CLONE_RennalaBloodhoundSummon,
    )
    CLONE_BloodhoundSummonDefeated(
        0,
        active_flag=Flags.CLONE_RennalaBloodhoundActive,
        bloodhound=Characters.CLONE_RennalaBloodhoundSummon,
    )
    CLONE_DisableBloodhoundSummon(0, bloodhound=Characters.CLONE_RennalaBloodhoundSummon)

    CLONE_RennalaSummonsTroll(
        0,
        active_flag=Flags.CLONE_RennalaTrollActive,
        rennala=Characters.CLONE_RennalaPhaseTwo,
        troll=Characters.CLONE_RennalaTrollSummon,
    )
    CLONE_RennalaResumesFightingAfterTroll(
        0,
        active_flag=Flags.CLONE_RennalaTrollActive,
        cleanup_flag=Flags.CLONE_RennalaTrollCleanup,
        troll=Characters.CLONE_RennalaTrollSummon,
        rennala=Characters.CLONE_RennalaPhaseTwo,
    )
    CLONE_TrollCleanup(
        0,
        active_flag=Flags.CLONE_RennalaTrollActive,
        cleanup_flag=Flags.CLONE_RennalaTrollCleanup,
        troll=Characters.CLONE_RennalaTrollSummon,
    )
    CLONE_TrollSummonDefeated(0, active_flag=Flags.CLONE_RennalaTrollActive, troll=Characters.CLONE_RennalaTrollSummon)
    CLONE_DisableTrollSummon(0, troll=Characters.CLONE_RennalaTrollSummon)

    CLONE_RennalaSummonsWolves(
        0,
        active_flag=Flags.CLONE_RennalaWolvesActive,
        rennala=Characters.CLONE_RennalaPhaseTwo,
        wolf_0=Characters.CLONE_RennalaWolfSummon0,
        wolf_1=Characters.CLONE_RennalaWolfSummon1,
        wolf_2=Characters.CLONE_RennalaWolfSummon2,
        wolf_3=Characters.CLONE_RennalaWolfSummon3,
    )
    CLONE_RennalaResumesFightingAfterWolves(
        0,
        active_flag=Flags.CLONE_RennalaWolvesActive,
        cleanup_flag=Flags.CLONE_RennalaWolvesCleanup,
        wolf_0=Characters.CLONE_RennalaWolfSummon0,
        wolf_1=Characters.CLONE_RennalaWolfSummon1,
        wolf_2=Characters.CLONE_RennalaWolfSummon2,
        wolf_3=Characters.CLONE_RennalaWolfSummon3,
        rennala=Characters.CLONE_RennalaPhaseTwo,
    )
    CLONE_WolvesCleanup(
        0,
        active_flag=Flags.CLONE_RennalaWolvesActive,
        flag_1=Flags.CLONE_RennalaWolvesCleanup,
        wolf_0=Characters.CLONE_RennalaWolfSummon0,
        wolf_1=Characters.CLONE_RennalaWolfSummon1,
        wolf_2=Characters.CLONE_RennalaWolfSummon2,
        wolf_3=Characters.CLONE_RennalaWolfSummon3,
    )
    CLONE_WolfSummonDefeated(0, active_flag=Flags.CLONE_RennalaWolvesActive, wolf=Characters.CLONE_RennalaWolfSummon0)
    CLONE_WolfSummonDefeated(1, active_flag=Flags.CLONE_RennalaWolvesActive, wolf=Characters.CLONE_RennalaWolfSummon1)
    CLONE_WolfSummonDefeated(2, active_flag=Flags.CLONE_RennalaWolvesActive, wolf=Characters.CLONE_RennalaWolfSummon2)
    CLONE_WolfSummonDefeated(3, active_flag=Flags.CLONE_RennalaWolvesActive, wolf=Characters.CLONE_RennalaWolfSummon3)
    CLONE_DisableWolfSummon(0, wolf=Characters.CLONE_RennalaWolfSummon0)
    CLONE_DisableWolfSummon(1, wolf=Characters.CLONE_RennalaWolfSummon1)
    CLONE_DisableWolfSummon(2, wolf=Characters.CLONE_RennalaWolfSummon2)
    CLONE_DisableWolfSummon(3, wolf=Characters.CLONE_RennalaWolfSummon3)

    CLONE_RennalaSummonsDragon(
        0,
        active_flag=Flags.CLONE_RennalaDragonActive,
        rennala=Characters.CLONE_RennalaPhaseTwo,
        dragon=Characters.CLONE_RennalaDragonSummon,
    )
    CLONE_RennalaResumesFightingAfterDragon(
        0,
        active_flag=Flags.CLONE_RennalaDragonActive,
        cleanup_flag=Flags.CLONE_RennalaDragonCleanup,
        dragon=Characters.CLONE_RennalaDragonSummon,
        rennala=Characters.CLONE_RennalaPhaseTwo,
    )
    CLONE_DragonCleanup(
        0,
        active_flag=Flags.CLONE_RennalaDragonActive,
        cleanup_flag=Flags.CLONE_RennalaDragonCleanup,
        dragon=Characters.CLONE_RennalaDragonSummon,
    )
    CLONE_DragonSummonDefeated(
        0,
        active_flag=Flags.CLONE_RennalaDragonActive,
        dragon=Characters.CLONE_RennalaDragonSummon,
    )
    CLONE_DisableDragonSummon(0, dragon=Characters.CLONE_RennalaDragonSummon)
    # endregion

    # RENNALA CLEANUP
    DismissSummonsOnRennalaDeath(
        0,
        rennala=Characters.RennalaPhaseTwo,
        summon_group=CharacterGroups.RennalaPhaseTwoSummons,
    )
    CLONE_DismissSummonsOnRennalaDeath(
        0,
        rennala=Characters.CLONE_RennalaPhaseTwo,
        summon_group=CharacterGroups.CLONE_RennalaPhaseTwoSummons,
    )
    DisableRennalaSpawners()
    KillStudentsWhenRennalaDies()
    
    CommonFunc_90005511(
        0,
        flag=14000560,
        asset=Assets.AEG257_013_0501,
        obj_act_id=14003560,
        obj_act_id_1=257013,
        left=0,
    )
    CommonFunc_90005512(0, flag=14000560, region=14002550, region_1=14002551)
    CommonFunc_90005511(
        0,
        flag=14000562,
        asset=Assets.AEG257_013_0500,
        obj_act_id=14003562,
        obj_act_id_1=257013,
        left=0,
    )
    CommonFunc_90005512(0, flag=14000562, region=14002552, region_1=14002553)
    CommonFunc_90005515(0, flag=14008550, anchor_entity=Assets.AEG257_018_0500)
    CommonFunc_90005515(0, flag=14008552, anchor_entity=Assets.AEG257_018_0501)
    CommonFunc_90005501(
        0,
        flag=14000510,
        flag_1=14000511,
        left=0,
        asset=Assets.AEG257_009_0500,
        asset_1=Assets.AEG257_002_0500,
        asset_2=m60_35_Assets.AEG257_002_2001,
        flag_2=14000512,
    )
    Event_14002510()
    CommonFunc_90005501(
        0,
        flag=14000515,
        flag_1=14000516,
        left=0,
        asset=Assets.AEG257_010_0500,
        asset_1=Assets.AEG257_002_0502,
        asset_2=Assets.AEG257_002_0503,
        flag_2=14000517,
    )
    CommonFunc_90005501(
        0,
        flag=14000520,
        flag_1=14000521,
        left=0,
        asset=Assets.AEG257_011_0500,
        asset_1=Assets.AEG257_002_0504,
        asset_2=m31_06_Assets.AEG257_002_1000,
        flag_2=14000522,
    )
    Event_14002580()
    CommonFunc_90005520(
        0,
        flag=14000546,
        asset=Assets.AEG257_008_0500,
        start_climbing_flag=14000544,
        stop_climbing_flag=14000545,
    )
    Event_14002498()
    Event_14002590()
    Event_14002592()
    Event_14002594()
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=14000276,
        character=Characters.RayaLucariaScholar23,
        item_lot=0,
        reward_delay=0.0,
        skip_reward=0,
    )
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=14000277,
        character=Characters.RayaLucariaScholar24,
        item_lot=0,
        reward_delay=0.0,
        skip_reward=0,
    )
    CommonFunc_90005525(0, flag=14000610, asset=Assets.AEG257_035_3000)
    CommonFunc_90005525(0, flag=14000611, asset=Assets.AEG257_035_3001)
    CommonFunc_90005525(0, flag=14000612, asset=Assets.AEG257_039_1000)
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=60,
        block_id=37,
        cc_id=46,
        dd_id=0,
        player_start=1037462650,
        unk_8_12=14000000,
        flag=14002660,
        left_flag=14002661,
        cancel_flag__right_flag=14002662,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    Event_14002328(0, character=Characters.PutridCorpse29)
    Event_14002328(1, character=Characters.PutridCorpse30)
    Event_14002328(2, character=Characters.PutridCorpse31)
    Event_14002328(3, character=Characters.PutridCorpse32)
    Event_14002328(4, character=Characters.PutridCorpse33)
    Event_14002328(5, character=Characters.PutridCorpse34)
    Event_14002328(6, character=Characters.PutridCorpse35)
    Event_14002328(7, character=Characters.PutridCorpse36)
    Event_14002328(8, character=Characters.PutridCorpse37)
    Event_14002328(9, character=Characters.PutridCorpse38)
    Event_14002328(10, character=Characters.PutridCorpse39)
    Event_14002328(11, character=Characters.PutridCorpse40)
    Event_14002328(12, character=Characters.PutridCorpse26)
    Event_14002328(13, character=Characters.PutridCorpse27)
    Event_14002328(14, character=Characters.PutridCorpse28)
    Event_14002328(15, character=Characters.PutridCorpseBare6)
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=14000633,
        character=Characters.SmallCrabCrystal0,
        item_lot=14000005,
        reward_delay=0.0,
        skip_reward=0,
    )
    CommonFunc_NonRespawningWithReward(0, dead_flag=14000634, character=14000634, item_lot=14000015, reward_delay=0.0, skip_reward=0)
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=14000637,
        character=Characters.SmallCrabCrystal1,
        item_lot=14000025,
        reward_delay=0.0,
        skip_reward=0,
    )
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=14000638,
        character=Characters.SmallCrabCrystal2,
        item_lot=14000035,
        reward_delay=0.0,
        skip_reward=0,
    )
    Event_14002491(0, character=Characters.Avionette2, region=14002492, radius=15.0, seconds=0.0, animation_id=3032)
    Event_14002491(1, character=Characters.Avionette3, region=14002493, radius=15.0, seconds=0.0, animation_id=3032)
    Event_14002491(2, character=Characters.Avionette4, region=14002493, radius=15.0, seconds=0.0, animation_id=3032)
    Event_14002490(0, character=Characters.Avionette0, region=14002490, seconds=0.0, animation_id=3032)
    Event_14002490(1, character=Characters.Avionette1, region=14002491, seconds=0.0, animation_id=3032)
    Event_14002490(2, character=Characters.Avionette6, region=14002496, seconds=0.0, animation_id=3032)
    Event_14002490(3, character=Characters.Avionette7, region=14002496, seconds=1.0, animation_id=3032)
    CommonFunc_NonRespawningWithReward(0, dead_flag=14000486, character=Characters.Scarab, item_lot=40272, reward_delay=0.0, skip_reward=0)
    CommonFunc_NonRespawningWithReward(
        0,
        dead_flag=14000499,
        character=Characters.MoongrumCarianKnight,
        item_lot=14000980,
        reward_delay=0.0,
        skip_reward=0,
    )
    CommonFunc_90005780(
        0,
        flag=Flags.RedWolfDead,
        summon_flag=14002160,
        dismissal_flag=14002161,
        character=Characters.SorceressSellen3,
        sign_type=20,
        region=14002731,
        right=1034509259,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=Flags.RedWolfDead, flag_1=14002160, flag_2=14002161, character=Characters.SorceressSellen3)
    CommonFunc_90005782(
        0,
        flag=14002160,
        region=14002855,
        character=Characters.SorceressSellen3,
        target_entity=14002850,
        region_1=14002859,
        animation=0,
    )
    CommonFunc_90005795(
        0,
        flag=7608,
        flag_1=0,
        flag_2=1051369239,
        left_flag=14002141,
        cancel_flag__right_flag=14002142,
        message=80609,
        action_button_id=9000,
        asset=Assets.AEG099_090_9001,
        model_point=30010,
    )
    SkipLinesIfCeremonyInactive(line_count=2, ceremony=20)
    CommonFunc_InvadeAndKillNPC(0, flag=7608, character=Characters.SorceressSellen2, banner_type=5, region=14002141)
    Event_14002145()
    CommonFunc_90005795(
        0,
        flag=7609,
        flag_1=0,
        flag_2=1034509269,
        left_flag=14002143,
        cancel_flag__right_flag=14002144,
        message=80608,
        action_button_id=9000,
        asset=Assets.AEG099_090_9002,
        model_point=30000,
    )
    SkipLinesIfCeremonyInactive(line_count=2, ceremony=30)
    Event_14002155()
    Event_14002165(0, flag=7609, character=Characters.WitchHunterJerren1, banner_type=7, region=14002151)
    Event_14002495()
    Event_14000700()
    Event_14000701()
    Event_14000702()
    Event_14000703()
    Event_14000710(0, asset__character=14000710, asset__character_1=14000711)
    Event_14000711()
    CommonFunc_90005702(0, character=Characters.SorceressSellen2, flag=3463, first_flag=3460, last_flag=3463)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9003,
        action_button_id=4110,
        item_lot=101070,
        first_flag=400107,
        last_flag=400107,
        flag=3469,
        model_point=0,
    )
    Event_14000712()
    Event_14000713()
    Event_14000714()
    Event_14000720()
    Event_14000730(0, character=Characters.WitchHunterJerren2)
    CommonFunc_90005703(
        0,
        character=Characters.WitchHunterJerren2,
        flag=3361,
        flag_1=3362,
        flag_2=14009351,
        flag_3=3361,
        first_flag=3360,
        last_flag=3363,
        right=-1,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.WitchHunterJerren2,
        flag=3361,
        flag_1=3360,
        flag_2=14009351,
        right=3,
    )
    CommonFunc_90005702(0, character=Characters.WitchHunterJerren2, flag=3363, first_flag=3360, last_flag=3363)
    CommonFunc_90005702(0, character=Characters.WitchHunterJerren1, flag=3363, first_flag=3360, last_flag=3363)
    Event_14000731()
    Event_14000740(0, character=Characters.BoctheSeamster)
    Event_14000741(0, character=Characters.DemiHumanShaman)
    Event_14000742()
    Event_14000750(0, character=Characters.SorcererThops, asset=14006700)
    CommonFunc_90005750(0, 14001720, 4110, 103600, 400360, 400362, 3806, 0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.RennalaNPC1)
    DisableBackread(Characters.RennalaNPC2)
    DisableBackread(Characters.SorceressSellen0)
    DisableBackread(Characters.GravenSchool)
    DisableBackread(Characters.SorceressSellen1)
    DisableBackread(Characters.SorceressSellen2)
    DisableBackread(Characters.WitchHunterJerren0)
    DisableBackread(Characters.WitchHunterJerren1)
    DisableBackread(Characters.WitchHunterJerren2)
    DisableBackread(Characters.BoctheSeamster)
    DisableBackread(Characters.DemiHumanShaman)
    DisableBackread(Characters.SorcererThops)
    DisableAsset(14006710)
    Event_14000519()
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar0, region=14002200, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar1, region=14002200, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.RayaLucariaScholar2,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002451,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.RayaLucariaScholar6,
        animation_id=30000,
        animation_id_1=20000,
        region=14002228,
        radius=15.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar7, region=14002228, seconds=0.0, animation_id=-1)
    CommonFunc_90005210(
        0,
        character=Characters.RayaLucariaScholar8,
        animation_id=30000,
        animation_id_1=20000,
        region=14002228,
        radius=15.0,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar9, region=14002228, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar3, region=14002222, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar11, region=14002222, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar13, region=14002251, seconds=0.5, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar14, region=14002251, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar15, region=14002252, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=14000260, region=14002260, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=14000261, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar17, region=14002260, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=14000263, region=14002260, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar16, region=14002267, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar18, region=14002267, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar20, region=14002267, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar19, region=14002266, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.RayaLucariaScholar21,
        region=14002268,
        radius=3.0,
        seconds=1.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.RayaLucariaScholar22,
        region=14002268,
        radius=3.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar23, region=14002276, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar24, region=14002276, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar25, region=14002285, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar26, region=14002285, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.RayaLucariaScholar27, region=14002285, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.PutridCorpse0, region=14002300, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse1,
        inactive_animation=30005,
        active_animation=20005,
        trigger_region=14002305,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.PutridCorpse2, region=14002310, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.PutridCorpse3,
        inactive_animation=30000,
        active_animation=20000,
        radius=5.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.PutridCorpse4,
        inactive_animation=30000,
        active_animation=20000,
        radius=5.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse5,
        inactive_animation=30005,
        active_animation=20005,
        trigger_region=14002315,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse6,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002315,
        trigger_delay=0.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse7,
        inactive_animation=30006,
        active_animation=20006,
        trigger_region=14002315,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse8,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002315,
        trigger_delay=0.699999988079071,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse9,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002315,
        trigger_delay=0.800000011920929,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse10,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002315,
        trigger_delay=0.6000000238418579,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse11,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002315,
        trigger_delay=0.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.PutridCorpse12, region=14002323, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse13,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002325,
        trigger_delay=0.800000011920929,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse14,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002325,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(
        0,
        character=Characters.PutridCorpse18,
        region=14002335,
        radius=3.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse15,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002325,
        trigger_delay=1.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse16,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002325,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse17,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002325,
        trigger_delay=1.7999999523162842,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse19,
        inactive_animation=30006,
        active_animation=20006,
        trigger_region=14002340,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=14000341,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002340,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=14000342,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002340,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.PutridCorpse20,
        inactive_animation=30000,
        active_animation=20000,
        radius=3.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.PutridCorpse21,
        inactive_animation=30000,
        active_animation=20000,
        radius=3.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRadius(
        0,
        character=Characters.PutridCorpse22,
        inactive_animation=30000,
        active_animation=20000,
        radius=3.0,
        delay=0.0,
        disable_gravity_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=14000355,
        animation_id=30000,
        animation_id_1=20000,
        region=14002355,
        radius=5.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=14000356,
        animation_id=30000,
        animation_id_1=20000,
        region=14002355,
        radius=5.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse23,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse24,
        inactive_animation=30006,
        active_animation=20006,
        trigger_region=14002361,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpse25,
        inactive_animation=30006,
        active_animation=20006,
        trigger_region=14002361,
        trigger_delay=1.399999976158142,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.PutridCorpseBare0, radius=16.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.PutridCorpseBare2, region=14002345, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=14000392,
        animation_id=30000,
        animation_id_1=20000,
        region=14002355,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpseBare4,
        inactive_animation=30006,
        active_animation=20006,
        trigger_region=14002361,
        trigger_delay=0.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpseBare5,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=14002396,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpseBare7,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=14002396,
        trigger_delay=2.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.PutridCorpseBare8,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=14002396,
        trigger_delay=0.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.SmallerDog0, region=14002345, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.SmallerDog1,
        animation_id=30001,
        animation_id_1=20001,
        region=14002345,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.SmallerDog3,
        animation_id=30001,
        animation_id_1=20001,
        region=14002345,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.SmallerDog4,
        animation_id=30001,
        animation_id_1=20001,
        region=14002345,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble0,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble1,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble2,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble3,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble4,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.WanderingNoble8,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=14002267,
        trigger_delay=1.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.WanderingNoble9,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=14002267,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.WanderingNoble10,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=14002267,
        trigger_delay=1.7999999523162842,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble11,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.WanderingNoble13, region=14002267, seconds=0.0, animation_id=-1)
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble12,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.LivingPot,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002228,
        trigger_delay=10.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.SmallLivingPot5,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002410,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.SmallLivingPot6,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002410,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.SmallLivingPot7,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002410,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.SmallLivingPot8,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002410,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.SmallLivingPot9,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002410,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.SmallLivingPot10,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002410,
        trigger_delay=1.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.SmallLivingPot0,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002252,
        trigger_delay=4.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.SmallLivingPot1,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002252,
        trigger_delay=6.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.SmallLivingPot2,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002252,
        trigger_delay=7.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.SmallLivingPot3,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002252,
        trigger_delay=2.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.SmallLivingPot4,
        inactive_animation=30000,
        active_animation=20000,
        trigger_region=14002252,
        trigger_delay=2.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.LargeCrabSnow0,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=14002635,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.LargeCrabSnow1,
        inactive_animation=30001,
        active_animation=20001,
        trigger_region=14002636,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Marionette0,
        inactive_animation=30010,
        active_animation=20010,
        trigger_region=14002450,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Marionette1,
        inactive_animation=30010,
        active_animation=20010,
        trigger_region=14002451,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Marionette3,
        inactive_animation=30010,
        active_animation=20010,
        trigger_region=14002451,
        trigger_delay=1.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Marionette2,
        inactive_animation=30010,
        active_animation=20010,
        trigger_region=14002452,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=1,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegionOrRadius(0, character=Characters.Marionette4, region=14002461, radius=20.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Marionette9, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRadius(0, character=Characters.Marionette10, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Marionette7,
        inactive_animation=30010,
        active_animation=20010,
        trigger_region=14002472,
        trigger_delay=0.0,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerInactiveEnemy_WithRegion(
        0,
        character=Characters.Marionette8,
        inactive_animation=30010,
        active_animation=20010,
        trigger_region=14002472,
        trigger_delay=0.5,
        disable_gravity_and_collision=0,
        trigger_on_ai_battle=0,
        trigger_on_ai_unknown5=0,
        trigger_on_ai_unknown6=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Marionette11, region=14002487, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Marionette12, region=14002487, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerInactiveEnemy_WithRegionOrRadius(
        0,
        character=Characters.Avionette5,
        animation_id=30000,
        animation_id_1=20001,
        region=14002495,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Avionette8, region=14002396, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Avionette9, region=14002396, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.Page, region=14002675, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.MadPumpkinHead, region=14002276, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.IronVirgin0, region=14002293, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, character=Characters.IronVirgin1, region=14002294, seconds=0.0, animation_id=-1)
    CommonFunc_TriggerEnemyAI_WithRegion(0, 14000499, 14002499, 0.0, -1)


@ContinueOnRest(14002080)
def Event_14002080():
    """Event 14002080"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=14002080))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 14307))
    
    MAIN.Await(AND_1)
    
    SetRespawnPoint(respawn_point=16002080)
    SaveRequest()
    EnableFlag(16000540)


@RestartOnRest(14002145)
def Event_14002145():
    """Event 14002145"""
    ReturnIfCeremonyState(event_return_type=EventReturnType.End, state=False, ceremony=20)
    EnableBackread(Characters.SorceressSellen2)
    EnableBackread(Characters.WitchHunterJerren0)
    SetTeamType(Characters.SorceressSellen2, TeamType.Human)
    SetTeamType(Characters.WitchHunterJerren0, TeamType.Enemy)
    DeleteAssetVFX(14006710)
    CreateAssetVFX(14006710, vfx_id=200, model_point=806700)


@RestartOnRest(14002155)
def Event_14002155():
    """Event 14002155"""
    ReturnIfCeremonyState(event_return_type=EventReturnType.End, state=False, ceremony=30)
    EnableBackread(Characters.WitchHunterJerren1)
    EnableBackread(Characters.SorceressSellen1)
    SetTeamType(Characters.WitchHunterJerren1, TeamType.Enemy)
    SetTeamType(Characters.SorceressSellen1, TeamType.Human)
    DeleteAssetVFX(14006700)
    CreateAssetVFX(14006700, vfx_id=200, model_point=806700)


@RestartOnRest(14002165)
def Event_14002165(_, flag: uint, character: uint, banner_type: uchar, region: uint):
    """Event 14002165"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(CharacterProportionDead(character=character))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayBanner(banner_type)
    if UnsignedNotEqual(left=region, right=0):
        SetPseudoMultiplayerReturnPosition(region=region)
    AddSpecialEffect(20000, 4822)
    IssueEndOfPseudoMultiplayerNotification(success=True)


@RestartOnRest(14002580)
def Event_14002580():
    """Event 14002580"""
    RegisterLadder(start_climbing_flag=14000530, stop_climbing_flag=14000531, asset=Assets.AEG257_037_0500)
    RegisterLadder(start_climbing_flag=14000532, stop_climbing_flag=14000533, asset=Assets.AEG257_004_0500)
    RegisterLadder(start_climbing_flag=14000534, stop_climbing_flag=14000535, asset=Assets.AEG257_005_0500)
    RegisterLadder(start_climbing_flag=14000536, stop_climbing_flag=14000537, asset=Assets.AEG257_006_0500)
    RegisterLadder(start_climbing_flag=14000538, stop_climbing_flag=14000539, asset=Assets.AEG257_003_0500)
    RegisterLadder(start_climbing_flag=14000540, stop_climbing_flag=14000541, asset=Assets.AEG257_007_0500)
    RegisterLadder(start_climbing_flag=14000542, stop_climbing_flag=14000543, asset=Assets.AEG257_015_0500)


@ContinueOnRest(14002510)
def Event_14002510():
    """Event 14002510"""
    CommonFunc_90005500(
        0,
        flag=14000510,
        flag_1=14001511,
        left=0,
        asset=Assets.AEG257_009_0500,
        asset_1=Assets.AEG257_002_0500,
        obj_act_id=14003511,
        asset_2=m60_35_Assets.AEG257_002_2001,
        obj_act_id_1=1035463512,
        region=14002511,
        region_1=14002512,
        flag_2=14000512,
        flag_3=14000513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=14000515,
        flag_1=14000516,
        left=0,
        asset=Assets.AEG257_010_0500,
        asset_1=Assets.AEG257_002_0502,
        obj_act_id=14003516,
        asset_2=Assets.AEG257_002_0503,
        obj_act_id_1=14003517,
        region=14002516,
        region_1=14002517,
        flag_2=14000517,
        flag_3=14000518,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        14000520,
        14000521,
        0,
        14001520,
        14001521,
        14003521,
        14001522,
        14003522,
        14002521,
        14002522,
        14000522,
        14000523,
        0,
    )


@ContinueOnRest(14000519)
def Event_14000519():
    """Event 14000519"""
    if ThisEventSlotFlagEnabled():
        return
    DisableThisSlotFlag()


@RestartOnRest(14002498)
def Event_14002498():
    """Event 14002498"""
    GotoIfFlagEnabled(Label.L0, flag=14000546)
    EnableNavmeshType(navmesh_id=14002498, navmesh_type=NavmeshType.Solid)
    
    MAIN.Await(FlagEnabled(14000546))

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNavmeshType(navmesh_id=14002498, navmesh_type=NavmeshType.Solid)
    End()


@RestartOnRest(14003500)
def Event_14003500(_, region: uint, flag: uint):
    """Event 14003500"""
    DisableNetworkSync()
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(PLAYER, 9621)
    Wait(0.10000000149011612)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_3.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_3)
    
    Wait(0.10000000149011612)
    RemoveSpecialEffect(PLAYER, 9621)
    Restart()


@RestartOnRest(14002590)
def Event_14002590():
    """Event 14002590"""
    EnableNetworkSync()
    GotoIfFlagRangeAllDisabled(Label.L0, flag_range=(14000276, 14000277))
    DisableAsset(Assets.AEG257_014_0500)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(Assets.AEG257_014_0500)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(FlagEnabled(14002595))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EndIfFlagRangeAllEnabled(flag_range=(14000276, 14000277))
    EnableAsset(Assets.AEG257_014_0500)
    ForceAnimation(Assets.AEG257_014_0500, 1)
    CreateTemporaryVFX(
        vfx_id=814630,
        anchor_entity=Assets.AEG003_316_9001,
        model_point=100,
        anchor_type=CoordEntityType.Asset,
    )
    if FlagEnabled(50):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500000,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    if FlagEnabled(51):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500010,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    if FlagEnabled(52):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500020,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    if FlagEnabled(53):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500030,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    if FlagEnabled(54):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500040,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    if FlagEnabled(55):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500050,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    if FlagEnabled(56):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500060,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    if FlagEnabled(57):
        CreateHazard(
            asset_flag=14000590,
            asset=Assets.AEG257_014_0500,
            model_point=200,
            behavior_param_id=802500070,
            target_type=DamageTargetType.Character,
            radius=3.799999952316284,
            life=10.0,
            repetition_time=0.0,
        )
    Wait(10.0)
    DisableAsset(Assets.AEG257_014_0500)
    Restart()


@RestartOnRest(14002592)
def Event_14002592():
    """Event 14002592"""
    DeleteAssetVFX(Assets.AEG003_316_9002)
    CreateAssetVFX(Assets.AEG003_316_9002, vfx_id=100, model_point=814631)


@RestartOnRest(14002594)
def Event_14002594():
    """Event 14002594"""
    EndIfFlagRangeAllEnabled(flag_range=(14000276, 14000277))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=14002590))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(14002595)
    Wait(10.0)
    DisableNetworkFlag(14002595)
    Restart()


@RestartOnRest(14002650)
def Event_14002650(
    _,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
):
    """Event 14002650"""
    if Multiplayer():
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    AND_1.Add(Singleplayer())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9140, entity=anchor_entity))
    
    MAIN.Await(AND_1)
    
    DisplayDialogAndSetFlags(
        message=4300,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=anchor_entity,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(14002328)
def Event_14002328(_, character: uint):
    """Event 14002328"""
    Kill(character)


@RestartOnRest(14002360)
def Event_14002360(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    attacked_entity: uint,
    attacked_entity_1: uint,
    attacked_entity_2: uint,
):
    """Event 14002360"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(AttackedWithDamageType(attacked_entity=attacked_entity))
    OR_3.Add(AttackedWithDamageType(attacked_entity=attacked_entity_1))
    OR_3.Add(AttackedWithDamageType(attacked_entity=attacked_entity_2))
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(14002490)
def Event_14002490(_, character: uint, region: uint, seconds: float, animation_id: int):
    """Event 14002490"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    DisableGravity(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)
    EnableAI(character)
    EnableGravity(character)
    Wait(2.799999952316284)

    # --- Label 1 --- #
    DefineLabel(1)
    End()


@RestartOnRest(14002491)
def Event_14002491(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 14002491"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    DisableGravity(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)
    EnableAI(character)
    EnableGravity(character)
    Wait(2.799999952316284)

    # --- Label 1 --- #
    DefineLabel(1)
    End()


@RestartOnRest(14002495)
def Event_14002495():
    """Event 14002495"""
    DisableNetworkSync()
    OR_1.Add(FlagEnabled(14002140))
    OR_1.Add(FlagEnabled(14002150))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(Characters.TalkDummy7, 9531)
    AND_1.Add(FlagDisabled(14002140))
    AND_1.Add(FlagDisabled(14002150))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.TalkDummy7, 9532)
    Wait(1.0)
    Restart()


@ContinueOnRest(14002606)
def Event_14002606():
    """Event 14002606"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=14000676)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AssetActivated(obj_act_id=14003606))
    
    MAIN.Await(AND_1)
    
    Wait(0.10000000149011612)
    DisplayDialog(text=208199, anchor_entity=Assets.AEG099_630_9006)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAssetActivation(Assets.AEG099_630_9006, obj_act_id=199630)
    End()


@RestartOnRest(14002665)
def Event_14002665():
    """Event 14002665"""
    DisableAsset(14006600)


@RestartOnRest(14002689)
def Event_14002689():
    """Event 14002689"""
    GotoIfFlagEnabled(Label.L0, flag=14000801)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=14002689))
    
    ActivateGparamOverride(gparam_sub_id=500, change_duration=0.0)
    Wait(0.10000000149011612)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DeactivateGparamOverride(change_duration=0.0)
    End()


@RestartOnRest(14002800)
def RennalaDies():
    """Event 14002800"""
    GotoIfFlagDisabled(Label.L1, flag=14000804)
    EndOfAnimation(asset=Assets.AEG258_184_5001, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5002, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5006, animation_id=0)
    MoveRemains(source_region=14002840, destination_region=14002843)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L0, flag=Flags.RennalaDefeated)
    
    MAIN.Await(HealthValue(Characters.RennalaPhaseTwo) <= 0 and HealthValue(Characters.CLONE_RennalaPhaseTwo) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(14008000, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(Characters.RennalaPhaseTwo))
    AND_2.Add(CharacterDead(Characters.CLONE_RennalaPhaseTwo))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(Flags.RennalaDefeated))
    
    MAIN.Await(OR_2)
    
    Kill(CharacterGroups.Students)
    Kill(CharacterGroups.CLONE_Students)
    KillBossAndDisplayBanner(character=Characters.RennalaPhaseTwo, banner_type=BannerType.LegendFelled)
    EnableNetworkFlag(Flags.RennalaDefeated)
    EnableFlag(9118)
    if PlayerInOwnWorld():
        EnableFlag(61118)
    SetRespawnPoint(respawn_point=14003900)
    SaveRequest()
    Wait(8.0)
    if PlayerNotInOwnWorld():
        return

    # --- Label 0 --- #
    DefineLabel(0)
    WarpToMap(game_map=RAYA_LUCARIA, player_start=14003900)
    SetRespawnPoint(respawn_point=14003900)
    SaveRequest()
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    EnableAssetActivation(Assets.AEG099_630_9006, obj_act_id=199630)
    MoveRemains(source_region=14002840, destination_region=14002843)
    EndOfAnimation(asset=Assets.AEG257_031_5004, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5003, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5002, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5001, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5000, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5001, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5002, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5006, animation_id=0)
    CreateVFX(14002600)
    CreateVFX(14002601)
    CreateVFX(14002602)
    CreateVFX(14002603)
    CreateVFX(14002604)
    CreateVFX(14002605)
    CreateVFX(14002606)
    CreateVFX(14002607)
    CreateVFX(14002608)
    CreateVFX(14002609)
    CreateVFX(14002610)
    CreateVFX(14002611)
    CreateVFX(14002612)
    CreateVFX(14002613)
    CreateVFX(14002614)
    CreateVFX(14002615)
    CreateVFX(14002616)
    CreateVFX(14002617)
    CreateVFX(14002618)
    CreateVFX(14002619)
    CreateVFX(14002620)
    CreateVFX(14002621)
    CreateVFX(14002622)
    CreateVFX(14002623)
    CreateVFX(14002624)
    CreateVFX(14002625)
    CreateVFX(14002626)
    CreateVFX(14002627)
    CreateVFX(14002628)
    CreateVFX(14002629)
    CreateVFX(14002630)
    CreateVFX(14002631)
    CreateVFX(14002680)
    CreateVFX(14002681)
    CreateVFX(14002682)
    CreateVFX(14002683)
    CreateVFX(14002684)
    CreateVFX(14002685)
    CreateVFX(14002686)
    CreateVFX(14002687)
    EnableFlag(14000804)
    SetBackreadStateAlternate(35000, False)
    SetNetworkUpdateRate(35000, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryFiveFrames)


@RestartOnRest(14002810)
def RennalaBattleTrigger():
    """Event 14002810"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.RennalaDefeated)
    DisableCharacter(CharacterGroups.RennalaBoss)
    DisableAnimations(CharacterGroups.RennalaBoss)
    Kill(CharacterGroups.RennalaBoss)
    EnableCharacter(Characters.RennalaNPC1)
    EnableAnimations(Characters.RennalaNPC1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(CharacterGroups.RennalaBoss)
    DisableCharacter(Characters.RennalaNPC1)
    DisableAnimations(Characters.RennalaNPC1)
    DisableCharacter(Characters.RennalaPhaseTwo)
    DisableAnimations(Characters.RennalaPhaseTwo)
    DisableCharacter(Characters.CLONE_RennalaPhaseTwo)
    DisableAnimations(Characters.CLONE_RennalaPhaseTwo)
    DisableAssetActivation(Assets.AEG099_630_9006, obj_act_id=199630)
    MoveRemains(source_region=14002840, destination_region=14002841)
    GotoIfFlagEnabled(Label.L1, flag=14000801)

    DisableCharacter(CharacterGroups.RennalaBoss)
    DisableAnimations(CharacterGroups.RennalaBoss)
    EndOfAnimation(asset=Assets.AEG257_031_5004, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5003, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5002, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5001, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5000, animation_id=10)
    EndOfAnimation(asset=Assets.AEG258_184_5001, animation_id=1)
    EndOfAnimation(asset=Assets.AEG258_184_5002, animation_id=1)
    EndOfAnimation(asset=Assets.AEG258_184_5006, animation_id=1)
    DeleteVFX(14002600, erase_root_only=False)
    DeleteVFX(14002601, erase_root_only=False)
    DeleteVFX(14002602, erase_root_only=False)
    DeleteVFX(14002603, erase_root_only=False)
    DeleteVFX(14002604, erase_root_only=False)
    DeleteVFX(14002605, erase_root_only=False)
    DeleteVFX(14002606, erase_root_only=False)
    DeleteVFX(14002607, erase_root_only=False)
    DeleteVFX(14002608, erase_root_only=False)
    DeleteVFX(14002609, erase_root_only=False)
    DeleteVFX(14002610, erase_root_only=False)
    DeleteVFX(14002611, erase_root_only=False)
    DeleteVFX(14002612, erase_root_only=False)
    DeleteVFX(14002613, erase_root_only=False)
    DeleteVFX(14002614, erase_root_only=False)
    DeleteVFX(14002615, erase_root_only=False)
    DeleteVFX(14002616, erase_root_only=False)
    DeleteVFX(14002617, erase_root_only=False)
    DeleteVFX(14002618, erase_root_only=False)
    DeleteVFX(14002619, erase_root_only=False)
    DeleteVFX(14002620, erase_root_only=False)
    DeleteVFX(14002621, erase_root_only=False)
    DeleteVFX(14002622, erase_root_only=False)
    DeleteVFX(14002623, erase_root_only=False)
    DeleteVFX(14002624, erase_root_only=False)
    DeleteVFX(14002625, erase_root_only=False)
    DeleteVFX(14002626, erase_root_only=False)
    DeleteVFX(14002627, erase_root_only=False)
    DeleteVFX(14002628, erase_root_only=False)
    DeleteVFX(14002629, erase_root_only=False)
    DeleteVFX(14002630, erase_root_only=False)
    DeleteVFX(14002631, erase_root_only=False)
    DeleteVFX(14002680, erase_root_only=False)
    DeleteVFX(14002681, erase_root_only=False)
    DeleteVFX(14002682, erase_root_only=False)
    DeleteVFX(14002683, erase_root_only=False)
    DeleteVFX(14002684, erase_root_only=False)
    DeleteVFX(14002685, erase_root_only=False)
    DeleteVFX(14002686, erase_root_only=False)
    DeleteVFX(14002687, erase_root_only=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent0, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent1, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent2, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent3, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent4, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent5, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent6, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent7, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent8, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent9, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent10, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent11, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent12, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent13, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent14, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent15, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent16, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent17, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent18, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent19, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent20, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent21, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent22, state=False)
    SetCharacterFadeOnEnable(character=Characters.RennalaStudent23, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent0, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent1, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent2, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent3, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent4, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent5, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent6, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent7, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent8, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent9, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent10, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent11, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent12, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent13, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent14, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent15, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent16, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent17, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent18, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent19, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent20, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent21, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent22, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaStudent23, state=False)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=14002801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.RennalaPhaseOne, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.CLONE_RennalaPhaseOne, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableFlag(9021)
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=14000000,
            cutscene_flags=0,
            move_to_region=14002802,
            map_id=14000000,
            player_id=PLAYER,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(14000000, cutscene_flags=0, player_id=PLAYER)
    WaitFramesAfterCutscene(frames=1)
    EnableNetworkFlag(14000801)
    EnableCharacter(Characters.RennalaPhaseOne)
    EnableAnimations(Characters.RennalaPhaseOne)
    EnableCharacter(Characters.CLONE_RennalaPhaseOne)
    EnableAnimations(Characters.CLONE_RennalaPhaseOne)
    EnableCharacter(CharacterGroups.Students)
    EnableAnimations(CharacterGroups.Students)
    EnableCharacter(CharacterGroups.CLONE_Students)
    EnableAnimations(CharacterGroups.CLONE_Students)
    EndOfAnimation(asset=Assets.AEG257_031_5004, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5003, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5002, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5001, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5000, animation_id=0)
    ForceAnimation(Assets.AEG257_031_5000, 0, loop=True)
    EndOfAnimation(asset=Assets.AEG258_184_5001, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5002, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5006, animation_id=0)
    CreateVFX(14002600)
    CreateVFX(14002601)
    CreateVFX(14002602)
    CreateVFX(14002603)
    CreateVFX(14002604)
    CreateVFX(14002605)
    CreateVFX(14002606)
    CreateVFX(14002607)
    CreateVFX(14002608)
    CreateVFX(14002609)
    CreateVFX(14002610)
    CreateVFX(14002611)
    CreateVFX(14002612)
    CreateVFX(14002613)
    CreateVFX(14002614)
    CreateVFX(14002615)
    CreateVFX(14002616)
    CreateVFX(14002617)
    CreateVFX(14002618)
    CreateVFX(14002619)
    CreateVFX(14002620)
    CreateVFX(14002621)
    CreateVFX(14002622)
    CreateVFX(14002623)
    CreateVFX(14002624)
    CreateVFX(14002625)
    CreateVFX(14002626)
    CreateVFX(14002627)
    CreateVFX(14002628)
    CreateVFX(14002629)
    CreateVFX(14002630)
    CreateVFX(14002631)
    CreateVFX(14002680)
    CreateVFX(14002681)
    CreateVFX(14002682)
    CreateVFX(14002683)
    CreateVFX(14002684)
    CreateVFX(14002685)
    CreateVFX(14002686)
    CreateVFX(14002687)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EndOfAnimation(asset=Assets.AEG257_031_5004, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5003, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5002, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5001, animation_id=0)
    EndOfAnimation(asset=Assets.AEG257_031_5000, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5001, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5002, animation_id=0)
    EndOfAnimation(asset=Assets.AEG258_184_5006, animation_id=0)
    CreateVFX(14002600)
    CreateVFX(14002601)
    CreateVFX(14002602)
    CreateVFX(14002603)
    CreateVFX(14002604)
    CreateVFX(14002605)
    CreateVFX(14002606)
    CreateVFX(14002607)
    CreateVFX(14002608)
    CreateVFX(14002609)
    CreateVFX(14002610)
    CreateVFX(14002611)
    CreateVFX(14002612)
    CreateVFX(14002613)
    CreateVFX(14002614)
    CreateVFX(14002615)
    CreateVFX(14002616)
    CreateVFX(14002617)
    CreateVFX(14002618)
    CreateVFX(14002619)
    CreateVFX(14002620)
    CreateVFX(14002621)
    CreateVFX(14002622)
    CreateVFX(14002623)
    CreateVFX(14002624)
    CreateVFX(14002625)
    CreateVFX(14002626)
    CreateVFX(14002627)
    CreateVFX(14002628)
    CreateVFX(14002629)
    CreateVFX(14002630)
    CreateVFX(14002631)
    CreateVFX(14002680)
    CreateVFX(14002681)
    CreateVFX(14002682)
    CreateVFX(14002683)
    CreateVFX(14002684)
    CreateVFX(14002685)
    CreateVFX(14002686)
    CreateVFX(14002687)
    AND_2.Add(FlagEnabled(Flags.RennalaBattleStarted))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=14002800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(CharacterGroups.RennalaBoss)
    SetNetworkUpdateRate(Characters.RennalaPhaseOne, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_RennalaPhaseOne, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(
        CharacterGroups.Students, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryFiveFrames
    )
    SetNetworkUpdateRate(
        CharacterGroups.CLONE_Students, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryFiveFrames)
    EnableBossHealthBar(Characters.RennalaPhaseOne, name=NameText.RennalaQueenOfTheFullMoon, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_RennalaPhaseOne, name=NameText.RhondaQueenOfTheWhiteDust, bar_slot=0)


@RestartOnRest(14002811)
def RennalaPhaseTwoTransition():
    """Event 14002811"""
    if FlagEnabled(Flags.RennalaDefeated):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterDead(Characters.RennalaPhaseOne))
    AND_1.Add(CharacterDead(Characters.CLONE_RennalaPhaseOne))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(14002802)
    SetCharacterFadeOnEnable(character=Characters.RennalaPhaseTwo, state=False)
    SetCharacterFadeOnEnable(character=Characters.CLONE_RennalaPhaseTwo, state=False)
    EndOfAnimation(asset=Assets.AEG257_031_5004, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5003, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5002, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5001, animation_id=10)
    EndOfAnimation(asset=Assets.AEG257_031_5000, animation_id=10)
    EndOfAnimation(asset=Assets.AEG258_184_5001, animation_id=1)
    EndOfAnimation(asset=Assets.AEG258_184_5002, animation_id=1)
    EndOfAnimation(asset=Assets.AEG258_184_5006, animation_id=1)
    DeleteVFX(14002600, erase_root_only=False)
    DeleteVFX(14002601, erase_root_only=False)
    DeleteVFX(14002602, erase_root_only=False)
    DeleteVFX(14002603, erase_root_only=False)
    DeleteVFX(14002604, erase_root_only=False)
    DeleteVFX(14002605, erase_root_only=False)
    DeleteVFX(14002606, erase_root_only=False)
    DeleteVFX(14002607, erase_root_only=False)
    DeleteVFX(14002608, erase_root_only=False)
    DeleteVFX(14002609, erase_root_only=False)
    DeleteVFX(14002610, erase_root_only=False)
    DeleteVFX(14002611, erase_root_only=False)
    DeleteVFX(14002612, erase_root_only=False)
    DeleteVFX(14002613, erase_root_only=False)
    DeleteVFX(14002614, erase_root_only=False)
    DeleteVFX(14002615, erase_root_only=False)
    DeleteVFX(14002616, erase_root_only=False)
    DeleteVFX(14002617, erase_root_only=False)
    DeleteVFX(14002618, erase_root_only=False)
    DeleteVFX(14002619, erase_root_only=False)
    DeleteVFX(14002620, erase_root_only=False)
    DeleteVFX(14002621, erase_root_only=False)
    DeleteVFX(14002622, erase_root_only=False)
    DeleteVFX(14002623, erase_root_only=False)
    DeleteVFX(14002624, erase_root_only=False)
    DeleteVFX(14002625, erase_root_only=False)
    DeleteVFX(14002626, erase_root_only=False)
    DeleteVFX(14002627, erase_root_only=False)
    DeleteVFX(14002628, erase_root_only=False)
    DeleteVFX(14002629, erase_root_only=False)
    DeleteVFX(14002630, erase_root_only=False)
    DeleteVFX(14002631, erase_root_only=False)
    DeleteVFX(14002680, erase_root_only=False)
    DeleteVFX(14002681, erase_root_only=False)
    DeleteVFX(14002682, erase_root_only=False)
    DeleteVFX(14002683, erase_root_only=False)
    DeleteVFX(14002684, erase_root_only=False)
    DeleteVFX(14002685, erase_root_only=False)
    DeleteVFX(14002686, erase_root_only=False)
    DeleteVFX(14002687, erase_root_only=False)
    SetPlayerPositionDisplay(
        state=False,
        aboveground=True,
        game_map=RAYA_LUCARIA,
        x=42.02000045776367,
        y=154.1999969482422,
        z=-23.889999389648438,
    )
    SetBackreadStateAlternate(Characters.RennalaPhaseTwo, True)
    SetBackreadStateAlternate(Characters.CLONE_RennalaPhaseTwo, True)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=14000010,
            cutscene_flags=0,
            move_to_region=14002803,
            map_id=14000000,
            player_id=PLAYER,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=14000010,
            cutscene_flags=0,
            move_to_region=14002806,
            map_id=14000000,
            player_id=PLAYER,
            unk_20_24=0,
            unk_24_25=False,
        )
    WaitFramesAfterCutscene(frames=1)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=4.960000038146973, y_angle=-117.80000305175781)
    EnableFlag(14002803)
    SetBackreadStateAlternate(35000, True)
    SetNetworkUpdateRate(35000, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryFiveFrames)
    Move(
        35000,
        destination=14002806,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.RennalaPhaseTwo,
    )
    Move(
        Characters.TalkDummy7,
        destination=14002806,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.RennalaPhaseTwo,
    )
    SetCharacterTalkRange(character=Characters.TalkDummy7, distance=200.0)
    SetWeather(weather=Weather.Default, duration=-1.0, immediate_change=False)
    EnableCharacter(Characters.RennalaPhaseTwo)
    EnableAnimations(Characters.RennalaPhaseTwo)
    ForceAnimation(Characters.RennalaPhaseTwo, 20005)
    EnableCharacter(Characters.CLONE_RennalaPhaseTwo)
    EnableAnimations(Characters.CLONE_RennalaPhaseTwo)
    ForceAnimation(Characters.CLONE_RennalaPhaseTwo, 20005)
    EnableBossHealthBar(Characters.RennalaPhaseTwo, name=NameText.RennalaQueenOfTheFullMoon2, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_RennalaPhaseTwo, name=NameText.RhondaQueenOfTheWhiteDust2, bar_slot=0)
    SetNetworkUpdateRate(Characters.RennalaPhaseTwo, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.CLONE_RennalaPhaseTwo, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    WaitFramesAfterCutscene(frames=1)
    AttachAssetToCharacter(character=Characters.TalkDummy7, model_point=10, asset=Assets.AEG099_052_9001)


@RestartOnRest(140028121)
def Event_140028121():
    """Event 140028121"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(Flags.RennalaDefeated):
        return
    OR_1.Add(CharacterHasSpecialEffect(Characters.RennalaPhaseOne, Effects.RennalaSpecialStudentRequest))
    
    MAIN.Await(OR_1)
    
    EnableFlag(14002707)
    AND_1.Add(FlagDisabled(14002707))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.RennalaPhaseOne, Effects.RennalaSpecialStudentRequest))
    
    MAIN.Await(AND_1)
    
    Restart()


@RestartOnRest(140028122)
def Event_140028122(_, character: uint, special_effect: int, special_effect_1: int):
    """Event 140028122"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(character):
        return
    OR_1.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_1.Add(CharacterHasSpecialEffect(character, special_effect_1))
    
    MAIN.Await(OR_1)
    
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=special_effect)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=character, special_effect=special_effect_1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(14002720)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(14002722)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_1.Add(FlagRangeAllDisabled(flag_range=(14002720, 14002723)))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, special_effect))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, special_effect_1))
    
    MAIN.Await(AND_1)
    
    Restart()


@RestartOnRest(14002849)
def Event_14002849():
    """Event 14002849"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.RennalaDefeated,
        fog_asset=Assets.AEG099_001_9000,
        fog_region=14002800,
        host_entered_fog_flag=Flags.RennalaBattleStarted,
        boss_characters=CharacterGroups.RennalaBoss,
        action_button_id=10000,
        first_time_done_flag=14000801,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.RennalaDefeated,
        fog_asset=Assets.AEG099_001_9000,
        fog_region=14002800,
        host_entered_fog_flag=Flags.RennalaBattleStarted,
        summon_entered_fog_flag=14002806,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.RennalaDefeated, fog_asset=Assets.AEG099_001_9000, model_point=3, required_flag=14000801)
    CommonFunc_ControlBossMusic(0, Flags.RennalaDefeated, 203000, Flags.RennalaBattleStarted, 14002806, 0, 14002803, 1, 0)


@RestartOnRest(14002850)
def RedWolfDies():
    """Event 14002850"""
    if FlagEnabled(Flags.RedWolfDead):
        return
    
    MAIN.Await(HealthRatio(Characters.RedWolf) <= 0.0 and HealthRatio(Characters.CLONE_RedWolf) <= 0.0)
    
    Wait(2.0)
    PlaySoundEffect(Characters.RedWolf, 77777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.RedWolf) and CharacterDead(Characters.CLONE_RedWolf))
    
    KillBossAndDisplayBanner(character=Characters.RedWolf, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(Flags.RedWolfDead)
    EnableFlag(9117)
    if PlayerInOwnWorld():
        EnableFlag(61117)


@RestartOnRest(14002860)
def RedWolfBattleTrigger():
    """Event 14002860"""
    GotoIfFlagDisabled(Label.L0, flag=Flags.RedWolfDead)
    DisableCharacter(Characters.RedWolf)
    DisableAnimations(Characters.RedWolf)
    Kill(Characters.RedWolf)
    DisableCharacter(Characters.CLONE_RedWolf)
    DisableAnimations(Characters.CLONE_RedWolf)
    Kill(Characters.CLONE_RedWolf)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.RedWolf)
    DisableAI(Characters.CLONE_RedWolf)
    GotoIfFlagEnabled(Label.L1, flag=14000851)
    ForceAnimation(Characters.RedWolf, 30002, loop=True)
    ForceAnimation(Characters.CLONE_RedWolf, 30002, loop=True)
    AND_2.Add(FlagEnabled(14002855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=14002850))
    
    MAIN.Await(AND_2)
    
    EnableNetworkFlag(14000851)
    ForceAnimation(Characters.RedWolf, 20002)
    ForceAnimation(Characters.CLONE_RedWolf, 20002)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(Characters.RedWolf, destination=RegionPoints.RedWolfFirstPosition, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.CLONE_RedWolf, destination=RegionPoints.CLONE_RedWolfFirstPosition, destination_type=CoordEntityType.Region, short_move=True)
    AND_2.Add(FlagEnabled(14002855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=14002850))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.RedWolf)
    EnableAI(Characters.CLONE_RedWolf)
    SetNetworkUpdateRate(CharacterGroups.RedWolfBoss, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.RedWolf, name=NameText.RedWolfOfRadagon, bar_slot=1)
    EnableBossHealthBar(Characters.CLONE_RedWolf, name=NameText.GingerSif, bar_slot=0)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(CharacterGroups.RedWolfBoss, authority_level=UpdateAuthority.Forced)


@RestartOnRest(14002889)
def RedWolfFogGateEvents():
    """Event 14002889"""
    CommonFunc_HostEntersBossFog(
        0,
        boss_dead_flag=Flags.RedWolfDead,
        fog_asset=Assets.AEG099_003_9000,
        fog_region=14002850,
        host_entered_fog_flag=14002855,
        boss_characters=14005850,
        action_button_id=10000,
        first_time_done_flag=0,
        first_time_trigger_region=0,
    )
    CommonFunc_SummonEntersBossFog(
        0,
        boss_dead_flag=Flags.RedWolfDead,
        fog_asset=Assets.AEG099_003_9000,
        fog_region=14002850,
        host_entered_fog_flag=14002855,
        summon_entered_fog_flag=14002856,
        action_button_id=10000,
    )
    CommonFunc_ControlBossFog(0, boss_dead_flag=Flags.RedWolfDead, fog_asset=Assets.AEG099_003_9000, model_point=3, required_flag=0)
    CommonFunc_9005813(
        0,
        flag=Flags.RedWolfDead,
        asset=Assets.AEG099_003_9001,
        model_point=3,
        right=14000851,
        model_point_1=806760,
    )
    CommonFunc_ControlBossMusic(0, Flags.RedWolfDead, 921400, 14002855, 14002856, 0, 14000852, 0, 0)


@RestartOnRest(14002820)
def Event_14002820(_, character: uint):
    """Event 14002820"""
    DisableAI(character)
    AND_1.Add(CharacterInsideRegion(character=20000, region=14002812))
    AND_1.Add(HasAIStatus(Characters.RennalaStudent0, ai_status=AIStatusType.Battle))
    
    MAIN.Await(AND_1)
    
    EnableAI(character)
    DisableAsset(Assets.AEG099_001_9000)
    DisableAsset(14006800)
    SetNetworkUpdateRate(Characters.RennalaPhaseOne, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(character)
    
    MAIN.Await(FlagEnabled(14002810))
    
    WaitFrames(frames=1)
    DisableBossHealthBar(Characters.RennalaPhaseOne)
    EnableBossHealthBar(character)


@RestartOnRest(14002821)
def Event_14002821(_, character: uint):
    """Event 14002821"""
    OR_1.Add(EntityWithinDistance(entity=20000, other_entity=character, radius=30.0))
    OR_1.Add(HealthRatio(character, target_comparison_type=ComparisonType.NotEqual) == 1.0)
    
    MAIN.Await(OR_1)
    
    SetNetworkUpdateRate(Characters.RennalaPhaseOne, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    EnableAI(character)
    EnableBossHealthBar(character)


@RestartOnRest(14002822)
def Event_14002822(_, character: uint):
    """Event 14002822"""
    MAIN.Await(CharacterDead(character))
    
    Wait(1.5)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.DemigodFelled)
    EnableFlag(14000899)


@RestartOnRest(Flags.EVENT_ChooseRandomGlowingStudent)
def ChooseRandomGlowingStudent(
    _,
    required_flag: uint,
    rennala: uint,
    student_group: uint,
    student_2: uint,
    student_3: uint,
    student_4: uint,
    student_5: uint,
    student_6: uint,
    student_7: uint,
    student_8: uint,
    student_9: uint,
    student_10: uint,
    student_11: uint,
    student_12: uint,
    student_13: uint,
    student_14: uint,
    student_15: uint,
    student_16: uint,
    student_17: uint,
    student_18: uint,
    student_19: uint,
    student_20: uint,
    student_21: uint,
    student_22: uint,
    student_23: uint,
    student_24: uint,
    student_25: uint,
):
    """Event 14003801"""
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(FlagEnabled(Flags.RennalaBattleStarted))
    AwaitConditionTrue(AND_10)
    AND_1.Add(FlagEnabled(required_flag))
    AND_1.Add(CharacterHasSpecialEffect(student_group, Effects.StudentGlowing, target_comparison_type=ComparisonType.LessThan))
    OR_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBarrierUnknown))
    OR_1.Add(CharacterHasSpecialEffect(rennala, Effects.FirstGlowingStudentChosen))
    OR_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBarrierDamagedOnce))
    OR_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBarrierDamagedTwice))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisableFlag(Flags.RennalaRandomFlag1)
    DisableFlag(Flags.RennalaRandomFlag2)
    DisableFlag(Flags.RennalaRandomFlag3)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(Flags.RennalaRandomFlag1, Flags.RennalaRandomFlag3))
    if FlagDisabled(Flags.RennalaRandomFlag3):
        GotoIfFlagEnabled(Label.L0, flag=Flags.RennalaRandomFlag1)
        GotoIfFlagEnabled(Label.L1, flag=Flags.RennalaRandomFlag2)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_2, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_2, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_2, special_effect=14393)
    AddSpecialEffect(student_2, Effects.StudentGlowing)
    ReplanAI(student_2)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_3, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_3, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_3, special_effect=14393)
    AddSpecialEffect(student_3, Effects.StudentGlowing)
    ReplanAI(student_3)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_4, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_4, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_4, special_effect=14393)
    AddSpecialEffect(student_4, Effects.StudentGlowing)
    ReplanAI(student_4)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_5, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_5, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_5, special_effect=14393)
    AddSpecialEffect(student_5, Effects.StudentGlowing)
    ReplanAI(student_5)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_6, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_6, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_6, special_effect=14393)
    AddSpecialEffect(student_6, Effects.StudentGlowing)
    ReplanAI(student_6)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_7, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_7, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_7, special_effect=14393)
    AddSpecialEffect(student_7, Effects.StudentGlowing)
    ReplanAI(student_7)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_8, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_8, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_8, special_effect=14393)
    AddSpecialEffect(student_8, Effects.StudentGlowing)
    ReplanAI(student_8)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_9, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_9, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_9, special_effect=14393)
    AddSpecialEffect(student_9, Effects.StudentGlowing)
    ReplanAI(student_9)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_10, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_10, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_10, special_effect=14393)
    AddSpecialEffect(student_10, Effects.StudentGlowing)
    ReplanAI(student_10)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_11, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_11, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_11, special_effect=14393)
    AddSpecialEffect(student_11, Effects.StudentGlowing)
    ReplanAI(student_11)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_12, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_12, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_12, special_effect=14393)
    AddSpecialEffect(student_12, Effects.StudentGlowing)
    ReplanAI(student_12)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_13, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_13, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_13, special_effect=14393)
    AddSpecialEffect(student_13, Effects.StudentGlowing)
    ReplanAI(student_13)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_14, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_14, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_14, special_effect=14393)
    AddSpecialEffect(student_14, Effects.StudentGlowing)
    ReplanAI(student_14)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_15, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_15, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_15, special_effect=14393)
    AddSpecialEffect(student_15, Effects.StudentGlowing)
    ReplanAI(student_15)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_16, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_16, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_16, special_effect=14393)
    AddSpecialEffect(student_16, Effects.StudentGlowing)
    ReplanAI(student_16)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_17, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_17, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_17, special_effect=14393)
    AddSpecialEffect(student_17, Effects.StudentGlowing)
    ReplanAI(student_17)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_18, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_18, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_18, special_effect=14393)
    AddSpecialEffect(student_18, Effects.StudentGlowing)
    ReplanAI(student_18)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_19, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_19, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_19, special_effect=14393)
    AddSpecialEffect(student_19, Effects.StudentGlowing)
    ReplanAI(student_19)
    Restart()
    Goto(Label.L10)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_20, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_20, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_20, special_effect=14393)
    AddSpecialEffect(student_20, Effects.StudentGlowing)
    ReplanAI(student_20)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_21, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_21, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_21, special_effect=14393)
    AddSpecialEffect(student_21, Effects.StudentGlowing)
    ReplanAI(student_21)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_22, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_22, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_22, special_effect=14393)
    AddSpecialEffect(student_22, Effects.StudentGlowing)
    ReplanAI(student_22)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_23, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_23, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_23, special_effect=14393)
    AddSpecialEffect(student_23, Effects.StudentGlowing)
    ReplanAI(student_23)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_24, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_24, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_24, special_effect=14393)
    AddSpecialEffect(student_24, Effects.StudentGlowing)
    ReplanAI(student_24)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_25, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=student_25, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=student_25, special_effect=14393)
    AddSpecialEffect(student_25, Effects.StudentGlowing)
    ReplanAI(student_25)
    Restart()


@RestartOnRest(Flags.EVENT_RennalaBarrierBreaks)
def RennalaBarrierBreaks(_, required_flag: uint, rennala: uint, student_group: uint, character_2: uint):
    """Event 14003805"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBarrierDamaged))
    AND_1.Add(CharacterHasSpecialEffect(student_group, Effects.GlowingStudentHit, target_count=0.0))  # NO students have it
    AND_1.Add(CharacterHasSpecialEffect(student_group, Effects.StudentGlowing, target_count=0.0))  # NO students have it
    AND_1.Add(FlagEnabled(required_flag))
    
    MAIN.Await(AND_1)  # Rennala vulnerable and no students are glowing (or have just been hit while glowing)
    
    GotoIfCharacterHasSpecialEffect(Label.L1, character=rennala, special_effect=Effects.RennalaBarrierDamagedTwice)
    GotoIfCharacterHasSpecialEffect(Label.L0, character=rennala, special_effect=Effects.RennalaBarrierDamagedOnce)
    if CharacterDoesNotHaveSpecialEffect(character=rennala, special_effect=Effects.FirstGlowingStudentChosen):
        return RESTART  # Rennala has not repaired her barrier yet; restart.

    # Barrier damaged ONCE.
    AddSpecialEffect(rennala, Effects.RennalaBarrierDamagedOnce)
    OR_15.Add(CharacterHasSpecialEffect(student_group, Effects.StudentGlowing, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AwaitConditionTrue(OR_15)  # wait for a new Glowing Student to be chosen
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    # Barrier damaged TWICE.
    AddSpecialEffect(rennala, Effects.RennalaBarrierDamagedTwice)
    OR_15.Add(CharacterHasSpecialEffect(student_group, Effects.StudentGlowing, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AwaitConditionTrue(OR_15)  # wait for a new Glowing Student to be chosen
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    # Barrier damaged THREE TIMES and BROKEN.
    AddSpecialEffect(rennala, Effects.RennalaBarrierUnknown)
    AddSpecialEffect(student_group, 14384)
    AddSpecialEffect(rennala, 14578)
    ReplanAI(rennala)
    EnableFlag(Flags.RennalaBarrierReset)
    DisableFlag(Flags.RennalaBarrierActive)
    AddSpecialEffect(student_group, 14388)
    AddSpecialEffect(character_2, 14388)
    Restart()


@RestartOnRest(Flags.EVENT_RennalaBarrierDamaged)
def RennalaBarrierDamaged(_, rennala: uint, student_group: uint):
    """Event 14003807"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBarrierUnknown))
    AND_1.Add(CharacterHasSpecialEffect(rennala, 14358))
    AND_1.Add(CharacterHasSpecialEffect(student_group, Effects.GlowingStudentHit, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(rennala, Effects.RennalaBarrierDamaged)
    AddSpecialEffect(student_group, Effects.StudentsReactToBarrierDamage)
    DisableFlag(Flags.RennalaBarrierReset)
    Restart()


@RestartOnRest(Flags.EVENT_RennalaVulnerableTimer)
def RennalaVulnerableTimer(_, barrier_active_flag: uint, rennala: uint):
    """Event 14003808"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(rennala, 14358))
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBarrierUnknown))
    AND_1.Add(FlagDisabled(barrier_active_flag))
    
    MAIN.Await(AND_1)
    
    Wait(10.0)  # vulnerability time for Rennala
    EnableFlag(barrier_active_flag)
    OR_15.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBarrierDamaged))
    AwaitConditionFalse(OR_15)  # wait for barrier to NOT be damaged
    Restart()


@RestartOnRest(Flags.EVENT_RennalaRequestsSpecialStudent)
def RennalaRequestsSpecialStudent(_, request_flag: uint, rennala: uint):
    """Event 14003809"""
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaSpecialStudentRequest))
    AND_1.Add(FlagDisabled(request_flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(request_flag)
    Wait(3.0)
    DisableFlag(request_flag)
    Restart()


@RestartOnRest(Flags.EVENT_ChooseRandomSpecialStudent)
def ChooseRandomSpecialStudent(
    _,
    request_flag: uint,
    student_group: uint,
    student_1: uint,
    student_2: uint,
    student_3: uint,
    student_4: uint,
    student_5: uint,
    student_6: uint,
    student_7: uint,
    student_8: uint,
    student_9: uint,
    student_10: uint,
    student_11: uint,
    student_12: uint,
    student_13: uint,
    student_14: uint,
    student_15: uint,
    student_16: uint,
    student_17: uint,
    student_18: uint,
    student_19: uint,
    student_20: uint,
    student_21: uint,
    student_22: uint,
    student_23: uint,
    student_24: uint,
):
    """Event 14003811"""

    # If five or more students have effect 14351, ignore request (disable `flag` and restart this event).
    OR_1.Add(CharacterHasSpecialEffect(
        student_group,
        Effects.SpecialStudent,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=5.0,
    ))
    SkipLinesIfConditionFalse(2, OR_1)
    DisableFlag(request_flag)
    Restart()

    AND_1.Add(FlagEnabled(request_flag))
    AND_1.Add(CharacterHasSpecialEffect(student_group, Effects.SpecialStudent, target_comparison_type=ComparisonType.LessThan, target_count=5.0))
    MAIN.Await(AND_1)

    # First die roll chooses one of three subsets of students to try.
    DisableFlag(Flags.RennalaRandomFlag1)
    DisableFlag(Flags.RennalaRandomFlag2)
    DisableFlag(Flags.RennalaRandomFlag3)
    EnableRandomFlagInRange(flag_range=(Flags.RennalaRandomFlag1, Flags.RennalaRandomFlag3))
    if FlagDisabled(Flags.RennalaRandomFlag3):
        GotoIfFlagEnabled(Label.L0, flag=Flags.RennalaRandomFlag1)
        GotoIfFlagEnabled(Label.L1, flag=Flags.RennalaRandomFlag2)

    # Being chosen applies effect 14351, To be chosen, a student must:
    #  - HAVE effects 14577 and 14393
    #  - NOT HAVE effects 14351 and 14394.

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_1, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_1, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_1, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_1, special_effect=14393)
    AddSpecialEffect(student_1, Effects.SpecialStudent)
    ReplanAI(student_1)
    SetNetworkUpdateRate(student_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_2, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_2, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_2, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_2, special_effect=14393)
    AddSpecialEffect(student_2, Effects.SpecialStudent)
    ReplanAI(student_2)
    SetNetworkUpdateRate(student_2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_3, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_3, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_3, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_3, special_effect=14393)
    AddSpecialEffect(student_3, Effects.SpecialStudent)
    ReplanAI(student_3)
    SetNetworkUpdateRate(student_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_4, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_4, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_4, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_4, special_effect=14393)
    AddSpecialEffect(student_4, Effects.SpecialStudent)
    ReplanAI(student_4)
    SetNetworkUpdateRate(student_4, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_5, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_5, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_5, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_5, special_effect=14393)
    AddSpecialEffect(student_5, Effects.SpecialStudent)
    ReplanAI(student_5)
    SetNetworkUpdateRate(student_5, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_6, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_6, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_6, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_6, special_effect=14393)
    AddSpecialEffect(student_6, Effects.SpecialStudent)
    ReplanAI(student_6)
    SetNetworkUpdateRate(student_6, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_7, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_7, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_7, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_7, special_effect=14393)
    AddSpecialEffect(student_7, Effects.SpecialStudent)
    ReplanAI(student_7)
    SetNetworkUpdateRate(student_7, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_8, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_8, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_8, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_8, special_effect=14393)
    AddSpecialEffect(student_8, Effects.SpecialStudent)
    ReplanAI(student_8)
    SetNetworkUpdateRate(student_8, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_9, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_9, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_9, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_9, special_effect=14393)
    AddSpecialEffect(student_9, Effects.SpecialStudent)
    ReplanAI(student_9)
    SetNetworkUpdateRate(student_9, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_10, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_10, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_10, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_10, special_effect=14393)
    AddSpecialEffect(student_10, Effects.SpecialStudent)
    ReplanAI(student_10)
    SetNetworkUpdateRate(student_10, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_11, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_11, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_11, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_11, special_effect=14393)
    AddSpecialEffect(student_11, Effects.SpecialStudent)
    ReplanAI(student_11)
    SetNetworkUpdateRate(student_11, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_12, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_12, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_12, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_12, special_effect=14393)
    AddSpecialEffect(student_12, Effects.SpecialStudent)
    ReplanAI(student_12)
    SetNetworkUpdateRate(student_12, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_13, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_13, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_13, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_13, special_effect=14393)
    AddSpecialEffect(student_13, Effects.SpecialStudent)
    ReplanAI(student_13)
    SetNetworkUpdateRate(student_13, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_14, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_14, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_14, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_14, special_effect=14393)
    AddSpecialEffect(student_14, Effects.SpecialStudent)
    ReplanAI(student_14)
    SetNetworkUpdateRate(student_14, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_15, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_15, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_15, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_15, special_effect=14393)
    AddSpecialEffect(student_15, Effects.SpecialStudent)
    ReplanAI(student_15)
    SetNetworkUpdateRate(student_15, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_16, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_16, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_16, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_16, special_effect=14393)
    AddSpecialEffect(student_16, Effects.SpecialStudent)
    ReplanAI(student_16)
    SetNetworkUpdateRate(student_16, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_17, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_17, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_17, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_17, special_effect=14393)
    AddSpecialEffect(student_17, Effects.SpecialStudent)
    ReplanAI(student_17)
    SetNetworkUpdateRate(student_17, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_18, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_18, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_18, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_18, special_effect=14393)
    AddSpecialEffect(student_18, Effects.SpecialStudent)
    ReplanAI(student_18)
    SetNetworkUpdateRate(student_18, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    Goto(Label.L10)  # TODO: Implies these four students between here and Label 10 CANNOT be chosen?
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_19, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_19, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_19, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_19, special_effect=14393)
    AddSpecialEffect(student_19, Effects.SpecialStudent)
    ReplanAI(student_19)
    SetNetworkUpdateRate(student_19, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_20, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_20, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_20, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_20, special_effect=14393)
    AddSpecialEffect(student_20, Effects.SpecialStudent)
    ReplanAI(student_20)
    SetNetworkUpdateRate(student_20, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_21, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_21, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_21, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_21, special_effect=14393)
    AddSpecialEffect(student_21, Effects.SpecialStudent)
    ReplanAI(student_21)
    SetNetworkUpdateRate(student_21, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_22, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_22, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_22, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_22, special_effect=14393)
    AddSpecialEffect(student_22, Effects.SpecialStudent)
    ReplanAI(student_22)
    SetNetworkUpdateRate(student_22, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_23, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_23, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_23, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_23, special_effect=14393)
    AddSpecialEffect(student_23, Effects.SpecialStudent)
    ReplanAI(student_23)
    SetNetworkUpdateRate(student_23, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=6, character=student_24, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_24, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_24, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_24, special_effect=14393)
    AddSpecialEffect(student_24, Effects.SpecialStudent)
    ReplanAI(student_24)
    SetNetworkUpdateRate(student_24, is_fixed=True, update_rate=CharacterUpdateRate.Always)

    Restart()


@RestartOnRest(Flags.EVENT_SyncRennalaSoundDummyPosition)
def SyncRennalaSoundDummyPosition(_, rennala: uint, rennala_sound_dummy: uint):
    """Event 14003814"""
    if ThisEventSlotFlagDisabled():
        DisableGravity(rennala_sound_dummy)
    Move(
        rennala_sound_dummy,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=20,
        short_move=True,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(Flags.EVENT_RennalaSoundDummyLoop)
def RennalaSoundDummyLoop(_, rennala: uint, rennala_sound_dummy: uint):
    """Event 14003815"""
    MAIN.Await(HasAIStatus(rennala, ai_status=AIStatusType.Battle))
    
    TriggerAISound(ai_sound_param_id=203000, anchor_entity=rennala_sound_dummy, unk_8_12=2)
    Wait(5.0)
    Restart()


@RestartOnRest(Flags.EVENT_RennalaStudentsUnknownEffect)
def RennalaStudentsUnknownEffect(_, student_group: uint):
    """Event 14003817"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(Flags.RennalaBarrierReset))
    AND_1.Add(CharacterProportionHasSpecialEffect(
        character_group=student_group,
        special_effect=14385,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_proportion=1.0,
    ))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(student_group, 14384)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(14003820)
def Event_14003820(_, asset: uint):
    """Event 14003820"""
    if ThisEventSlotFlagDisabled():
        SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
        Restart()
    
    MAIN.Await(ThisEventSlotFlagDisabled())
    
    Wait(20.0)
    EnableAsset(asset)
    if AssetDestroyed(asset):
        RestoreAsset(asset)
    ForceAnimation(asset, 1, wait_for_completion=True)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Restart()


@RestartOnRest(Flags.EVENT_StudentChosenAtBattleStart)
def StudentChosenAtBattleStart(_, flag: uint, rennala: uint, student_group: uint):
    """One of three students (0, 8, 16) is randomly chosen to protect Rennala's barrier first."""
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(CharacterBackreadEnabled(rennala))
    AND_10.Add(CharacterBackreadEnabled(Characters.RennalaStudent0))
    AND_10.Add(CharacterBackreadEnabled(Characters.RennalaStudent8))
    AND_10.Add(CharacterBackreadEnabled(Characters.RennalaStudent16))
    AND_10.Add(FlagEnabled(Flags.RennalaBattleStarted))

    AwaitConditionTrue(AND_10)

    # Add "Chosen" effect marker to a random student from three.
    DisableFlag(Flags.RennalaRandomFlag1)
    DisableFlag(Flags.RennalaRandomFlag2)
    DisableFlag(Flags.RennalaRandomFlag3)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(Flags.RennalaRandomFlag1, Flags.RennalaRandomFlag3))
    if FlagEnabled(Flags.RennalaRandomFlag1):
        AddSpecialEffect(Characters.RennalaStudent0, Effects.StudentGlowing)
    if FlagEnabled(Flags.RennalaRandomFlag2):
        AddSpecialEffect(Characters.RennalaStudent8, Effects.StudentGlowing)
    if FlagEnabled(Flags.RennalaRandomFlag3):
        AddSpecialEffect(Characters.RennalaStudent16, Effects.StudentGlowing)

    AddSpecialEffect(rennala, Effects.FirstGlowingStudentChosen)
    WaitFrames(frames=1)

    EnableFlag(flag)
    DisableThisSlotFlag()
    OR_1.Add(CharacterHasSpecialEffect(student_group, Effects.GlowingStudentHit, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AwaitConditionTrue(OR_1)
    EnableFlag(Flags.FirstGlowingStudentHit)
    End()


@RestartOnRest(14003950)
def Event_14003950(_, flag: uint, asset: uint):
    """Event 14003950"""
    AND_1.Add(AssetDestroyed(asset))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    DisableNetworkFlag(flag)
    Restart()


@RestartOnRest(14003834)
def Event_14003834(_, asset: uint):
    """Event 14003834"""
    if ThisEventSlotFlagDisabled():
        SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
        Restart()
    
    MAIN.Await(ThisEventSlotFlagDisabled())
    
    Wait(20.0)
    EnableAsset(asset)
    ForceAnimation(asset, 2, wait_for_completion=True)
    Wait(3.0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Restart()


@RestartOnRest(14003840)
def Event_14003840(_, character: uint, left: uint, left_1: uint, left_2: uint, flag: uint, flag_1: uint, flag_2: uint):
    """Event 14003840"""
    WaitFrames(frames=1)
    SkipLinesIfUnsignedEqual(2, left=left_2, right=0)
    SkipLinesIfFlagDisabled(1, flag_2)
    OR_1.Add(EntityWithinDistance(entity=20000, other_entity=left_2, radius=10.0))
    SkipLinesIfUnsignedEqual(2, left=left_1, right=0)
    SkipLinesIfFlagDisabled(1, flag_1)
    OR_1.Add(EntityWithinDistance(entity=20000, other_entity=left_1, radius=10.0))
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    SkipLinesIfFlagDisabled(1, flag)
    OR_1.Add(EntityWithinDistance(entity=20000, other_entity=left, radius=10.0))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 14367))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 14367)
    ReplanAI(character)
    Wait(8.0)
    Restart()


@RestartOnRest(14003845)
def Event_14003845(
    _,
    character: uint,
    asset: uint,
    asset_1: uint,
    asset_2: uint,
    asset_3: uint,
    asset_4: uint,
    asset_5: uint,
):
    """Event 14003845"""
    MAIN.Await(CharacterHasSpecialEffect(character, 14362))
    
    if FlagEnabled(asset_5):
        CreateAssetVFX(asset_2, vfx_id=200, model_point=814625)
    if FlagEnabled(asset_4):
        CreateAssetVFX(asset_1, vfx_id=200, model_point=814625)
    if FlagEnabled(asset_3):
        CreateAssetVFX(asset, vfx_id=200, model_point=814625)
    Wait(1.5)
    if FlagEnabled(asset_5):
        OR_1.Add(EntityWithinDistance(entity=20000, other_entity=asset_2, radius=4.5))
    if FlagEnabled(asset_4):
        OR_1.Add(EntityWithinDistance(entity=20000, other_entity=asset_1, radius=4.5))
    if FlagEnabled(asset_3):
        OR_1.Add(EntityWithinDistance(entity=20000, other_entity=asset, radius=4.5))
    OR_1.Add(TimeElapsed(seconds=5.0))
    AwaitConditionTrue(OR_1)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L10, character=character, special_effect=14363)
    ReplanAI(character)
    ForceAnimation(character, 3014)
    Wait(0.699999988079071)
    AND_1.Add(EntityWithinDistance(entity=20000, other_entity=asset_2, radius=4.5))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    GotoIfFlagDisabled(Label.L0, flag=asset_5)
    GotoIfAssetDestroyed(Label.L0, asset=asset_5)
    DisableNetworkFlag(asset_5)
    ShootProjectile(
        owner_entity=character,
        source_entity=asset_2,
        model_point=200,
        behavior_id=220400140,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableAsset(asset_2)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(EntityWithinDistance(entity=20000, other_entity=asset_1, radius=4.5))
    GotoIfConditionFalse(Label.L1, input_condition=AND_2)
    GotoIfFlagDisabled(Label.L1, flag=asset_4)
    GotoIfAssetDestroyed(Label.L1, asset=asset_4)
    DisableNetworkFlag(asset_4)
    ShootProjectile(
        owner_entity=character,
        source_entity=asset_1,
        model_point=200,
        behavior_id=220400140,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableAsset(asset_1)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(EntityWithinDistance(entity=20000, other_entity=asset, radius=4.5))
    GotoIfConditionFalse(Label.L2, input_condition=AND_3)
    GotoIfFlagDisabled(Label.L2, flag=asset_3)
    GotoIfAssetDestroyed(Label.L2, asset=asset_3)
    DisableNetworkFlag(asset_3)
    ShootProjectile(
        owner_entity=character,
        source_entity=asset,
        model_point=200,
        behavior_id=220400140,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableAsset(asset)

    # --- Label 2 --- #
    DefineLabel(2)

    # --- Label 10 --- #
    DefineLabel(10)
    DeleteAssetVFX(asset_2)
    DeleteAssetVFX(asset_1)
    DeleteAssetVFX(asset)
    Restart()


@RestartOnRest(14003850)
def Event_14003850(
    _,
    character: uint,
    asset: uint,
    asset_1: uint,
    asset_2: uint,
    asset_3: uint,
    asset_4: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
    flag_4: uint,
    asset__asset_flag: uint,
    asset__asset_flag_1: uint,
    asset__asset_flag_2: uint,
    asset__asset_flag_3: uint,
    asset__asset_flag_4: uint,
    region: uint,
    region_1: uint,
    region_2: uint,
    region_3: uint,
    region_4: uint,
):
    """Event 14003850"""
    MAIN.Await(CharacterHasSpecialEffect(character, 14363))
    
    SkipLinesIfCharacterOutsideRegion(line_count=24, character=20000, region=region)
    if FlagEnabled(flag):
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        DisableNetworkFlag(flag)
        ForceAnimation(asset, 1)
        AddSpecialEffect(character, 5032)
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(1.0)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        CreateHazard(
            asset_flag=asset__asset_flag,
            asset=asset__asset_flag,
            model_point=210,
            behavior_param_id=220400150,
            target_type=DamageTargetType.Character,
            radius=3.5,
            life=12.0,
            repetition_time=0.0,
        )
        Wait(7.5)
        DisableAsset(asset)
        Goto(Label.L10)
    SkipLinesIfCharacterOutsideRegion(line_count=24, character=20000, region=region_1)
    if FlagEnabled(flag_1):
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        DisableNetworkFlag(flag_1)
        ForceAnimation(asset_1, 1)
        AddSpecialEffect(character, 5032)
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(1.0)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_1,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        CreateHazard(
            asset_flag=asset__asset_flag_1,
            asset=asset__asset_flag_1,
            model_point=210,
            behavior_param_id=220400150,
            target_type=DamageTargetType.Character,
            radius=3.5,
            life=12.0,
            repetition_time=0.0,
        )
        Wait(7.5)
        DisableAsset(asset_1)
        Goto(Label.L10)
    SkipLinesIfCharacterOutsideRegion(line_count=24, character=20000, region=region_2)
    if FlagEnabled(flag_2):
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        DisableNetworkFlag(flag_2)
        ForceAnimation(asset_2, 1)
        AddSpecialEffect(character, 5032)
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(1.0)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_2,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        CreateHazard(
            asset_flag=asset__asset_flag_2,
            asset=asset__asset_flag_2,
            model_point=210,
            behavior_param_id=220400150,
            target_type=DamageTargetType.Character,
            radius=3.5,
            life=12.0,
            repetition_time=0.0,
        )
        Wait(7.5)
        DisableAsset(asset_2)
        Goto(Label.L10)
    SkipLinesIfCharacterOutsideRegion(line_count=24, character=20000, region=region_3)
    if FlagEnabled(flag_3):
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        DisableNetworkFlag(flag_3)
        ForceAnimation(asset_3, 1)
        AddSpecialEffect(character, 5032)
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(1.0)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_3,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        CreateHazard(
            asset_flag=asset__asset_flag_3,
            asset=asset__asset_flag_3,
            model_point=210,
            behavior_param_id=220400150,
            target_type=DamageTargetType.Character,
            radius=3.5,
            life=12.0,
            repetition_time=0.0,
        )
        Wait(7.5)
        DisableAsset(asset_3)
        Goto(Label.L10)
    SkipLinesIfCharacterOutsideRegion(line_count=24, character=20000, region=region_4)
    if FlagEnabled(flag_4):
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        DisableNetworkFlag(flag_4)
        ForceAnimation(asset_4, 1)
        AddSpecialEffect(character, 5032)
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=220,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(1.0)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=223,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=225,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=221,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Wait(0.5)
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=222,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=character,
            source_entity=asset__asset_flag_4,
            model_point=224,
            behavior_id=220400155,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        CreateHazard(
            asset_flag=asset__asset_flag_4,
            asset=asset__asset_flag_4,
            model_point=210,
            behavior_param_id=220400150,
            target_type=DamageTargetType.Character,
            radius=3.5,
            life=12.0,
            repetition_time=0.0,
        )
        Wait(7.5)
        DisableAsset(asset_4)
        Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    Restart()


@ContinueOnRest(14003880)
def Event_14003880(
    _,
    character: uint,
    destination: uint,
    destination_1: uint,
    destination_2: uint,
    destination_3: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
):
    """Event 14003880"""
    DisableNetworkSync()
    if FlagEnabled(14000899):
        return
    GotoIfThisEventSlotFlagDisabled(Label.L10)
    OR_14.Add(CharacterType(20000, character_type=CharacterType.WhitePhantom))
    if not OR_14:
        return
    if FlagDisabled(flag):
        EnableFlag(flag)
        Move(20000, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=0)
        End()
    if FlagDisabled(flag_1):
        EnableFlag(flag_1)
        Move(20000, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=0)
        End()
    if FlagDisabled(flag_2):
        EnableFlag(flag_2)
        Move(20000, destination=destination_3, destination_type=CoordEntityType.Region, copy_draw_parent=0)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    OR_15.Add(CharacterType(20000, character_type=CharacterType.WhitePhantom))
    OR_15.Add(CharacterType(20000, character_type=CharacterType.BlackPhantom))
    SkipLinesIfConditionFalse(1, OR_15)
    End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    WaitFrames(frames=1)
    DisableAI(Characters.RennalaPhaseTwo)
    SetNetworkUpdateRate(CharacterGroups.Students, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    Wait(4.0)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=0)
    DisableBossHealthBar(character)
    Wait(3.0)
    AND_10.Add(CharacterType(ProtectedEntities.ClientPlayer1, character_type=CharacterType.WhitePhantom))
    GotoIfConditionFalse(Label.L0, input_condition=AND_10)
    if FlagDisabled(flag):
        EnableFlag(flag)
        Move(
            ProtectedEntities.ClientPlayer1,
            destination=destination_1,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_1):
        EnableFlag(flag_1)
        Move(
            ProtectedEntities.ClientPlayer1,
            destination=destination_2,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_2):
        EnableFlag(flag_2)
        Move(
            ProtectedEntities.ClientPlayer1,
            destination=destination_3,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )

    # --- Label 0 --- #
    DefineLabel(0)
    AND_11.Add(CharacterType(ProtectedEntities.ClientPlayer2, character_type=CharacterType.WhitePhantom))
    GotoIfConditionFalse(Label.L1, input_condition=AND_11)
    if FlagDisabled(flag):
        EnableFlag(flag)
        Move(
            ProtectedEntities.ClientPlayer2,
            destination=destination_1,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_1):
        EnableFlag(flag_1)
        Move(
            ProtectedEntities.ClientPlayer2,
            destination=destination_2,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_2):
        EnableFlag(flag_2)
        Move(
            ProtectedEntities.ClientPlayer2,
            destination=destination_3,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    AND_12.Add(CharacterType(ProtectedEntities.ClientPlayer3, character_type=CharacterType.WhitePhantom))
    GotoIfConditionFalse(Label.L2, input_condition=AND_12)
    if FlagDisabled(flag):
        EnableFlag(flag)
        Move(
            ProtectedEntities.ClientPlayer3,
            destination=destination_1,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_1):
        EnableFlag(flag_1)
        Move(
            ProtectedEntities.ClientPlayer3,
            destination=destination_2,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_2):
        EnableFlag(flag_2)
        Move(
            ProtectedEntities.ClientPlayer3,
            destination=destination_3,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagEnabled(flag_2):
        return
    AND_13.Add(CharacterType(ProtectedEntities.ClientPlayer4, character_type=CharacterType.WhitePhantom))
    GotoIfConditionFalse(Label.L3, input_condition=AND_13)
    if FlagDisabled(flag):
        EnableFlag(flag)
        Move(
            ProtectedEntities.ClientPlayer4,
            destination=destination_1,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_1):
        EnableFlag(flag_1)
        Move(
            ProtectedEntities.ClientPlayer4,
            destination=destination_2,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_2):
        EnableFlag(flag_2)
        Move(
            ProtectedEntities.ClientPlayer4,
            destination=destination_3,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )

    # --- Label 3 --- #
    DefineLabel(3)
    if FlagEnabled(flag_2):
        return
    AND_14.Add(CharacterType(ProtectedEntities.ClientPlayer5, character_type=CharacterType.WhitePhantom))
    GotoIfConditionFalse(Label.L4, input_condition=AND_14)
    if FlagDisabled(flag):
        EnableFlag(flag)
        Move(
            ProtectedEntities.ClientPlayer5,
            destination=destination_1,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_1):
        EnableFlag(flag_1)
        Move(
            ProtectedEntities.ClientPlayer5,
            destination=destination_2,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )
    if FlagDisabled(flag_2):
        EnableFlag(flag_2)
        Move(
            ProtectedEntities.ClientPlayer5,
            destination=destination_3,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)


@RestartOnRest(14003885)
def Event_14003885(
    _,
    character: uint,
    destination: uint,
    destination_1: uint,
    destination_2: uint,
    destination_3: uint,
    special_effect: int,
    special_effect_1: int,
    special_effect_2: int,
    special_effect_3: int,
):
    """Event 14003885"""
    MAIN.Await(CharacterHasSpecialEffect(character, 14372))
    
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=special_effect)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=special_effect_1)
    Move(character, destination=destination_3, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=special_effect_2)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=special_effect_3)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)
    Wait(1.0)
    Restart()


@RestartOnRest(14003886)
def Event_14003886(_, character: uint, region: uint, special_effect__special_effect_id: int):
    """Event 14003886"""
    AND_1.Add(CharacterInsideRegion(character=character, region=region))
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect__special_effect_id, target_count=0.0))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, special_effect__special_effect_id)
    Restart()


@RestartOnRest(Flags.EVENT_RennalaForceStudentUpdate)
def RennalaForceStudentUpdate(_, rennala: uint, student_group: uint):
    """Event 14003892"""
    MAIN.Await(CharacterHasSpecialEffect(rennala, 14378))
    
    SetNetworkUpdateRate(student_group, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Wait(1.0)
    Restart()


@RestartOnRest(Flags.EVENT_RennalaStudentsEffect14353)
def RennalaStudentsEffect14353(_, rennala: uint, student_group: uint):
    """Event 14003893"""
    MAIN.Await(CharacterHasSpecialEffect(rennala, 5028))
    
    AddSpecialEffect(student_group, 14353)
    Wait(1.0)
    Restart()


@RestartOnRest(Flags.EVENT_RennalaStudentsEffect14355)
def RennalaStudentsEffect14355(_, rennala: uint, student_group: uint):
    """Event 14003894"""
    MAIN.Await(CharacterHasSpecialEffect(rennala, 5029))
    
    AddSpecialEffect(student_group, 14355)
    Wait(1.0)
    Restart()


@RestartOnRest(14003898)
def Event_14003898(
    _,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
    character_5: uint,
    character_6: uint,
    character_7: uint,
    character_8: uint,
):
    """Event 14003898"""
    if ThisEventSlotFlagDisabled():
        MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Normal, target_comparison_type=ComparisonType.NotEqual))
    Wait(40.0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_1, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_1, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_1, special_effect=14393)
    AddSpecialEffect(character_1, 14367)
    ReplanAI(character_1)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_2, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_2, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_2, special_effect=14393)
    AddSpecialEffect(character_2, 14367)
    ReplanAI(character_2)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_3, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_3, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_3, special_effect=14393)
    AddSpecialEffect(character_3, 14367)
    ReplanAI(character_3)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_4, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_4, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_4, special_effect=14393)
    AddSpecialEffect(character_4, 14367)
    ReplanAI(character_4)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_5, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_5, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_5, special_effect=14393)
    AddSpecialEffect(character_5, 14367)
    ReplanAI(character_5)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_6, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_6, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_6, special_effect=14393)
    AddSpecialEffect(character_6, 14367)
    ReplanAI(character_6)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_7, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_7, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_7, special_effect=14393)
    AddSpecialEffect(character_7, 14367)
    ReplanAI(character_7)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=character_8, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=character_8, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_8, special_effect=14393)
    AddSpecialEffect(character_8, 14367)
    ReplanAI(character_8)
    DisableThisSlotFlag()
    Restart()


@RestartOnRest(14003900)
def Event_14003900(_, owner_entity: uint, source_entity: uint):
    """Event 14003900"""
    WaitRandomSeconds(min_seconds=3.0, max_seconds=10.0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=220400180,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Restart()


@RestartOnRest(Flags.EVENT_KillStudentsWhenRennalaDies)
def KillStudentsWhenRennalaDies():
    """Event 14003915"""
    MAIN.Await(FlagEnabled(Flags.RennalaDefeated))
    
    Kill(CharacterGroups.Students)
    End()


@RestartOnRest(Flags.EVENT_RennalaSummonsBloodhoundKnight)
def RennalaSummonsBloodhoundKnight(_, active_flag: uint, rennala: uint, bloodhound: uint):
    """Event 14003922"""
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBloodhoundRequest))
    AND_1.Add(FlagDisabled(active_flag))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(bloodhound)
    Move(
        bloodhound,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=230,
        copy_draw_parent=rennala,
    )
    SetNetworkUpdateRate(bloodhound, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RemoveSpecialEffect(bloodhound, Effects.RennalaSummonInactive)
    EnableFlag(active_flag)
    ReplanAI(bloodhound)
    WaitFrames(frames=1)
    ForceAnimation(bloodhound, 20010)
    Wait(0.800000011920929)
    EnableAnimations(bloodhound)
    Restart()


@RestartOnRest(Flags.EVENT_RennalaResumesFightingAfterBloodhound)
def RennalaResumesFightingAfterBloodhound(_, active_flag: uint, cleanup_flag: uint, bloodhound: uint, rennala: uint):
    """Event 14003923"""
    AND_1.Add(FlagDisabled(cleanup_flag))
    AND_1.Add(FlagEnabled(active_flag))
    OR_1.Add(CharacterHasSpecialEffect(bloodhound, Effects.RennalaSummonDisableOnRennalaDeath))
    OR_1.Add(CharacterHasSpecialEffect(bloodhound, Effects.RequestSummonDisable))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(cleanup_flag)
    RemoveSpecialEffect(rennala, Effects.RennalaLetsSummonFight)
    ReplanAI(rennala)
    Wait(3.0)
    Restart()


@RestartOnRest(Flags.EVENT_BloodhoundCleanup)
def BloodhoundCleanup(_, active_flag: uint, cleanup_flag: uint, bloodhound: uint):
    """Event 14003924"""
    AND_1.Add(FlagEnabled(active_flag))
    AND_1.Add(FlagEnabled(cleanup_flag))
    AND_1.Add(CharacterHasSpecialEffect(bloodhound, Effects.RequestSummonDisable))
    
    MAIN.Await(AND_1)
    
    DisableFlag(active_flag)
    DisableFlag(cleanup_flag)
    RemoveSpecialEffect(bloodhound, Effects.RequestSummonDisable)
    Restart()


@RestartOnRest(Flags.EVENT_BloodhoundSummonDefeated)
def BloodhoundSummonDefeated(_, active_flag: uint, bloodhound: uint):
    """Event 14003925"""
    AND_1.Add(HealthValue(bloodhound) <= 1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(bloodhound, Effects.RequestSummonDisable))
    AND_1.Add(FlagEnabled(active_flag))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(bloodhound, 20011)
    Wait(5.0)
    Restart()


@RestartOnRest(Flags.EVENT_DisableBloodhoundSummon)
def DisableBloodhoundSummon(_, bloodhound: uint):
    """Event 14003926"""
    if ThisEventSlotFlagDisabled():
        DisableCharacter(bloodhound)
        DisableAnimations(bloodhound)
    AND_1.Add(CharacterHasSpecialEffect(bloodhound, Effects.RequestSummonDisable))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(bloodhound, Effects.RennalaSummonInactive))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(bloodhound, Effects.RennalaSummonHeal)
    AddSpecialEffect(bloodhound, Effects.RennalaSummonInactive)
    RemoveSpecialEffect(bloodhound, Effects.RennalaSummonDisableOnRennalaDeath)
    RemoveSpecialEffect(bloodhound, Effects.RequestSummonDisable)
    RemoveSpecialEffect(bloodhound, 14576)
    DisableCharacter(bloodhound)
    DisableAnimations(bloodhound)
    Restart()


@RestartOnRest(Flags.EVENT_RennalaSummonsWolves)
def RennalaSummonsWolves(
    _,
    active_flag: uint,
    rennala: uint,
    wolf_0: uint,
    wolf_1: uint,
    wolf_2: uint,
    wolf_3: uint,
):
    """Event 14003937"""
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaWolvesRequest))
    AND_1.Add(FlagDisabled(active_flag))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(wolf_0)
    EnableAnimations(wolf_0)
    Move(
        wolf_0,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=71,
        copy_draw_parent=rennala,
    )
    ReplanAI(wolf_1)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(wolf_0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(wolf_0, 20015)
    RemoveSpecialEffect(wolf_0, Effects.RennalaSummonInactive)
    EnableFlag(active_flag)
    Wait(0.10000000149011612)
    EnableCharacter(wolf_1)
    EnableAnimations(wolf_1)
    Move(
        wolf_1,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=72,
        copy_draw_parent=rennala,
    )
    ReplanAI(wolf_1)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(wolf_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(wolf_1, 20015)
    RemoveSpecialEffect(wolf_1, Effects.RennalaSummonInactive)
    Wait(0.20000000298023224)
    EnableCharacter(wolf_2)
    EnableAnimations(wolf_2)
    Move(
        wolf_2,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=73,
        copy_draw_parent=rennala,
    )
    ReplanAI(wolf_2)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(wolf_2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(wolf_2, 20015)
    RemoveSpecialEffect(wolf_2, Effects.RennalaSummonInactive)
    Wait(0.10000000149011612)
    EnableCharacter(wolf_3)
    EnableAnimations(wolf_3)
    Move(
        wolf_3,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=70,
        copy_draw_parent=rennala,
    )
    ReplanAI(wolf_3)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(wolf_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(wolf_3, 20015)
    RemoveSpecialEffect(wolf_3, Effects.RennalaSummonInactive)
    Restart()


@RestartOnRest(Flags.EVENT_RennalaResumesFightingAfterWolves)
def RennalaResumesFightingAfterWolves(
    _,
    active_flag: uint,
    cleanup_flag: uint,
    wolf_0: uint,
    wolf_1: uint,
    wolf_2: uint,
    wolf_3: uint,
    rennala: uint,
):
    """Event 14003938"""
    AND_1.Add(FlagDisabled(cleanup_flag))
    AND_1.Add(FlagEnabled(active_flag))
    OR_1.Add(CharacterHasSpecialEffect(wolf_0, Effects.RennalaSummonDisableOnRennalaDeath))
    OR_1.Add(CharacterHasSpecialEffect(wolf_0, Effects.RequestSummonDisable))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterHasSpecialEffect(wolf_1, Effects.RennalaSummonDisableOnRennalaDeath))
    OR_2.Add(CharacterHasSpecialEffect(wolf_1, Effects.RequestSummonDisable))
    AND_1.Add(OR_2)
    OR_3.Add(CharacterHasSpecialEffect(wolf_2, Effects.RennalaSummonDisableOnRennalaDeath))
    OR_3.Add(CharacterHasSpecialEffect(wolf_2, Effects.RequestSummonDisable))
    AND_1.Add(OR_3)
    OR_4.Add(CharacterHasSpecialEffect(wolf_3, Effects.RennalaSummonDisableOnRennalaDeath))
    OR_4.Add(CharacterHasSpecialEffect(wolf_3, Effects.RequestSummonDisable))
    AND_1.Add(OR_4)
    
    MAIN.Await(AND_1)
    
    EnableFlag(cleanup_flag)
    RemoveSpecialEffect(rennala, Effects.RennalaLetsSummonFight)
    ReplanAI(rennala)
    Restart()


@RestartOnRest(Flags.EVENT_WolvesCleanup)
def WolvesCleanup(
    _,
    active_flag: uint,
    flag_1: uint,
    wolf_0: uint,
    wolf_1: uint,
    wolf_2: uint,
    wolf_3: uint,
):
    """Event 14003939"""
    AND_1.Add(FlagEnabled(active_flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterHasSpecialEffect(wolf_0, Effects.RequestSummonDisable))
    AND_1.Add(CharacterHasSpecialEffect(wolf_1, Effects.RequestSummonDisable))
    AND_1.Add(CharacterHasSpecialEffect(wolf_2, Effects.RequestSummonDisable))
    AND_1.Add(CharacterHasSpecialEffect(wolf_3, Effects.RequestSummonDisable))
    
    MAIN.Await(AND_1)
    
    DisableFlag(active_flag)
    DisableFlag(flag_1)
    RemoveSpecialEffect(wolf_0, Effects.RequestSummonDisable)
    RemoveSpecialEffect(wolf_1, Effects.RequestSummonDisable)
    RemoveSpecialEffect(wolf_2, Effects.RequestSummonDisable)
    RemoveSpecialEffect(wolf_3, Effects.RequestSummonDisable)
    Restart()


@RestartOnRest(Flags.EVENT_WolfSummonDefeated)
def WolfSummonDefeated(_, active_flag: uint, wolf: uint):
    """Event 14003940"""
    AND_1.Add(HealthValue(wolf) <= 1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(wolf, Effects.RequestSummonDisable))
    AND_1.Add(FlagEnabled(active_flag))
    
    MAIN.Await(AND_1)
    
    DisableAnimations(wolf)
    ForceAnimation(wolf, 3035)
    Wait(5.0)
    Restart()


@RestartOnRest(Flags.EVENT_DisableWolfSummon)
def DisableWolfSummon(_, wolf: uint):
    """Event 14003945"""
    if ThisEventSlotFlagDisabled():
        DisableCharacter(wolf)
        DisableAnimations(wolf)
    AND_1.Add(CharacterHasSpecialEffect(wolf, Effects.RequestSummonDisable))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(wolf, Effects.RennalaSummonInactive))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(wolf, Effects.RennalaSummonHeal)
    AddSpecialEffect(wolf, Effects.RennalaSummonInactive)
    RemoveSpecialEffect(wolf, Effects.RennalaSummonDisableOnRennalaDeath)
    RemoveSpecialEffect(wolf, 14576)
    DisableCharacter(wolf)
    DisableAnimations(wolf)
    Restart()


@RestartOnRest(Flags.EVENT_RennalaSummonsTroll)
def RennalaSummonsTroll(_, active_flag: uint, rennala: uint, troll: uint):
    """Event 14003962"""
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaTrollRequest))
    AND_1.Add(FlagDisabled(active_flag))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(troll)
    Move(
        troll,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=243,
        copy_draw_parent=rennala,
    )
    SetNetworkUpdateRate(troll, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RemoveSpecialEffect(troll, Effects.RennalaSummonInactive)
    EnableFlag(active_flag)
    ReplanAI(troll)
    WaitFrames(frames=1)
    ForceAnimation(troll, 20026)
    DisableAnimations(troll)
    Wait(4.0)
    EnableAnimations(troll)
    Restart()


@RestartOnRest(Flags.EVENT_RennalaResumesFightingAfterTroll)
def RennalaResumesFightingAfterTroll(_, active_flag: uint, cleanup_flag: uint, troll: uint, rennala: uint):
    """Event 14003963"""
    AND_1.Add(FlagDisabled(cleanup_flag))
    AND_1.Add(FlagEnabled(active_flag))
    OR_1.Add(CharacterHasSpecialEffect(troll, Effects.RennalaSummonDisableOnRennalaDeath))
    OR_1.Add(CharacterHasSpecialEffect(troll, Effects.RequestSummonDisable))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(cleanup_flag)
    RemoveSpecialEffect(rennala, Effects.RennalaLetsSummonFight)
    ReplanAI(rennala)
    Restart()


@RestartOnRest(Flags.EVENT_TrollCleanup)
def TrollCleanup(_, active_flag: uint, cleanup_flag: uint, troll: uint):
    """Event 14003964"""
    AND_1.Add(FlagEnabled(active_flag))
    AND_1.Add(FlagEnabled(cleanup_flag))
    AND_1.Add(CharacterHasSpecialEffect(troll, Effects.RequestSummonDisable))
    
    MAIN.Await(AND_1)
    
    DisableFlag(active_flag)
    DisableFlag(cleanup_flag)
    RemoveSpecialEffect(troll, Effects.RequestSummonDisable)
    Restart()


@RestartOnRest(Flags.EVENT_TrollSummonDefeated)
def TrollSummonDefeated(_, active_flag: uint, troll: uint):
    """Event 14003965"""
    AND_1.Add(HealthValue(troll) <= 1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(troll, Effects.RequestSummonDisable))
    AND_1.Add(FlagEnabled(active_flag))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(troll, 20025)
    Wait(5.0)
    Restart()


@RestartOnRest(Flags.EVENT_DisableTrollSummon)
def DisableTrollSummon(_, troll: uint):
    """Event 14003966"""
    if ThisEventSlotFlagDisabled():
        DisableCharacter(troll)
        DisableAnimations(troll)
    AND_1.Add(CharacterHasSpecialEffect(troll, Effects.RequestSummonDisable))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(troll, Effects.RennalaSummonInactive))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(troll, Effects.RennalaSummonHeal)
    AddSpecialEffect(troll, Effects.RennalaSummonInactive)
    RemoveSpecialEffect(troll, Effects.RennalaSummonDisableOnRennalaDeath)
    RemoveSpecialEffect(troll, Effects.RequestSummonDisable)
    RemoveSpecialEffect(troll, 14576)
    DisableCharacter(troll)
    DisableAnimations(troll)
    Restart()


@RestartOnRest(Flags.EVENT_RennalaSummonsDragon)
def RennalaSummonsDragon(_, active_flag: uint, rennala: uint, dragon: uint):
    """Event 14003972"""
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaDragonRequest))
    AND_1.Add(FlagDisabled(active_flag))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(dragon)
    Move(
        dragon,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=65,
        copy_draw_parent=rennala,
    )
    SetNetworkUpdateRate(dragon, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RemoveSpecialEffect(dragon, Effects.RennalaSummonInactive)
    EnableFlag(active_flag)
    ReplanAI(dragon)
    WaitFrames(frames=1)
    ForceAnimation(dragon, 20026)
    Wait(0.800000011920929)
    EnableAnimations(dragon)
    Restart()


@RestartOnRest(Flags.EVENT_RennalaResumesFightingAfterDragon)
def RennalaResumesFightingAfterDragon(_, active_flag: uint, cleanup_flag: uint, dragon: uint, rennala: uint):
    """Event 14003973"""
    AND_1.Add(FlagDisabled(cleanup_flag))
    AND_1.Add(FlagEnabled(active_flag))
    OR_1.Add(CharacterHasSpecialEffect(dragon, Effects.RennalaSummonDisableOnRennalaDeath))
    OR_1.Add(CharacterHasSpecialEffect(dragon, Effects.RequestSummonDisable))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(cleanup_flag)
    RemoveSpecialEffect(rennala, Effects.RennalaLetsSummonFight)
    ReplanAI(rennala)
    Restart()


@RestartOnRest(Flags.EVENT_DragonCleanup)
def DragonCleanup(_, active_flag: uint, cleanup_flag: uint, dragon: uint):
    """Event 14003974"""
    AND_1.Add(FlagEnabled(active_flag))
    AND_1.Add(FlagEnabled(cleanup_flag))
    AND_1.Add(CharacterHasSpecialEffect(dragon, Effects.RequestSummonDisable))
    
    MAIN.Await(AND_1)
    
    DisableFlag(active_flag)
    DisableFlag(cleanup_flag)
    RemoveSpecialEffect(dragon, Effects.RequestSummonDisable)
    Restart()


@RestartOnRest(Flags.EVENT_DragonSummonDefeated)
def DragonSummonDefeated(_, active_flag: uint, dragon: uint):
    """Event 14003975"""
    AND_1.Add(HealthValue(dragon) <= 1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(dragon, Effects.RequestSummonDisable))
    AND_1.Add(FlagEnabled(active_flag))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(dragon, 20027)
    Wait(5.0)
    Restart()


@RestartOnRest(Flags.EVENT_DisableDragonSummon)
def DisableDragonSummon(_, dragon: uint):
    """Event 14003976"""
    if ThisEventSlotFlagDisabled():
        DisableCharacter(dragon)
        DisableAnimations(dragon)
    AND_1.Add(CharacterHasSpecialEffect(dragon, Effects.RequestSummonDisable))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(dragon, Effects.RennalaSummonInactive))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(dragon, Effects.RennalaSummonHeal)
    AddSpecialEffect(dragon, Effects.RennalaSummonInactive)
    RemoveSpecialEffect(dragon, Effects.RennalaSummonDisableOnRennalaDeath)
    RemoveSpecialEffect(dragon, Effects.RequestSummonDisable)
    RemoveSpecialEffect(dragon, 14576)
    DisableCharacter(dragon)
    DisableAnimations(dragon)
    Restart()


@RestartOnRest(Flags.EVENT_DismissSummonsOnRennalaDeath)
def DismissSummonsOnRennalaDeath(_, rennala: uint, summon_group: uint):
    """Event 14003977"""
    MAIN.Await(HealthValue(rennala) == 0)
    
    AddSpecialEffect(summon_group, Effects.RennalaSummonDisableOnRennalaDeath)
    ReplanAI(summon_group)


@RestartOnRest(Flags.EVENT_DisableRennalaSpawners)
def DisableRennalaSpawners():
    """Event 14003978"""
    MAIN.Await(FlagEnabled(Flags.RennalaDefeated))
    
    DisableSpawner(entity=Spawners.RennalaStudents0)
    DisableSpawner(entity=Spawners.RennalaStudents1)
    DisableSpawner(entity=Spawners.RennalaStudents2)
    DisableSpawner(entity=Spawners.RennalaStudents3)
    DisableSpawner(entity=Spawners.RennalaStudents4)
    DisableSpawner(entity=Spawners.RennalaStudents5)
    DisableSpawner(entity=Spawners.RennalaStudents6)
    DisableSpawner(entity=Spawners.RennalaStudents7)
    DisableSpawner(entity=Spawners.RennalaStudents8)

    DisableSpawner(entity=Spawners.CLONE_RennalaStudents0)
    DisableSpawner(entity=Spawners.CLONE_RennalaStudents1)
    DisableSpawner(entity=Spawners.CLONE_RennalaStudents2)
    DisableSpawner(entity=Spawners.CLONE_RennalaStudents3)
    DisableSpawner(entity=Spawners.CLONE_RennalaStudents4)
    DisableSpawner(entity=Spawners.CLONE_RennalaStudents5)
    DisableSpawner(entity=Spawners.CLONE_RennalaStudents6)
    DisableSpawner(entity=Spawners.CLONE_RennalaStudents7)
    DisableSpawner(entity=Spawners.CLONE_RennalaStudents8)


@RestartOnRest(14000700)
def Event_14000700():
    """Event 14000700"""
    if FlagEnabled(14009205):
        return
    SetCharacterTalkRange(character=Characters.RennalaNPC1, distance=30.0)
    AND_1.Add(FlagEnabled(Flags.RennalaDefeated))
    AND_1.Add(FlagDisabled(3468))
    AND_1.Add(EntityWithinDistance(entity=Characters.RennalaNPC1, other_entity=PLAYER, radius=10.0))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(14002705)
    End()


@RestartOnRest(14000701)
def Event_14000701():
    """Event 14000701"""
    if FlagEnabled(14009210):
        return
    SetCharacterTalkRange(character=Characters.RennalaNPC1, distance=30.0)
    AND_1.Add(FlagEnabled(Flags.RennalaDefeated))
    AND_1.Add(FlagEnabled(3468))
    AND_1.Add(EntityWithinDistance(entity=Characters.RennalaNPC2, other_entity=PLAYER, radius=10.0))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(14002706)
    End()


@RestartOnRest(14000702)
def Event_14000702():
    """Event 14000702"""
    WaitFrames(frames=1)
    DisableCharacter(Characters.RennalaNPC1)
    DisableBackread(Characters.RennalaNPC1)
    DisableCharacter(Characters.RennalaNPC2)
    DisableBackread(Characters.RennalaNPC2)
    AwaitFlagEnabled(flag=9118)
    OR_1.Add(FlagEnabled(3468))
    GotoIfConditionTrue(Label.L1, input_condition=OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(Characters.RennalaNPC1)
    EnableBackread(Characters.RennalaNPC1)
    ForceAnimation(Characters.RennalaNPC1, 930010)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(Characters.RennalaNPC2)
    EnableBackread(Characters.RennalaNPC2)
    ForceAnimation(Characters.RennalaNPC2, 930010)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(14000703)
def Event_14000703():
    """Event 14000703"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9614))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9615))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 60540)
    Wait(0.20000000298023224)
    Restart()


@RestartOnRest(14000710)
def Event_14000710(_, asset__character: uint, asset__character_1: uint):
    """Event 14000710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3460))
    AND_1.Add(FlagEnabled(14009253))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(14009253)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(asset__character)
    DisableBackread(asset__character)
    DisableCharacter(asset__character_1)
    DisableBackread(asset__character_1)
    OR_1.Add(FlagEnabled(3468))
    OR_1.Add(FlagEnabled(3469))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    OR_2.Add(FlagEnabled(3468))
    OR_2.Add(FlagEnabled(3469))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3460)
    GotoIfFlagEnabled(Label.L2, flag=3461)
    GotoIfFlagEnabled(Label.L4, flag=3462)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(3468):
        EnableCharacter(asset__character)
        EnableBackread(asset__character)
        ForceAnimation(asset__character, 90100)
    if FlagEnabled(14002713):
        Move(asset__character, destination=14002701, destination_type=CoordEntityType.Region, short_move=True)
    if FlagEnabled(3469):
        EnableCharacter(asset__character_1)
        EnableBackread(asset__character_1)
        SetTeamType(asset__character_1, TeamType.FriendlyNPC)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagEnabled(3468):
        EnableCharacter(asset__character)
        EnableBackread(asset__character)
        SetTeamType(asset__character, TeamType.HostileNPC)
    if FlagEnabled(3469):
        EnableCharacter(asset__character_1)
        EnableBackread(asset__character_1)
        SetTeamType(asset__character_1, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    if FlagEnabled(3468):
        DropMandatoryTreasure(asset__character)
        DisableCharacter(asset__character)
        DisableBackread(asset__character)
        DisableAsset(asset__character)
    if FlagEnabled(3469):
        DropMandatoryTreasure(asset__character_1)
        DisableCharacter(asset__character_1)
        DisableBackread(asset__character_1)
        DisableAsset(asset__character_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(3468))
    OR_15.Add(FlagEnabled(3469))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(14000711)
def Event_14000711():
    """Event 14000711"""
    if FlagEnabled(3463):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(HealthValue(Characters.SorceressSellen0) == 0)
    
    MAIN.Await(AND_1)
    
    SetBackreadStateAlternate(Characters.SorceressSellen0, True)
    AND_2.Add(TimeElapsed(seconds=20.0))
    
    MAIN.Await(AND_2)
    
    SetBackreadStateAlternate(Characters.SorceressSellen0, False)
    End()


@RestartOnRest(14000712)
def Event_14000712():
    """Event 14000712"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400401):
        return
    AND_2.Add(TimeElapsed(seconds=2.0))
    AND_2.Add(FlagEnabled(7609))
    AwaitConditionTrue(AND_2)
    EnableFlag(14002713)
    AwardItemLot(104010, host_only=False)
    End()


@RestartOnRest(14000713)
def Event_14000713():
    """Event 14000713"""
    AwaitFlagEnabled(flag=7609)
    AwaitFlagEnabled(flag=14002713)
    Move(Characters.SorceressSellen0, destination=14002701, destination_type=CoordEntityType.Region, short_move=True)
    End()


@RestartOnRest(14000714)
def Event_14000714():
    """Event 14000714"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(3461, 3463)))
    AwaitConditionTrue(AND_1)
    DisableNetworkFlag(1034509259)
    End()


@RestartOnRest(14000720)
def Event_14000720():
    """Event 14000720"""
    if FlagEnabled(14009300):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=14002080))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 14307))
    
    MAIN.Await(AND_1)
    
    EnableFlag(14009300)
    End()


@RestartOnRest(14000730)
def Event_14000730(_, character: uint):
    """Event 14000730"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3360):
        DisableFlag(1041339253)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3371)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3371))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3360)
    GotoIfFlagEnabled(Label.L2, flag=3361)
    GotoIfFlagEnabled(Label.L4, flag=3363)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101)
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
    
    MAIN.Await(FlagDisabled(3371))
    
    Restart()


@RestartOnRest(14000731)
def Event_14000731():
    """Event 14000731"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400106):
        return
    AND_2.Add(TimeElapsed(seconds=2.0))
    AND_2.Add(FlagEnabled(7608))
    AwaitConditionTrue(AND_2)
    AwardItemLot(101060, host_only=False)
    End()


@RestartOnRest(14000740)
def Event_14000740(_, character: uint):
    """Event 14000740"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3948)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3948))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3940)
    GotoIfFlagEnabled(Label.L2, flag=3941)
    GotoIfFlagEnabled(Label.L4, flag=3943)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3948))
    
    Restart()


@RestartOnRest(14000741)
def Event_14000741(_, character: uint):
    """Event 14000741"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3949)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3949))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930025)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3949))
    
    Restart()


@RestartOnRest(14000742)
def Event_14000742():
    """Event 14000742"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3943):
        return
    AND_1.Add(FlagEnabled(3948))
    AND_1.Add(FlagDisabled(11109306))
    AND_1.Add(EntityWithinDistance(entity=Characters.BoctheSeamster, other_entity=20000, radius=4.0))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(11109306)
    End()


@RestartOnRest(14000750)
def Event_14000750(_, character: uint, asset: uint):
    """Event 14000750"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3806)
    DisableCharacter(character)
    DisableBackread(character)
    EnableAsset(asset)
    
    MAIN.Await(FlagEnabled(3806))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character)
    EnableBackread(character)
    DisableGravity(character)
    DisableAnimations(character)
    ResetCharacterPosition(character=character)
    EnableAsset(asset)
    EnableAssetInvulnerability(asset)
    ForceAnimation(character, 90103)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3806))
    
    Restart()


# region Cloned Rennala Summon Events

@RestartOnRest(Flags.CLONE_EVENT_RennalaSummonsBloodhoundKnight)
def CLONE_RennalaSummonsBloodhoundKnight(_, active_flag: uint, rennala: uint, bloodhound: uint):
    """CLONE Event 14003722"""
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBloodhoundRequest))
    AND_1.Add(FlagDisabled(active_flag))

    MAIN.Await(AND_1)

    EnableCharacter(bloodhound)
    Move(
        bloodhound,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=230,
        copy_draw_parent=rennala,
    )
    SetNetworkUpdateRate(bloodhound, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RemoveSpecialEffect(bloodhound, Effects.RennalaSummonInactive)
    EnableFlag(active_flag)
    ReplanAI(bloodhound)
    WaitFrames(frames=1)
    ForceAnimation(bloodhound, 20010)
    Wait(0.800000011920929)
    EnableAnimations(bloodhound)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaResumesFightingAfterBloodhound)
def CLONE_RennalaResumesFightingAfterBloodhound(
    _, active_flag: uint, cleanup_flag: uint, bloodhound: uint, rennala: uint
):
    """CLONE Event 14003723"""
    AND_1.Add(FlagDisabled(cleanup_flag))
    AND_1.Add(FlagEnabled(active_flag))
    OR_1.Add(CharacterHasSpecialEffect(bloodhound, Effects.RennalaSummonDisableOnRennalaDeath))
    OR_1.Add(CharacterHasSpecialEffect(bloodhound, Effects.RequestSummonDisable))
    AND_1.Add(OR_1)

    MAIN.Await(AND_1)

    EnableFlag(cleanup_flag)
    RemoveSpecialEffect(rennala, Effects.RennalaLetsSummonFight)
    ReplanAI(rennala)
    Wait(3.0)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_BloodhoundCleanup)
def CLONE_BloodhoundCleanup(_, active_flag: uint, cleanup_flag: uint, bloodhound: uint):
    """CLONE Event 14003724"""
    AND_1.Add(FlagEnabled(active_flag))
    AND_1.Add(FlagEnabled(cleanup_flag))
    AND_1.Add(CharacterHasSpecialEffect(bloodhound, Effects.RequestSummonDisable))

    MAIN.Await(AND_1)

    DisableFlag(active_flag)
    DisableFlag(cleanup_flag)
    RemoveSpecialEffect(bloodhound, Effects.RequestSummonDisable)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_BloodhoundSummonDefeated)
def CLONE_BloodhoundSummonDefeated(_, active_flag: uint, bloodhound: uint):
    """CLONE Event 14003725"""
    AND_1.Add(HealthValue(bloodhound) <= 1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(bloodhound, Effects.RequestSummonDisable))
    AND_1.Add(FlagEnabled(active_flag))

    MAIN.Await(AND_1)

    ForceAnimation(bloodhound, 20011)
    Wait(5.0)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_DisableBloodhoundSummon)
def CLONE_DisableBloodhoundSummon(_, bloodhound: uint):
    """CLONE Event 14003726"""
    if ThisEventSlotFlagDisabled():
        DisableCharacter(bloodhound)
        DisableAnimations(bloodhound)
    AND_1.Add(CharacterHasSpecialEffect(bloodhound, Effects.RequestSummonDisable))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(bloodhound, Effects.RennalaSummonInactive))

    MAIN.Await(AND_1)

    AddSpecialEffect(bloodhound, Effects.RennalaSummonHeal)
    AddSpecialEffect(bloodhound, Effects.RennalaSummonInactive)
    RemoveSpecialEffect(bloodhound, Effects.RennalaSummonDisableOnRennalaDeath)
    RemoveSpecialEffect(bloodhound, Effects.RequestSummonDisable)
    RemoveSpecialEffect(bloodhound, 14576)
    DisableCharacter(bloodhound)
    DisableAnimations(bloodhound)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaSummonsWolves)
def CLONE_RennalaSummonsWolves(
    _,
    active_flag: uint,
    rennala: uint,
    wolf_0: uint,
    wolf_1: uint,
    wolf_2: uint,
    wolf_3: uint,
):
    """CLONE Event 14003737"""
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaWolvesRequest))
    AND_1.Add(FlagDisabled(active_flag))

    MAIN.Await(AND_1)

    EnableCharacter(wolf_0)
    EnableAnimations(wolf_0)
    Move(
        wolf_0,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=71,
        copy_draw_parent=rennala,
    )
    ReplanAI(wolf_1)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(wolf_0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(wolf_0, 20015)
    RemoveSpecialEffect(wolf_0, Effects.RennalaSummonInactive)
    EnableFlag(active_flag)
    Wait(0.10000000149011612)
    EnableCharacter(wolf_1)
    EnableAnimations(wolf_1)
    Move(
        wolf_1,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=72,
        copy_draw_parent=rennala,
    )
    ReplanAI(wolf_1)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(wolf_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(wolf_1, 20015)
    RemoveSpecialEffect(wolf_1, Effects.RennalaSummonInactive)
    Wait(0.20000000298023224)
    EnableCharacter(wolf_2)
    EnableAnimations(wolf_2)
    Move(
        wolf_2,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=73,
        copy_draw_parent=rennala,
    )
    ReplanAI(wolf_2)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(wolf_2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(wolf_2, 20015)
    RemoveSpecialEffect(wolf_2, Effects.RennalaSummonInactive)
    Wait(0.10000000149011612)
    EnableCharacter(wolf_3)
    EnableAnimations(wolf_3)
    Move(
        wolf_3,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=70,
        copy_draw_parent=rennala,
    )
    ReplanAI(wolf_3)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(wolf_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(wolf_3, 20015)
    RemoveSpecialEffect(wolf_3, Effects.RennalaSummonInactive)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaResumesFightingAfterWolves)
def CLONE_RennalaResumesFightingAfterWolves(
    _,
    active_flag: uint,
    cleanup_flag: uint,
    wolf_0: uint,
    wolf_1: uint,
    wolf_2: uint,
    wolf_3: uint,
    rennala: uint,
):
    """CLONE Event 14003738"""
    AND_1.Add(FlagDisabled(cleanup_flag))
    AND_1.Add(FlagEnabled(active_flag))
    OR_1.Add(CharacterHasSpecialEffect(wolf_0, Effects.RennalaSummonDisableOnRennalaDeath))
    OR_1.Add(CharacterHasSpecialEffect(wolf_0, Effects.RequestSummonDisable))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterHasSpecialEffect(wolf_1, Effects.RennalaSummonDisableOnRennalaDeath))
    OR_2.Add(CharacterHasSpecialEffect(wolf_1, Effects.RequestSummonDisable))
    AND_1.Add(OR_2)
    OR_3.Add(CharacterHasSpecialEffect(wolf_2, Effects.RennalaSummonDisableOnRennalaDeath))
    OR_3.Add(CharacterHasSpecialEffect(wolf_2, Effects.RequestSummonDisable))
    AND_1.Add(OR_3)
    OR_4.Add(CharacterHasSpecialEffect(wolf_3, Effects.RennalaSummonDisableOnRennalaDeath))
    OR_4.Add(CharacterHasSpecialEffect(wolf_3, Effects.RequestSummonDisable))
    AND_1.Add(OR_4)

    MAIN.Await(AND_1)

    EnableFlag(cleanup_flag)
    RemoveSpecialEffect(rennala, Effects.RennalaLetsSummonFight)
    ReplanAI(rennala)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_WolvesCleanup)
def CLONE_WolvesCleanup(
    _,
    active_flag: uint,
    flag_1: uint,
    wolf_0: uint,
    wolf_1: uint,
    wolf_2: uint,
    wolf_3: uint,
):
    """CLONE Event 14003739"""
    AND_1.Add(FlagEnabled(active_flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterHasSpecialEffect(wolf_0, Effects.RequestSummonDisable))
    AND_1.Add(CharacterHasSpecialEffect(wolf_1, Effects.RequestSummonDisable))
    AND_1.Add(CharacterHasSpecialEffect(wolf_2, Effects.RequestSummonDisable))
    AND_1.Add(CharacterHasSpecialEffect(wolf_3, Effects.RequestSummonDisable))

    MAIN.Await(AND_1)

    DisableFlag(active_flag)
    DisableFlag(flag_1)
    RemoveSpecialEffect(wolf_0, Effects.RequestSummonDisable)
    RemoveSpecialEffect(wolf_1, Effects.RequestSummonDisable)
    RemoveSpecialEffect(wolf_2, Effects.RequestSummonDisable)
    RemoveSpecialEffect(wolf_3, Effects.RequestSummonDisable)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_WolfSummonDefeated)
def CLONE_WolfSummonDefeated(_, active_flag: uint, wolf: uint):
    """CLONE Event 14003740"""
    AND_1.Add(HealthValue(wolf) <= 1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(wolf, Effects.RequestSummonDisable))
    AND_1.Add(FlagEnabled(active_flag))

    MAIN.Await(AND_1)

    DisableAnimations(wolf)
    ForceAnimation(wolf, 3035)
    Wait(5.0)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_DisableWolfSummon)
def CLONE_DisableWolfSummon(_, wolf: uint):
    """CLONE Event 14003745"""
    if ThisEventSlotFlagDisabled():
        DisableCharacter(wolf)
        DisableAnimations(wolf)
    AND_1.Add(CharacterHasSpecialEffect(wolf, Effects.RequestSummonDisable))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(wolf, Effects.RennalaSummonInactive))

    MAIN.Await(AND_1)

    AddSpecialEffect(wolf, Effects.RennalaSummonHeal)
    AddSpecialEffect(wolf, Effects.RennalaSummonInactive)
    RemoveSpecialEffect(wolf, Effects.RennalaSummonDisableOnRennalaDeath)
    RemoveSpecialEffect(wolf, 14576)
    DisableCharacter(wolf)
    DisableAnimations(wolf)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaSummonsTroll)
def CLONE_RennalaSummonsTroll(_, active_flag: uint, rennala: uint, troll: uint):
    """CLONE Event 14003762"""
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaTrollRequest))
    AND_1.Add(FlagDisabled(active_flag))

    MAIN.Await(AND_1)

    EnableCharacter(troll)
    Move(
        troll,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=243,
        copy_draw_parent=rennala,
    )
    SetNetworkUpdateRate(troll, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RemoveSpecialEffect(troll, Effects.RennalaSummonInactive)
    EnableFlag(active_flag)
    ReplanAI(troll)
    WaitFrames(frames=1)
    ForceAnimation(troll, 20026)
    DisableAnimations(troll)
    Wait(4.0)
    EnableAnimations(troll)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaResumesFightingAfterTroll)
def CLONE_RennalaResumesFightingAfterTroll(_, active_flag: uint, cleanup_flag: uint, troll: uint, rennala: uint):
    """CLONE Event 14003763"""
    AND_1.Add(FlagDisabled(cleanup_flag))
    AND_1.Add(FlagEnabled(active_flag))
    OR_1.Add(CharacterHasSpecialEffect(troll, Effects.RennalaSummonDisableOnRennalaDeath))
    OR_1.Add(CharacterHasSpecialEffect(troll, Effects.RequestSummonDisable))
    AND_1.Add(OR_1)

    MAIN.Await(AND_1)

    EnableFlag(cleanup_flag)
    RemoveSpecialEffect(rennala, Effects.RennalaLetsSummonFight)
    ReplanAI(rennala)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_TrollCleanup)
def CLONE_TrollCleanup(_, active_flag: uint, cleanup_flag: uint, troll: uint):
    """CLONE Event 14003764"""
    AND_1.Add(FlagEnabled(active_flag))
    AND_1.Add(FlagEnabled(cleanup_flag))
    AND_1.Add(CharacterHasSpecialEffect(troll, Effects.RequestSummonDisable))

    MAIN.Await(AND_1)

    DisableFlag(active_flag)
    DisableFlag(cleanup_flag)
    RemoveSpecialEffect(troll, Effects.RequestSummonDisable)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_TrollSummonDefeated)
def CLONE_TrollSummonDefeated(_, active_flag: uint, troll: uint):
    """CLONE Event 14003765"""
    AND_1.Add(HealthValue(troll) <= 1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(troll, Effects.RequestSummonDisable))
    AND_1.Add(FlagEnabled(active_flag))

    MAIN.Await(AND_1)

    ForceAnimation(troll, 20025)
    Wait(5.0)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_DisableTrollSummon)
def CLONE_DisableTrollSummon(_, troll: uint):
    """CLONE Event 14003766"""
    if ThisEventSlotFlagDisabled():
        DisableCharacter(troll)
        DisableAnimations(troll)
    AND_1.Add(CharacterHasSpecialEffect(troll, Effects.RequestSummonDisable))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(troll, Effects.RennalaSummonInactive))

    MAIN.Await(AND_1)

    AddSpecialEffect(troll, Effects.RennalaSummonHeal)
    AddSpecialEffect(troll, Effects.RennalaSummonInactive)
    RemoveSpecialEffect(troll, Effects.RennalaSummonDisableOnRennalaDeath)
    RemoveSpecialEffect(troll, Effects.RequestSummonDisable)
    RemoveSpecialEffect(troll, 14576)
    DisableCharacter(troll)
    DisableAnimations(troll)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaSummonsDragon)
def CLONE_RennalaSummonsDragon(_, active_flag: uint, rennala: uint, dragon: uint):
    """CLONE Event 14003772"""
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaDragonRequest))
    AND_1.Add(FlagDisabled(active_flag))

    MAIN.Await(AND_1)

    EnableCharacter(dragon)
    Move(
        dragon,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=65,
        copy_draw_parent=rennala,
    )
    SetNetworkUpdateRate(dragon, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RemoveSpecialEffect(dragon, Effects.RennalaSummonInactive)
    EnableFlag(active_flag)
    ReplanAI(dragon)
    WaitFrames(frames=1)
    ForceAnimation(dragon, 20026)
    Wait(0.800000011920929)
    EnableAnimations(dragon)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaResumesFightingAfterDragon)
def CLONE_RennalaResumesFightingAfterDragon(_, active_flag: uint, cleanup_flag: uint, dragon: uint, rennala: uint):
    """CLONE Event 14003773"""
    AND_1.Add(FlagDisabled(cleanup_flag))
    AND_1.Add(FlagEnabled(active_flag))
    OR_1.Add(CharacterHasSpecialEffect(dragon, Effects.RennalaSummonDisableOnRennalaDeath))
    OR_1.Add(CharacterHasSpecialEffect(dragon, Effects.RequestSummonDisable))
    AND_1.Add(OR_1)

    MAIN.Await(AND_1)

    EnableFlag(cleanup_flag)
    RemoveSpecialEffect(rennala, Effects.RennalaLetsSummonFight)
    ReplanAI(rennala)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_DragonCleanup)
def CLONE_DragonCleanup(_, active_flag: uint, cleanup_flag: uint, dragon: uint):
    """CLONE Event 14003774"""
    AND_1.Add(FlagEnabled(active_flag))
    AND_1.Add(FlagEnabled(cleanup_flag))
    AND_1.Add(CharacterHasSpecialEffect(dragon, Effects.RequestSummonDisable))

    MAIN.Await(AND_1)

    DisableFlag(active_flag)
    DisableFlag(cleanup_flag)
    RemoveSpecialEffect(dragon, Effects.RequestSummonDisable)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_DragonSummonDefeated)
def CLONE_DragonSummonDefeated(_, active_flag: uint, dragon: uint):
    """CLONE Event 14003775"""
    AND_1.Add(HealthValue(dragon) <= 1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(dragon, Effects.RequestSummonDisable))
    AND_1.Add(FlagEnabled(active_flag))

    MAIN.Await(AND_1)

    ForceAnimation(dragon, 20027)
    Wait(5.0)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_DisableDragonSummon)
def CLONE_DisableDragonSummon(_, dragon: uint):
    """CLONE Event 14003776"""
    if ThisEventSlotFlagDisabled():
        DisableCharacter(dragon)
        DisableAnimations(dragon)
    AND_1.Add(CharacterHasSpecialEffect(dragon, Effects.RequestSummonDisable))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(dragon, Effects.RennalaSummonInactive))

    MAIN.Await(AND_1)

    AddSpecialEffect(dragon, Effects.RennalaSummonHeal)
    AddSpecialEffect(dragon, Effects.RennalaSummonInactive)
    RemoveSpecialEffect(dragon, Effects.RennalaSummonDisableOnRennalaDeath)
    RemoveSpecialEffect(dragon, Effects.RequestSummonDisable)
    RemoveSpecialEffect(dragon, 14576)
    DisableCharacter(dragon)
    DisableAnimations(dragon)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_DismissSummonsOnRennalaDeath)
def CLONE_DismissSummonsOnRennalaDeath(_, rennala: uint, summon_group: uint):
    """CLONE Event 14003777"""
    MAIN.Await(HealthValue(rennala) == 0)

    AddSpecialEffect(summon_group, Effects.RennalaSummonDisableOnRennalaDeath)
    ReplanAI(summon_group)

# endregion


# region Rennala Phase One Clones
@RestartOnRest(Flags.CLONE_EVENT_ChooseRandomGlowingStudent)
def CLONE_ChooseRandomGlowingStudent(
        _,
        required_flag: uint,
        rennala: uint,
        student_group: uint,
        student_2: uint,
        student_3: uint,
        student_4: uint,
        student_5: uint,
        student_6: uint,
        student_7: uint,
        student_8: uint,
        student_9: uint,
        student_10: uint,
        student_11: uint,
        student_12: uint,
        student_13: uint,
        student_14: uint,
        student_15: uint,
        student_16: uint,
        student_17: uint,
        student_18: uint,
        student_19: uint,
        student_20: uint,
        student_21: uint,
        student_22: uint,
        student_23: uint,
        student_24: uint,
        student_25: uint,
):
    """Event 14003801"""
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(FlagEnabled(Flags.RennalaBattleStarted))
    AwaitConditionTrue(AND_10)
    AND_1.Add(FlagEnabled(required_flag))
    AND_1.Add(CharacterHasSpecialEffect(student_group, Effects.StudentGlowing,
                                        target_comparison_type=ComparisonType.LessThan))
    OR_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBarrierUnknown))
    OR_1.Add(CharacterHasSpecialEffect(rennala, Effects.FirstGlowingStudentChosen))
    OR_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBarrierDamagedOnce))
    OR_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBarrierDamagedTwice))
    AND_1.Add(OR_1)

    MAIN.Await(AND_1)

    DisableFlag(Flags.CLONE_RennalaRandomFlag1)
    DisableFlag(Flags.CLONE_RennalaRandomFlag2)
    DisableFlag(Flags.CLONE_RennalaRandomFlag3)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(Flags.CLONE_RennalaRandomFlag1, Flags.CLONE_RennalaRandomFlag3))
    if FlagDisabled(Flags.CLONE_RennalaRandomFlag3):
        GotoIfFlagEnabled(Label.L0, flag=Flags.CLONE_RennalaRandomFlag1)
        GotoIfFlagEnabled(Label.L1, flag=Flags.CLONE_RennalaRandomFlag2)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_2, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_2, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_2, special_effect=14393)
    AddSpecialEffect(student_2, Effects.StudentGlowing)
    ReplanAI(student_2)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_3, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_3, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_3, special_effect=14393)
    AddSpecialEffect(student_3, Effects.StudentGlowing)
    ReplanAI(student_3)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_4, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_4, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_4, special_effect=14393)
    AddSpecialEffect(student_4, Effects.StudentGlowing)
    ReplanAI(student_4)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_5, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_5, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_5, special_effect=14393)
    AddSpecialEffect(student_5, Effects.StudentGlowing)
    ReplanAI(student_5)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_6, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_6, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_6, special_effect=14393)
    AddSpecialEffect(student_6, Effects.StudentGlowing)
    ReplanAI(student_6)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_7, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_7, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_7, special_effect=14393)
    AddSpecialEffect(student_7, Effects.StudentGlowing)
    ReplanAI(student_7)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_8, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_8, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_8, special_effect=14393)
    AddSpecialEffect(student_8, Effects.StudentGlowing)
    ReplanAI(student_8)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_9, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_9, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_9, special_effect=14393)
    AddSpecialEffect(student_9, Effects.StudentGlowing)
    ReplanAI(student_9)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_10, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_10, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_10, special_effect=14393)
    AddSpecialEffect(student_10, Effects.StudentGlowing)
    ReplanAI(student_10)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_11, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_11, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_11, special_effect=14393)
    AddSpecialEffect(student_11, Effects.StudentGlowing)
    ReplanAI(student_11)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_12, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_12, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_12, special_effect=14393)
    AddSpecialEffect(student_12, Effects.StudentGlowing)
    ReplanAI(student_12)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_13, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_13, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_13, special_effect=14393)
    AddSpecialEffect(student_13, Effects.StudentGlowing)
    ReplanAI(student_13)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_14, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_14, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_14, special_effect=14393)
    AddSpecialEffect(student_14, Effects.StudentGlowing)
    ReplanAI(student_14)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_15, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_15, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_15, special_effect=14393)
    AddSpecialEffect(student_15, Effects.StudentGlowing)
    ReplanAI(student_15)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_16, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_16, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_16, special_effect=14393)
    AddSpecialEffect(student_16, Effects.StudentGlowing)
    ReplanAI(student_16)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_17, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_17, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_17, special_effect=14393)
    AddSpecialEffect(student_17, Effects.StudentGlowing)
    ReplanAI(student_17)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_18, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_18, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_18, special_effect=14393)
    AddSpecialEffect(student_18, Effects.StudentGlowing)
    ReplanAI(student_18)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_19, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_19, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_19, special_effect=14393)
    AddSpecialEffect(student_19, Effects.StudentGlowing)
    ReplanAI(student_19)
    Restart()
    Goto(Label.L10)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_20, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_20, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_20, special_effect=14393)
    AddSpecialEffect(student_20, Effects.StudentGlowing)
    ReplanAI(student_20)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_21, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_21, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_21, special_effect=14393)
    AddSpecialEffect(student_21, Effects.StudentGlowing)
    ReplanAI(student_21)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_22, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_22, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_22, special_effect=14393)
    AddSpecialEffect(student_22, Effects.StudentGlowing)
    ReplanAI(student_22)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_23, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_23, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_23, special_effect=14393)
    AddSpecialEffect(student_23, Effects.StudentGlowing)
    ReplanAI(student_23)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_24, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_24, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_24, special_effect=14393)
    AddSpecialEffect(student_24, Effects.StudentGlowing)
    ReplanAI(student_24)
    Restart()
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_25, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=3, character=student_25, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=student_25, special_effect=14393)
    AddSpecialEffect(student_25, Effects.StudentGlowing)
    ReplanAI(student_25)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaBarrierBreaks)
def CLONE_RennalaBarrierBreaks(_, required_flag: uint, rennala: uint, student_group: uint, character_2: uint):
    """Event 14003805"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBarrierDamaged))
    AND_1.Add(
        CharacterHasSpecialEffect(student_group, Effects.GlowingStudentHit, target_count=0.0))  # NO students have it
    AND_1.Add(CharacterHasSpecialEffect(student_group, Effects.StudentGlowing, target_count=0.0))  # NO students have it
    AND_1.Add(FlagEnabled(required_flag))

    MAIN.Await(AND_1)  # Rennala vulnerable and no students are glowing (or have just been hit while glowing)

    GotoIfCharacterHasSpecialEffect(Label.L1, character=rennala, special_effect=Effects.RennalaBarrierDamagedTwice)
    GotoIfCharacterHasSpecialEffect(Label.L0, character=rennala, special_effect=Effects.RennalaBarrierDamagedOnce)
    if CharacterDoesNotHaveSpecialEffect(character=rennala, special_effect=Effects.FirstGlowingStudentChosen):
        return RESTART  # Rennala has not repaired her barrier yet; restart.

    # Barrier damaged ONCE.
    AddSpecialEffect(rennala, Effects.RennalaBarrierDamagedOnce)
    OR_15.Add(CharacterHasSpecialEffect(student_group, Effects.StudentGlowing,
                                        target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AwaitConditionTrue(OR_15)  # wait for a new Glowing Student to be chosen
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    # Barrier damaged TWICE.
    AddSpecialEffect(rennala, Effects.RennalaBarrierDamagedTwice)
    OR_15.Add(CharacterHasSpecialEffect(student_group, Effects.StudentGlowing,
                                        target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AwaitConditionTrue(OR_15)  # wait for a new Glowing Student to be chosen
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    # Barrier damaged THREE TIMES and BROKEN.
    AddSpecialEffect(rennala, Effects.RennalaBarrierUnknown)
    AddSpecialEffect(student_group, 14384)
    AddSpecialEffect(rennala, 14578)
    ReplanAI(rennala)
    EnableFlag(Flags.CLONE_RennalaBarrierReset)
    DisableFlag(Flags.CLONE_RennalaBarrierActive)
    AddSpecialEffect(student_group, 14388)
    AddSpecialEffect(character_2, 14388)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaBarrierDamaged)
def CLONE_RennalaBarrierDamaged(_, rennala: uint, student_group: uint):
    """Event 14003807"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBarrierUnknown))
    AND_1.Add(CharacterHasSpecialEffect(rennala, 14358))
    AND_1.Add(CharacterHasSpecialEffect(student_group, Effects.GlowingStudentHit,
                                        target_comparison_type=ComparisonType.GreaterThanOrEqual))

    MAIN.Await(AND_1)

    AddSpecialEffect(rennala, Effects.RennalaBarrierDamaged)
    AddSpecialEffect(student_group, Effects.StudentsReactToBarrierDamage)
    DisableFlag(Flags.CLONE_RennalaBarrierReset)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaVulnerableTimer)
def CLONE_RennalaVulnerableTimer(_, barrier_active_flag: uint, rennala: uint):
    """Event 14003808"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(rennala, 14358))
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBarrierUnknown))
    AND_1.Add(FlagDisabled(barrier_active_flag))

    MAIN.Await(AND_1)

    Wait(10.0)  # vulnerability time for Rennala
    EnableFlag(barrier_active_flag)
    OR_15.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaBarrierDamaged))
    AwaitConditionFalse(OR_15)  # wait for barrier to NOT be damaged
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaRequestsSpecialStudent)
def CLONE_RennalaRequestsSpecialStudent(_, request_flag: uint, rennala: uint):
    """Event 14003809"""
    AND_1.Add(CharacterHasSpecialEffect(rennala, Effects.RennalaSpecialStudentRequest))
    AND_1.Add(FlagDisabled(request_flag))

    MAIN.Await(AND_1)

    EnableFlag(request_flag)
    Wait(3.0)
    DisableFlag(request_flag)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_ChooseRandomSpecialStudent)
def CLONE_ChooseRandomSpecialStudent(
    _,
    request_flag: uint,
    student_group: uint,
    student_1: uint,
    student_2: uint,
    student_3: uint,
    student_4: uint,
    student_5: uint,
    student_6: uint,
    student_7: uint,
    student_8: uint,
    student_9: uint,
    student_10: uint,
    student_11: uint,
    student_12: uint,
    student_13: uint,
    student_14: uint,
    student_15: uint,
    student_16: uint,
    student_17: uint,
    student_18: uint,
    student_19: uint,
    student_20: uint,
    student_21: uint,
    student_22: uint,
    student_23: uint,
    student_24: uint,
):
    """Event 14003811"""

    # If five or more students have effect 14351, ignore request (disable `flag` and restart this event).
    OR_1.Add(CharacterHasSpecialEffect(
        student_group,
        Effects.SpecialStudent,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=5.0,
    ))
    SkipLinesIfConditionFalse(2, OR_1)
    DisableFlag(request_flag)
    Restart()

    AND_1.Add(FlagEnabled(request_flag))
    AND_1.Add(
        CharacterHasSpecialEffect(student_group, Effects.SpecialStudent, target_comparison_type=ComparisonType.LessThan,
                                  target_count=5.0))
    MAIN.Await(AND_1)

    # First die roll chooses one of three subsets of students to try.
    DisableFlag(Flags.CLONE_RennalaRandomFlag1)
    DisableFlag(Flags.CLONE_RennalaRandomFlag2)
    DisableFlag(Flags.CLONE_RennalaRandomFlag3)
    EnableRandomFlagInRange(flag_range=(Flags.CLONE_RennalaRandomFlag1, Flags.CLONE_RennalaRandomFlag3))
    if FlagDisabled(Flags.CLONE_RennalaRandomFlag3):
        GotoIfFlagEnabled(Label.L0, flag=Flags.CLONE_RennalaRandomFlag1)
        GotoIfFlagEnabled(Label.L1, flag=Flags.CLONE_RennalaRandomFlag2)

    # Being chosen applies effect 14351, To be chosen, a student must:
    #  - HAVE effects 14577 and 14393
    #  - NOT HAVE effects 14351 and 14394.

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_1, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_1, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_1, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_1, special_effect=14393)
    AddSpecialEffect(student_1, Effects.SpecialStudent)
    ReplanAI(student_1)
    SetNetworkUpdateRate(student_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_2, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_2, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_2, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_2, special_effect=14393)
    AddSpecialEffect(student_2, Effects.SpecialStudent)
    ReplanAI(student_2)
    SetNetworkUpdateRate(student_2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_3, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_3, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_3, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_3, special_effect=14393)
    AddSpecialEffect(student_3, Effects.SpecialStudent)
    ReplanAI(student_3)
    SetNetworkUpdateRate(student_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_4, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_4, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_4, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_4, special_effect=14393)
    AddSpecialEffect(student_4, Effects.SpecialStudent)
    ReplanAI(student_4)
    SetNetworkUpdateRate(student_4, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_5, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_5, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_5, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_5, special_effect=14393)
    AddSpecialEffect(student_5, Effects.SpecialStudent)
    ReplanAI(student_5)
    SetNetworkUpdateRate(student_5, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_6, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_6, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_6, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_6, special_effect=14393)
    AddSpecialEffect(student_6, Effects.SpecialStudent)
    ReplanAI(student_6)
    SetNetworkUpdateRate(student_6, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_7, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_7, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_7, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_7, special_effect=14393)
    AddSpecialEffect(student_7, Effects.SpecialStudent)
    ReplanAI(student_7)
    SetNetworkUpdateRate(student_7, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_8, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_8, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_8, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_8, special_effect=14393)
    AddSpecialEffect(student_8, Effects.SpecialStudent)
    ReplanAI(student_8)
    SetNetworkUpdateRate(student_8, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_9, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_9, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_9, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_9, special_effect=14393)
    AddSpecialEffect(student_9, Effects.SpecialStudent)
    ReplanAI(student_9)
    SetNetworkUpdateRate(student_9, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_10, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_10, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_10, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_10, special_effect=14393)
    AddSpecialEffect(student_10, Effects.SpecialStudent)
    ReplanAI(student_10)
    SetNetworkUpdateRate(student_10, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_11, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_11, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_11, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_11, special_effect=14393)
    AddSpecialEffect(student_11, Effects.SpecialStudent)
    ReplanAI(student_11)
    SetNetworkUpdateRate(student_11, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_12, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_12, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_12, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_12, special_effect=14393)
    AddSpecialEffect(student_12, Effects.SpecialStudent)
    ReplanAI(student_12)
    SetNetworkUpdateRate(student_12, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_13, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_13, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_13, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_13, special_effect=14393)
    AddSpecialEffect(student_13, Effects.SpecialStudent)
    ReplanAI(student_13)
    SetNetworkUpdateRate(student_13, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_14, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_14, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_14, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_14, special_effect=14393)
    AddSpecialEffect(student_14, Effects.SpecialStudent)
    ReplanAI(student_14)
    SetNetworkUpdateRate(student_14, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_15, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_15, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_15, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_15, special_effect=14393)
    AddSpecialEffect(student_15, Effects.SpecialStudent)
    ReplanAI(student_15)
    SetNetworkUpdateRate(student_15, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_16, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_16, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_16, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_16, special_effect=14393)
    AddSpecialEffect(student_16, Effects.SpecialStudent)
    ReplanAI(student_16)
    SetNetworkUpdateRate(student_16, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_17, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_17, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_17, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_17, special_effect=14393)
    AddSpecialEffect(student_17, Effects.SpecialStudent)
    ReplanAI(student_17)
    SetNetworkUpdateRate(student_17, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_18, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_18, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_18, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_18, special_effect=14393)
    AddSpecialEffect(student_18, Effects.SpecialStudent)
    ReplanAI(student_18)
    SetNetworkUpdateRate(student_18, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    Goto(Label.L10)  # TODO: Implies these four students between here and Label 10 CANNOT be chosen?
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_19, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_19, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_19, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_19, special_effect=14393)
    AddSpecialEffect(student_19, Effects.SpecialStudent)
    ReplanAI(student_19)
    SetNetworkUpdateRate(student_19, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_20, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_20, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_20, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_20, special_effect=14393)
    AddSpecialEffect(student_20, Effects.SpecialStudent)
    ReplanAI(student_20)
    SetNetworkUpdateRate(student_20, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_21, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_21, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_21, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_21, special_effect=14393)
    AddSpecialEffect(student_21, Effects.SpecialStudent)
    ReplanAI(student_21)
    SetNetworkUpdateRate(student_21, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_22, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_22, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_22, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_22, special_effect=14393)
    AddSpecialEffect(student_22, Effects.SpecialStudent)
    ReplanAI(student_22)
    SetNetworkUpdateRate(student_22, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=7, character=student_23, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=6, character=student_23, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_23, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=student_23, special_effect=14393)
    AddSpecialEffect(student_23, Effects.SpecialStudent)
    ReplanAI(student_23)
    SetNetworkUpdateRate(student_23, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()

    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=6, character=student_24, special_effect=14577)
    SkipLinesIfCharacterHasSpecialEffect(line_count=5, character=student_24, special_effect=Effects.SpecialStudent)
    SkipLinesIfCharacterHasSpecialEffect(line_count=4, character=student_24, special_effect=Effects.StudentGlowing)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=student_24, special_effect=14393)
    AddSpecialEffect(student_24, Effects.SpecialStudent)
    ReplanAI(student_24)
    SetNetworkUpdateRate(student_24, is_fixed=True, update_rate=CharacterUpdateRate.Always)

    Restart()


@RestartOnRest(Flags.CLONE_EVENT_SyncRennalaSoundDummyPosition)
def CLONE_SyncRennalaSoundDummyPosition(_, rennala: uint, rennala_sound_dummy: uint):
    """Event 14003814"""
    if ThisEventSlotFlagDisabled():
        DisableGravity(rennala_sound_dummy)
    Move(
        rennala_sound_dummy,
        destination=rennala,
        destination_type=CoordEntityType.Character,
        model_point=20,
        short_move=True,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaSoundDummyLoop)
def CLONE_RennalaSoundDummyLoop(_, rennala: uint, rennala_sound_dummy: uint):
    """Event 14003815"""
    MAIN.Await(HasAIStatus(rennala, ai_status=AIStatusType.Battle))

    TriggerAISound(ai_sound_param_id=203000, anchor_entity=rennala_sound_dummy, unk_8_12=2)
    Wait(5.0)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaStudentsUnknownEffect)
def CLONE_RennalaStudentsUnknownEffect(_, student_group: uint):
    """Event 14003817"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(Flags.RennalaBarrierReset))
    AND_1.Add(CharacterProportionHasSpecialEffect(
        character_group=student_group,
        special_effect=14385,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_proportion=1.0,
    ))

    MAIN.Await(AND_1)

    AddSpecialEffect(student_group, 14384)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaForceStudentUpdate)
def CLONE_RennalaForceStudentUpdate(_, rennala: uint, student_group: uint):
    """Event 14003892"""
    MAIN.Await(CharacterHasSpecialEffect(rennala, 14378))

    SetNetworkUpdateRate(student_group, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Wait(1.0)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaStudentsEffect14353)
def CLONE_RennalaStudentsEffect14353(_, rennala: uint, student_group: uint):
    """Event 14003893"""
    MAIN.Await(CharacterHasSpecialEffect(rennala, 5028))

    AddSpecialEffect(student_group, 14353)
    Wait(1.0)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_RennalaStudentsEffect14355)
def CLONE_RennalaStudentsEffect14355(_, rennala: uint, student_group: uint):
    """Event 14003894"""
    MAIN.Await(CharacterHasSpecialEffect(rennala, 5029))

    AddSpecialEffect(student_group, 14355)
    Wait(1.0)
    Restart()


@RestartOnRest(Flags.CLONE_EVENT_StudentChosenAtBattleStart)
def CLONE_StudentChosenAtBattleStart(_, flag: uint, rennala: uint, student_group: uint):
    """One of three students (0, 8, 16) is randomly chosen to protect Rennala's barrier first."""
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(CharacterBackreadEnabled(rennala))
    AND_10.Add(CharacterBackreadEnabled(Characters.CLONE_RennalaStudent0))
    AND_10.Add(CharacterBackreadEnabled(Characters.CLONE_RennalaStudent8))
    AND_10.Add(CharacterBackreadEnabled(Characters.CLONE_RennalaStudent16))
    AND_10.Add(FlagEnabled(Flags.RennalaBattleStarted))

    AwaitConditionTrue(AND_10)

    # Add "Chosen" effect marker to a random student from three.
    DisableFlag(Flags.CLONE_RennalaRandomFlag1)
    DisableFlag(Flags.CLONE_RennalaRandomFlag2)
    DisableFlag(Flags.CLONE_RennalaRandomFlag3)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(Flags.CLONE_RennalaRandomFlag1, Flags.CLONE_RennalaRandomFlag3))
    if FlagEnabled(Flags.CLONE_RennalaRandomFlag1):
        AddSpecialEffect(Characters.CLONE_RennalaStudent0, Effects.StudentGlowing)
    if FlagEnabled(Flags.CLONE_RennalaRandomFlag2):
        AddSpecialEffect(Characters.CLONE_RennalaStudent8, Effects.StudentGlowing)
    if FlagEnabled(Flags.CLONE_RennalaRandomFlag3):
        AddSpecialEffect(Characters.CLONE_RennalaStudent16, Effects.StudentGlowing)

    AddSpecialEffect(rennala, Effects.FirstGlowingStudentChosen)
    WaitFrames(frames=1)

    EnableFlag(flag)
    DisableThisSlotFlag()
    OR_1.Add(CharacterHasSpecialEffect(student_group, Effects.GlowingStudentHit, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AwaitConditionTrue(OR_1)
    EnableFlag(Flags.CLONE_FirstGlowingStudentHit)
    End()

# endregion
