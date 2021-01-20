import json
from pathlib import Path
import os
import shutil

def setup():
    b_profile = input("Please enter filename of bash profile: ").strip()
    settings = {"BASH_PROFILE": b_profile}
    with open("config.json", "w+") as config:
        json.dump(settings, config)
    
    HOME = str(Path.home())
    CUR_DIR = os.getcwd()
    if CUR_DIR != HOME + '/bash-manager':
        shutil.move(CUR_DIR, HOME)
        print("\nbash-manager has been moved to ~/bash-manager\n")
        print("""to enable default behavior, please execute: 
                    $ python3 ~/bash-manager/bash.py --default\n""")
    else:
        print(f"\nbash profile changed to {b_profile}\n")

if __name__ == "__main__":
    setup()