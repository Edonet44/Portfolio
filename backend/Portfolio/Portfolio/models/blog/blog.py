from django.db import models
#from django.contrib.auth.models import User
from Portfolio.models.utenti.utenti import Utente
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descrizione = models.TextField()

    def __str__(self):
        return self.nome

class Post(models.Model):
    titolo = models.CharField(max_length=200)
    contenuto = models.TextField()
    data_pubblicazione = models.DateTimeField(default=timezone.now)
    autore = models.ForeignKey(Utente, on_delete=models.CASCADE)
    categorie = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titolo


