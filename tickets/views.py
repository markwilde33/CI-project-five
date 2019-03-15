from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Ticket, Comment
from .forms import TicketForm, CommentForm

@login_required()
def get_tickets(request):
    """
    Create a view that will return a
    list of tickets that were published prior to'now'
    and render them to the 'tickets.html' template
    """
    tickets = Ticket.objects.filter(most_recent_update__lte=timezone.now()
                                ).order_by('-most_recent_update')
    return render(request, "tickets.html", {'tickets': tickets})


@login_required()
def ticket_view(request, pk):
    """
    Create a view that will return a single ticket
    object based on the ticket ID and render it
    to the 'ticket_view.html' template
    Or return a 404 error if ticket is not found
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.views += 1
    ticket.save()
    """
    Try catch logic found at:
        "https://stackoverflow.com/questions/3090302/
        how-do-i-get-the-object-if-it-exists-or-none-if-it-does-not-exist/29455777"
    """
    try:
        all_comments = Comment.objects.filter(
            ticket=ticket).order_by('-created_date'
            )
    except Comment.DoesNotExist:
        all_comments = None
    comments_form = CommentForm()
    return render(request, "ticket_view.html", {
        'ticket': ticket, 'all_comments': all_comments, 'comments_form':comments_form
    })
    
