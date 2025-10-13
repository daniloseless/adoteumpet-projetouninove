from django.urls import path
from usuarios.views import cadastro, sair 
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),   
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', sair, name='logout')
] 