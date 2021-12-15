from django.core.mail import send_mail
from django.forms.models import model_to_dict
from django.http.response import (HttpResponse, HttpResponseForbidden,
                                  JsonResponse)
from django.shortcuts import render

from seminar.forms import SParticipantForm
from seminar.models import (SDocument, Seminar, SParticipant, SPartner,
                            SPromoCode, SSubscriber, STheme)


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
    seminar_partners = None
    if seminar:
        banners = seminar.banners.select_related().order_by("number")
        descriptions = seminar.descriptions.select_related().order_by("number")
        speakers = seminar.speakers.select_related().order_by("number")
        themes = STheme.objects.filter(speaker__in=speakers).order_by("number")
        theme_documents = SDocument.objects.filter(theme__in=themes)
        seminar_documents = SDocument.objects.filter(seminar=seminar)
        seminar_partners = SPartner.objects.filter(
            seminar=seminar, super_status=True
        ).order_by("number")
    content = {
        "title": title,
        "seminar": seminar,
        "banners": banners,
        "partners": seminar_partners,
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
            form_promo_code = form.cleaned_data["promocode"]
            instance = form.save()
            promocode = SPromoCode.objects.filter(
                code=form_promo_code,
            ).first()
            # __import__("pdb").set_trace()
            registration_info = model_to_dict(instance)
            registration_info["phone"] = f"{instance.phone}"
            if promocode:
                partner = promocode.promo_partner
                promocode.participant = instance
                promocode.activate()
                registration_info.update(
                    {
                        "promocode": promocode.code,
                    }
                )
                partner.count_promocodes()
            if instance.subscribe_accepted:
                SSubscriber.objects.create(
                    seminar=seminar, fio=instance.fio, email=instance.email
                )
            if request.POST.get("nksystem") or request.POST.get("question"):
                instance.json_data = {
                    "nksystem": request.POST.get("nksystem"),
                    "question": request.POST.get("question"),
                }
                # __import__("ipdb").set_trace()
                instance.save()
            # send email with confirmation
            send_mail(
                "Успешная регистрация: {}!".format(seminar.title),
                f"""Ваша регистрация подтверждена:
{seminar.sub_title} {seminar.title}
Email: {registration_info['email']},
ФИО участника: {registration_info['fio']},
Телефон участника: {registration_info['phone']},
Спасибо за регистрацию!
    """,
                "noreply@naks.ru",
                [instance.email],
                fail_silently=False,
            )
            return JsonResponse({"success": registration_info})
        return JsonResponse({"errors": form.errors})
