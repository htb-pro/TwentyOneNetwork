from django.urls import path
from tonApp.views import *
app_name='tonApp'
urlpatterns = [
    path('',homePage,name="tonApp-homePage"),
    path("aboutUs",aboutUs,name="aboutUs"),
    path("service",Service,name="service"),
    path("join",joinUs,name="joinUs"),
    path('coachingservice',Coaching,name="coaching"),
    path('mentoringService',Mentoring,name="mentoring"),
    path('discoveringService',Discovering,name="Discovering"),
    path('coordonneeForm',UserCoordonnees,name="CoordonneeUser"),#formulaire des coordonnees des utilisateur
    path('TalentService',Talent,name="talent"),
    path('pointOfView',PointOfView,name="POV"),
    path('improvement',Improvement,name="improvement"),
    path('OpenlessWoldWild',WorldWild,name="worldWild"),
    path('Legacy',legacy,name="legacy"),
    path('logo',Logo,name="logo"),
]