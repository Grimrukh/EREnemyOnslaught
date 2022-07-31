from soulstruct.eldenring.game_types import *


class Flags(Flag):
    PrologueGraftedScionBattleDone = 101
    ButterflyOutcropBroken = 10010500
    DelayedAreaWelcomeMessageDone = 10010502
    GraftedScionDead = 10010800
    GraftedScionFirstTimeDone = 10010801
    GraftedScionInPhaseTwo = 10012802


class Characters(Character):
    FingerMaiden = 10011700  # c0000_9010 col h001000 npc 523380016 think 523380000 chara 23380
    GraftedScion = 10010800  # c4690_9000 col h002200 npc 46900008 think 46900900

    CLONE_GraftedScion = 10010801  # c4690_9000 col h002200 npc 46900008 think 46900900


class Regions(Region):
    GraftedScionPositionAfterFirstTime = 10012810
    CLONE_GraftedScionPositionAfterFirstTime = 10012811


class NameText(NPCName):
    GraftedScion = 904690000
    CLONE_GraftedScion = 904690010


class Assets(Asset):
    AEG099_001_9000 = 10011800  # AEG099
    AEG099_001_9001 = 10011801  # AEG099
    AEG099_630_9000 = 10011600  # AEG099
    AEG099_990_9000 = 10011705  # AEG099
    AEG210_451_0500 = 10011500  # AEG210
    AEG219_000_0500 = 10011560  # AEG219
    AEG219_002_0500 = 10011540  # AEG219
