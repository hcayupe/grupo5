from django.shortcuts import render
from .models import SliderIndex, SliderGaleria, MisionVision,Insumos

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as login_autent
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index(request):
    autos = SliderIndex.objects.all()
    return render(request,'web/index.html',{'autos':autos})

@login_required(login_url='/login/')
@permission_required('myCarW.add_insumos',login_url='/login/')
@permission_required('myCarW.view_insumos',login_url='/login/')
def insumos(request):
    if request.POST:
        nombre = request.POST.get("nombreinsumo")
        precio = request.POST.get("precio")
        descripcion = request.POST.get("descripcion")
        stock = request.POST.get("stock")
        
        insumo = Insumos(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            stock=stock
        )
        insumo.save()
        return render(request,'web/insumos.html',{'msg':'Insumo registrado'})

    return render(request,'web/insumos.html')

@login_required(login_url='/login/')
@permission_required('myCarW.change_insumos',login_url='/login/')
@permission_required('myCarW.view_insumos',login_url='/login/')
def modi_insumos(request):
    if request.POST:
        nombre = request.POST.get("nombreinsumo")
        precio = request.POST.get("precio")
        descripcion = request.POST.get("descripcion")
        stock = request.POST.get("stock")

        try:
            insumo = Insumos.objects.get(nombre=nombre)
            insumo.precio = precio
            insumo.descripcion = descripcion
            insumo.stock = stock
            insumo.save()
            msg ='Insumo actualizado'
        except:
            msg ='Insumo no actualizado'
    insumos = Insumos.objects.all()   
    return render(request,'web/admi_insumo.html',{'insumos':insumos,'msg':msg})

@login_required(login_url='/login/')
@permission_required('myCarW.view_insumos',login_url='/login/')
@permission_required('myCarW.change_insumos',login_url='/login/')
def modificar(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        return render(request,'web/modificar.html',{'insumo':insumo})
    except:
        msg="No existe le insumo"
    insumos = Insumos.objects.all()   
    return render(request,'web/admi_insumo.html',{'insumos':insumos,'msg':msg})

@login_required(login_url='/login/')
@permission_required('myCarW.view_insumos',login_url='/login/')
@permission_required('myCarW.change_insumos',login_url='/login/')
def admin_insumos(request):
    insumos = Insumos.objects.all()
    return render(request,'web/admi_insumo.html',{'insumos':insumos})

@login_required(login_url='/login/')
@permission_required('myCarW.delete_insumos',login_url='/login/')
def eliminar(request,id):
    try:
       insumo = Insumos.objects.get(nombre=id)
       insumo.delete()
       msg = "Insumo eliminado"
    except:
       msg = "Insumo no eliminado"
    insumos = Insumos.objects.all()   
    return render(request,'web/admi_insumo.html',{'insumos':insumos,'msg':msg})   


@login_required(login_url='/login/')
def ubicacion(request):
    return render(request,'web/ubicacion.html')
     
@login_required(login_url='/login/')   
def galeria(request):
    gale = SliderGaleria.objects.all()
    return render(request,'web/galeria.html',{'gale':gale})

@login_required(login_url='/login/')
def laEmpresa(request):
    emp = MisionVision.objects.all()
    return render(request,'web/la_empresa.html',{'emp':emp})

def registro(request):
    if request.POST:
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        usuario = request.POST.get("nomusuario")
        password = request.POST.get("contrasena")
        password2 = request.POST.get("contrasena2")

        if password != password2:
            return render(request,'web/registro.html',{'msg':'Contraseñas no conciden'})
        
        try:
            u = User.objects.get(username=usuario)
            return render(request,'web/registro.html',{'msg':'El usuario ya existe'})
        except:
            
            u = User()
            u.username = usuario
            u.first_name = nombre
            u.last_name = apellido
            u.email = correo
            u.set_password(password)
            u.save()

            us = authenticate(request, username=usuario,password=password)
            login_autent(request,us)
            autos = SliderIndex.objects.all()
            return render(request,'web/index.html',{'user':us,'autos':autos})
    return render(request,'web/registro.html')

def login(request):
    if request.POST:
        usuario = request.POST.get("txtusuario")
        password = request.POST.get("txtclave")
        us = authenticate(request, username=usuario,password=password)
        if us is not None and us.is_active:
            login_autent(request,us)
            autos = SliderIndex.objects.all()
            return render(request,'web/index.html',{'user':us,'autos':autos})
        else:
            return render(request,'web/login.html',{'msg':'Usuario o Contraeña incorrecta'})  
    return render(request,'web/login.html')

@login_required(login_url='/login/')        
def logout_vista(request):
    logout(request)
    autos = SliderIndex.objects.all()
    return render(request,'web/index.html',{'autos':autos})

