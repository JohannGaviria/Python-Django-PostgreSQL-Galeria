from django.urls import path
from . import views


# URls para la aplicación de imagenes
urlpatterns = [
    path('', views.image_list_create, name='image_list_create'),
    path('<int:image_id>/', views.image_detail, name='image_detail'),
    path('search/', views.search_images, name='search_images'),
]
