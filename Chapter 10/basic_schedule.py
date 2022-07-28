from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()

scheduler.add_job(lambda : print('Automation'),'interval',seconds=5)

scheduler.start()
