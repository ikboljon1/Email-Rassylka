from __future__ import absolute_import 
from celery import Celery 
from datetime import timedelta

celery = Celery('tasks', broker="amqp://guest@localhost//") 
celery.conf.update( 
 CELERYBEAT_SCHEDULE={ 
  'add-every-couple-seconds': { 
   'task': 'send_mail', 
   'schedule': timedelta(seconds=30), 
  }, 
 }
) 

@celery.task
def send_mail(): 
 from emailapp.models import Subscriber, Template 
 subscribers = Subscriber.objects.all() 
 templates = Template.objects.all() 

 for subscriber in subscribers: 
  template = templates.get(name="default_template") 
  message = template.html.format( 
   name=subscriber.name, email=subscriber.email, 
   birthdate=subscriber.birthdate
  ) 
  # Ваш код отправки сообщения 
  sbj = "Рассылка по %s" % subscriber.name
  send_mail("info@yourdomain.com", [subscriber.email], sbj, message)