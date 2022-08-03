from rest_framework.permissions import BasePermission

from core.enums import Profile


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return Profile.CUSTOMER.value in user.userprofile.profile


class IsCustomerOrAdmin(BasePermission):
    def has_permission(self, request, view, user=None):
        if not user:
            user = request.user
        return (Profile.CUSTOMER.value in user.userprofile.profile) or user.is_superuser


class IsDealer(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return Profile.DEALER.value in user.userprofile.profile


class IsDealerOrAdmin(BasePermission):
    def has_permission(self, request, view, user=None):
        if not user:
            user = request.user
        return (Profile.DEALER.value in user.userprofile.profile) or user.is_superuser
