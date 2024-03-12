from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_service, name='all_service')
]
