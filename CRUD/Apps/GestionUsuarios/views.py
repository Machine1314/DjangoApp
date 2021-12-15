from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.db import connection
from django.shortcuts import render, redirect
from .forms import *
import datetime


# Create your views here.
def callSP(request):
    with connection.cursor() as cursor:
        zona = 'America/Guayaquil'
        cursor.execute('SET TIMEZONE="{}"'.format(zona))
        cursor.execute('call insert_bulk()')
    return redirect('home')


def home(request):

    try:
        rolobject = Rol.objects.get(descripcion__icontains='admin')
        codrol = rolobject.codigo
        usuario = Integrante.objects.get(usuario=request.session['Usuario'])
        rol = usuario.rol.descripcion
        if 'dmin' not in request.session['Usuario']:
            proyectos = Proyecto.objects.filter(equipo_Asociado=request.session['equipo']).order_by('codigo')
            context = {'proyectos': proyectos, 'rol': rol}
            return render(request, 'GestionUsuarios/home.html', context)
        else:
            integrantes = Integrante.objects.exclude(rol=codrol).order_by('codigo')
            context = {'usuarios': integrantes, 'rol': rol}
            return render(request, 'GestionUsuarios/home.html', context)
    except Exception:
        messages.success(request, 'No estás ingresado en el sistema!')
        return redirect('login')


def tables(request):
    rol = Rol.objects.all().order_by('codigo')
    estado = Estado.objects.all().order_by('codigo')
    context = {'roles': rol, 'estados': estado}
    return render(request, 'GestionUsuarios/tables.html', context)


def teams(request):
    equipos = Equipo.objects.all().order_by('codigo')
    context = {'equipos': equipos}
    return render(request, 'GestionUsuarios/teams.html', context)


def login(request):
    zona = 'America/Guayaquil'
    with connection.cursor() as cursor:
        cursor.execute('SET TIMEZONE="{}"'.format(zona))
    if request.method == 'POST':
        try:
            if 'nalgona' in request.POST['correo'] and 'tengo21' in request.POST['pwd']:
                return render(request, 'GestionUsuarios/birthday.html')
            usuario = Integrante.objects.get(usuario=request.POST['correo'])
            if check_password(request.POST['pwd'], usuario.contrasena):
                request.session['Usuario'] = usuario.usuario
                request.session['rol'] = usuario.rol.descripcion
                if 'admin' not in usuario.usuario:
                    request.session['equipo'] = usuario.equipo.codigo
                return redirect('home')
            else:
                messages.success(request, 'Contraseña incorrecta!')
                return redirect('login')
        except Exception as e:
            if request.POST['pwd'] != '':
                messages.success(request, 'Usuario no existe!')
            context = {'message': e}
    return render(request, 'GestionUsuarios/login.html')

def logout(request):
    try:
        if 'dmin' not in request.session['Usuario']:
            del request.session['equipo']
        del request.session['Usuario']
        del request.session['rol']
        return redirect('login')
    except Exception as e:
        print('fallo salir sesion ', e)
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


def addTeam(request):
    equipo = Equipo.objects.order_by('-codigo').first()
    maxcod = equipo.codigo + 1
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro creado de manera exitosa!')
            return redirect('teams')
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('teams')
    else:
        form = EquipoForm(initial={'codigo': maxcod})
    context = {'form': form}
    return render(request, 'GestionUsuarios/addTeam.html', context)


