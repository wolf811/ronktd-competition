from django.http import HttpResponse
from django.shortcuts import render

from publications.models import Post

# Create your views here.


def details(request, post_pk):
    post = Post.objects.filter(pk=post_pk).first()
    # main/templates/main/news-detail.html
    content = {
        "title": "detailed",
        "post": post,
    }
    return render(request, "main/news-detail.html", content)
