from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from App.models import DataUser

login_required()
def index(request):
    return render(request, 'general/template.html')

@csrf_exempt
def registro(request):
    return render(request, 'registration/registro.html')

@csrf_exempt
def login(request):
    return render(request, 'registration/login.html')

def deslogout(request):
    logout(request)
    return redirect('/')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            error_message = 'Usuario o contraseña incorrectos'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

@csrf_exempt
def enviar_nombre_usuario(request):
    usuario = request.user
    nombre_usuario = usuario.username
    data = {
        'nombre_usuario': nombre_usuario
    }
    print(nombre_usuario)
    return JsonResponse(data)

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        gmail = request.POST.get('gmail')
        descripcion = request.POST.get('descripcion')
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contrasena')
        imagen = request.FILES.get('imagen')

        # Verificar si el usuario ya está registrado
        if User.objects.filter(username=usuario).exists():
            return JsonResponse({'message': 'El usuario ya está registrado.'})

        # Crear el usuario en Django
        user = User.objects.create_user(username=usuario, password=contraseña)
        user.first_name = nombre
        user.last_name = apellidos
        user.email = gmail
        user.save()

        # Guardar datos adicionales en el modelo DataUser si es necesario
        data_user = DataUser(
            Nombre=nombre,
            Apellidos=apellidos,
            Gmail=gmail,
            Descripcion=descripcion,
            Usuario=user,
            Imagen=imagen
        )
        data_user.save()

        return JsonResponse({'message': 'Usuario creado correctamente.'})
    else:
        return JsonResponse({'message': 'Método no permitido.'})