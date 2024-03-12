from django.urls import path
from services.views import all_service
from . import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.userLogin, name='userLogin'),
    path('logout/', views.userLogout, name='userLogout'),
    path('', all_service, name='home'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
    path('promote_to_admin/', views.promote_to_admin, name='promote_to_admin'),
]