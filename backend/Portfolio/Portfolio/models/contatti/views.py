from rest_framework import generics
from .contatti import Contatti
from .serializers import ContattiSerializer # Assicurati che l'import sia corretto

#utilizzo di generics per la creazione delle api
class ContattiListAPIView(generics.ListAPIView):
    queryset = Contatti.objects.all()
    serializer_class = ContattiSerializer