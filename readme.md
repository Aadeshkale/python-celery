This is simple example to demostrate the use of celery framework
----------------------------------------------------------------


celery :-

Task queues are used as a mechanism to distribute work across threads or machines.
A task queue’s input is a unit of work called a task. Dedicated worker processes constantly monitor task queues for new work to perform. 


requrinment :-

Celery requires a message transport to send and receive messages. The RabbitMQ and Redis broker transports are feature complete, but there’s also support for a myriad of other experimental solutions, including using SQLite for local development.

-------------------------------------------------------------------


commands :-

celery -A tasks worker --loglevel=info

-------------------------------------------------------------------

reference :- 

https://docs.celeryproject.org/en/stable/getting-started/introduction.html


https://www.youtube.com/watch?v=fg-JfZBetpM

