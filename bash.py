import argparse
import os
import subprocess
from pathlib import Path
from shutil import copyfile

# i use zsh, hence the name. you may have another profile name, so change here:
BASH_PROFILE = ".zsh_aliases"
HOME = str(Path.home())
PATH = HOME + "/" + BASH_PROFILE
BACKUP_PATH = HOME + "/bash-manager/" + BASH_PROFILE

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
    if os.path.exists(PATH):
        copyfile(PATH, BACKUP_PATH)
        print("successfully backed up bash profile")
    else:
        print("ERROR: a bash profile with provided name '" + BASH_PROFILE + "' does not exist")

# reverts bash profile to saved version from earlier
def revert():
    copyfile(BACKUP_PATH, PATH)
    print("successfully reverted back to earlier bash profile")

# checks if a provided alias already exists and returns corresponding action
def alias_exists(alias):
    bash = open(PATH, "r")
    alias_name = "alias " + alias + "="

    for line in bash:
        if alias_name in line:
            action = line.strip("\n")[len(alias_name)+1:-1]
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
    print(alias)
    exists = alias_exists(alias)

    if exists == "":
        print("alias " + alias + " does not exist!")
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
    print(alias)
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

if not os.path.exists(BACKUP_PATH):
    print("no backup detected, taking one now just in case")
    backup()

parser = argparse.ArgumentParser(description='Modifies your existing bash profile and allows for quick alias management.')
parser.add_argument('--open', nargs='?', type=int, const=1, default=0, help='this opens your bash profile in vim.')
parser.add_argument('--backup', nargs='?', type=bool, const=True, default=False, help='this creates a backup of your current bash profile just in case something goes wrong later.')
parser.add_argument('--revert', nargs='?', type=bool, const=True, default=False, help='this reverts your bash profile back to a previously working state.')
parser.add_argument('--refresh', nargs='?', type=bool, const=True, default=False, help='this refreshes your bash profile.')
parser.add_argument('--list', nargs='?', type=bool, const=True, default=False, help='this will list all of the aliases in your bash profile.')
parser.add_argument('--add', nargs=2, type=str, default=["",""], help='this will add given alias and action to your bash profile.')
parser.add_argument('--rm', type=str, default="", help='this will remove the given alias from your bash profile.')
parser.add_argument('--whatami', type=str, default="", help='this will define a provided alias.')
args = parser.parse_args()

OPEN = args.open
BACKUP = args.backup
REVERT = args.revert
REFRESH = args.refresh
LIST = args.list
ADD_ALIAS = args.add[0]
ADD_ACTION = args.add[1]
RM = args.rm
WHATAMI = args.whatami

count = 0

if OPEN > 0: count += 1
if BACKUP: count += 1
if REVERT: count += 1
if REFRESH: count += 1
if LIST: count += 1
if ADD_ALIAS != "" or ADD_ACTION != "": count += 1
if RM != "": count += 1
if WHATAMI != "": count += 1

if count == 0:
    print("you need to provide at least 1 command to work (use -h or --help for assistance)")
elif count > 1:
    print("ERROR: please execute exactly one command at a time")
elif OPEN > 0:
    if OPEN == 1:
        open_bash()
    else:
        open_bash(True)
elif BACKUP:
    backup()
elif REVERT:
    revert()
    refresh()
elif REFRESH:
    refresh()
elif LIST:
    list_alias()
elif ADD_ALIAS != "" or ADD_ACTION != "":
    add_alias(ADD_ALIAS, ADD_ACTION)
elif RM != "":
    rm_alias(RM)
elif WHATAMI != "":
    action = alias_exists(WHATAMI)
    if action == "":
        print("ERROR: provided alias does not exist")
    else:
        print(action)