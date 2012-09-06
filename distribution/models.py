# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.template import Context, Template
import datetime

class Event(models.Model):
    name_event = models.CharField(max_length=200,verbose_name='Краткое описание события')
    text_mail = models.TextField(verbose_name='Текст письма')

    def anchor(self,eid,uid):
        u = User.objects.get(id=uid)
        e = Event.objects.get(id=eid)
        mail = Template(e.text_mail).render(Context({'user': u.username}))
        '''
        отправка письма
        '''
        o = Occurred(id_event=e,id_user=u,time_event=datetime.datetime.now())
        o.save()
        return mail
        
    def __unicode__(self):
        return u'%s' % (self.name_event)
        
class Occurred(models.Model):
    id_event = models.ForeignKey(Event)
    id_user = models.ForeignKey(User)
    time_event = models.DateTimeField()



