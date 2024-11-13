from threading import Thread
from time import sleep

def scream():
    while True:
        print(1)
        sleep(1)

def taskmgr_kill():
    while True:
        print(0.5)
        sleep(0.5)

def main():
    Thread(target=taskmgr_kill).start()
    scream()

if __name__ == "__main__":
    main()