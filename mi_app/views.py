# mi_app/views.py
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from mi_app.models import Producto
from csp.decorators import csp
def index(request):
    return render(request, 'index.html')



@csp(SCRIPT_SRC=["'self'", "http://localhost:8000/"])
def mi_vista(request):
    
    return HttpResponse("Hola, mundo!")

from django.http import JsonResponse

def reducirSTOCK(request):
    if request.method == 'POST':
        try:
            producto = Producto.objects.get(id=2)
            producto.stock -= 1
            if producto.stock <= 2:
                print("Cuidado: poco stock")
            producto.save()
            return JsonResponse({'mensaje': 'Stock reducido correctamente'})
        except Producto.DoesNotExist:
            return JsonResponse({'error': 'Producto no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Error al reducir stock: {str(e)}'}, status=500)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

      
