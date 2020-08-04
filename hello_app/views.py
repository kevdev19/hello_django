from django.shortcuts import render

from . import views


def index(request):
    greeting = {'greeting': 'Hello, World!'}
    return render(request, 'index.html', {'greeting': greeting})
