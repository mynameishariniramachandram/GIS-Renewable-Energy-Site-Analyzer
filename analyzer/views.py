from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from pathlib import Path

from .energy_data import get_satellite_data
from .ml_model import predict_energy
from .scoring import renewable_score
from .village_planner import plan_village
from .forecast import energy_forecast

BASE_DIR=Path(__file__).resolve().parent

def home(request):

    return render(request,"analyzer/home.html")

def district_data(request):

    df=pd.read_csv(BASE_DIR/"data/districts.csv")

    return JsonResponse(df.to_dict(orient="records"),safe=False)

def analyze(request):

    lat=request.GET.get("lat")
    lon=request.GET.get("lon")

    solar,wind,cloud,temp=get_satellite_data(lat,lon)

    energy=predict_energy(solar,temp,wind)

    score,label=renewable_score(solar,wind,temp)

    return JsonResponse({

    "solar":solar,
    "wind":wind,
    "energy":energy,
    "score":score,
    "label":label

    })

def village(request):

    houses=int(request.GET.get("houses"))

    result=plan_village(houses,5.5,4)

    return JsonResponse(result)

def forecast(request):

    lat=request.GET.get("lat")
    lon=request.GET.get("lon")

    data=energy_forecast(lat,lon)

    return JsonResponse(data,safe=False)
def home(request):
    return render(request, "analyzer/home.html")