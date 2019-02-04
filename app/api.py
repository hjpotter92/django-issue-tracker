from rest_framework import routers

from app.views import (
    UserViewSet, IssueViewSet,
    ProjectViewSet, CommentViewSet,
    IssueListViewSet, MembershipViewSet)

router = routers.DefaultRouter()

for path, view in (
        ('issue', IssueViewSet),
        ('issues', IssueListViewSet),
        ('user', UserViewSet),
        ('project', ProjectViewSet),
        ('comment', CommentViewSet),
        ('membership', MembershipViewSet)):
    router.register(path, view)
