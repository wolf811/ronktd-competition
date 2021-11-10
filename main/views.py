from django.shortcuts import render

# Create your views here.
def index(request):
    title = "Главная"
    content = {
        "title": title,
    }
    return render(request, "main/index.html", content)

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
    title = "О конкурсе"
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
