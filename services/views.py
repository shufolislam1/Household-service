from django.shortcuts import render
from .models import Services
# Create your views here.
def all_service(request):
    services = Services.objects.all()
    return render(request, 'base.html', {'services': services})