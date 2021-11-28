from django.shortcuts import render

from seminar.models import Seminar


# Create your views here.
def index(request):
    title = "Семинар"
    seminar = Seminar.objects.filter(publish_on_main_page=True).first()
    banners = seminar.banners.select_related()
    descriptions = seminar.descriptions.select_related().order_by("number")
    content = {
        "title": title,
        "seminar": seminar,
        "banners": banners,
        "descriptions": descriptions,
    }
    return render(request, "seminar/index.html", content)
