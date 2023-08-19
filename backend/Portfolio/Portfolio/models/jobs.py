from backend.Portfolio.Portfolio.models.utenti import Utente
from django.db import models

class Job(models.Model):
    titolo = models.CharField(max_length=100)
    descrizione = models.TextField()
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo