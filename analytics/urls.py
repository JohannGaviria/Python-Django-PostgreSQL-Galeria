from django.urls import path
from . import views


# URls para la aplicación de analítica
urlpatterns = [
    path('<int:image_id>/stats/', views.image_stast, name='image_stats'),
]
