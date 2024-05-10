from django.shortcuts import render
from sim3_api.models import sim3
from django.http import JsonResponse

# Create your views here.
def sim3_list(request):
    simtri = sim3.objects.all() # Complex Date
    simtri_Python = list(simtri.values()) # Python DS
    return JsonResponse({
        'simtri': simtri_Python
    })