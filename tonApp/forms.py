from django import forms
from tonApp.models import Commentaire
class UserMessage(forms.ModelForm):
    class Meta:
        model=Commentaire
        fields=['Nom','Mail','Tel','message',]
    