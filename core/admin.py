from django.contrib import admin
from core.models import Evento

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'date_creation')
    list_filter = ('title', 'date', 'user_name',)

admin.site.register(Evento, EventAdmin)
