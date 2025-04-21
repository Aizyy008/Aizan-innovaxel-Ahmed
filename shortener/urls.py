from django.urls import path
from . import views

urlpatterns = [
    path('shorten', views.create_short_url, name='create_short_url'),
    path('shorten/<str:short_code>', views.get_original_url, name='get_original_url'),
    path('shorten/<str:short_code>/stats', views.get_url_stats, name='get_url_stats'),
    path('r/<str:short_code>', views.redirect_to_original, name='redirect_to_original'),
    path('shorten/<str:short_code>', views.update_url, name='update_url'),
    path('shorten/<str:short_code>', views.delete_url, name='delete_url'),
]