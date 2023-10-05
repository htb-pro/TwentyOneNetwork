from datetime import datetime
from django.shortcuts import render,redirect
from tonApp.forms import UserMessage
from tonAppManagement.models import Services
from tonAppManagement.forms import UserForm
from tonApp.models import *
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as _,ngettext
# Create your views here.
    
def homePage(request):
    """la definition de la vue de la page principale"""
    text=_("Knowledge is the key for a best futur. wherever you are, Network twenty one is there to accompany you with its services.")
    if request.method=='POST':
        form=UserMessage(request.POST)
        if form.is_valid():

            form.save()
            return redirect('tonApp-homePage')
    else:
        form=UserMessage()
    return render(request,"Network 21 Formation.html",context={"date": datetime.today(),'Formulaire':form,'text':text})
def aboutUs(request):
    """View of abous us """
    return render(request,"aboutUs.html")

def Logo(request):
    """View logo"""
    return render(request,'logoPage.html',{})
def Service(request):
    return render(request,"Service.html")
def joinUs(request):
    return render(request,"joinUs.html")

def Coaching(request):
    return render(request,'Services/coaching.html',context={"Date": datetime.today()})

def Mentoring(request):
    return render(request,'Services/mentoring.html',context={"Date": datetime.today()})

def Discovering(request):
    return render(request,'Services/Discovering.html',context={"Date": datetime.today()})

def Talent(request):
    return render(request,'Services/Talent.html',context={})

def PointOfView(request):
    return render(request,'Services/pointOfview.html',context={})

def Improvement(request):
    return render(request,'Services/improvement.html',context={})

def WorldWild(request):
    return render(request,'Services/openWorldWild.html',context={})

def legacy(request):
    return render(request,'Services/legacy.html',context={'Houre':datetime.now(),'Id':1})

def UserCoordonnees(request):
    #Form of user
    services=Services.objects.all()
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tonApp:CoordonneeUser')
        else:
            form=UserForm()
    return render(request,'Services/coordonnee.html',{'services':services}) 
# Create your views here.
