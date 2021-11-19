from django.shortcuts import render
from django.http import HttpResponse
from gestionpedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionpedidos.forms import FormContacto

# Create your views here.
def busqueda_productos(request):
    return render(request, "busqueda_productos.html")
def buscar(request):
    if request.GET["prd"]:
        #mensaje = "articulo buscado: %r" %request.GET["prd"] #para probar que llega al servidor
        producto = request.GET["prd"]
        if len(producto)>25:
            mensaje = "texto de busqueda muy largo"
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "resultado_busqueda.html", {"articulos": articulos, "query": producto})

    else:
        mensaje = "no se introdujo nada" #para probar que llega al servidor

    return HttpResponse(mensaje) #para probar que llega al servidor
"""
def contacto(request):
    if request.method=="POST":

        subject=request.POST["asunto"]
        message=request.POST["mensaje"] + " " + request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["ramndiazgzmn@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)

        return render(request,"gracias.html")

    return render(request,"contacto.html")
"""
def contacto(request):
    if request.method=="POST":
        miFormulario = FormContacto(request.POST)
        if miFormulario.is_valid():
            infForm = miFormulario.cleaned_data
            send_mail(infForm['asunto'], infForm['mensaje'], infForm.get('email', ''), ['ramndiazgzmn@gmail.com'],)
            return render(request,"gracias.html")
    else:
        miFormulario = FormContacto
    return render(request,"form_contacto.html", {"form": miFormulario})
