from django.conf.urls import url    
from .views import dashboard

#URL patterns for home app functionality
urlpatterns = [
    url(r'^dashboard/$', dashboard, name='dashboard'),
    ]
    