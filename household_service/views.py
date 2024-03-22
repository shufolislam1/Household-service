from django.shortcuts import render

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')