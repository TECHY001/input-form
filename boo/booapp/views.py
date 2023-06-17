from django.shortcuts import render
from django.http import HttpResponse
from .function import ufile

# Create your views here.
def home(request):
      return render(request,'index.html')

def product(request):
    mobile=request.POST['mob']
    keyboard=request.POST['keyboard']
    prince=int(mobile)+int(keyboard)
    

    return render(request,'result.html',{'Price':prince})
