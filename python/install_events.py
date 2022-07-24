from pathlib import Path
from soulstruct.eldenring.events import EMEVD, EMEVDDirectory
from soulstruct.bloodborne.text import MSGDirectory


ELDEN_RING_PATH = Path("C:/Steam/steamapps/common/ELDEN RING (Modding)/Game")

MAPS_TO_INSTALL = [
    "m10_00_00_00",
    "m14_00_00_00",
    "m15_00_00_00",
    "m16_00_00_00",
    "m19_00_00_00",
    "m60_52_38_00",  # Radahn
]


def install():
    # ed = EMEVDDirectory("events")

    for map_name in MAPS_TO_INSTALL:
        emevd = EMEVD(f"events/{map_name}.evs.py")
        emevd.write(ELDEN_RING_PATH / f"event/{map_name}.emevd.dcx")
        emevd.write(ELDEN_RING_PATH / f"OnslaughtMod/event/{map_name}.emevd.dcx")


if __name__ == '__main__':
    install()
