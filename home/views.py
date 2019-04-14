from django.shortcuts import render

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")
    
def dashboard(request):
    return render(request, 'dashboard.html')