"""Install selected EMEVD."""

import shutil
from pathlib import Path
from soulstruct.eldenring.events import EMEVD


ELDEN_RING_PATH = Path("C:/Steam/steamapps/common/ELDEN RING (Modding) (1.06)/Game")
MOD_EVENT_PATH = ELDEN_RING_PATH / "OnslaughtMod/event"


FILTER_EVS = [
    "m19_00_00_00",
]


def install_events():

    MOD_EVENT_PATH.mkdir(exist_ok=True, parents=True)

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
    install_events()
