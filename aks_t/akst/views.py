from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import infoligne, compagnie, bus, ligne, suggestion, ville, v_arrivee, v_depart, date_depart, heure_depart
from django.db import connection
import datetime
# from django.views.generic.dates import TodayArchiveView
# from akst.models import Article

# def accueil_view(request):
#     return render(request, 'index.html')


def accueil_view(request):
    context = {
        "ville": ville.objects.all(),
        "ville_dep": v_depart.objects.all(),
        "ville_arr": v_arrivee.objects.all(),
        "ligne": ligne.objects.all(),
        "infln": infoligne.objects.all(),
        "comp": compagnie.objects.all(),
        "lesbus": bus.objects.all(),
        "lesdates":date_depart.objects.all(),
        "dnow":datetime.date.today(),
    }
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))


def resultats_view(request):
    return render(request, 'resultats.html')


def base_view(request):
    return render(request, 'base.html')


# def bus_view(request, bus_id):
#     context = {"bs": get_object_or_404(bus, pk=bus_id), }
#     return render(request, 'show.html', context)


def result(request, date_depart_id):
    context = {"rdt": get_object_or_404(date_depart, pk=date_depart_id),
               "infln": infoligne.objects.all().filter(date_dep=date_depart_id).order_by('ligne_id'),
               }
    return render(request, 'result.html', context)


# def result_view(request):
#     rslt = infoligne.objects.all()

#     if request.method == "GET":
#         val = request.GET.get("date_dep")
#         n=date_depart.objects.get(id).filter(ladate=val)
#         rslt = infoligne.objects.filter(date_dep=n)
        # if val is not None:
        #      dt_dp = date_depart.objects.filter(ladate=val)
        # for r in infoligne.objects.raw('select heure_depart.l_heure,ville.nom_ville,ville.nom_ville,comppagnie.nom_cp,ligne.prix from infoligne join heure_depart on heure_depart.id=heure_dep join ligne on ligne.id=ligne_id join v_depart on v_depart.id=ville_dep join v_arrivee on v_arrivee.id=ville_arr join ville on ville.id=v_depart.ville_id join ville on ville.id=v_arrivee.ville_id join date_depart on date_depart.id=date_dep join bus on bus.id=bus_id join compagnie on compagnie.id=compagnie_id where date_depart.ladate='val';'):
        #     print r

    # context = {"infln": infoligne.objects.all(),
    #            "ville": ville.objects.all(),
    #            "ville_dep": v_depart.objects.all(),
    #            "ville_arr": v_arrivee.objects.all(),
    #            "comp": compagnie.objects.all(),
    #            "hr_dp": heure_depart.objects.all(),
    #            "ln": ligne.objects.all(),
    #            "lesdates": rslt,
    #            }
    # return render(request, 'resultats.html', context)


# def requete_view(self):
#     with connection.cursor() as cursor:
        # cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        # cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        # cursor.execute("SELECT heure_depart.l_heure,ville.nom_ville,ville.nom_ville,comppagnie.nom_cp,ligne.prix FROM infoligne \
        #                JOIN heure_depart ON heure_depart.id=heure_dep \
        #                JOIN ligne ON ligne.id=ligne_id \
        #                JOIN v_depart ON v_depart.id=ville_dep \
        #                JOIN v_arrivee ON v_arrivee.id=ville_arr \ 
        #                JOIN ville ON ville.id=v_depart.ville_id \
        #                JOIN ville ON ville.id=v_arrivee.ville_id \
        #                JOIN date_depart ON date_depart.id=date_dep \ 
        #                JOIN bus ON bus.id=bus_id \
        #                JOIN compagnie ON compagnie.id=compagnie_id \
        #                WHERE date_depart.ladate='val'")
        # row = cursor.fetchone()

    # return row
