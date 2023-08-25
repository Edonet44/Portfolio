from django.views.generic import ListView
from Portfolio.models.utenti.utenti import Utente



class UtenteListView(ListView):
    model = Utente
    template_name = 'utenti/utente_list.html'
    context_object_name = 'utenti'  # Nome del contesto da utilizzare nel template
