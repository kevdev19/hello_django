from django.shortcuts import render

from . import views


def index(request):
    my_greeting = {"greeting": "Hello, World!"}
    return render(request, "index.html", my_greeting)
