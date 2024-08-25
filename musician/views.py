from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from . import models
from . import forms

class MusicianCreateView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')

class MusicianUpdateView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('homepage')
    def get_object(self):
        return models.Musician.objects.get(id=self.kwargs['id'])
