from django.shortcuts import render
from .models import *
# Create your views here.
def maintenance(request):
    data_to_repairs = ToRepairs.objects.all()
    data_to_services = ToServices.objects.all()
    data_to_shedule = ToShedule.objects.all()

    context = {
        'to_repairs':data_to_repairs,
        'to_services':data_to_services,
        'to_shedule':data_to_shedule,
    }
    return render(request, "maintenance_app/maintenance.html", context)