from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
    event_name = models.CharField(max_length=60)
    date = models.DateField(verbose_name='Дата события')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_events')
    event_text = models.TextField()

    def __str__(self):
        return f'{self.event_name} + {self.id}'


