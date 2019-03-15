from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# The ticket model 
class Ticket(models.Model):
   
    STATUS_CHOICES = (
        ('TODO', 'To Do'),
        ('DOING', 'Doing'),
        ('DONE', 'Done')
    )

    TICKET_CHOICES = (
        ('BUG', 'Bug'),
        ('FEATURE', 'Feature')
    )

    user = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='ticket_creator')
    title = models.CharField(max_length=255)
    description = models.TextField()
    ticket_type = models.CharField(max_length=20, choices=TICKET_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TO DO')
    upvotes = models.IntegerField(default=0)
    user_upvoted_list = models.ManyToManyField(User, related_name='ticket_upvoter')
    created_date = models.DateTimeField(auto_now_add=True)
    most_recent_update = models.DateTimeField(blank=True, null=True,
    default=timezone.now)
    views = models.IntegerField(default=0)
    

    def __str__(self):
        return self.title

# The comment model
class Comment(models.Model):
    
    author = models.ForeignKey(User, related_name='ticket_creator')
    comment = models.TextField()
    ticket = models.ForeignKey(Ticket)
    created_date = models.DateTimeField(auto_now_add=True)
    most_recent_update = models.DateTimeField(blank=True, null=True,
    default=timezone.now)
    
   

    def __str__(self):
        return self.comment 
