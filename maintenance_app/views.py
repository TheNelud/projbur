from django.shortcuts import render
from .models import *
from django.http import FileResponse, Http404, HttpResponse
import os

# def pdf(request):
#     with open('static/maintenance_app/pdf/keys.pdf', 'rb') as pdf:
#         response = HttpResponse(pdf.read(),content_type='application/pdf')
#         response['Content-Disposition'] = 'filename=keys.pdf'
#         return response
    # try:
    #     filepath = os.path.join('static/maintenance_app/pdf', 'keys.pdf')
    #     return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    # except FileNotFoundError:
    #     raise Http404('not found')

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