from django.db import models

from .user import CustomUser
from .project import Project
from .status import Status
from .priority import Priority


class IssueQuerySet(models.QuerySet):
    def active(self):
        return self.filter(deleted=False)


class Issue(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                related_name='creator_id')
    assignee = models.ForeignKey(CustomUser, default=None, null=True,
                                 on_delete=models.SET_NULL,
                                 related_name='assignee_id')
    status = models.ForeignKey(Status, null=True,
                               on_delete=models.SET_NULL)
    priority = models.ForeignKey(Priority, null=True,
                                 on_delete=models.SET_NULL)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = IssueQuerySet.as_manager()

    class Meta:
        verbose_name = "Issue"
        verbose_name_plural = "Issues"
        ordering = ("priority__order", "-created",)
