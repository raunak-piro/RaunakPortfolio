from django.shortcuts import render
from mainApp.models import *
def home(Request):
    data =portfolio.objects.all()
    
    return render(Request,'index.html',{'data':data})

# Create your views here.