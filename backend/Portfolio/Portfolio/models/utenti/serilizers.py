from rest_framework import serializers
from .utenti import Utente


#Nel tuo caso, stai definendo un serializer chiamato UtenteSerializer che è basato sul modello Utente.
#  I serializer in Django REST framework funzionano in modo simile agli ModelForm di Django, semplificando la creazione di rappresentazioni JSON dei tuoi modelli.
# modello : utente
# all. voglio includere tutti i campi del modello utente



class UtenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utente
        fields = '__all__'
