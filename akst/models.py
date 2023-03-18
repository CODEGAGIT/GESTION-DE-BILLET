from django.db import models


class suggestion(models.Model):
    email=models.CharField(max_length=20)
    message=models.TextField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)
    
    
class billet(models.Model):
    code_billet=models.PositiveIntegerField(default=0)
    reservation_id=models.ForeignKey('reservation', on_delete=models.DO_NOTHING)
    compagnie_id=models.ForeignKey('compagnie', on_delete=models.DO_NOTHING)
    client_id=models.ForeignKey('client', on_delete=models.DO_NOTHING)

class bus(models.Model):
    matricule_bus=models.CharField(max_length=12)
    nb_place=models.PositiveSmallIntegerField(default=0)
    compagnie_id=models.ForeignKey('compagnie', on_delete=models.DO_NOTHING)

class compagnie(models.Model):
    nom_cp=models.CharField(max_length=10)
    siege_cp=models.CharField(max_length=100)

class reservation(models.Model):
    nb_billet=models.PositiveSmallIntegerField(default=0)
    bl_valide=models.BooleanField
 
class client(models.Model):
    nom_clt=models.CharField(max_length=30)
    prenom_clt=models.CharField(max_length=50)
    email_clt=models.CharField(max_length=60)
    telephone_clt=models.PositiveIntegerField(default=0)
    
class grade(models.Model):
    libelle_grd=models.CharField(max_length=20)
    
class ville(models.Model):
    nom_ville=models.CharField(max_length=100)
    
    
class v_depart(models.Model):
    ville_id=models.ForeignKey('ville', on_delete=models.DO_NOTHING)
    
    
class v_arrivee(models.Model):
    ville_id=models.ForeignKey('ville', on_delete=models.DO_NOTHING)
    
    
class ligne(models.Model):
    ville_dep=models.ForeignKey('v_depart',on_delete=models.DO_NOTHING )
    ville_arr=models.ForeignKey('v_arrivee',on_delete=models.DO_NOTHING )
    prix=models.FloatField(default=0)
    
    
class infoligne(models.Model):
    date_dep=models.ForeignKey('date_depart',on_delete=models.DO_NOTHING)
    heure_dep=models.ForeignKey('heure_depart',on_delete=models.DO_NOTHING)
    ligne_id=models.ForeignKey('ligne',on_delete=models.DO_NOTHING)
    bus_id=models.ForeignKey('bus', on_delete=models.DO_NOTHING)
    
class date_depart(models.Model):
    ladate=models.DateField()
    
    
class heure_depart(models.Model):
    l_heure=models.TimeField(default='05:00.0')
    
   
class utilisateur(models.Model):
    grade_id=models.ForeignKey('grade', on_delete=models.DO_NOTHING)
    nom_user=models.CharField(max_length=30)
    prenom_user=models.CharField(max_length=50)
    email_user=models.CharField(max_length=60)
    id_user=models.CharField(max_length=10)
    pw_user=models.CharField(max_length=12)
    compagnie_id=models.ForeignKey('compagnie', on_delete=models.DO_NOTHING)
    