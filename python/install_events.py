from pathlib import Path
from soulstruct.eldenring.events import EMEVD, EMEVDDirectory
from soulstruct.bloodborne.text import MSGDirectory


ELDEN_RING_PATH = Path("C:/Steam/steamapps/common/ELDEN RING (Modding)/Game")


def install():
    # ed = EMEVDDirectory("events")

    stormveil = EMEVD("events/m10_00_00_00.evs.py")
    stormveil.write(ELDEN_RING_PATH / "event/m10_00_00_00.emevd.dcx")
    stormveil.write(ELDEN_RING_PATH / "OnslaughtMod/event/m10_00_00_00.emevd.dcx")

    raya_lucaria = EMEVD("events/m14_00_00_00.evs.py")
    raya_lucaria.write(ELDEN_RING_PATH / "event/m14_00_00_00.emevd.dcx")
    raya_lucaria.write(ELDEN_RING_PATH / "OnslaughtMod/event/m14_00_00_00.emevd.dcx")

    haligtree = EMEVD("events/m15_00_00_00.evs.py")
    haligtree.write(ELDEN_RING_PATH / "event/m15_00_00_00.emevd.dcx")
    haligtree.write(ELDEN_RING_PATH / "OnslaughtMod/event/m15_00_00_00.emevd.dcx")

    volcano_manor = EMEVD("events/m16_00_00_00.evs.py")
    volcano_manor.write(ELDEN_RING_PATH / "event/m16_00_00_00.emevd.dcx")
    volcano_manor.write(ELDEN_RING_PATH / "OnslaughtMod/event/m16_00_00_00.emevd.dcx")

    radahn_tile = EMEVD("events/m60_52_38_00.evs.py")
    radahn_tile.write(ELDEN_RING_PATH / "event/m60_52_38_00.emevd.dcx")
    radahn_tile.write(ELDEN_RING_PATH / "OnslaughtMod/event/m60_52_38_00.emevd.dcx")


if __name__ == '__main__':
    install()
