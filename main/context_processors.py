"""module docstring"""
from django.conf import settings
from django.middleware.csrf import get_token
from django.utils.functional import SimpleLazyObject

from main.models import Profile

# from ndtadmin.models import AccreditedCenter
# from users.services import get_user_menu

# from django.template import Context, Template
# from django.shortcuts import redirect
# from django.http import HttpResponseForbidden


def get_media_url(request):
    return {"MEDIA_URL": settings.MEDIA_URL}


def csrf(request):
    """
    Context processor that provides a CSRF token, or the string 'NOTPROVIDED' if
    it has not been provided by either a view decorator or the middleware
    """

    def _get_val():
        token = get_token(request)
        if token is None:
            # In order to be able to provide debugging info in the
            # case of misconfiguration, we use a sentinel value
            # instead of returning an empty dict.
            return "NOTPROVIDED"
        else:
            return token

    return {"csrf_token": SimpleLazyObject(_get_val)}


def profile(request):
    profile = Profile.objects.first()
    if profile:
        return {"profile": profile}
    return {"profile": None}


"""
def render_user_menu(request):
    if request.user.is_authenticated:
        menu_template_path = get_user_menu(request.user)
        return {"user_menu": menu_template_path}
    else:
        return {"user_menu": "users/menus/not_authorized.html"}
"""


"""
def center_short_code(request):
    # import pdb; pdb.set_trace()
    user = request.user
    if not user.is_anonymous:
        center = AccreditedCenter.objects.filter(user=request.user).first()
        if center:
            return {"center_short_code": center.short_code}
        return {"center_short_code": "ЭДО СНК ОПО РОНКТД"}
    return ""
"""


"""
def user_groups(request):
    groups = {
        "examen_db_editors": []
    }
    return groups
"""
