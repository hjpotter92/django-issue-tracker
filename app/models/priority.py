from django.db import models


class Priority(models.Model):
    name = models.CharField(max_length=32, unique=True)
    order = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Issue Priority"
        verbose_name_plural = "Issue Priorities"

    def __str__(self):
        return self.name
