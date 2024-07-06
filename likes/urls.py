from django.urls import path
from . import views


# URls para la aplicación de likes
urlpatterns = [
    path('<int:image_id>/likes/', views.like_list_create, name='like_list_create'),
    path('likes/<int:like_id>/', views.like_detail, name='like_detail'),
]
