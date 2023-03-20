from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader


def saludar(request):
    return HttpResponse("Hola Mundo!")

def segunda_vista(request):
    return HttpResponse("Ya entendi!! esto parece ser bastante facil!!!")

def dia_de_hoy(request):
    dia=datetime.datetime.today()
    cadena=f"Hoy es {dia}"
    return HttpResponse(cadena)

def saludo_con_nombre(request, nombre):
    return HttpResponse(f"Hola {nombre} como estas! aca la comi 51325 te saluda!")


def calcula_anio_nacimiento(request, edad):
    anio_actual=datetime.datetime.today().year
    anio_nacimiento=anio_actual-int(edad)
    return HttpResponse(f"Usted nacio en el anio {anio_nacimiento}")

""" def probandoHtml(request):

    diccionario={"nombre":"Juan", "apellido":"Perez", "edad":25, "lista":[10,5,2,7,8,3,8,10]}

    archivo=open(r"H:\CODERHOUSE\51325\clase17\proyecto1\Plantillas\template1.html")

    texto=archivo.read()
    archivo.close()

    template=Template(texto)
    contexto=Context(diccionario)
    documento=template.render(contexto)
    return HttpResponse(documento) """



def probandoHtml(request):

    diccionario={"nombre":"Juan", "apellido":"Perez", "edad":25, "lista":[10,5,2,7,8,3,8,10]}

    template=loader.get_template("template1.html")
    
    documento=template.render(diccionario)
    return HttpResponse(documento)
