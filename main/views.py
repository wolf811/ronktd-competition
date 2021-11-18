from django.http.response import JsonResponse
from django.shortcuts import render
from publications.models import Banner, Document
from rest_framework.parsers import JSONParser

from main.forms import ParticipantForm
from main.models import Chunk


# Create your views here.
def index(request):
    title = "Главная"
    main_page_banners = Banner.objects.filter(activated=True).order_by("number")
    main_page_chunks = Chunk.objects.filter(
        activated=True,
        publish_on_main_page=True,
    ).order_by("number")
    main_page_documents = Document.objects.filter(publish_on_main_page=True).order_by(
        "number"
    )
    form = ParticipantForm()
    content = {
        "title": title,
        "banners": main_page_banners,
        "chunks": main_page_chunks,
        "documents": main_page_documents,
        "form": form,
    }
    return render(request, "main/index.html", content)


def participant_form(request):
    post_data = {k: v for k, v in JSONParser().parse(request).items()}
    form = ParticipantForm(post_data)
    if form.is_valid():
        print("FORM is valid")
        return JsonResponse({"success": post_data})
    else:
        print("ERRORS", form.errors)
    return JsonResponse({"errors": form.errors})


def news(request):
    title = "Новости"
    content = {
        "title": title,
    }
    return render(request, "main/news.html", content)


def news_detail(request):
    title = "Новости"
    content = {
        "title": title,
    }
    return render(request, "main/news-detail.html", content)


def structure(request):
    title = "Организационная структура"
    content = {
        "title": title,
    }
    return render(request, "main/structure.html", content)


def docs(request):
    title = "Документы"
    content = {
        "title": title,
    }
    return render(request, "main/docs.html", content)


def stages(request):
    title = "Отборочные этапы"
    content = {
        "title": title,
    }
    return render(request, "main/stages.html", content)


def final_stage(request):
    title = "Финальный этап"
    content = {
        "title": title,
    }
    return render(request, "main/final-stage.html", content)


def gallery(request):
    title = "Галерея"
    content = {
        "title": title,
    }
    return render(request, "main/gallery.html", content)


def members(request):
    title = "Участники"
    content = {
        "title": title,
    }
    return render(request, "main/members.html", content)


def member_detail(request):
    title = "Участники"
    content = {
        "title": title,
    }
    return render(request, "main/member-detail.html", content)


def memb_info(request):
    title = "Участникам"
    content = {
        "title": title,
    }
    return render(request, "main/memb-info.html", content)


def organizers(request):
    title = "Организаторы"
    content = {
        "title": title,
    }
    return render(request, "main/organizers.html", content)


def organizer_detail(request):
    title = "Организаторы"
    content = {
        "title": title,
    }
    return render(request, "main/organizer-detail.html", content)


def sponsors(request):
    title = "Спонсоры"
    content = {
        "title": title,
    }
    return render(request, "main/sponsors.html", content)


def sponsor_detail(request):
    title = "Спонсоры"
    content = {
        "title": title,
    }
    return render(request, "main/sponsor-detail.html", content)


def spon_info(request):
    title = "Спонсорам"
    content = {
        "title": title,
    }
    return render(request, "main/spon-info.html", content)


def contacts(request):
    title = "Контакты"
    content = {
        "title": title,
    }
    return render(request, "main/contacts.html", content)


def authorization(request):
    title = "Вход в личный кабинет"
    content = {
        "title": title,
    }
    return render(request, "main/authorization.html", content)


def profile(request):
    title = "Личный кабинет"
    subtitle = "Мой профиль"
    content = {
        "title": title,
        "subtitle": subtitle,
    }
    return render(request, "main/profile.html", content)


def page_details(request, pk):
    pass
