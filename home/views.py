from django.shortcuts import render
from exercises.models import Exercise

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
