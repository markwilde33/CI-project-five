from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Ticket, TicketComment
from .forms import TicketForm, CommentForm
import stripe


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
    or return a 404 error if ticket is not found
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
        ticket.views += 1
        ticket.save()
        return render(request, 'ticket_view.html', {'ticket':ticket, 'get_comments':get_comments, 'comment_form':comment_form})
 
  
def create_or_edit_ticket(request, pk=None):
    """
     Create a view that allows a user to create
     or edit a ticket depending on if the
     ticket ID is null or not
     """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES, instance=ticket)
        if ticket_form.is_valid():
            ticket = ticket_form.save()
            ticket.author = request.user
            ticket.save()
            return redirect(ticket_view, ticket.pk)
    else:
        ticket_form = TicketForm(instance=ticket)
    return render(request, 'ticket_form.html', {'ticket_form': ticket_form})


@login_required() 
def delete_ticket(request, pk):
    """
    Delete a bug
    """
    ticket =  get_object_or_404(Ticket, pk=pk) 
    ticket.delete()
    return redirect('profile')
     

@login_required
def upvote_bug(request, pk):
    """
    Upvote a bug
    """
    if request.method == "POST":
        bug = get_object_or_404(Ticket, pk=pk)
        bug.upvotes += 1
        bug.save()
        return redirect(reverse('ticket_view', kwargs={'pk': pk}))

     
        
