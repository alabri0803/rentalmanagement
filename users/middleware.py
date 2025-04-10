from datetime import datetime

from django.utils.deprecation import MiddlewareMixin


class UpdateLastActivityMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            request.user.profile.last_seen = datetime.now()
            request.user.profile.save(update_fields=["last_seen"])