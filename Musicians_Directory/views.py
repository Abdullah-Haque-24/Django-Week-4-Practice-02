from django.shortcuts import render
from album import models

def home(request):
    data = models.Album.objects.all()
    print(data)
    return render(request, 'home.html', {"data" : data})