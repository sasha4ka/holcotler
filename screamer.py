from config import SCREAMERS_DIR
import os

def run():
    path = os.path.join(SCREAMERS_DIR, "1.mp4")
    os.system("start {}".format(path))