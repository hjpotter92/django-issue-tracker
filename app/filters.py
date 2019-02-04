from django_filters import rest_framework as filters

from app.models import (Project, Comment, Issue)


class ProjectFilter(filters.FilterSet):
    class Meta:
        model = Project
        fields = ('creator', 'deleted')


class CommentFilter(filters.FilterSet):
    class Meta:
        model = Comment
        fields = ('id', 'issue', 'creator', 'deleted')


class IssueFilter(filters.FilterSet):
    class Meta:
        model = Issue
        fields = (
            'id', 'assignee', 'creator', 'created', 'status', 'priority', 'project')
