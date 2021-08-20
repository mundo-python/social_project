from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='twitter/login.html'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('editar/', views.editar, name='editar')
]
