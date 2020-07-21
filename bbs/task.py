from celery import Celery
from flask_mail import Message
# from bbs import app
from exts import mail
from flask import Flask
import config


app = Flask(__name__)
mail.init_app(app)


def make_celery(app):
    celery = Celery(
        app.import_name,
        # backend=app.config['CELERY_RESULT_BACKEND'],
        # broker=app.config['CELERY_BROKER_URL']
        backend=config.CELERY_RESULT_BACKEND,
        broker=config.CELERY_BROKER_URL
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery = make_celery(app)


@celery.task
def celery_send_mail(subject,recipients,body):
    message = Message(subject=subject, recipients=recipients,body=body)
    mail.send(message)