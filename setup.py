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
    print("\nbash-manager has been moved to ~/bash-manager\n")
    print("""to enable default behavior, please execute: 
                $ python3 ~/bash-manager/bash.py --default\n""")
if __name__ == "__main__":
    setup()
    os.chdir(str(Path.home()) + "/bash-manager")