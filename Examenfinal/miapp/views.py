from django.shortcuts import render, HttpResponse


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




