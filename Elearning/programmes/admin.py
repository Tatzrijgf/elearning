from django.contrib import admin
from .models import Niveau,Matiere,Lesson,Commentaire,Reponse

# Register your models here.

admin.site.register(Niveau)
admin.site.register(Matiere)
admin.site.register(Lesson)
admin.site.register(Commentaire)
admin.site.register(Reponse)