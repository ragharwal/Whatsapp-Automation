from apscheduler.schedulers.blocking import BlockingScheduler
from whatsappAutoMsgSender import sendMsg

sched = BlockingScheduler()
sched.add_job(sendMsg, 'interval', seconds=1800)
sched.start()
