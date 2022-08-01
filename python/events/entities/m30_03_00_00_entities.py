from soulstruct.eldenring.game_types import *


class Flags(Flag):
    SnailDead = 30030800

    SnailSummoningActivated = 30032812  # sort of useless
    CrucibleKnightSummon0Killed = 30032813
    CrucibleKnightSummon1Killed = 30032814
    CrucibleKnightSummons23Killed = 30032815
    CrucibleKnightSummons45Killed = 30032816
    CrucibleKnightSummons67Killed = 30032817

    SnailWarpingDisabled = 30032822  # marks phase one (>90% HP)
    SnailWarpFlag0 = 30032823
    SnailWarpFlag1 = 30032824
    SnailWarpFlag2 = 30032825
    SnailWarpFlag3 = 30032826
    SnailWarpFlag4 = 30032827
    SnailWarpFlag5 = 30032828
    SnailWarpFlag6 = 30032829
    SnailWarpFlag7 = 30032830
    SnailWarpFlag8 = 30032831
    SnailWarpFlag9 = 30032832
    SnailWarpFlag10 = 30032833
    SnailWarpFlag11 = 30032834
    SnailIsWarping = 30032839

    CrucibleKnightSummon0Unlocked = 30032882
    CrucibleKnightSummon1Unlocked = 30032883
    CrucibleKnightSummons23Unlocked = 30032884
    CrucibleKnightSummons45Unlocked = 30032885
    CrucibleKnightSummons67Unlocked = 30032886
    CrucibleKnightSummons89Unlocked = 30032887

    CLONE_SnailSummoningActivated = 30032712  # sort of useless
    CLONE_CrucibleKnightSummon0Killed = 30032713
    CLONE_CrucibleKnightSummon1Killed = 30032714
    CLONE_CrucibleKnightSummons23Killed = 30032715
    CLONE_CrucibleKnightSummons45Killed = 30032716
    CLONE_CrucibleKnightSummons67Killed = 30032717

    CLONE_SnailWarpingDisabled = 30032722
    CLONE_SnailWarpFlag0 = 30032723
    CLONE_SnailWarpFlag1 = 30032724
    CLONE_SnailWarpFlag2 = 30032725
    CLONE_SnailWarpFlag3 = 30032726
    CLONE_SnailWarpFlag4 = 30032727
    CLONE_SnailWarpFlag5 = 30032728
    CLONE_SnailWarpFlag6 = 30032729
    CLONE_SnailWarpFlag7 = 30032730
    CLONE_SnailWarpFlag8 = 30032731
    CLONE_SnailWarpFlag9 = 30032732
    CLONE_SnailWarpFlag10 = 30032733
    CLONE_SnailWarpFlag11 = 30032734
    CLONE_SnailIsWarping = 30032739

    CLONE_CrucibleKnightSummon0Unlocked = 30032782
    CLONE_CrucibleKnightSummon1Unlocked = 30032783
    CLONE_CrucibleKnightSummons23Unlocked = 30032784
    CLONE_CrucibleKnightSummons45Unlocked = 30032785
    CLONE_CrucibleKnightSummons67Unlocked = 30032786
    CLONE_CrucibleKnightSummons89Unlocked = 30032787


