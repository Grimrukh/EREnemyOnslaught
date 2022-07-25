from soulstruct.eldenring.game_types import *


class Flags(Flag):
    RegalAncestorSpiritDead = 12090800

    AncestorInPhaseTwo = 12092802  # after first heal

    # ORIGINAL
    AncestorFirstAnimalLifeDrainDone = 12092862
    AncestorSecondAnimalLifeDrainDone = 12092863
    AncestorRequestWarpAttack3014 = 12092901
    ProjectileRequest_LowAnimalCount = 12092907  # 1 to 12 animals
    ProjectileRequest_MediumAnimalCount = 12092908  # 13 to 19 animals
    ProjectileRequest_HighAnimalCount = 12092909  # 20+ animals
    RequestAnimalRecount = 12092858
    DoNotSpawnAnimals = 12092853
    AncestorRequestWarpToAnimal0 = 12092870
    AncestorRequestWarpToAnimal1 = 12092871
    AncestorRequestWarpToAnimal2 = 12092872
    AncestorRequestWarpToAnimal3 = 12092873
    AncestorRequestWarpToAnimal4 = 12092874
    AncestorRequestWarpToAnimal5 = 12092875
    AncestorRequestWarpToAnimal6 = 12092876
    AncestorRequestWarpToAnimal7 = 12092877
    AncestorRequestWarpToAnimal8 = 12092878
    AncestorRequestWarpToAnimal9 = 12092879
    AncestorRequestWarpToAnimal10 = 12092880
    AncestorRequestWarpToAnimal11 = 12092881
    AncestorRequestWarpToAnimal12 = 12092882
    AncestorRequestWarpToAnimal13 = 12092883
    AncestorRequestWarpToAnimal14 = 12092884
    AncestorRequestWarpToAnimal15 = 12092885
    AncestorRequestWarpToAnimal16 = 12092886
    AncestorRequestWarpToAnimal17 = 12092887
    AncestorRequestWarpToAnimal18 = 12092888
    AncestorRequestWarpToAnimal19 = 12092889
    AncestorRequestWarpToAnimal20 = 12092890
    AncestorRequestWarpToAnimal21 = 12092891
    AncestorRequestWarpToAnimal22 = 12092892
    AncestorRequestWarpToAnimal23 = 12092893
    AncestorRequestWarpToAnimal24 = 12092894
    AncestorRequestWarpToAnimal25 = 12092895
    AncestorRequestWarpToAnimal26 = 12092896
    AncestorRequestWarpToAnimal27 = 12092897

    # CLONE (all IDs -200 except first two)
    CLONE_AncestorFirstAnimalLifeDrainDone = 12092866  # +4
    CLONE_AncestorSecondAnimalLifeDrainDone = 12092867  # +4
    CLONE_AncestorRequestWarpAttack3014 = 12092701
    CLONE_ProjectileRequest_LowAnimalCount = 12092707  # 1 to 12 animals
    CLONE_ProjectileRequest_MediumAnimalCount = 12092708  # 13 to 19 animals
    CLONE_ProjectileRequest_HighAnimalCount = 12092709  # 20+ animals
    CLONE_RequestAnimalRecount = 12092658
    CLONE_DoNotSpawnAnimals = 12092653
    CLONE_AncestorRequestWarpToAnimal0 = 12092870
    CLONE_AncestorRequestWarpToAnimal1 = 12092871
    CLONE_AncestorRequestWarpToAnimal2 = 12092872
    CLONE_AncestorRequestWarpToAnimal3 = 12092873
    CLONE_AncestorRequestWarpToAnimal4 = 12092874
    CLONE_AncestorRequestWarpToAnimal5 = 12092875
    CLONE_AncestorRequestWarpToAnimal6 = 12092876
    CLONE_AncestorRequestWarpToAnimal7 = 12092877
    CLONE_AncestorRequestWarpToAnimal8 = 12092878
    CLONE_AncestorRequestWarpToAnimal9 = 12092879
    CLONE_AncestorRequestWarpToAnimal10 = 12092880
    CLONE_AncestorRequestWarpToAnimal11 = 12092881
    CLONE_AncestorRequestWarpToAnimal12 = 12092882
    CLONE_AncestorRequestWarpToAnimal13 = 12092883
    CLONE_AncestorRequestWarpToAnimal14 = 12092884
    CLONE_AncestorRequestWarpToAnimal15 = 12092885
    CLONE_AncestorRequestWarpToAnimal16 = 12092886
    CLONE_AncestorRequestWarpToAnimal17 = 12092887
    CLONE_AncestorRequestWarpToAnimal18 = 12092888
    CLONE_AncestorRequestWarpToAnimal19 = 12092889
    CLONE_AncestorRequestWarpToAnimal20 = 12092890
    CLONE_AncestorRequestWarpToAnimal21 = 12092891
    CLONE_AncestorRequestWarpToAnimal22 = 12092892
    CLONE_AncestorRequestWarpToAnimal23 = 12092893
    CLONE_AncestorRequestWarpToAnimal24 = 12092894
    CLONE_AncestorRequestWarpToAnimal25 = 12092895
    CLONE_AncestorRequestWarpToAnimal26 = 12092896
    CLONE_AncestorRequestWarpToAnimal27 = 12092897


