from django.contrib.auth.mixins import LoginRequiredMixin
from django import http
from response_code import RETCODE


class LoginRequiredJSONMixin(LoginRequiredMixin):

    def handle_no_permission(self):
        return http.JsonResponse({'code': RETCODE.SESSIONERR, "errmsg": "用户未登录！"})


"""
def handle_no_permission(self):
    if self.raise_exception or self.request.user.is_authenticated:
        raise PermissionDenied(self.get_permission_denied_message())

    path = self.request.build_absolute_uri()
    resolved_login_url = resolve_url(self.get_login_url())
    # If the login url is the same scheme and net location then use the
    # path as the "next" url.
    login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
    current_scheme, current_netloc = urlparse(path)[:2]
    if (not login_scheme or login_scheme == current_scheme) and (
        not login_netloc or login_netloc == current_netloc
    ):
        path = self.request.get_full_path()
    return redirect_to_login(
        path,
        resolved_login_url,
        self.get_redirect_field_name(),
    )
    
class LoginRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
        
"""
