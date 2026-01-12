from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView, FormView
from .models import Niveau, Matiere
from .form import LessonForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .form import ComForm, RepForm

# Create your views here.
class NiveauListView(ListView):
    context_object_name = 'niveaux'
    model = Niveau
    template_name = 'programmes/niveau_list.html'

class MatiereListview(DetailView):
    context_object_name = 'niveau'
    model = Niveau
    template_name = 'programmes/matiereList.html'

class LessonListview(DetailView):
    model = Matiere
    template_name = 'programmes/LessonList.html'
    context_object_name = 'matiere'


class LessonListviewDetail(DetailView, FormView):
    model = Lesson
    template_name = 'programmes/LessonListdetail.html'
    context_object_name = 'lesson'
    form_class = ComForm
    second_form_class = RepForm

    def get_context_data(self, **kwargs):
        context = super(LessonListviewDetail,self).get_context_data(**kwargs)

        if 'form' not in context:
            context['form'] =self.form_class()
        if 'form2' not in context:
            context['form2'] =self.second_form_class()

        return context

        def get_success_url(self):
            self.object = self.get_object()
            return reverse_lazy('programmes:lessonListDetail', kwargs={
            'niveau': self.object.niveau.slug,  # ou self.object.niveau
            'matiere': self.object.matiere.slug,  # ou self.object.matiere  
            'slug': self.object.slug
            })
    
    def form_valid(self,form):
        self.object = self.get_object()
        fd = form.save(commit=False)
        fd.auteur = self.request.user
        fd.lesson = self.object
        fd.nom_lesson_id = self.object.id
        fd.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_valid2(self,form):
        self.object = self.get_object()
        fd = form.save(commit=False)
        fd.auteur = self.request.user
        fd.nom_comm_id = self.request.POST.get('comment_id')
        fd.save()
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        self.object = self.get_object()
        niveau = self.object.niveau
        matiere = self.object.matiere
        return reverse_lazy('programmes:lessonListDetail', kwargs={
        'niveau': self.object.niveau.slug,  # ou self.object.niveau
        'matiere': self.object.matiere.slug,  # ou self.object.matiere  
        'slug': self.object.slug
        })
    

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.form_class
            form_name = 'form'

        else:
            form_class = self.second_form_class
            form_name = 'form2'
        form = self.get_form(form_class)

        if form_name == "form" and form.is_valid():
            print("nouveau commentaire")
            return self.form_valid(form)
        
        if form_name=='form' and form.is_valid():
            print("nouveau commentaire")
            return self.form_valid(form)

        if form_name=='form2' and form.is_valid():
            print("nouvelle reponse")
            return self.form_valid2(form)









class LessonCreateView(CreateView):
    form_class =LessonForm
    model = Matiere
    template_name = 'programmes/Lessoncreate.html'

    def get_success_url(self):
        self.object = self.get_object()
        niveau = self.object.niveau
        return reverse_lazy('programmes:lessonList',kwargs={'niveau':niveau, 'slug':self.object.slug})

    def form_valid(self,form,*args, **kwargs):
        self.object = self.get_object()
        ls = form.save(commit=False)
        ls.creer_par = self.request.user
        ls.niveau = self.object.niveau
        ls.matiere = self.object
        ls.save()
        return HttpResponseRedirect(self.get_success_url())

class LessonUpdateView(UpdateView):
    model = Lesson 
    fields = ('nom','position','pdf','fpe')
    context_object_name = 'lesson'
    template_name = 'programmes/lessonupdate.html'



class LessonDeleteView(DeleteView):
    model = Lesson
    context_object_name = 'lesson'
    template_name = 'programmes/lessondelete.html'

    def get_success_url(self):
        niveau = self.object.niveau
        return reverse_lazy("programmes:lessonList",kwargs={'niveau':niveau,'slug':self.object.matiere.slug})
