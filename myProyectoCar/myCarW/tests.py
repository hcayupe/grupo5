from django.test import TestCase 
import unittest
from .models import Insumos,MisionVision



# Create your tests here.
class TestCasos(unittest.TestCase):

    def test_insumo(self):
        valor =0
        try:
            i = Insumos(nombre="aspiradora",
                 precio=3000,
                 descripcion="limpia bien",
                 stock=1)
            i.save()
            valor =1
        except:
            valor = 0
        self.assertEqual(valor, 1)

    def test_misionvision(self):
        valor =0
        try:
            mv = MisionVision(ident="tercera",
                mision="Aca esta el mision",
                vision="Aca esta la vision")
            mv.save()
            valor =1
        except:
            valor = 0
        self.assertEqual(valor, 1)


