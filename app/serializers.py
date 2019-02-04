from rest_framework import serializers
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly)
from app.models import (Comment, Issue, Project, CustomUser, Membership)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'name')


class CommentSerializer(serializers.ModelSerializer):
    permission_classes = (IsAuthenticated,)

    class Meta:
        model = Comment
        fields = ('id', 'body', 'creator', 'created')


class IssueListSerializer(serializers.ModelSerializer):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    comments = CommentSerializer(source='comment_set',
                                 many=True, read_only=True)
    created_by = UserSerializer(source='creator')
    assigned_to = UserSerializer(source='assignee')

    class Meta:
        model = Issue
        fields = ('__all__')


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ('__all__')


class IssueSerializer(serializers.ModelSerializer):
    permission_classes = (IsAuthenticated,)

    class Meta:
        model = Issue
        fields = ('title', 'body', 'project', 'assignee', 'status', 'priority')


class ProjectSerializer(serializers.ModelSerializer):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description')
