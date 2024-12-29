from django.db import models

class Producto (models.Model):
    nombre = models.CharField(max_length=30)
    droga = models.CharField(max_length=30)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=10,decimal_places=5)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return self.nombre