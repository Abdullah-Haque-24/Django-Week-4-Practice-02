from django.urls import path
from .views import AlbumCreateView, AlbumUpdateView, AlbumDeleteView

urlpatterns = [
    path('add/', AlbumCreateView.as_view(), name='add_album'),
    path('edit/<int:id>/', AlbumUpdateView.as_view(), name='edit_album'),
    path('delete/<int:id>/', AlbumDeleteView.as_view(), name='delete_album'),
]

