from django.urls import path
from programmes.views import *
from . import views

app_name = "programmes"
urlpatterns =[
    path('', NiveauListView.as_view(), name='niveauList' ),
    path('<str:niveau>/<slug:slug>',LessonListview.as_view(),name='lessonList'),
    path('<slug:slug>',MatiereListview.as_view(),name='matiereList'),
    path('<str:niveau>/<str:matiere>/<slug:slug>/',LessonListviewDetail.as_view(),name='lessonListDetail'),
    path('<str:niveau>/<slug:slug>/create',LessonCreateView.as_view(),name='lessonCreate'),
    path('<str:niveau>/<str:matiere>/<slug:slug>/update/',LessonUpdateView.as_view(),name='lessonUpdate'),
    path('<str:niveau>/<str:matiere>/<slug:slug>/delete/',LessonDeleteView.as_view(),name='lessonDelete'),
]