from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Personas

# Create your views here.

layout = """
    <h1> Proyecto Web (LP3 - 2024) | Henry Fabian </h1>
    <hr/>
    <ul>
        <li>
            <a href="/personas"> Personas</a>
        </li>
        
    </ul>
    <hr/>
"""


def index(request):
    mensaje="""
        <h1>Nombre de personas</h1>
    """
    return HttpResponse(layout + mensaje)

def crear_personas(request):
    Personas = Personas(
        nombre = "La persona posee nombre",
        apellido = "La persona posee apellido",
        sexo= "sexo de la persona M o F"
        fecha_de_registro = True
    )
    Personas.save()
    return HttpResponse(f"Persona Creada: {Personas.nombre} - {Personas.apellido} - {Personas.sexo}")


