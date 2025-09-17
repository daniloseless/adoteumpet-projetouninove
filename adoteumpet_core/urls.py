
from django.contrib import admin
from django.urls import path, include
from django.conf import settings                
from django.conf.urls.static import static      

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('divulgar/', include('divulgar.urls')),
    path('adotar/', include('adotar.urls')),

] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Nome na página de Login e no header do django admin
admin.site.site_header = 'AdoteUmPet - Sistema de Adocão de Pets'    
# Nome que aparece no titulo da aba do navegador
admin.site.site_title = 'AdoteUmPet'                                          
# Nome no lado esquerdo do painel django admin
admin.site.index_title = 'AdoteUmPet'                                    


