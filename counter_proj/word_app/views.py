from django.shortcuts import render
from . models import Word, Document, WordCount 

# Create your views here.
def index(request): 
    pass

def word_count(request): 
    form = request.POST
    author_name = form.get('author')
    title = form.get('title')
    year = form.get('year')

    pass