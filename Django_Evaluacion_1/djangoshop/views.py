from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'djangoshop/index.html')

def usuario(request):
    id =  '20104'
    nombre = 'Jose'
    email = 'jose@gmail.com'

    page = f"""
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Usuario</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
    </head>
    <body>
    <div class="container text-center">
        <h1 class="m-5">Informacion Usuario</h1>
        <div class="card border-0" style="width: 18rem;">
            <img src="../static/images/user.jpg" class="card-img-top rounded-circle" alt="...">
            <div class="card-body">
                <h5 class="card-title">{nombre}</h5>
                <div class="col">
                    <div class="row mb-2">rut: {id}</div>
                    <div class="row">Correo electrónico: {email}</div>
                </div>
            </div>
        </div>
    <a href="/" class="btn btn-primary">Volver</a>
    </div>
    
    
    </body>
    """

    return HttpResponse(page)

def productos(request, tipo):
    if (tipo == 'ropa'):
        data = {
            'producto': tipo,
            'product1_name': 'Regatta',
            'product1_description': 'parka',
            'product1_price': 24990,
            'product2_name': 'Aziz',
            'product2_description': 'Polera estampada',
            'product2_price': 12990,
            'product3_name': 'Barbados',
            'product3_description': 'Chaqueta Sherpa Oversize',
            'product3_price': 27990,
        }
    elif (tipo == 'juguetes'):
        data = {
            'producto': tipo,
            'product1_name': 'Iron Studio',
            'product1_description': 'Figura Iron Studio Mandalorian Scala 110 Original',
            'product1_price': 139990,
            'product2_name': 'Banpresto',
            'product2_description': 'Dragon Ball Z G Materia The Krillin',
            'product2_price': '21990',
            'product3_name': 'Funko',
            'product3_description': 'Funko Pop! Doctor Strange Multiverse of Madness - Doctor Strange 1000',
            'product3_price': 12990,
        }
    else:
        return render(request, 'djangoshop/notfound.html')
    return render(request, 'djangoshop/productos.html', data)
