from rest_framework import generics
from .utenti import Utente
from .serilizers import UtenteSerializer  # Assicurati che l'import sia corretto

#utilizzo di generics per la creazione delle api
class UtenteListAPIView(generics.ListAPIView):
    queryset = Utente.objects.all()
    serializer_class = UtenteSerializer