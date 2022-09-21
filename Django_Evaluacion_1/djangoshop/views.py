from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'djangoshop/index.html')

def usuario(request):
    data = {
        'id': '20104',
        'nombre': 'Jose',
        'email': 'jose@gmail.com'
    }
    return HttpResponse(f'<p>Id : {data["id"]}</p> <p>Nombre : {data["nombre"]}</p> <p>Correo electrónico : {data["email"]}</p>')

def juguetes(request):
    return render(request, 'djangoshop/juguetes.html')

def ropa(request):
    return render(request, 'djangoshop/ropa.html')