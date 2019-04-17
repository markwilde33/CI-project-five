from django import forms
from .models import Ticket, TicketComment
from django.utils import timezone


class TicketForm(forms.ModelForm):
    """
    The form for a ticket
    """
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'ticket_type')


class CommentForm(forms.ModelForm):
    """
    The form for a comment
    """
    class Meta:
        model = TicketComment
        fields = ( 'comment', )