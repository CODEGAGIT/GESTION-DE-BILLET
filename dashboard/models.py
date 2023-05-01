from django.db import models


class compagnie(models.Model):
    nom_cp=models.CharField(max_length=10)
    siege_cp=models.CharField(max_length=100)