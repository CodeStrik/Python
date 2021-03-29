from django.http import HttpResponse

def saludo(request):    # primera vista

    return HttpResponse("Hola Mundo!")

def despedida(request):

    return HttpResponse("Adiós!")