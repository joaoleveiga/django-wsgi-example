from django.shortcuts import render


def index(request, name=None):
    name = name or 'Anonymous'
    return render(request, 'myapp/index.html', {'name': name})
