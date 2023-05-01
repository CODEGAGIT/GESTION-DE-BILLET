from django.db import models

from dashboard.models import compagnie

class suggestion(models.Model):
    email=models.CharField(max_length=20)
    message=models.TextField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)
    
class client(models.Model):
    nom_clt=models.CharField(max_length=30)
    prenom_clt=models.CharField(max_length=50)
    email_clt=models.CharField(max_length=60)
    telephone_clt=models.PositiveIntegerField(default=0)
class billet(models.Model):
    code_billet=models.PositiveIntegerField(default=0)
    compagnie_id=models.ForeignKey(compagnie, on_delete=models.DO_NOTHING)
    client_id=models.ForeignKey(client, on_delete=models.DO_NOTHING)
    place=models.SmallIntegerField(default=0)
    bl_valide=models.BooleanField