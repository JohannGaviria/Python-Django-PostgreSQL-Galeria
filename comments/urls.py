from django.urls import path
from . import views


# URls para la aplicación de comentarios
urlpatterns = [
    path('<int:image_id>/comments/', views.comment_list_create, name='comment_list_create'),
    path('comments/<int:comment_id>/', views.comment_detail, name='comment_detail'),
]
