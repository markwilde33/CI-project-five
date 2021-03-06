from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Ticket, TicketComment
from .forms import TicketForm, CommentForm
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import stripe



@login_required()
def get_tickets(request):
    """
    Create a view that will return a
    list of tickets that were published prior to'now'
    and render them to the 'tickets.html' template,
    Use Paginator to return 5 tickets per page
    """
    get_tickets = Ticket.objects.filter(most_recent_update__lte=timezone.now()
                                ).order_by('-most_recent_update')
                                
    # Pagination
    paginator = Paginator(get_tickets, 5)
    page = request.GET.get('page', 1)
    
    # Handle out of range and invalid page numbers:
    try:
        tickets = paginator.page(page)
    except PageNotAnInteger:
        tickets = paginator.page(1)
    except EmptyPage:
        tickets = paginator.page(paginator.num_pages)

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
            messages.success(
                request, "Your ticket has been updated")
            return redirect(ticket_view, ticket.pk)
    else:
        ticket_form = TicketForm(instance=ticket)
    return render(request, 'ticket_form.html', {'ticket_form': ticket_form})


@login_required() 
def delete_ticket(request, pk):
    """
    Delete a ticket
    """
    ticket =  get_object_or_404(Ticket, pk=pk) 
    ticket.delete()
    messages.success(
        request, "Your ticket has been deleted")
    return redirect(reverse('profile'))
     

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

@login_required
def make_payment(request):
    """
    Return the payments.html file
    """
    # Auto fill stripe dummy payment details for test mode
    payment_details = { "stripe_key": settings.STRIPE_PUBLISHABLE }
    return render(request, "make_payment.html", payment_details)
    
    
@login_required
def checkout(request):
    """
    Complete payment transaction using Stripe checkout
    link: https://stripe.com/docs/checkout
    """
    # Gets Stripe secret key needed to make payment
    stripe.api_key = settings.STRIPE_SECRET
    
    if request.method == "POST":
        token = request.POST.get("stripeToken")
    try:
        stripe.Charge.create(
            amount = '0999',
            currency = 'eur',
            source = token,
        )
    except stripe.error.CardError:
                messages.error(request, "Your card was declined")
    
    else:
        messages.success(
            request, "Payment received, thank you!")
            
            
        return redirect(reverse('get_tickets'))


