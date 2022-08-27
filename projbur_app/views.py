from django.shortcuts import render
import psycopg2

from .models import *


# Create your views here.
def index(request):
    data_ref_equip = RefEquip.objects.all()
    data_ref_obj = RefObj.objects.all()
    data_ref_sys = RefSys.objects.all()
    context = {
        'ref_equip':data_ref_equip,
        'ref_obj':data_ref_obj,
        'ref_sys':data_ref_sys
        } 
    return render(request,"projbur_app/index.html", context)