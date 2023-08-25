from django.contrib import admin
from .models.utenti.utenti import Utente
from .models.contatti.contatti import Contatti
from .models.jobs.jobs import Job
from .models.blog.blog import Categoria,Post


admin.site.register(Utente)
admin.site.register(Contatti)
admin.site.register(Job)
admin.site.register(Categoria)
admin.site.register(Post)