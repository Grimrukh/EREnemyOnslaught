from soulstruct.eldenring.game_types import *


class Flags(Flag):
    HoarahLouxDead = 11050800
    GodfreyHoarahLouxFirstTimeDone = 11050801
    HoarahLouxInPhaseTwo = 11052802  # either one
    SirGideonOfnirDead = 11050850
    SirGideonOfnirFirstTimeDone = 11050851
    SirGideonOfnirInPhaseTwo = 11052852  # for music


class NameText(NPCName):
    GodfreyFirstEldenLord = 904720000
    CLONE_GodfreyFirstEldenLord = 904720010
    HoarahLoux = 904720001
    CLONE_HoarahLoux = 904720011
    SirGideonOfnir = 132400
    CLONE_SirGideonOfnir = 132401  # TODO: Have Gideon's clone also sitting in Roundtable Hold with him.


class RegionPoints(RegionPoint):
    # TODO: Two new regions for Godfrey post-cutscene. Both Hoarah Loux transitions can use the original one below.
    GodfreyPostCutscenePosition = 11052813
    CLONE_GodfreyPostCutscenePosition = 11052814
    HoarahLouxPostCutscenePosition = 11052815
    PlayerPostHoarahLouxCutscenePosition = 11052816


class CharacterGroups(Character):
    GodfreyHoarahLouxBoss = 11055800
    SirGideonOfnirBoss = 11055850
    SirGideonOfnirVariants = 11055851


class Characters(Character):
    SirGideonOfnir = 11050850  # c0000_9020 col h013700 npc 523240070 think 523240100 chara 23241 talk 324001105 group 11055850,11055102
    SirGideonOfnirVariant1 = 11050851  # c0000_9021 col h013700 npc 523240070 think 523240100 chara 23242 group 11055850,11055851
    SirGideonOfnirVariant2 = 11050852  # c0000_9022 col h013700 npc 523240070 think 523240100 chara 23243 group 11055850,11055851
    SirGideonOfnirVariant3 = 11050853  # c0000_9023 col h013700 npc 523240070 think 523240100 chara 23244 group 11055850,11055851
    SirGideonOfnirVariant4 = 11050854  # c0000_9024 col h013700 npc 523240070 think 523240100 chara 23245 group 11055850,11055851
    SirGideonOfnirVariant5 = 11050855  # c0000_9025 col h013700 npc 523240070 think 523240100 chara 23246 group 11055850,11055851
    SirGideonOfnirVariant6 = 11050856  # c0000_9026 col h013700 npc 523240070 think 523240100 chara 23247 group 11055850,11055851
    SirGideonOfnirVariant7 = 11050857  # c0000_9027 col h013700 npc 523240070 think 523240100 chara 23248 group 11055850,11055851
    BrotherCorhyn = 11050710  # c0000_9030 col h024300 npc 523510070 think 523510000 chara 23510 talk 351001105
    Shabriri = 11050740  # c0000_9031 col h020000 npc 533181070 think 533181000 chara 23184
    NepheliLoux = 11050750  # c0000_9032 col h020000 npc 533340070 think 533340000 chara 23341
    TalkDummy0 = 11050950  # c1000_9000 npc 10000000 think 1 talk 1000
    TalkDummy1 = 11050951  # c1000_9001 col h013700 npc 10000000 think 1 talk 1000
    TalkDummy2 = 11050952  # c1000_9002 npc 10000000 think 1 talk 1000
    TalkDummy3 = 11050953  # c1000_9003 col h024000 npc 10000000 think 1 talk 1000
    TalkDummy4 = 11050954  # c1000_9004 npc 10000000 think 1 talk 1000
    TalkDummy5 = 11050955  # c1000_9005 npc 10000000 think 1 talk 1000
    TalkDummy6 = 11050100  # c1000_9010 col h020100 npc 10001000 think 1 talk 2000
    TalkDummy7 = 11050102  # c1000_9011 col h013700 npc 10001000 think 1 talk 2000
    Commoner0 = 11050720  # c3660_9000 col h024000 npc 36609170 think 500000000 talk 706001105
    Commoner1 = 11050721  # c3660_9001 col h014500 npc 36609170 think 500000000 talk 706011105
    Commoner2 = 11050202  # c3660_9002 col h012900 npc 36600070 think 36600000
    Commoner3 = 11050203  # c3660_9003 col h012900 npc 36600070 think 36600000
    Commoner4 = 11050205  # c3660_9005 col h015800 npc 36600070 think 36600000
    Commoner5 = 11050206  # c3660_9006 col h015800 npc 36600070 think 36600000
    Commoner6 = 11050207  # c3660_9007 col h015800 npc 36600070 think 36600000
    Commoner7 = 11050208  # c3660_9008 col h015800 npc 36600070 think 36600000
    Goldmask = 11050705  # c3666_9000 col h015900 npc 36660070 think 36660000 talk 112001105
    DemiHumanShaman = 11050730  # c4110_9000 col h001300 npc 41109170 think 41109000 talk 223001105
    GiantMirandaFlower = 11050240  # c4480_9000 col h015900 npc 44800370 think 44800000
    MirandaFlower0 = 11050250  # c4481_9000 col h015900 npc 44810370 think 44810000
    MirandaFlower1 = 11050251  # c4481_9001 col h015900 npc 44810370 think 44810000
    UlceratedTreeSpirit0 = 11050300  # c4640_9000 col h018000 npc 46400070 think 46400000
    UlceratedTreeSpirit1 = 11050301  # c4640_9001 col h018000 npc 46400070 think 46400000
    UlceratedTreeSpirit2 = 11050302  # c4640_9002 col h018000 npc 46400070 think 46400000
    GuardianGolem = 11050320  # c4660_9000 col h019500 npc 46600070 think 46600000
    Godfrey = 11050801  # c4720_9000 col h020100 npc 47200070 think 47200900 talk 206101105 group 11055800,11055100
    HoarahLoux = 11050800  # c4721_9000 col h020100 npc 47210070 think 47210900 talk 206101105 group 11055800,11055100
    Gargoyle = 11050310  # c4770_9000 col h013200 npc 47700070 think 47700000

    # TODO: New starting points for Godfrey and Gideon.
    CLONE_Godfrey = 11050803
    CLONE_HoarahLoux = 11050802
    CLONE_SirGideonOfnir = 11050858


