from soulstruct.eldenring.game_types import *


class Flags(Flag):
    GodrickDead = 10000800
    MargitDead = 10000850  # also his entity ID


class Characters(Character):
    Godrick = 10000800
    GodrickClone = 10000801
    Margit = 10000850  # also his death flag
    MargitClone = 10000851
