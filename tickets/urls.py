from django.conf.urls import url
from .views import get_tickets, ticket_view, create_or_edit_ticket


urlpatterns = [
    url(r'^$', get_tickets, name='get_tickets'),
    url(r'^(?P<pk>\d+)/$', ticket_view, name='ticket_view'),
    url(r'^new/$', create_or_edit_ticket, name='create_ticket'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_ticket, name="edit_ticket"),
    ]