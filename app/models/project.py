from django.db import models

from .user import CustomUser


class ProjectQuerySet(models.QuerySet):
    def active(self):
        return self.filter(deleted=False)


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    members = models.ManyToManyField(
        CustomUser, through='Membership', related_name='projects')
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProjectQuerySet.as_manager()

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ("name",)

    def __str__(self):
        return self.name
