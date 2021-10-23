from django.shortcuts import render, redirect
from .models import Integrante, Proyecto, Catalogo, Historia
from .forms import IntegranteForm, ProyectoForm
from django.template import RequestContext



# Create your views here.
def home(request):
    proyectos = Proyecto.objects.all()
    context = {'proyectos': proyectos}
    return render(request, 'GestionUsuarios/home.html', context)

def historias(request):
    historias = Historia.objects.all()
    context = {'proyectos': historias}
    return render(request, 'GestionUsuarios/historias.html', context)


def start(request):
    return render(request, 'GestionUsuarios/start.html')


def addProject(request):
    print (request.method)
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProyectoForm()
    context = {'form': form}
    return render(request, 'GestionUsuarios/addProject.html', context)


def addMember(request):
    roles = Catalogo.objects.all()
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EquipoForm()
    context = {'form': form, 'roles': roles}
    return render(request, 'GestionUsuarios/addMember.html', context)


def delete(request, usuario_id):
    usuario = Integrante.objects.get(codigo=usuario_id)
    usuario.delete()
    return redirect('home')


def update(request, usuario_id):
    usuario = Integrante.objects.get(codigo=usuario_id)
    if request.method == 'POST':
        form = IntegranteForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IntegranteForm(instance=usuario)

    context = {'form': form}
    return render(request, 'GestionUsuarios/update.html', context)


def login(request):
    if request.method == 'POST':
        try:
            usuario = Integrante.objects.get(usuario=request.POST['correo'], contrasena=request.POST['pwd'])
            print('Usuario', usuario.nombre)
            request.session['Usuario'] = usuario.usuario
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




def handler404(request, exception):
    response = render(request, 'GestionUsuarios/404.html')
    return response


def handler500(request):
    response = render(request, 'GestionUsuarios/500.html')
    return response

def handler403(request, exception):
    response = render(request, 'GestionUsuarios/403.html')
    return response
