import json
from pathlib import Path
import os
import shutil

def setup():
    b_profile = input("Please enter filename of bash profile: ").strip()
    settings = {"BASH_PROFILE": b_profile}
    with open("config.json", "w+") as config:
        json.dump(settings, config)
    shutil.move(os.getcwd(), str(Path.home()))

if __name__ == "__main__":
    setup()