from django.urls import path
from . import views

app_name="akst"

urlpatterns = [
    path('',views.accueil_view,name='index'),
    path('<int:date_depart_id>/',views.result,name='result'),
    path('<int:reserv_id>/',views.reserv,name='reservation'),
    path('suggestion/',views.suggestionForm,name='suggestion')
]