import re
from pathlib import Path


BOSS_DEATH_EVENT_RE = re.compile(r"^def Event_(\d\d\d\d28[05]0)\(\):$")
BOSS_HEALTH_VALUE_RE = re.compile(r"^ {4}MAIN.Await\(HealthValue\(Characters\.(.*)\) <= 0\)$")
BOSS_DEAD_RE = re.compile(r"^ {4}MAIN.Await\(CharacterDead\(Characters\.(.*)\)\)$")

FULL_BOSS_EVENT_RE = re.compile(
    r"def Event_(?P<event_id>\d\d\d\d28[05]0)\(\):\n"
    r"(?P<gap1>.*?)\n"
    r" {4}MAIN\.Await\(HealthValue\(Characters\.(?P<chr_health>.*?)\) <= 0\)\n"
    r"(?P<gap2>.*?)\n"
    r" {4}MAIN\.Await\(CharacterDead\(Characters\.(?P<chr_dead>.*?)\)\)\n"
    r"(?P<gap3>.*?)\n"
    r"\n\n",
    re.DOTALL,
)


FULL_BOSS_EVENT_REPL = (
    "def Event_{event_id}():\n"
    "{gap1}\n"
    "    AND_7.Add(HealthValue(Characters.{chr_health}) <= 0)\n"
    "    AND_7.Add(HealthValue(Characters.CLONE_{chr_health}) <= 0)\n"
    "    MAIN.Await(AND_7)\n"
    "{gap2}\n"
    "    AND_8.Add(CharacterDead(Characters.{chr_dead}))\n"
    "    AND_8.Add(CharacterDead(Characters.CLONE_{chr_dead}))\n"
    "    MAIN.Await(AND_8)\n"
    "{gap3}\n"
    "\n\n"
)


def main():
    for generic_evs_path in Path("events").glob("m3*.evs.py"):
        if generic_evs_path.name[2] not in "012" or "mod" in generic_evs_path.name:
            continue  # only m30, m31, m32

        new_evs = evs = generic_evs_path.read_text()

        print(generic_evs_path.name)

        for match in FULL_BOSS_EVENT_RE.finditer(evs):
            print(match.group(0))
            match_dict = match.groupdict()
            if match_dict["chr_health"] != match_dict["chr_dead"]:
                raise ValueError(f"Health check character does not match dead check character.")
            repl = FULL_BOSS_EVENT_REPL.format(**match_dict)
            print("-->")
            print(repl)
            new_evs = new_evs.replace(match.group(0), repl)

        # Path(str(generic_evs_path).replace(".evs.py", "_mod.evs.py")).write_text(new_evs)
        generic_evs_path.write_text(new_evs)

        # for i, line in enumerate(evs.splitlines()):
        #     if BOSS_DEATH_EVENT_RE.match(line):
        #         print(f"    {i}:   {line}")
        #     elif BOSS_HEALTH_VALUE_RE.match(line):
        #         print(f"    {i}:   {line}")
        #     elif BOSS_DEAD_RE.match(line):
        #         print(f"    {i}:   {line}")


if __name__ == '__main__':
    main()
