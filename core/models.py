from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
# Create your models here.


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True,null=True)
    dataEvemto = models.DateTimeField()
    dataCriacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'
    def __str__(self):
        return self.titulo

    def getDataEvento(self):
        return self.dataEvemto.strftime('%d/%m/%Y %H:%M')


    def getDataInputEvento(self):
        return self.dataEvemto.strftime('%Y-%m-%dT%H:%M')

    def getEventoAtrasado(self):
        if self.dataEvemto < datetime.now():
            return True
        else:
            return False



