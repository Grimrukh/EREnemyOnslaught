from soulstruct.eldenring.game_types import *


class Flags(Flag):
    FireGiantDead = 1252520800
    FireGiantFirstTimeDone = 1252520801
    FireGiantInPhaseThree = 1252522802  # either Giant
    EnableFireGiantFog = 1252520804

    FireGiantFirstLegDamage0 = 1052522820
    FireGiantFirstLegDamage1 = 1052522821
    FireGiantFirstLegDamage2 = 1052522822
    FireGiantFirstLegDamage3 = 1052522823
    FireGiantFirstLegDamage4 = 1052522824
    FireGiantFirstLegDamage5 = 1052522825
    FireGiantFirstLegDamage6 = 1052522826
    FireGiantFirstLegDamage7 = 1052522827
    FireGiantFirstLegDamage8 = 1052522828

    FireGiantSecondLegDamage0 = 1052522830
    FireGiantSecondLegDamage1 = 1052522831
    FireGiantSecondLegDamage2 = 1052522832
    FireGiantSecondLegDamage3 = 1052522833
    FireGiantSecondLegDamage4 = 1052522834
    FireGiantSecondLegDamage5 = 1052522835
    FireGiantSecondLegDamage6 = 1052522836
    FireGiantSecondLegDamage7 = 1052522837
    FireGiantSecondLegDamage8 = 1052522838

    CLONE_FireGiantFirstLegDamage0 = 1052522850
    CLONE_FireGiantFirstLegDamage1 = 1052522851
    CLONE_FireGiantFirstLegDamage2 = 1052522852
    CLONE_FireGiantFirstLegDamage3 = 1052522853
    CLONE_FireGiantFirstLegDamage4 = 1052522854
    CLONE_FireGiantFirstLegDamage5 = 1052522855
    CLONE_FireGiantFirstLegDamage6 = 1052522856
    CLONE_FireGiantFirstLegDamage7 = 1052522857
    CLONE_FireGiantFirstLegDamage8 = 1052522858

    CLONE_FireGiantSecondLegDamage0 = 1052522860
    CLONE_FireGiantSecondLegDamage1 = 1052522861
    CLONE_FireGiantSecondLegDamage2 = 1052522862
    CLONE_FireGiantSecondLegDamage3 = 1052522863
    CLONE_FireGiantSecondLegDamage4 = 1052522864
    CLONE_FireGiantSecondLegDamage5 = 1052522865
    CLONE_FireGiantSecondLegDamage6 = 1052522866
    CLONE_FireGiantSecondLegDamage7 = 1052522867
    CLONE_FireGiantSecondLegDamage8 = 1052522868


class NameText(NPCName):
    FireGiant = 904760000
    CLONE_FireGiant = 904760010


class CharacterGroups(Character):
    FireGiantBoss = 1052525800


class Characters(Character):
    FireGiantPhaseOneTwo = 1052520801  # c4760_9000 npc 47600050 think 47600900 group 1052525800
    FireGiantPhaseThree = 1052520800  # c4760_9001 npc 47601050 think 47600900 group 1052525800,1052525100

    CLONE_FireGiantPhaseOneTwo = 1052520803
    CLONE_FireGiantPhaseThree = 1052520802


class Assets(Asset):
    AEG099_019_1000 = 1052521800  # AEG099
