from rest_framework.permissions import BasePermission, SAFE_METHODS

from core.enums import Profile


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.is_admin


class IsCustomer(BasePermission):
    def has_permission(self, request, view, user=None):
        if not user:
            user = request.user
        return Profile.CUSTOMER.value in user.userprofile.profile


class IsCustomerOrAdmin(BasePermission):
    def has_permission(self, request, view, user=None):
        if not user:
            user = request.user
        return (Profile.CUSTOMER.value in user.userprofile.profile) or user.is_superuser


class IsDealer(BasePermission):
    def has_permission(self, request, view, user=None):
        if not user:
            user = request.user
        return Profile.DEALER.value in user.userprofile.profile


class IsDealerOrAdmin(BasePermission):
    def has_permission(self, request, view, user=None):
        if not user:
            user = request.user
        return (Profile.DEALER.value in user.userprofile.profile) or user.is_superuser
