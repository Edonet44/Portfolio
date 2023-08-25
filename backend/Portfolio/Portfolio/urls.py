"""
URL configuration for Portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Portfolio.views.utenti_list import UtenteListView
from Portfolio.views.utenti_create import UtenteCreateView
from Portfolio.views.utenti_update import UtenteUpdateView
from Portfolio.views.utenti_delete import UtenteDeleteView
from Portfolio.models.utenti.views import UtenteListAPIView
from Portfolio.models.contatti.views import ContattiListAPIView
from Portfolio.models.jobs.views import JobListAPIView
from Portfolio.models.blog.views import CategoriaApiViewSet,PostViewApiSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('utenti/', UtenteListView.as_view(), name='utente_list'),
    path('utenti/create/', UtenteCreateView.as_view(), name='utente_create'),
    path('utenti/<int:pk>/update/', UtenteUpdateView.as_view(), name='utente_update'),
    path('utenti/<int:pk>/delete/', UtenteDeleteView.as_view(), name='utente_delete'),
    #path per le api dell utente
    path('api/v1/utenti/', UtenteListAPIView.as_view(), name='utente-api'),
    path('api/v1/contatti/', ContattiListAPIView.as_view(), name='contatti-api'),
    path('api/v1/jobs/', JobListAPIView.as_view(), name='jobs-api'),
    path('api/v1/categorie/', CategoriaApiViewSet.as_view(({'get': 'list'})), name='categorie-api'),
    path('api/v1/posts/', PostViewApiSet.as_view({'get': 'list'}), name='posts-api'),
 ]
#setta la cartella dei media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

