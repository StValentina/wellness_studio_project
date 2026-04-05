from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class HostOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return (
            self.request.user.is_authenticated
            and self.request.user.profile.role == 'Host'
        )

    def handle_no_permission(self):
        raise PermissionDenied("Only hosts are allowed to perform this action.")