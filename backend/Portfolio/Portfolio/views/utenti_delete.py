from django.views.generic.edit import DeleteView
from Portfolio.models.utenti import Utente

class UtenteDeleteView(DeleteView):
    model = Utente
    template_name = 'utente_confirm_delete.html'
    success_url = '/utenti/'  # URL da reindirizzare dopo l'eliminazione
