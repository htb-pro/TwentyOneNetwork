from django.db import models

class Services(models.Model):
    """Services table """
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class UserInformations(models.Model):
    """table of users informations """
    firstname=models.CharField(max_length=50)
    secondname=models.CharField(max_length=40)
    service=models.CharField(max_length=50)
    number=models.IntegerField()
    email=models.EmailField()
    etat=[("T","traité"),
          ("N","Non traité")
    ]
    status=models.CharField(max_length=20,choices=etat)
    def __str__(self) -> str:
        return self.firstname

