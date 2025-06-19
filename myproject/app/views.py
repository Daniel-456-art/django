from django.shortcuts import render

# Create your views here.
def index(rquest):
    return render(rquest, 'index.html')