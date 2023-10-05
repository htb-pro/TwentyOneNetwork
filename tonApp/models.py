from django.db import models
from django.utils.translation import gettext_lazy as _
#irheritierhtb/htb115

class Commentaire(models.Model):
    Nom=models.CharField(max_length=20,verbose_name=_("Name"))
    Mail=models.EmailField(primary_key=True,verbose_name=_("Mail"))
    message=models.TextField(max_length=1000,verbose_name=_("Message"))
    Tel=models.CharField(max_length=13,unique=True,verbose_name=_("Phone"))
    def __str__(self):
        return f"{self.Nom}"


# Create your models here.
