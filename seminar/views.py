from django.http.response import (HttpResponse, HttpResponseForbidden,
                                  JsonResponse)
from django.shortcuts import render

from seminar.forms import SParticipantForm
from seminar.models import (SDocument, Seminar, SParticipant, SPromoCode,
                            SSubscriber, STheme)


# Create your views here.
def index(request):
    title = "Семинар"
    seminar = Seminar.objects.filter(publish_on_main_page=True).first()
    form = SParticipantForm()
    banners = None
    descriptions = None
    themes = None
    speakers = None
    theme_documents = None
    seminar_documents = None
    if seminar:
        banners = seminar.banners.select_related().order_by("number")
        descriptions = seminar.descriptions.select_related().order_by("number")
        speakers = seminar.speakers.select_related().order_by("number")
        themes = STheme.objects.filter(speaker__in=speakers).order_by("number")
        theme_documents = SDocument.objects.filter(theme__in=themes)
        seminar_documents = SDocument.objects.filter(seminar=seminar)
    content = {
        "title": title,
        "seminar": seminar,
        "banners": banners,
        "descriptions": descriptions,
        "themes": themes,
        "speakers": speakers,
        "theme_documents": theme_documents,
        "seminar_documents": seminar_documents,
        "form": form,
    }
    return render(request, "seminar/index.html", content)


def create_participant(data):
    participant = SParticipant.objects.create(
        fio=data["fio"],
        phone=data["phone"],
        email=data["email"],
        org=data["org"],
        city=data["city"],
        pdn_accepted=True,
        subscribe_accepted=data["subscribe_accepted"],
    )
    return participant


def send_confirmation_email(email_addr, data):
    pass


def register_participant(request):
    if request.method == "POST":
        seminar = Seminar.objects.filter(publish_on_main_page=True).first()
        form = SParticipantForm(request.POST)
        if form.is_valid():
            print("form is valid", form.cleaned_data)
            prcode = form.cleaned_data["promocode"]
            instance = form.save()
            promocode = SPromoCode.objects.filter(
                code=prcode,
                seminar=seminar,
                participant=instance,
            ).first()
            promocode.activate()
            if instance.subscribe_accepted:
                SSubscriber.objects.create(
                    seminar=seminar, fio=instance.fio, email=instance.email
                )
            # send email with confirmation
            return JsonResponse({"success": "all is ok!"})
        return JsonResponse({"errors": form.errors})
