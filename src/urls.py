from django.contrib import admin
from django.urls import path, include


# URLs Globales
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/albums/', include('albums.urls')),
    path('api/images/', include('images.urls')),
    path('api/comments/', include('comments.urls')),
    path('api/likes/', include('likes.urls')),
    path('api/tags/', include('tags.urls')),
    path('api/statistics/', include('analytics.urls')),
]
