from celery import Celery
import time

celery = Celery('task',broker='redis://127.0.0.1:6379/0',backend='redis://127.0.0.1:6379/0')

@celery.task
def send_mail():
    print('邮件发送')
    time.sleep(2)
    print('邮件发送完毕')