from django.db import models
from django.contrib.auth.models import User
from Portfolio.models.utenti.utenti import Utente
#import uuid 

class Contatti(models.Model):
   # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=50)
    valore = models.CharField(max_length=255)
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo}: {self.valore}"
