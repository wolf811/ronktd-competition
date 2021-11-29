from django.shortcuts import render

from seminar.models import Seminar, STheme


# Create your views here.
def index(request):
    title = "Семинар"
    seminar = Seminar.objects.filter(publish_on_main_page=True).first()
    banners = None
    descriptions = None
    themes = None
    speakers = None
    if seminar:
        banners = seminar.banners.select_related().order_by("number")
        descriptions = seminar.descriptions.select_related().order_by("number")
        speakers = seminar.speakers.select_related().order_by("number")
        themes = STheme.objects.filter(speaker__in=speakers).order_by("number")
        # __import__("pdb").set_trace()
    content = {
        "title": title,
        "seminar": seminar,
        "banners": banners,
        "descriptions": descriptions,
        "themes": themes,
        "speakers": speakers,
    }
    return render(request, "seminar/index.html", content)
