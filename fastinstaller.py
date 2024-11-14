import os
from config import FILES, DIRS, RUN

autorun_path = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")

for path in DIRS:
    if not os.path.exists(path):
        os.mkdir(os.path.join(autorun_path, path))

for path in FILES:
    os.system('copy "{0}" "{1}"'.format(path, os.path.join(autorun_path, path)))

for run in RUN:
    command = '"' + os.path.join(autorun_path, run) + '"'
    os.popen(command)

os.system(command)