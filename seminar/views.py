from django.shortcuts import render

# Create your views here.
def index(request):
    title = "Семинар"
    content = {
        "title": title,
    }
    return render(request, "seminar/index.html", content)
