from celery import Celery

app = Celery('tasks',broker='amqp://localhost/')


@app.task
def revers(string):
    return string[::-1]

revers.delay('kunal')