from django.contrib import admin
from django.urls import path, include
from .views import index, galeria, insumos,ubicacion,laEmpresa, registro, login, logout_vista,admin_insumos,eliminar,modificar,modi_insumos

urlpatterns = [
    
    path('',index,name='INDX'),
    path('galeria/',galeria,name='GALE'),
    path('insumos/',insumos,name='INSU'),
    path('ubicacion/',ubicacion,name='UBI'),
    path('laEmpresa/',laEmpresa,name='EMPRE'),
    path('registro/',registro,name='REGIS'),
    path('login/',login,name='LOGIN'),
    path('logout_vista/',logout_vista, name='LOGOUT'),
    path('admin_insumos/',admin_insumos, name='ADMI'),
    path('eliminar/<id>/',eliminar, name="DELETE"),
    path('modificar/<id>/',modificar,name='MODI'),
    path('modi_insumos/',modi_insumos,name='MODIIN'),

]