class Characters(Character):
    TalkDummy0 = 30030500  # c1000_9001 col h000200 npc 10003100 think 1
    TalkDummy1 = 30030100  # c1000_9002 npc 10001000 think 1 talk 2000
    TalkDummy2 = 30030600  # c1000_9003 npc 10003100 think 1
    TalkDummy3 = 30030950  # c1000_9004 npc 10000000 think 1 talk 1000
    CrucibleKnightSummon0 = 30030801  # c2500_9000 col h000400 npc 25007020 think 25001000 group 30035800,30035100
    CrucibleKnightSummon4 = 30030805  # c2500_9001 col h000400 npc 25006020 think 25000000 group 30035800,30035100
    CrucibleKnightSummon5 = 30030806  # c2500_9002 col h000400 npc 25007120 think 25001100 group 30035800,30035100
    CrucibleKnightSummon1 = 30030802  # c2500_9003 col h000400 npc 25006120 think 25000100 group 30035800,30035100
    CrucibleKnightSummon2 = 30030803  # c2500_9004 col h000400 npc 25006020 think 25000000 group 30035800,30035100
    CrucibleKnightSummon3 = 30030804  # c2500_9005 col h000400 npc 25007120 think 25001100 group 30035800,30035100
    CrucibleKnightSummon6 = 30030807  # c2500_9006 col h000400 npc 25006020 think 25000000 group 30035800,30035100
    CrucibleKnightSummon7 = 30030808  # c2500_9007 col h000400 npc 25007120 think 25001100 group 30035800,30035100
    CrucibleKnightSummon8 = 30030809  # c2500_9008 col h000400 npc 25006020 think 25000000 group 30035800,30035100
    CrucibleKnightSummon9 = 30030810  # c2500_9009 col h000400 npc 25007120 think 25001100 group 30035800,30035100
    Imp0 = 30030200  # c3080_9000 col h000101 npc 30806020 think 30802000
    Imp1 = 30030201  # c3080_9001 col h000101 npc 30800020 think 30800010
    Imp2 = 30030202  # c3080_9002 col h000101 npc 30800020 think 30800010
    Imp3 = 30030203  # c3080_9003 col h000200 npc 30800020 think 30800010
    Imp4 = 30030204  # c3080_9004 col h000200 npc 30800020 think 30800020
    Imp5 = 30030205  # c3080_9005 col h000200 npc 30801120 think 30800000
    Imp6 = 30030206  # c3080_9006 col h000200 npc 30801120 think 30800000
    Imp7 = 30030207  # c3080_9007 col h000101 npc 30800020 think 30800010
    Imp8 = 30030208  # c3080_9008 col h000101 npc 30806020 think 30802000
    Imp9 = 30030209  # c3080_9009 col h000101 npc 30800020 think 30800000
    Snail = 30030800  # c4140_9000 col h000400 npc 41402920 think 41402000 group 30035800,30035100

    CLONE_CrucibleKnightSummon0 = 30030821
    CLONE_CrucibleKnightSummon4 = 30030825
    CLONE_CrucibleKnightSummon5 = 30030826
    CLONE_CrucibleKnightSummon1 = 30030822
    CLONE_CrucibleKnightSummon2 = 30030823
    CLONE_CrucibleKnightSummon3 = 30030824
    CLONE_CrucibleKnightSummon6 = 30030827
    CLONE_CrucibleKnightSummon7 = 30030828
    CLONE_CrucibleKnightSummon8 = 30030829
    CLONE_CrucibleKnightSummon9 = 30030830
    CLONE_Snail = 30030820


class Spawners(SpawnerEvent):
    SnailCrucibleKnightSpawner1 = 30033801  # spawns CrucibleKnight0
    SnailCrucibleKnightSpawner2 = 30033802  # spawns CrucibleKnight1
    SnailCrucibleKnightSpawner3 = 30033803  # spawns CrucibleKnight2 and CrucibleKnight3
    SnailCrucibleKnightSpawner4 = 30033804  # spawns CrucibleKnight4 and CrucibleKnight5
    SnailCrucibleKnightSpawner5 = 30033805  # spawns CrucibleKnight6 and CrucibleKnight7
    SnailCrucibleKnightSpawner6 = 30033806  # spawns CrucibleKnight8 and CrucibleKnight9

    CLONE_SnailCrucibleKnightSpawner1 = 30033811
    CLONE_SnailCrucibleKnightSpawner2 = 30033812
    CLONE_SnailCrucibleKnightSpawner3 = 30033813
    CLONE_SnailCrucibleKnightSpawner4 = 30033814
    CLONE_SnailCrucibleKnightSpawner5 = 30033815
    CLONE_SnailCrucibleKnightSpawner6 = 30033816


class Assets(Asset):
    AEG027_041_0500 = 30031540  # AEG027
    AEG027_044_0500 = 30031600  # AEG027
    AEG027_115_0500 = 30031541  # AEG027
    AEG027_157_0500 = 30031570  # AEG027
    AEG027_157_0501 = 30031571  # AEG027
    AEG027_157_0502 = 30031572  # AEG027
    AEG027_157_0503 = 30031573  # AEG027
    AEG027_157_0504 = 30031574  # AEG027
    AEG027_157_0505 = 30031575  # AEG027
    AEG027_157_0506 = 30031576  # AEG027
    AEG027_157_0507 = 30031577  # AEG027
    AEG099_001_9000 = 30031800  # AEG099
    AEG099_053_9000 = 30031100  # AEG099
    AEG099_060_9001 = 30031950  # AEG099
    AEG099_065_9000 = 30031840  # AEG099
    AEG099_500_9000 = 30031940  # AEG099
    AEG099_630_9000 = 30031520  # AEG099