class Assets(Asset):
    AEG099_001_9001 = 11051800  # AEG099
    AEG099_001_9002 = 11051801  # AEG099
    AEG099_001_9003 = 11051850  # AEG099
    AEG099_001_9004 = 11051851  # AEG099
    AEG099_001_9005 = 11051852  # AEG099
    AEG099_001_9006 = 11051854  # AEG099
    AEG099_001_9007 = 11051855  # AEG099
    AEG099_001_9008 = 11051856  # AEG099
    AEG099_002_9000 = 11051853  # AEG099
    AEG099_052_9000 = 11051100  # AEG099
    AEG099_052_9001 = 11051102  # AEG099
    AEG099_060_9000 = 11051950  # AEG099
    AEG099_060_9001 = 11051951  # AEG099
    AEG099_060_9002 = 11051952  # AEG099
    AEG099_060_9003 = 11051953  # AEG099
    AEG099_060_9004 = 11051954  # AEG099
    AEG099_060_9005 = 11051955  # AEG099
    AEG099_090_9000 = 11051700  # AEG099
    AEG099_504_9000 = 11051941  # AEG099
    AEG099_510_9000 = 11051680  # AEG099
    AEG099_590_9000 = 11051710  # AEG099
    AEG099_591_9000 = 11051720  # AEG099
    AEG099_620_9000 = 11051721  # AEG099
    AEG099_990_9010 = 11051730  # AEG099
    AEG099_990_9011 = 11051740  # AEG099
    AEG227_001_0500 = 11051610  # AEG227
    AEG227_003_0500 = 11051525  # AEG227
    AEG227_010_0500 = 11051560  # AEG227
    AEG227_026_0500 = 11051592  # AEG227
    AEG227_029_0500 = 11051578  # AEG227
    AEG227_030_0500 = 11051552  # AEG227
    AEG227_050_0507 = 11051611  # AEG227
    AEG227_050_0508 = 11051612  # AEG227
    AEG227_051_0500 = 11051526  # AEG227
    AEG227_051_0501 = 11051527  # AEG227
    AEG227_052_0500 = 11051536  # AEG227
    AEG227_052_0501 = 11051537  # AEG227
    AEG227_052_0502 = 11051532  # AEG227
    AEG227_052_0503 = 11051531  # AEG227
    AEG227_090_0500 = 11051530  # AEG227
    AEG227_090_0501 = 11051535  # AEG227
    AEG228_076_3500 = 11051820  # AEG228
    AEG228_098_1038 = 11051691  # AEG228
