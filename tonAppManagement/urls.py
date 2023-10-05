from django.urls import path
from tonAppManagement.views import *


app_name='tonAppManagement'
urlpatterns=[
    path('mailPage',Mail,name="mail"),
    path('Comment/<str:commentaireId>',Comment,name="comment"),
    path('AboutUser',Coordonnee,name="userInfo"),
    path('home',index,name="homePage"),
    #path('filter/<int:infoId>',Filtre,name="filtre"),
]