class Effects(SpecialEffectParam):
    AnimalActive = 13605
    AnimalDrained = 13617
    Ancestor_NoDeerActive = 13606
    Ancestor_NoBoarsActive = 13607
    Ancestor_NoWildMouflonsActive = 13608
    Ancestor_NoSpringharesActive = 13609
    Ancestor_WarpToAnimalRequest = 13610
    Ancestor_Reactivate = 13623
    Ancestor_AnimalLifeDrainRequest = 13624
    Ancestor_LessThanFiveAnimalsActive = 13625
    Ancestor_FirstHeal = 13632
    Ancestor_SecondHeal = 13633
    Ancestor_ThirdPlusHeal = 13634
    AnimalSpawnRequest = 13642
    FirstDeerRequest = 13645
    FirstBoarRequest = 13646
    FirstWildMouflonRequest = 13647


class NameText(NPCName):
    RegalAncestorSpirit = 904670001
    CLONE_RegalAncestorSpirit = 904670011


class Spawners(SpawnerEvent):
    DeerSpawner0 = 12093200
    DeerSpawner1 = 12093201
    DeerSpawner2 = 12093202
    DeerSpawner3 = 12093203
    DeerSpawner4 = 12093204
    DeerSpawner5 = 12093205
    DeerSpawner6 = 12093206
    BoarSpawner0 = 12093220
    BoarSpawner1 = 12093221
    BoarSpawner2 = 12093222
    BoarSpawner3 = 12093223
    BoarSpawner4 = 12093224
    BoarSpawner5 = 12093225
    BoarSpawner6 = 12093226
    WildMouflonSpawner0 = 12093240
    WildMouflonSpawner1 = 12093241
    WildMouflonSpawner2 = 12093242
    WildMouflonSpawner3 = 12093243
    WildMouflonSpawner4 = 12093244
    WildMouflonSpawner5 = 12093245
    WildMouflonSpawner6 = 12093246
    SpringhareSpawner0 = 12093260
    SpringhareSpawner1 = 12093261
    SpringhareSpawner2 = 12093262
    SpringhareSpawner3 = 12093263
    SpringhareSpawner4 = 12093264
    SpringhareSpawner5 = 12093265
    SpringhareSpawner6 = 12093266

    CLONE_DeerSpawner0 = 12093300
    CLONE_DeerSpawner1 = 12093301
    CLONE_DeerSpawner2 = 12093302
    CLONE_DeerSpawner3 = 12093303
    CLONE_DeerSpawner4 = 12093304
    CLONE_DeerSpawner5 = 12093305
    CLONE_DeerSpawner6 = 12093306
    CLONE_BoarSpawner0 = 12093320
    CLONE_BoarSpawner1 = 12093321
    CLONE_BoarSpawner2 = 12093322
    CLONE_BoarSpawner3 = 12093323
    CLONE_BoarSpawner4 = 12093324
    CLONE_BoarSpawner5 = 12093325
    CLONE_BoarSpawner6 = 12093326
    CLONE_WildMouflonSpawner0 = 12093340
    CLONE_WildMouflonSpawner1 = 12093341
    CLONE_WildMouflonSpawner2 = 12093342
    CLONE_WildMouflonSpawner3 = 12093343
    CLONE_WildMouflonSpawner4 = 12093344
    CLONE_WildMouflonSpawner5 = 12093345
    CLONE_WildMouflonSpawner6 = 12093346
    CLONE_SpringhareSpawner0 = 12093360
    CLONE_SpringhareSpawner1 = 12093361
    CLONE_SpringhareSpawner2 = 12093362
    CLONE_SpringhareSpawner3 = 12093363
    CLONE_SpringhareSpawner4 = 12093364
    CLONE_SpringhareSpawner5 = 12093365
    CLONE_SpringhareSpawner6 = 12093366


class CharacterGroups(Character):
    RegalAncestorAnimals = 12095200
    RegalAncestorDeer = 12095201
    RegalAncestorBoars = 12095202
    RegalAncestorWildMouflons = 12095203
    RegalAncestorSpringhares = 12095204

    CLONE_RegalAncestorAnimals = 12095210
    CLONE_RegalAncestorDeer = 12095211
    CLONE_RegalAncestorBoars = 12095212
    CLONE_RegalAncestorWildMouflons = 12095213
    CLONE_RegalAncestorSpringhares = 12095214


