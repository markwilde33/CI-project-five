from django.conf.urls import url
from .views import get_tickets, ticket_view


urlpatterns = [
    url(r'^$', get_tickets, name='get_tickets'),
    url(r'^(?P<pk>\d+)/$', ticket_view, name='ticket_view'),
    ]