from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album
from .forms import AlbumForm

class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')  # Redirect to the same page after success

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage') 
    def get_object(self):
        return Album.objects.get(id=self.kwargs['id'])  

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'confirm_delete.html'  
    success_url = reverse_lazy('homepage')

    def get_object(self):
        return Album.objects.get(id=self.kwargs['id']) 