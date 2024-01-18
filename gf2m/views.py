from django.shortcuts import render
import ctypes
from ctypes import CDLL, c_int

# Create your views here.
def start(request):
    return render(request, "gf2m/start.html")

def index(request):
    return render(request, "gf2m/index.html")

def add(request):
    return render(request, 'gf2m/add.html')

def addition(request):
    gf = ctypes.CDLL('/home/dave/projects/GaloisFields/gf2m/external/gf2m/gf.so')
    if request.method == 'POST':
        num1 = int(request.POST.get('num1', 0))
        num2 = int(request.POST.get('num2', 0))
        
        resultado = gf.gf_add(c_int(num1), c_int(num2))
        
        return render(request, 'gf2m/addition.html', {'resultado': resultado})
    return render(request, 'gf2m/addition.html')

def multiplication(request):
    gf = ctypes.CDLL('/home/dave/projects/GaloisFields/gf2m/external/gf2m/gf.so')
    if request.method == 'POST':
        num1 = int(request.POST.get('num1', 0))
        num2 = int(request.POST.get('num2', 0))
        
        resultado = gf.gf_mul(c_int(num1), c_int(num2))
        
        return render(request, 'gf2m/multiplication.html', {'resultado': resultado})
    return render(request, 'gf2m/multiplication.html')

def division(request):
    gf = ctypes.CDLL('/home/dave/projects/GaloisFields/gf2m/external/gf2m/gf.so')
    if request.method == 'POST':
        num1 = int(request.POST.get('num1', 0))
        num2 = int(request.POST.get('num2', 0))
        
        resultado = gf.gf_frac(c_int(num1), c_int(num2))
        
        return render(request, 'gf2m/division.html', {'resultado': resultado})
    return render(request, 'gf2m/division.html')

def polyoperations(request):
    return render(request, "gf2m/polyoperations.html")