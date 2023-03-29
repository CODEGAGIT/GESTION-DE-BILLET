from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import suggestion, client
from django.db import connection
from companyman.models import infoligne,bus,ligne,ville,v_arrivee,v_depart,date_depart,heure_depart
from dashboard.models import compagnie
from .forms import SuggestionForm
import datetime



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


def result(request, date_depart_id):
    context = {"rdt": get_object_or_404(date_depart, pk=date_depart_id),
               "infln": infoligne.objects.all().filter(date_dep=date_depart_id).order_by('ligne_id'),
               }
    return render(request, 'result.html', context)

def reserv(request, reserv_id):

    return render(request, 'templates/pages/doreserv.html')

def suggestionForm(request):
    form=SuggestionForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'suggestion.html',{'form':form})