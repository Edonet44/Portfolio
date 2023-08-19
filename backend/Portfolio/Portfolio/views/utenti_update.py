from django.views.generic.edit import UpdateView
from Portfolio.models.utenti import Utente
class UtenteUpdateView(UpdateView):
    model = Utente
    fields = ['nome', 'cognome', 'citta', 'indirizzo', 'immagine', 'git', 'linkedin', 'web']
    template_name = 'utente_form.html'
    success_url = '/utenti/'  # URL da reindirizzare dopo l'aggiornamento
