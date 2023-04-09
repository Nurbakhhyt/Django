from django.contrib import admin
from django.urls import path

from shelter.views import *
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shelter.urls')),
]

handler404 = pageNotFound
