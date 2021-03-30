from django.http import HttpResponse
import datetime

def saludo(request):    # primera vista

    documento = """<html>
    <body>
    <h1>
    HOLA MUNDO!!
    </h1>
    </body>
    </html>"""

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Adiós!")

def fecha(requst):
    fecha_actual = datetime.datetime.now()

    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calcula_edad(request, edad, year):

    periodo = year - 2021
    edad_futura = edad + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años</html></body></h2>" %(year, edad_futura)

    return HttpResponse(documento)