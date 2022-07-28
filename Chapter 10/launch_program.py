import subprocess
from apscheduler.schedulers.background import BackgroundScheduler


def open_notepad():
    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

scheduler = BackgroundScheduler()

scheduler.add_job(open_notepad, trigger='cron', minute='*')

scheduler.start()
