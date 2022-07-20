from soulstruct.eldenring.game_types import *


class Flags(Flag):
    RennalaDefeated = 14000800  # also entity ID of Phase 2
    RedWolfDead = 14000850


class CharacterGroups(Character):
    Rennala = 14005800
    Sweetlings = 14005810


class Characters(Character):
    RennalaNPC1 = 14000700  # maybe NPC
    RennalaNPC2 = 14000701  # off to the side, same talk ID
    Sellen1 = 14000710
    Sellen2 = 14000712
    Sellen3 = 14000713
    UnknownNPC1 = 14000715  # in Rennala fight
    UnknownNPC2 = 14000716  # in Rennala fight
    UnknownNPCSummon = 14000717  # in Rennala fight (summon version of above)
    NakedManNPC = 14000720  # in Rennala fight
    RennalaBossPhase2 = 14000800  # far below map
    RennalaBossPhase1 = 14000801  # in library
    RennalaBossPhase2Clone = 14000802  # far below map
    RennalaBossPhase1Clone = 14000803  # in library

    Sweetling1 = 14000810
    Sweetling2 = 14000811
    Sweetling3 = 14000812
    Sweetling4 = 14000813
    Sweetling5 = 14000814
    Sweetling6 = 14000815
    Sweetling7 = 14000816
    Sweetling8 = 14000817
    Sweetling9 = 14000818
    Sweetling10 = 14000819
    Sweetling11 = 14000820
    Sweetling12 = 14000821
    Sweetling13 = 14000822
    Sweetling14 = 14000823
    Sweetling15 = 14000824
    Sweetling16 = 14000825
    Sweetling17 = 14000826
    Sweetling18 = 14000827
    Sweetling19 = 14000828
    Sweetling20 = 14000829
    Sweetling21 = 14000830  # NOTE: was 140008230 (typo)
    Sweetling22 = 14000831
    Sweetling23 = 14000832
    Sweetling24 = 14000833

    RennalaBloodhoundSummon = 14000840
    RennalaWolfSummon1 = 14000841
    RennalaWolfSummon2 = 14000842
    RennalaWolfSummon3 = 14000843
    RennalaWolfSummon4 = 14000844
    RennalaTrollSummon = 14000845
    RennalaDragonSummon = 14000846

    # NOTE: Rennala clone currently cannot summon.
    # RennalaBloodhoundSummonClone = 14000834
    # RennalaWolfSummon1Clone = 14000835
    # RennalaWolfSummon2Clone = 14000836
    # RennalaWolfSummon3Clone = 14000837
    # RennalaWolfSummon4Clone = 14000838
    # RennalaTrollSummonClone = 14000839
    # RennalaDragonSummonClone = 14000847

    RedWolfOfRadagon = 14000850
    RedWolfOfRadagonClone = 14000851

    NewRennalaGrace = 14000954
