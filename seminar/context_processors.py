# from django.conf import settings_deploy_variables

from seminar.models import Seminar


def active_seminar(request):
    seminar = Seminar.objects.filter(publish_on_main_page=True)
    # __import__("pdb").set_trace()
    if seminar.exists():
        return {
            "glob_seminar": seminar.first(),
        }
    return {"glob_seminar": None}
