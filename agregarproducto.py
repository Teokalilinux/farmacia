import os
import django




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webfarma.settings')


django.setup()

if not django.apps.apps.ready:
    raise Exception("El registro de aplicaciones no ha sido cargado aún.")
from mi_app.models import Producto

import decimal

def agregarProducto():
  print("Bienvenido a tu almacen donde cargaras todos los datos de tus productos  ")
  ok = True 
  while ok:
    menu = input("Para comenzar presiona E para salir presiona Q ,para borrar todo presiona D  ")
    while True:
      if menu.lower() == "d":
        seguro = input ("estas seguro?, presiona si ,de lo contrario presiona cualquier otra tecla")
        if seguro == "si":
          print("ya hemos borrado todo")
          Producto.objects.all().delete()
          break
        else:
          print("La Base de datos continua")
          break
      if menu == "q" or menu == "Q": 
       print("Adios!")
       ok = False
       break
      if menu == "e" or menu == "E":
      
        print("Agreguemos un nuevo producto!")
        nombre = input("Ingrese Nombre del Producto ")
        if nombre.lower() == "q": 
          print("Adios!")
          ok= False
          break
        droga = input("Ingrese el nombre de la droga ")
    
        while True:
           try:
             stock = int(input("Indique el número de stock: "))
             break
           except ValueError:
               print("Por favor, ingrese un número válido para el stock. ")
            
        while True:
          try:
            precio = decimal.Decimal(input("Escriba el precio inicial que desea ponerle: "))
            break
          except decimal.InvalidOperation:
            print("Por favor, ingrese un precio válido. ")

        producto = Producto(
           nombre=nombre,
           droga=droga,
           stock=stock,
           precio=precio,
        )
        guardado = input("Deseas guardar? , escribe 'y' si es un si ,de lo contrario presiona cualquier tecla  ")
        if guardado.lower()== "y":
          print("biennn")
          producto.save()
          print("Su producto",producto.nombre," fue guardado exitosamente")
          from django.core.management import call_command
          call_command('makemigrations')
          call_command('migrate')
          print("Migración realizada con éxito")
          break
        else:
          print("Error al guardar el producto,producto eliminado")
    else:
      if  menu !="q" and menu != "Q":
        print("Por favor presione E para iniciar o Q para salir")
agregarProducto()
      



