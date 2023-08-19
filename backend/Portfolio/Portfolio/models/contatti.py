from django.db import models
from backend.Portfolio.Portfolio.models.utenti import Utente

class Contatti(models.Model):
    tipo = models.CharField(max_length=50)
    valore = models.CharField(max_length=255)
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo}: {self.valore}"
