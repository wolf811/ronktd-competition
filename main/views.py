from django.shortcuts import render

# Create your views here.
def index(request):
    title = "Главная"
    content = {
        "title": title,
    }
    return render(request, "main/index.html", content)
