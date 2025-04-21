from django.contrib import admin
from django.urls import path, include
from shortener.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shortener.urls')), 
    path('', home, name='home'),
]