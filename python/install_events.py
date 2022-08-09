"""Install selected EMEVD."""

import re
import shutil
from pathlib import Path
from soulstruct.eldenring.events import EMEVD


def fix_evs_kwargs(evs: str):
    pattern = re.compile(r"CommonFunc_NonRespawningWithReward\((\d+), (\d+), (\d+), (\d+), ([\d.]+), (\d+)\)")
    return pattern.sub(
        r"CommonFunc_NonRespawningWithReward(\1, dead_flag=\2, character=\3, "
        r"item_lot=\4, reward_delay=\5, skip_reward=\6",
        evs,
    )


ELDEN_RING_PATH = Path("C:/Steam/steamapps/common/ELDEN RING (Modding)/Game")


FILTER_EVS = [
    "m12_02_00_00",
    "m12_03_00_00",
    "m13_00_00_00",
    "m32_11_00_00",
    "m60_39_54_00",
    "m60_48_51_00",
    "m60_51_36_00",
]


def install_all_maps():

    common_func = EMEVD("events/common_func.py")
    common_func.write(ELDEN_RING_PATH / "event/common_func.emevd.dcx")
    shutil.copy2(
        ELDEN_RING_PATH / f"event/common_func.emevd.dcx",
        ELDEN_RING_PATH / f"OnslaughtMod/event/common_func.emevd.dcx"
    )
    print("common_func.py")

    for evs_path in Path("events").glob("*.evs.py"):
        if FILTER_EVS and evs_path.name.split(".")[0] not in FILTER_EVS:
            continue
        if evs_path.name.startswith("m31_22_00_00"):
            continue  # Spiritcaller Cave not done
        print(evs_path.name)
        emevd = EMEVD(evs_path)
        emevd.write(ELDEN_RING_PATH / f"event/{emevd.map_name}.emevd.dcx")
        shutil.copy2(
            ELDEN_RING_PATH / f"event/{emevd.map_name}.emevd.dcx",
            ELDEN_RING_PATH / f"OnslaughtMod/event/{emevd.map_name}.emevd.dcx"
        )


if __name__ == '__main__':
    # install_select_maps()
    install_all_maps()
