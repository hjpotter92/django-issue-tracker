from django.core.exceptions import ObjectDoesNotExist

from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Membership, Project


class IsProjectMember(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        project_id = int(request.data.get('project'))
        try:
            membership = Membership.objects.filter(
                project=project_id, user=request.user)
        except ObjectDoesNotExist:
            return False
        return membership.exists()


class IsProjectOwner(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if view.action in ('list',):
            return True
        project_id = int(request.data.get('project', 0))
        try:
            project = Project.objects.filter(pk=project_id).first()
        except ObjectDoesNotExist:
            return False
        return project.creator == request.user if project else False
