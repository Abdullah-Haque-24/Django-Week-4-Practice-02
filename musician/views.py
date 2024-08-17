from django.shortcuts import render,redirect
from . import models
from . import forms
# Create your views here.
def add_musician(request):
    if request.method == "POST":
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    else:        
        musician_form = forms.MusicianForm()
    return render(request, 'add_musician.html', {"form" : musician_form})


#Edit
def edit_musician(request, id):
    musician = models.Musician.objects.get(id=id) #here the name of the pk and id, id is fixed
    musician_form = forms.MusicianForm(instance=musician)
    if request.method == "POST":
        musician_form = forms.MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    return render(request, 'add_musician.html', {"form" : musician_form})