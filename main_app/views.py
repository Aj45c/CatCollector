from django.shortcuts import render
from django.http import HttpResponse
from .models import Cat
# Create your views here.

    
def home(request):
    return HttpResponse('<h1>Hey Hey hey yoyo </h1>')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', { 'cats': cats })