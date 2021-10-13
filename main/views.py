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

def about(request):
    title = "О конкурсе"
    content = {
        "title": title,
    }
    return render(request, "main/about.html", content)


def members(request):
    title = "Участники"
    content = {
        "title": title,
    }
    return render(request, "main/members.html", content)


def gallery(request):
    title = "Галерея"
    content = {
        "title": title,
    }
    return render(request, "main/gallery.html", content)


def partners(request):
    title = "Партнеры"
    content = {
        "title": title,
    }
    return render(request, "main/partners.html", content)


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
