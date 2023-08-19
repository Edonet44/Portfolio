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
from django.urls import path
from Portfolio.views.utenti_list import UtenteListView
from Portfolio.views.utenti_create import UtenteCreateView
from Portfolio.views.utenti_update import UtenteUpdateView
from Portfolio.views.utenti_delete import UtenteDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('utenti/', UtenteListView.as_view(), name='utente_list'),
    path('utenti/create/', UtenteCreateView.as_view(), name='utente_create'),
    path('utenti/<int:pk>/update/', UtenteUpdateView.as_view(), name='utente_update'),
    path('utenti/<int:pk>/delete/', UtenteDeleteView.as_view(), name='utente_delete'),
 ]
    

