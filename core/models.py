from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Evento(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    date = models.DateTimeField(verbose_name='Event Date')
    date_creation = models.DateTimeField(verbose_name='Creation Date', auto_now=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'  # Esta class vai fazer com que o arquivo se chame 'evento', senão o sistema nomeia de acordo um padrão pré-definido

    def __str__(self):
        return self.title
