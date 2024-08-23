from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def detailbook(request, slug):
    return render(request, 'detailbook.html', {'book': book})