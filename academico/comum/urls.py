from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('perfil', views.perfil, name='perfil'),
    path('confirma_cadastro', views.confirma_cadastro, name='confirma_cadastro'),
]
