from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm


# Create your views here.
def home(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'GestionUsuarios/home.html', context)


def add(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UsuarioForm()
    context = {'form': form}
    return render(request, 'GestionUsuarios/add.html', context)


def delete(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.delete()
    return redirect('home')


def update(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UsuarioForm(instance=usuario)

    context = {'form': form}
    return render(request, 'GestionUsuarios/update.html', context)


def login(request):
    if request.method == 'POST':
        try:
            usuario = Usuario.objects.get(Usuario=request.POST['correo'], Contrasena=request.POST['pwd'])
            print('Usuario', usuario)
            request.session['Usuario'] = usuario.Usuario
            return redirect('home')
        except:
            print('fallo')
    return render(request, 'GestionUsuarios/login.html')


def logout(request):
    try:
        del request.session['Usuario']
        print('elimina')
        return redirect('login')
    except:
        print('fallo salir sesion')
        return render(request, 'GestionUsuarios/login.html')
    return render(request, 'GestionUsuarios/login.html')
