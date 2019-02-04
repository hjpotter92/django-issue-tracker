from django.db import models

from .user import CustomUser


class Status(models.Model):
    name = models.CharField(max_length=32, unique=True)
    locked = models.BooleanField(default=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tracker Status"
        verbose_name_plural = "Tracker Statuses"

    def __str__(self):
        return self.name
