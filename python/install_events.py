"""Install selected EMEVD."""

import re
import shutil
from pathlib import Path
from soulstruct.eldenring.events import EMEVD, EMEVDDirectory


def fix_evs_kwargs(evs: str):
    pattern = re.compile(r"CommonFunc_NonRespawningWithReward\((\d+), (\d+), (\d+), (\d+), ([\d.]+), (\d+)\)")
    return pattern.sub(
        r"CommonFunc_NonRespawningWithReward(\1, dead_flag=\2, character=\3, "
        r"item_lot=\4, reward_delay=\5, skip_reward=\6",
        evs,
    )


ELDEN_RING_PATH = Path("C:/Steam/steamapps/common/ELDEN RING (Modding)/Game")

MAPS_TO_INSTALL = [
    "m10_00_00_00",
    "m11_00_00_00",
    "m11_05_00_00",
    "m12_01_00_00",
    "m12_02_00_00",
    "m12_03_00_00",
    "m12_04_00_00",
    "m12_05_00_00",
    "m12_07_00_00",
    "m12_08_00_00",
    "m12_09_00_00",
    "m14_00_00_00",
    "m15_00_00_00",
    "m16_00_00_00",
    "m19_00_00_00",
    "m60_52_38_00",  # Radahn
]


def install_select_maps():

    for map_name in MAPS_TO_INSTALL:
        emevd = EMEVD(f"events/{map_name}.evs.py")
        packed = emevd.pack()
        (ELDEN_RING_PATH / f"event/{map_name}.emevd.dcx").write_bytes(packed)
        (ELDEN_RING_PATH / f"OnslaughtMod/event/{map_name}.emevd.dcx").write_bytes(packed)


def install_all_maps():

    for evs_path in Path("events").glob("*.evs.py"):
        if evs_path.name[:3] in {"m31", "m32", "m34"}:
            # Skip Caves, Tunnels, and Divine Towers.
            continue
        print(evs_path.name)
        emevd = EMEVD(evs_path)
        emevd.write(ELDEN_RING_PATH / f"event/{emevd.map_name}.emevd.dcx")
        shutil.copy2(
            ELDEN_RING_PATH / f"event/{emevd.map_name}.emevd.dcx",
            ELDEN_RING_PATH / f"OnslaughtMod/event/{emevd.map_name}.emevd.dcx"
        )


if __name__ == '__main__':
    install_all_maps()