def updateTeam(request, id):
    equipo = Equipo.objects.get(codigo=id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro actualizado de manera exitosa!')
            return redirect('teams')
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('teams')
    else:
        form = EquipoForm(instance=equipo)
    context = {'form': form, 'cod': id}
    return render(request, 'GestionUsuarios/updateTeam.html', context)


def deleteTeam(request, id):
    team = Equipo.objects.get(codigo=id)
    team.delete()
    messages.success(request, 'Registro eliminado con éxito!')
    return redirect('teams')


def addRol(request):
    rol = Rol.objects.order_by('-codigo').first()
    maxcod = rol.codigo + 1
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro creado de manera exitosa!')
            return redirect('tables')
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('tables')
    else:
        form = RolForm(initial={'codigo': maxcod})
    context = {'form': form}
    return render(request, 'GestionUsuarios/addRol.html', context)


def updateRol(request, id):
    rol = Rol.objects.get(codigo=id)
    if request.method == 'POST':
        form = RolForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro actualizado de manera exitosa!')
            return redirect('tables')
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('tables')
    else:
        form = RolForm(instance=rol)
    context = {'form': form, 'cod': id}
    return render(request, 'GestionUsuarios/updateRol.html', context)


def deleteRol(request, id):
    rol = Rol.objects.get(codigo=id)
    rol.delete()
    messages.success(request, 'Registro eliminado de manera exitosa!')
    return redirect('tables')


def addStatus(request):
    estado = Estado.objects.order_by('-codigo').first()
    maxcod = estado.codigo + 1
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro creado de manera exitosa!')
            return redirect('tables')
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('tables')
    else:
        form = EstadoForm(initial={'codigo': maxcod})
    context = {'form': form}
    return render(request, 'GestionUsuarios/addStatus.html', context)


def updateStatus(request, id):
    estado = Estado.objects.get(codigo=id)
    if request.method == 'POST':
        form = EstadoForm(request.POST, instance=estado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro actualizado de manera exitosa!')
            return redirect('tables')
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('tables')
    else:
        form = EstadoForm(instance=estado)
    context = {'form': form, 'cod': id}
    return render(request, 'GestionUsuarios/updateStatus.html', context)


def deleteStatus(request, id):
    estado = Estado.objects.get(codigo=id)
    estado.delete()
    messages.success(request, 'Registro eliminado de manera exitosa!')
    return redirect('tables')


def metrica(request, proyecto_id):
    today = datetime.date.today()
    with connection.cursor() as cursor:
        cursor.execute('''CALL public.insert_time({},'{}')'''.format(str(proyecto_id), str(today)))
    tiemposActuales = []
    tiemposIdeales = []
    fechas = []
    equipo = Proyecto.objects.filter(codigo=proyecto_id).values_list('equipo_Asociado', flat=True)[0]
    queryset = Integrante.objects.filter(equipo=equipo).values_list('capacidad', flat=True)
    value = Tiempos.objects.filter(fecha=today, proyecto_id=proyecto_id).values_list('tiempo_Ideal', 'tiempo_Actual')
    ideal = 0 if value[0][0] is None else value[0][0]
    actual = 0 if value[0][0] is None else value[0][1]
    for p in Tiempos.objects.filter(proyecto_id=proyecto_id).order_by('id'):
        if p.tiempo_Actual is not None:
            tiemposActuales.append(p.tiempo_Actual)
        tiemposIdeales.append(p.tiempo_Ideal)
        fechas.append(p.fecha.strftime('%Y-%m-%d'))
    if actual - ideal > queryset[0]:
        cod = Historia.objects.filter(proyecto_Asociado=proyecto_id).values_list('codigo', flat=True)
        tareas = Tarea.objects.filter(historia_Asociada=cod[0]).exclude(tiempo=0)
        messages.success(request, 'Aviso: Diferencia entre tendencias significable!')
        context = {'dates': fechas, 'tendencia': tiemposIdeales, 'actual': tiemposActuales, 'tareas': tareas}
    else:
        context = {'dates': fechas, 'tendencia': tiemposIdeales, 'actual': tiemposActuales}
    return render(request, 'GestionUsuarios/metrica.html', context)


def historias(request, proyecto_id):
    try:
        hist = []
        val = 0
        cursor = connection.cursor()
        cursor.execute('''select "codigo" from "GestionUsuarios_estado" where descripcion = 'Removido' ''')
        row2 = cursor.fetchone()
        if row2 != None:
            val = row2[0]
        historias = Historia.objects.filter(proyecto_Asociado=proyecto_id).exclude(estado=val).order_by('codigo')
        for histo in historias:
            hist.append(histo.codigo)
        tareas = Tarea.objects.filter(historia_Asociada__in=hist).exclude(estado=val).order_by('codigo')
        bugs = Bug.objects.filter(historia_Asociada__in=hist).exclude(estado=val).order_by('codigo')
        context = {'historias': historias, 'tareas': tareas, 'bugs': bugs, 'proyecto': proyecto_id}
    except Exception as e:
        print('Error: ', e)
        historias = None
    return render(request, 'GestionUsuarios/historias.html', context)


def addHistoria(request, proy):
    historia = Historia.objects.order_by('-codigo').first()
    maxcod = historia.codigo + 1
    proyecto = Proyecto.objects.get(codigo=proy)
    equipo = proyecto.equipo_Asociado.codigo
    if request.method == 'POST':
        form = HistoriaForm(request.POST, equipo=equipo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro creado de manera exitosa!')
            return redirect('historias', proy)
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('historias', proy)
    else:
        form = HistoriaForm(initial={'proyecto_Asociado': proy, 'codigo': maxcod}, equipo=equipo)
    context = {'form': form, 'id': proy}
    return render(request, 'GestionUsuarios/addHistoria.html', context)


def updateHistoria(request, id):
    historia = Historia.objects.get(codigo=id)
    proyecto = Proyecto.objects.get(codigo=historia.proyecto_Asociado.codigo)
    equipo = proyecto.equipo_Asociado.codigo
    if request.method == 'POST':
        form = HistoriaForm(request.POST, instance=historia, equipo=equipo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro actualizado de manera exitosa!')
            return redirect('historias', request.POST['proyecto_Asociado'])
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('historias', request.POST['proyecto_Asociado'])
    else:
        form = HistoriaForm(instance=historia, equipo=equipo)
    context = {'form': form, 'cod': id}
    return render(request, 'GestionUsuarios/updateHistoria.html', context)


def addTarea(request, hist):
    with connection.cursor() as cursor:
        zona = 'America/Guayaquil'
        cursor.execute('SET TIMEZONE="{}"'.format(zona))
    tarea = Tarea.objects.order_by('-codigo').first()
    maxcod = tarea.codigo + 1
    historia = Historia.objects.get(codigo=hist)
    proy = historia.proyecto_Asociado.codigo
    proyecto = Proyecto.objects.get(codigo=proy)
    equipo = proyecto.equipo_Asociado.codigo
    if request.method == 'POST':
        _mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST['tiempo'] = request.POST['tiempo_estimado']
        request.POST['tiempo_usado'] = 0
        request.POST._mutable = _mutable
        form = TareaForm(request.POST, equipo=equipo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro creado de manera exitosa!')
            return redirect('historias', proy)
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('historias', proy)
    else:
        form = TareaForm(initial={'historia_Asociada': hist, 'codigo': maxcod}, equipo=equipo)
    context = {'form': form, 'hist': hist}
    return render(request, 'GestionUsuarios/addTarea.html', context)


def updateTarea(request, id):
    with connection.cursor() as cursor:
        zona = 'America/Guayaquil'
        cursor.execute('SET TIMEZONE="{}"'.format(zona))
    tarea = Tarea.objects.get(codigo=id)
    historia = Historia.objects.get(codigo=tarea.historia_Asociada.codigo)
    proy = historia.proyecto_Asociado.codigo
    proyecto = Proyecto.objects.get(codigo=proy)
    equipo = proyecto.equipo_Asociado.codigo
    if request.method == 'POST':
        form = TareaActForm(request.POST, instance=tarea, equipo=equipo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro actualizado de manera exitosa!')
            return redirect('historias', proy)
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('historias', proy)
    else:
        form = TareaActForm(instance=tarea, equipo=equipo)
    context = {'form': form, 'cod': id}
    return render(request, 'GestionUsuarios/updateTarea.html', context)


def addBug(request, hist):
    bug = Bug.objects.order_by('-codigo').first()
    maxcod = bug.codigo + 1
    historia = Historia.objects.get(codigo=hist)
    proy = historia.proyecto_Asociado.codigo
    proyecto = Proyecto.objects.get(codigo=proy)
    equipo = proyecto.equipo_Asociado.codigo
    if request.method == 'POST':
        form = BugForm(request.POST, equipo=equipo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro creado de manera exitosa!')
            return redirect('historias', proy)
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('historias', proy)
    else:
        form = BugForm(initial={'historia_Asociada': hist, 'codigo': maxcod}, equipo=equipo)
    context = {'form': form, 'hist': hist}
    return render(request, 'GestionUsuarios/addBug.html', context)


def updateBug(request, id):
    bug = Bug.objects.get(codigo=id)
    historia = Historia.objects.get(codigo=bug.historia_Asociada.codigo)
    proy = historia.proyecto_Asociado.codigo
    proyecto = Proyecto.objects.get(codigo=proy)
    equipo = proyecto.equipo_Asociado.codigo
    if request.method == 'POST':
        form = BugForm(request.POST, instance=bug, equipo=equipo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro actualizado de manera exitosa!')
            return redirect('historias', proy)
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('historias', proy)
    else:
        form = BugForm(instance=bug, equipo=equipo)
    context = {'form': form, 'cod': id}
    return render(request, 'GestionUsuarios/updateBug.html', context)


def start(request):
    return render(request, 'GestionUsuarios/start.html')


def addProject(request):
    proyecto = Proyecto.objects.order_by('-codigo').first()
    maxcod = proyecto.codigo + 1
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro creado de manera exitosa!')
            return redirect('home')
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('home')
    else:
        form = ProyectoForm(initial={'codigo': maxcod})
    context = {'form': form}
    return render(request, 'GestionUsuarios/addProject.html', context)


def updateProject(request, proyecto_id):
    proyecto = Proyecto.objects.get(codigo=proyecto_id)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro actualizado de manera exitosa!')
            return redirect('home')
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('home')
    else:
        form = ProyectoForm(instance=proyecto)
    context = {'form': form, 'codigo': proyecto_id}
    return render(request, 'GestionUsuarios/updateProject.html', context)


def addMember(request):
    integrante = Integrante.objects.order_by('-codigo').first()
    maxcod = integrante.codigo + 1
    if request.method == 'POST':
        _mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST['contrasena'] = make_password(request.POST['contrasena'], salt=None, hasher='default')
        request.POST._mutable = _mutable
        form = IntegranteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro creado de manera exitosa!')
            return redirect('home')
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('home')
    else:
        form = IntegranteForm(initial={'codigo': maxcod})
    context = {'form': form}
    return render(request, 'GestionUsuarios/addMember.html', context)


def updateMember(request, member_id):
    usuario = Integrante.objects.get(codigo=member_id)
    if request.method == 'POST':
        form = IntegranteForm(request.POST, instance=usuario)
        if form.has_changed() and ('contrasena' in form.changed_data):
            _mutable = request.POST._mutable
            request.POST._mutable = True
            request.POST['contrasena'] = make_password(request.POST['contrasena'], salt=None, hasher='default')
            request.POST._mutable = _mutable
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro actualizado de manera exitosa!')
            return redirect('home')
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('home')
    else:
        form = IntegranteForm(instance=usuario)
    context = {'form': form, 'cod': member_id}
    return render(request, 'GestionUsuarios/updateMember.html', context)


def deleteMember(request, member_id):
    usuario = Integrante.objects.get(codigo=member_id)
    usuario.delete()
    messages.success(request, 'Registro eliminado con éxito!')
    return redirect('home')


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
