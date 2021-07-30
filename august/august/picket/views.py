from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# accept a request, return simple string
def home(request):
    return HttpResponse("API Service: You're looking at Picket")

def signup(request):
    return HttpResponse(f"Account Registration {datetime.now()}: You need an Algoritma email for this service.")