class Characters(Character):
    AncestorProjectileOwner = 12090290  # c0100_9000 npc 1002000 think 1
    TalkDummy = 12090100  # c1000_9000 col h020300 npc 10001000 think 1 talk 2000

    RegalAncestorSpirit = 12090800  # c4670_9000 col h020300 npc 46700065 think 46700100 group 12095800,12095100
    Deer0 = 12090200  # c6010_9000 col h020300 npc 60100965 think 60100000 group 12095200,12095201
    Deer1 = 12090201  # c6010_9001 col h020300 npc 60100965 think 60100000 group 12095200,12095201
    Deer2 = 12090202  # c6010_9002 col h020300 npc 60100965 think 60100000 group 12095200,12095201
    Deer3 = 12090203  # c6010_9003 col h020300 npc 60100965 think 60100000 group 12095200,12095201
    Deer4 = 12090204  # c6010_9004 col h020300 npc 60100965 think 60100000 group 12095200,12095201
    Deer5 = 12090205  # c6010_9005 col h020300 npc 60100965 think 60100000 group 12095200,12095201
    Deer6 = 12090206  # c6010_9006 col h020300 npc 60100965 think 60100000 group 12095200,12095201
    Boar0 = 12090220  # c6050_9000 col h020300 npc 60500965 think 60500000 group 12095200,12095202
    Boar1 = 12090221  # c6050_9001 col h020300 npc 60500965 think 60500000 group 12095200,12095202
    Boar2 = 12090222  # c6050_9002 col h020300 npc 60500965 think 60500000 group 12095200,12095202
    Boar3 = 12090223  # c6050_9003 col h020300 npc 60500965 think 60500000 group 12095200,12095202
    Boar4 = 12090224  # c6050_9004 col h020300 npc 60500965 think 60500000 group 12095200,12095202
    Boar5 = 12090225  # c6050_9005 col h020300 npc 60500965 think 60500000 group 12095200,12095202
    Boar6 = 12090226  # c6050_9006 col h020300 npc 60500965 think 60500000 group 12095200,12095202
    WildMouflon0 = 12090240  # c6060_9000 col h020300 npc 60600965 think 60600000 group 12095200,12095203
    WildMouflon1 = 12090241  # c6060_9001 col h020300 npc 60600965 think 60600000 group 12095200,12095203
    WildMouflon2 = 12090242  # c6060_9002 col h020300 npc 60600965 think 60600000 group 12095200,12095203
    WildMouflon3 = 12090243  # c6060_9003 col h020300 npc 60600965 think 60600000 group 12095200,12095203
    WildMouflon4 = 12090244  # c6060_9004 col h020300 npc 60600965 think 60600000 group 12095200,12095203
    WildMouflon5 = 12090245  # c6060_9005 col h020300 npc 60600965 think 60600000 group 12095200,12095203
    WildMouflon6 = 12090246  # c6060_9006 col h020300 npc 60600965 think 60600000 group 12095200,12095203
    Springhare0 = 12090260  # c6100_9000 col h020300 npc 61000965 think 60600000 group 12095200,12095204
    Springhare1 = 12090261  # c6100_9001 col h020300 npc 61000965 think 60600000 group 12095200,12095204
    Springhare2 = 12090262  # c6100_9002 col h020300 npc 61000965 think 60600000 group 12095200,12095204
    Springhare3 = 12090263  # c6100_9003 col h020300 npc 61000965 think 60600000 group 12095200,12095204
    Springhare4 = 12090264  # c6100_9004 col h020300 npc 61000965 think 60600000 group 12095200,12095204
    Springhare5 = 12090265  # c6100_9005 col h020300 npc 61000965 think 60600000 group 12095200,12095204
    Springhare6 = 12090266  # c6100_9006 col h020300 npc 61000965 think 60600000 group 12095200,12095204

    CLONE_RegalAncestorSpirit = 12090801
    CLONE_Deer0 = 12090300
    CLONE_Deer1 = 12090301
    CLONE_Deer2 = 12090302
    CLONE_Deer3 = 12090303
    CLONE_Deer4 = 12090304
    CLONE_Deer5 = 12090305
    CLONE_Deer6 = 12090306
    CLONE_Boar0 = 12090320
    CLONE_Boar1 = 12090321
    CLONE_Boar2 = 12090322
    CLONE_Boar3 = 12090323
    CLONE_Boar4 = 12090324
    CLONE_Boar5 = 12090325
    CLONE_Boar6 = 12090326
    CLONE_WildMouflon0 = 12090340
    CLONE_WildMouflon1 = 12090341
    CLONE_WildMouflon2 = 12090342
    CLONE_WildMouflon3 = 12090343
    CLONE_WildMouflon4 = 12090344
    CLONE_WildMouflon5 = 12090345
    CLONE_WildMouflon6 = 12090346
    CLONE_Springhare0 = 12090360
    CLONE_Springhare1 = 12090361
    CLONE_Springhare2 = 12090362
    CLONE_Springhare3 = 12090363
    CLONE_Springhare4 = 12090364
    CLONE_Springhare5 = 12090365
    CLONE_Springhare6 = 12090366


class Assets(Asset):
    AEG099_002_9000 = 12091800  # AEG099
    AEG099_053_9000 = 12091100  # AEG099
    AEG099_065_9000 = 12091848  # AEG099
    AEG099_504_9000 = 12091940  # AEG099
