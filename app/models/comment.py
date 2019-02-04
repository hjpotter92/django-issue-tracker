from django.db import models

from .user import CustomUser
from .issue import Issue


class CommentQuerySet(models.QuerySet):
    def active(self):
        return self.filter(deleted=False)


class Comment(models.Model):
    body = models.TextField()
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CommentQuerySet.as_manager()

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ("created",)

    def __str__(self):
        return self.body
