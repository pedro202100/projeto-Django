from django.contrib import admin
from core.models import Evento
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','dataEvemto','dataCriacao')
    list_filter = ('titulo','dataEvemto')
admin.site.register(Evento, EventoAdmin)
