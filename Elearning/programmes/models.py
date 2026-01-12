from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Niveau(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

class Matiere(models.Model):
    matiere_id = models.CharField(unique=True)
    nom = models.CharField(unique=True)
    slug = models.SlugField(max_length=100, blank=True)
    description = models.TextField()
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE, related_name='matieres')
    image = models.ImageField(upload_to='matieres/', null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super().save(*args, **kwargs)


class Lesson(models.Model):
    lesson_id = models.CharField(unique=True,max_length=100)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE, )
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    contenu = models.TextField()
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='lessons')
    video = models.FileField(upload_to='video', null=True, blank=True, verbose_name='cours en video')
    fpe = models.FileField(upload_to ='FPE', null=True, blank=True, verbose_name='cours en presentation')
    pdf = models.FileField(upload_to='PDF', null=True, blank=True, verbose_name='cours en pdf')
    creer_par = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    position = models.PositiveBigIntegerField(verbose_name='chapitre no', default=0)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['position']
        unique_together = ['matiere', 'slug'] 

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("programmes:lessonList", kwargs={"slug": self.matiere.slug, "niveau":self.niveau.slug})   

class Commentaire(models.Model):
    nom_lesson = models.ForeignKey(Lesson, null=True, on_delete=models.CASCADE, related_name='comments')
    nom_comm = models.CharField(max_length=100, blank=True)
    auteur = models.ForeignKey(User, on_delete = models.CASCADE)
    corps = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self,*args, **kwargs):
        self.nom_comm = slugify("commenter par " + str(self.auteur) + "a" + str(self.date_added))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom_comm

class Meta:
    ordering = ['-date_added']


class  Reponse(models.Model):
    nom_comm = models.ForeignKey(Commentaire, on_delete=models.CASCADE, related_name='reponses')
    corps = models.TextField(max_length=500)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reponse a" + str(self.nom_comm.nom_com)