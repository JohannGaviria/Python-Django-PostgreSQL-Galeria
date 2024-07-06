from django.urls import path
from . import views


# URls para la aplicación de albums
urlpatterns = [
    path('', views.album_list_create, name='album_list_create'),
    path('<int:album_id>/', views.album_detail, name='album_detail'),
]
