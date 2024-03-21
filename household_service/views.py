from django.shortcuts import render

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')