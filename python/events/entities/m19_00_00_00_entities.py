from soulstruct.eldenring.game_types import *


class Flags(Flag):
    EldenLordEndingChosen = 19000100  # one of the four Elden Lord ending variants
    EldenBeastDead = 19000800
    RadagonFirstTimeDone = 19000801
    RadagonDead = 19000802  # new flag that makes Radagon's phase one-off
    StonePlatformEntered = 19002500  # host has gone through the Erdtree fog
    RadagonBattleStarted = 19002801
    RequestEldenBeast = 19002802  # now unused
    EndingCanBeChosen = 19001100  # enabled when Elden Beast dies
    RanniEndingAvailable = 1034509406


class NameText(NPCName):
    RadagonOfTheGoldenOrder = 902190000
    CLONE_RadagonOfTheGoldenOrder = 902190010
    EldenBeast = 902200000
    CLONE_EldenBeast = 902200010


class RegionPoints(RegionPoint):
    HostPositionAfterEldenBeastCutscene = 19002812
    SummonPositionAfterEldenBeastCutscene = 19002813


class CharacterGroups(Character):
    RadagonEldenBeast = 19005800


class Characters(Character):
    TalkDummy0 = 19000950  # c1000_9000 npc 10000000 think 1 talk 1000
    TalkDummy1 = 19000700  # c1000_9001 col h003000 npc 506070078 think 500000000 talk 607001900
    TalkDummy2 = 19000710  # c1000_9002 col h003000 npc 501060078 think 500000000 talk 106901900
    TalkDummy3 = 19000130  # c1000_9003 col h003000 npc 10001000 think 1 talk 2000
    Radagon = 19000810  # c2190_9000 col h003000 npc 21900078 think 21900000 group 19005800,19005130
    EldenBeast = 19000800  # c2200_9000 col h008000 npc 22000078 think 22000000 group 19005800,19005130
    Unknown = 19000811

    CLONE_Radagon = 19000812  # something else using 811
    CLONE_EldenBeast = 19000805  # unused "spirits" use 801-804


class Assets(Asset):
    AEG099_001_9000 = 19001800  # AEG099
    AEG099_003_9000 = 19001500  # AEG099
    AEG099_003_9001 = 19001501  # AEG099
    AEG099_052_9000 = 19001130  # AEG099
    AEG099_060_9000 = 19001950  # AEG099
    AEG099_090_9000 = 19001900  # AEG099
    AEG099_090_9001 = 19001110  # AEG099
    AEG099_090_9002 = 19001120  # AEG099
    AEG227_017_1000 = 19001101  # AEG227
    BrokenMarikaStatue = 19001100  # AEG227
    BrokenRadagonStatue = 19001810  # AEG301
