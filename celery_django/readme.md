This is simple example to demostrate the use of celery framework with django application
----------------------------------------------------------------------------------------

Configure following files in,project directory

celery.py,

__init__.py 

task.py in django application

---------------------------------------------------------------------------------------

create tasks.py for task queue

import tasks.py in your views to see in action

use delay method with tasks.py methods with parameters


----------------------------------------------------------------------------------------
command :-

start message broker server

celery -A project worker --loglevel=info 


----------------------------------------------------------------------------------------
reference :- 

https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
