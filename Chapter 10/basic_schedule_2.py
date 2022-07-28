from apscheduler.schedulers.background import BackgroundScheduler


def hello_bot():
    print("Hello bot")

scheduler = BackgroundScheduler()

scheduler.add_job(hello_bot, trigger='cron', second='*')

scheduler.start()
