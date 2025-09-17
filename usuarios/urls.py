from django.urls import path, include
from usuarios.views import *
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('login/', logar, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', sair, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 