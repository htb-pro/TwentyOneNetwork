from django.shortcuts import render,redirect
from tonAppManagement.models import UserInformations
from tonApp.models import Commentaire
from datetime import datetime

def index(request):
    return render(request,'UserManagement/index.html')

def Mail(request):
    Commentaires=Commentaire.objects.all()
    return render(request,'UserManagement/mailPage.html',{'commentaires':Commentaires})

def Comment(request,commentaireId):
    Comments=Commentaire.objects.filter(pk=commentaireId)
    return render(request,'UserManagement/commentaire.html',{'comments':Comments})

def Coordonnee(request):
    """View of user information"""
    userInfo=UserInformations.objects.all()
    if request.method=="GET":
        search=request.GET.get('chercher')
        if search is not None:
            userInfo=UserInformations.objects.filter(firstname__iexact=search)
        else:
            userInfo=UserInformations.objects.all()
    return render(request,'UserManagement/CordonneesUser.html',context={'userInfos':userInfo,'date':datetime.now()})

"""def Filtre(request,infoId):
    userInfo=UserInformations.objects.get(pk=infoId)
    return render(request,'UserManagement/CordonneesUser.html',context={'userInfos':userInfo,'date':datetime.now()})
"""