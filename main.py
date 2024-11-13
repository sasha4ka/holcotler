from threading import Thread
from time import sleep
from config import ACTIVATE
import datetime


def run_screammer():
    print("hello")


def match_time(time: datetime.time, template: str):
    h, m, s = time.hour, time.minute, time.second
    template = template.split(':')

    if template[0] != '*' and template[0] != str(h): return False
    if len(template) >= 2 and template[1] != '*' and template[1] != str(m): return False
    if len(template) >= 3 and template[2] != '*' and template[2] != str(s): return False

    return True


def scream():
    while True:
        time = datetime.datetime.today().time()

        if match_time(time, "0:0"):
            for i in range(len(ACTIVATE)):
                ACTIVATE[i][1] = False

        for i in range(len(ACTIVATE)):
            if ACTIVATE[i][1]: continue
            if not match_time(time, ACTIVATE[i][0]): continue
            ACTIVATE[i][1] = True

            run_screammer()


def taskmgr_kill():
    while True:
        print(0.5)
        sleep(0.5)


def main():
    # Thread(target=taskmgr_kill).start()
    # scream()
    scream()


if __name__ == "__main__":
    main()