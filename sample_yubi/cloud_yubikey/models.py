from django.db import models
from django.contrib.auth.models import User


class UserYubi(models.Model):
    user = models.ForeignKey(User)
    device_id = models.CharField(max_length=12)

    class Meta:
        verbose_name = 'YubiKey User'
        verbose_name_plural = 'YubiKey Users'
