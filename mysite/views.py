from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

def index(request):
    response = 'This is the Project Homepage!'
    return render(request, 'index.html', {'response' : response})
