from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from .models import Ticket, TicketComment
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
    to the 'ticket_view.html' template, return a
    comment form for users to add a comment,
    and return all previously added comments,
    Or return a 404 error if ticket is not found
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        
        comment_form = CommentForm(request.POST, request.FILES)
        
        if comment_form.is_valid():
            ticketComment = comment_form.save(commit=False)
            ticketComment.ticket = ticket
            ticketComment.user = request.user
            ticketComment.save()
            return redirect(reverse('ticket_view', kwargs={'pk': pk}))
            
    else:
        comment_form = CommentForm()
        get_comments = TicketComment.objects.filter(ticket__pk=ticket.pk)
        total_comments = len(get_comments)
        ticket.views += 1
        ticket.save()
        return render(request, 'ticket_view.html', {'ticket':ticket, 'get_comments':get_comments, 'total_comments ':total_comments , 'comment_form':comment_form})
  
