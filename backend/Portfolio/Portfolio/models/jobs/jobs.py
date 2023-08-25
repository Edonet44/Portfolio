from django.contrib.auth.models import User
from Portfolio.models.utenti.utenti import Utente
from django.db import models
#import uuid 

class Job(models.Model):
  #  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titolo = models.CharField(max_length=100)
    descrizione = models.TextField()
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo