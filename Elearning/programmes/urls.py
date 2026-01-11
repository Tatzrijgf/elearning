from django.urls import path
from programmes.views import *

urlpatterns =[
    path('', NiveauListView.as_view(), name='niveauList' ),
]