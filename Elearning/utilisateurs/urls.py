from django.urls import path
from utilisateurs.views import  accueil,user_login,user_logout,register

urlpatterns = [
    path('', accueil, name='accueil'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('register', register, name='register'),
]