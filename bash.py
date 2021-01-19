import argparse
import os
import subprocess
from pathlib import Path
from shutil import copyfile

# i use zsh, hence the name. you may have another profile name, so change here:
BASH_PROFILE = ".zsh_aliases"
HOME = str(Path.home())
PATH = HOME + "/" + BASH_PROFILE

# opens bash file in vim or vscode (defaults to vim)
def open_bash(code=False):
    if code:
        command = "code " + PATH
    else:
        command = "vim " + PATH

    subprocess.call(command, shell=True)

# refreshes the bash profile ensuring user can use newly aliased commands
def refresh():
    command = ". " + PATH
    subprocess.call(command, shell=True)

# saves a backup of your current bash profile to this directory (just in case)
def backup():
    l = sorted(os.listdir(HOME))
    if os.path.exists(PATH):
        copyfile(PATH, BASH_PROFILE)
    else:
        print("ERROR: a bash profile with provided name '" + BASH_PROFILE + "' does not exist")
        print(l)

# reverts bash profile to saved version from earlier
def revert(hard=False):
    if hard:
        copyfile("double_backup/" + BASH_PROFILE, PATH)
    else:
        copyfile(BASH_PROFILE, PATH)

# checks if a provided alias already exists and returns corresponding action
def alias_exists(alias):
    bash = open(PATH, "r")
    alias_name = "alias " + alias + "="

    for line in bash:
        if alias_name in line:
            action = line[len(alias_name)+1:-1]
            # print("found " + line)
            bash.close()
            return action

    bash.close()
    return ""

# prints an alphabetical list of all the active aliases
def list_alias():
    f = open(PATH, "r")
    starter = "alias "
    aliases = []

    for line in f:
        if starter in line:
            action = ""
            index = 6
            while line[index] != "=":
                action = action + line[index]
                index+=1
            
            aliases.append(action)

    f.close()
    
    print(sorted(aliases))

# removes a provided alias from bash profile
def rm_alias(alias):
    exists = alias_exists(alias)

    if exists == "":
        print("alias " + alias + " does not exists!")
    else:
        f = open(PATH, "r")
        lines = f.readlines()
        f.close()

        f = open(".tmp_bash", "w")
        target = "alias " + alias +  "="
        for line in lines:
            if target in line:
                print("removed alias " + alias)
            else:
                f.write(line)

        f.close()

        os.rename(".tmp_bash", PATH)

# adds a provided alias to bash profile
def add_alias(alias, action):
    exists = alias_exists(alias).strip("'")

    if exists == action:
        print("alias " + alias + " with identical action already exists!")
        return
    elif exists != "":
        val = input("alias " + alias + " already mapped to '" + exists + "', do you want to replace it? [y/n] ")

        count = 0
        while count < 3:
            if val == "y" or val == "n" or val == "Y" or val == "N" or val == "yes" or val == "no" or val == "Yes" or val == "No" or val == "YES" or val == "NO":
                if val == "y" or val == "Y" or val == "yes" or val == "Yes" or val == "YES":
                    rm_alias(alias)
                    break
                else:
                    return
    
            val = input("invalid response '" + val + "', do you want to replace it? [y/n] ")
            count += 1

        if count == 3:
            print("received invalid responses 3 times, aborting now and defaulting to 'no'")
            return

    # append the alias to the end of the bash profile
    new_alias = "alias " + alias + "=" + "'" + action + "'"
    f = open(PATH, "a")
    f.write(new_alias + "\n")
    f.close()
    print("added new " + new_alias)



if not os.path.exists(BASH_PROFILE):
    backup()