from apscheduler.schedulers.blocking import BlockingScheduler
from whatsappAutoMsgSender import sendMsg

sched = BlockingScheduler()
sched.add_job(sendMsg, 'interval', seconds=2)
sched.start()
