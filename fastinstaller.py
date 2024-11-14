import os
from config import FILES, DIRS

autorun_path = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")

for path in DIRS:
    os.mkdir(os.path.join(autorun_path, path))

for path in FILES:
    os.system('copy "{0}" "{1}"'.format(path, os.path.join(autorun_path, path)))