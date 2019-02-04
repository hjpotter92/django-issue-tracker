from django.db.models import Q

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from app.filters import CommentFilter, IssueFilter, ProjectFilter
from app.models import Comment, Issue, CustomUser, Project, Membership
from app.permissions import IsProjectMember, IsProjectOwner
from app.serializers import (
    CommentSerializer, IssueSerializer,
    ProjectSerializer, UserSerializer,
    IssueListSerializer, MembershipSerializer)

__all__ = ('UserListView', 'IssueViewSet', 'ProjectViewSet', 'CommentViewSet')


class CommentViewSet(viewsets.ModelViewSet):
    """Methods for easing the process regarding issue comment.

    get:
    Fetch issue comment provided a few filters.

    post:
    Create a new issue comment.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.active()
    serializer_class = CommentSerializer
    filterset_class = CommentFilter

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(creator=user)


class IssueViewSet(
        mixins.CreateModelMixin, mixins.UpdateModelMixin,
        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """Methods for create/update issues.

    create:
    Create a new issue.
    """
    permission_classes = (IsAuthenticated, IsProjectMember)
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class IssueListViewSet(
        mixins.ListModelMixin, mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    """Fetching or reading issues.

    list:
    Fetch issues provided a few filters.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Issue.objects.all()
    serializer_class = IssueListSerializer
    filterset_class = IssueFilter


class ProjectViewSet(viewsets.ModelViewSet):
    """Methods for easing the process regarding project.

    get:
    Fetch project provided a few filters.

    post:
    Create a new project.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class MembershipViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsProjectOwner)
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('username', 'email', 'name')

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(id=user.id)
