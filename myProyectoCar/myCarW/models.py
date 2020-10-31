from django.db import models

# Create your models here.
class SliderIndex(models.Model):
    ident = models.CharField(max_length=40,primary_key=True)
    imagen = models.ImageField(upload_to='car',null=True)

    def __str__(self):
        return self.ident


class SliderGaleria(models.Model):
    ident = models.CharField(max_length=40,primary_key=True)
    slider1 = models.ImageField(upload_to='car',null=True)
    slider2 = models.ImageField(upload_to='car',null=True)

    def __str__(self):
        return self.ident

class MisionVision(models.Model):
    ident = models.CharField(max_length=40,primary_key=True)
    mision = models.TextField()
    vision = models.TextField()

    def __str__(self):
        return self.ident


class Insumos(models.Model):
    nombre = models.CharField(max_length=120,primary_key=True)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre