from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# The ticket model 
class Ticket(models.Model):
   
    STATUS_CHOICES = (
        ('TO DO', 'To Do'),
        ('DOING', 'Doing'),
        ('DONE', 'Done')
    )

    TICKET_CHOICES = (
        ('BUG', 'Bug'),
        ('FEATURE', 'Feature')
    )

    author = models.ForeignKey(User, null=True, related_name='ticket_maker')
    title = models.CharField(max_length=255)
    description = models.TextField()
    ticket_type = models.CharField(max_length=20, choices=TICKET_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TO DO')
    upvotes = models.IntegerField(default=0)
    upvoters = models.ManyToManyField(User, related_name='upvoters')
    created_date = models.DateTimeField(auto_now_add=True)
    most_recent_update = models.DateTimeField(blank=True, null=True,
    default=timezone.now)
    views = models.IntegerField(default=0)
    

    def __str__(self):
        return self.title

# The comment model
class TicketComment(models.Model):
    
    comment = models.TextField()
    ticket = models.ForeignKey(Ticket, related_name='comments')
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
   

    def __str__(self):
        return self.comment 