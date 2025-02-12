from django.shortcuts import render , HttpResponse

# Create your views here.

def home(request):
    html_response = "<hl> mi pagina web</hl>"
    for i in range(10):
        html_response += "<cp> Esto es la portada</p>"
    return HttpResponse(html_response)