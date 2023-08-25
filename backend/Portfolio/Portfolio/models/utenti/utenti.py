from django.db import models
#import uuid

class Utente(models.Model):
   # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    citta = models.CharField(max_length=100)
    indirizzo = models.CharField(max_length=255)
    immagine = models.ImageField(upload_to='utenti/')
    git = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    web = models.URLField(blank=True)

    def __str__(self):
        return f"{self.nome} {self.cognome}"
