import psutil
import sys

for proc in psutil.process_iter():
    try:
        if proc.name() == "Taskmgr.exe": # If process detected.
            proc.kill()
            print("Task Manager process closed.")
            sys.exit()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

print("Task Manager not detected.") # If process not detected.