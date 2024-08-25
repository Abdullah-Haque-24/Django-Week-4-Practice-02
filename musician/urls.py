from django.urls import path
from .views import MusicianCreateView, MusicianUpdateView

urlpatterns = [
    path('add/', MusicianCreateView.as_view(), name='add_musician'),
    path('edit/<int:id>/', MusicianUpdateView.as_view(), name='edit_musician'),
]
