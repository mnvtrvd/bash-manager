# bash-manager
Easily create, delete, list, and define aliases in your bash profile.
Also allows you to backup and revert to various bash profiles.

## Background:

This was designed using Python3 and works on MacOS BigSur.
(I believe it works on other OSs as well, but I haven't tested it yet)

## Build/Run:

All of the libraries are native so you won't have to install any new modules

There isn't much to do in order to get this up and running.

Simply run `python setup.py` and enter the name of your bash profile.
(Special thanks to Joe Michelini for helping create the setup.py)

Also, I recommend adding some (or all) of these aliases to you bash
profile to make it easier to edit your bash profile from anywhere.

Run to automatically add them all:
`python3 ~/bash-manager/bash.py --default`

```bash
$ alias ahelp='python3 ~/bash-manager/bash.py --help' # opens bash manager helper
$ alias aopen='python3 ~/bash-manager/bash.py --open' # open bash profile
$ alias abu='python3 ~/bash-manager/bash.py --backup' # backup bash profile
$ alias arv='python3 ~/bash-manager/bash.py --revert' # revert to old bash profile
$ alias arf='python3 ~/bash-manager/bash.py --refresh' # refresh bash profile (allows you to use new aliases)
$ alias als='python3 ~/bash-manager/bash.py --list' # lists aliases in bash profile
$ alias aadd='python3 ~/bash-manager/bash.py --add' # adds new alias to bash profile
$ alias arm='python3 ~/bash-manager/bash.py --rm' # removes provided alias from bash profile
$ alias adef='python3 ~/bash-manager/bash.py --whatami' # defines alias in bash profile
```

## Usage:

https://asciinema.org/a/R73YpiXi77JbcdbrRqrQrocPE
[![asciicast](https://asciinema.org/a/R73YpiXi77JbcdbrRqrQrocPE.svg)](https://asciinema.org/a/R73YpiXi77JbcdbrRqrQrocPE)