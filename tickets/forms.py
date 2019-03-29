from django import forms
from .models import Ticket, TicketComment
from django.utils import timezone

# The form for a ticket
class TicketForm(forms.ModelForm):
    
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'ticket_type')

# The form for a comment
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = TicketComment
        fields = ( 'comment', )