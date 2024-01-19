from cffi import FFI

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def start(request):
    return render(request, "gf2m/start.html")

def index(request):
    return render(request, "gf2m/index.html")

def add(request):
    return render(request, 'gf2m/add.html')



ffi = FFI()

# Cargar la biblioteca compartida
try:
    gf = ffi.dlopen('/home/dave/projects/GaloisFields/gf2m/external/gf2m/gf.so')
except OSError as e:
    print(f'Error al cargar la biblioteca: {e}')
    JsonResponse({'error': 'Error al cargar la biblioteca'})

# Definir la interfaz de la función gf_add
ffi.cdef("""
typedef uint16_t gf;
gf gf_add(gf in0, gf in1);
gf gf_mul(gf in0, gf in1);
gf gf_frac(gf in0, gf in1);
""")

# Función para manejar la adición
def addition(request):
    if request.method == 'POST':
        try:
            num1 = ffi.cast('gf', int(request.POST.get('num1', 0)))
            num2 = ffi.cast('gf', int(request.POST.get('num2', 0)))
        except ValueError as ve:
            print(f'Error al convertir números: {ve}')
            return JsonResponse({'error': 'Error al convertir números'})

        try:
            resultado = gf.gf_add(num1, num2)
        except Exception as e:
            print(f'Error al llamar a la función: {e}')
            return JsonResponse({'error': 'Error al llamar a la función'})

        return JsonResponse({'resultado': resultado})
    return render(request, 'gf2m/addition.html')

# Función para manejar la multiplicación
def multiplication(request):
    if request.method == 'POST':
        try:
            num1 = ffi.cast('gf', int(request.POST.get('num1', 0)))
            num2 = ffi.cast('gf', int(request.POST.get('num2', 0)))
        except ValueError as ve:
            print(f'Error al convertir números: {ve}')
            return JsonResponse({'error': 'Error al convertir números'})

        try:
            resultado = gf.gf_mul(num1, num2)
        except Exception as e:
            print(f'Error al llamar a la función: {e}')
            return JsonResponse({'error': 'Error al llamar a la función'})

        return JsonResponse({'resultado': resultado})
    return render(request, 'gf2m/multiplication.html')

# Función para manejar la división
def division(request):
    if request.method == 'POST':
        try:
            num1 = ffi.cast('gf', int(request.POST.get('num1', 0)))
            num2 = ffi.cast('gf', int(request.POST.get('num2', 0)))
        except ValueError as ve:
            print(f'Error al convertir números: {ve}')
            return JsonResponse({'error': 'Error al convertir números'})

        try:
            resultado = gf.gf_frac(num1, num2)
        except Exception as e:
            print(f'Error al llamar a la función: {e}')
            return JsonResponse({'error': 'Error al llamar a la función'})

        return JsonResponse({'resultado': resultado})
    return render(request, 'gf2m/division.html')


def polyoperations(request):
    return render(request, "gf2m/polyoperations.html")