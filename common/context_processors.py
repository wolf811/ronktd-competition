from common.models import Event


def active_event(request):
    active_event = Event.objects.filter(active_now=True).first()
    if active_event:
        return {"glob_event": active_event}
    return ""
