from django.urls import path
from . import views


# URls para la aplicación de etiquetas
urlpatterns = [
    path('labels/', views.labels_list, name='labels_list'),
]
