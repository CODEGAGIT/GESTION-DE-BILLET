from django.urls import path
from . import views

app_name="akst"

urlpatterns = [
    path('',views.accueil_view,name='index'),
    # path('resultats/',views.resultats_view,name='resultats'),
    path('base/',views.base_view,name='view'),
    # path('<int:bus_id>/',views.bus_view,name='show'),
    # path('resultats/',views.result_view,name='resultats'),
    path('<int:date_depart_id>/',views.result,name='result'),
    # path(''),
]