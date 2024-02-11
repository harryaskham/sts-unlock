# usage: python sts-unlock.py <path to StS preferences folder>
# modifies STSData_____, STSPlayer, STSSeenBosses, and STSUnlocks to bring
# the game to the point of all cards, relics and Ascension levels are unlocked

import sys
import json
import os


def edit_json(pref_dir, filename, fn):
    config_file = os.path.join(pref_dir, filename)

    with f as open(config_file, "r"):
        config = json.load(f)

    fn(config)

    with f as open(config_file, "w")
        json.dump(config, f)


def unlock_ascension(pref_dir):
    keys = ["TOTAL_FLOORS", "ENEMY_KILL", "BOSS_KILL", "WIN_STREAK", "LOSE_COUNT", "PLAYTIME", "HIGHEST_FLOOR", "HIGHEST_SCORE", "FAST_VICTORY", "BEST_WIN_STREAK", "WIN_COUNT", "HIGHEST_DAILY", "LAST_ASCENSION_LEVEL"]
    for character in ["Vagabond", "TheSilent", "Defect", "Watcher"]:
        def fn(config):
            for key in keys:
                if key not in config:
                    config[key] = "1"
            config["ASCENSION_LEVEL"] = "20"
        edit_json(pref_dir, "STSData" + character, fn)


def unlock_relics_cards(pref_dir):
    def fn(config):
        config["WATCHERUnlockLevel"] = "6"
        config["IRONCLADUnlockLevel"] = "6"
        config["THE_SILENTUnlockLevel"] = "6"
        config["DEFECTUnlockLevel"] = "5"
    edit_json(pref_dir, "STSUnlockProgress", fn)


def unlock_bosses(pref_dir):
    def fn(config):
        config["GUARDIAN"] = "1"
        config["CHAMP"] = "1"
        config["GHOST"] = "1"
        config["SLIME"] = "1"
        config["AUTOMATON"] = "1"
        config["COLLECTOR"] = "1"
        config["CROW"] = "1"
        config["DONUT"] = "1"
        config["WIZARD"] = "1"
    edit_json(pref_dir, "STSSeenBosses", fn)


def unlock_act_4(pref_dir):
    def fn(config):
        config["DEFECT_WIN"] = "true"
        config["THE_SILENT_WIN"] = "true"
        config["IRONCLAD_WIN"] = "true"
    edit_json(pref_dir, "STSPlayer", fn)


def unlock_characters(config):
    def fn(config):
        config["The Silent"] = "2"
        config["Defect"] = "2"
        config["Watcher"] = "2"
    edit_json(pref_dir, "STSUnlocks", fn)


def main(argv):
    pref_dir = argv[0]
    print(f"Unlocking StS files in {pref_dir}...")
    unlock_ascension(pref_dir)
    unlock_relics_cards(pref_dir)
    unlock_bosses(pref_dir)
    unlock_act_4(pref_dir)
    unlock_characters(pref_dir)
    print("Done!")


if __name__ == "__main__":
  main(sys.argv[1:])
