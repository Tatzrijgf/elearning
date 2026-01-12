from django import forms
from .models import Lesson,Commentaire,Reponse
from django.forms import widgets

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = {'lesson_id', 'nom', 'video','fpe', 'pdf', 'position'}

class ComForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = {'corps'}
        labels = {'corps':'Commentaires'}
        widgets= {
            'corps':forms.Textarea(attrs={
            'class':'form-control',
            'rows':4,
            'cols':70,
            'placeholder':'Entrer votre commentaire ici',
            })
        }


class RepForm(forms.ModelForm):
    class Meta:
        model = Reponse
        fields = {'corps'}
        labels = {'corps':'Reponse'}
        widgets= {
            'corps':forms.Textarea(attrs={
            'class':'form-control',
            'rows':4,
            'cols':70,
            'placeholder':'Repondez a ce commentaire ici',
            })
        }        