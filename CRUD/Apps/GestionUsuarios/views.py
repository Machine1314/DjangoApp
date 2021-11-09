from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.db import connection
from django.shortcuts import render, redirect
from .forms import *
from django.db.models import Q
import datetime


# Create your views here.
def callSP(request):
    with connection.cursor() as cursor:
        cursor.execute('call insert_bulk()')
    return redirect('home')


def home(request):
    integrantes = Integrante.objects.exclude(capacidad = 0).order_by('codigo')
    proyectos = Proyecto.objects.all().order_by('codigo')
    context = {'proyectos': proyectos, 'usuarios': integrantes}
    return render(request, 'GestionUsuarios/home.html', context)


def tables(request):
    rol = Rol.objects.all().order_by('codigo')
    estado = Estado.objects.all().order_by('codigo')
    context = {'roles': rol, 'estados': estado}
    return render(request, 'GestionUsuarios/tables.html', context)


def teams(request):
    equipos = Equipo.objects.all().order_by('codigo')
    context = {'equipos': equipos}
    return render(request, 'GestionUsuarios/teams.html', context)


def addTeam(request):
    cursor = connection.cursor()
    cursor.execute('''select max(codigo) + 1 from "GestionUsuarios_equipo"''')
    row = cursor.fetchone()
    value = row[0]
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
        form = EquipoForm(initial={'codigo': value})
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


def addRol(request):
    cursor = connection.cursor()
    cursor.execute('''select max(codigo) + 1 from "GestionUsuarios_rol"''')
    row = cursor.fetchone()
    value = row[0]
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
        form = RolForm(initial={'codigo': value})
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
    return redirect('tables')


def addStatus(request):
    cursor = connection.cursor()
    cursor.execute('''select max(codigo) + 1 from "GestionUsuarios_estado"''')
    row = cursor.fetchone()
    value = row[0]
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
        form = EstadoForm(initial={'codigo': value})
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
    return redirect('tables')


def metrica(request, proyecto_id):
    start = datetime.date.today()
    end = start + datetime.timedelta(days=5)
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]
    date = [date.strftime('%Y-%m-%d') for date in date_generated]
    tiemposTendencia = []
    tiemposTareas = []
    with connection.cursor() as cursor:
        cursor.execute('''select sum((COALESCE("capacidad",0)) * 5) from "GestionUsuarios_integrante" where "codigo" 
in (SELECT "integrante_Encargado_id" FROM "GestionUsuarios_tarea" where "historia_Asociada_id" 
	in (select "codigo" from "GestionUsuarios_historia" where "proyecto_Asociado_id" = {}))'''.format(str(proyecto_id)))
        row = cursor.fetchone()
        cursor.execute('''SELECT sum(abs(COALESCE("tiempo_Real", 0) - COALESCE("tiempo_Estimado", 0))) FROM "GestionUsuarios_tarea" 
where "historia_Asociada_id" in (select "codigo" from "GestionUsuarios_historia" where "proyecto_Asociado_id" = {})'''.format(
            str(proyecto_id)))
        row2 = cursor.fetchone()
    tendencia = row[0]
    capacidad = tendencia / 4
    while tendencia != 0:
        if tendencia < 0:
            tendencia = 0
            break
        tiemposTendencia.append(round(tendencia, 1))
        tendencia = tendencia - capacidad
    tiemposTendencia.append(tendencia)

    actual = row2[0]
    capActual = actual / 4
    while actual != 0:
        if actual < 0:
            actual = 0
            break
        tiemposTareas.append(round(actual, 1))
        actual = actual - capActual
    tiemposTareas.append(actual)
    context = {'dates': date, 'tendencia': tiemposTendencia, 'actual': tiemposTareas}
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
    cursor = connection.cursor()
    cursor.execute('''select max(codigo) + 1 from "GestionUsuarios_historia"''')
    row = cursor.fetchone()
    value = row[0]
    if request.method == 'POST':
        form = HistoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro creado de manera exitosa!')
            return redirect('historias', proy)
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('historias', proy)
    else:
        form = HistoriaForm(initial={'proyecto_Asociado': proy, 'codigo': value})
    context = {'form': form, 'id': proy}
    return render(request, 'GestionUsuarios/addHistoria.html', context)


def updateHistoria(request, id):
    historia = Historia.objects.get(codigo=id)
    cod = id
    if request.method == 'POST':
        form = HistoriaForm(request.POST, instance=historia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro actualizado de manera exitosa!')
            return redirect('historias', request.POST['proyecto_Asociado'])
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('historias', request.POST['proyecto_Asociado'])
    else:
        form = HistoriaForm(instance=historia)
    context = {'form': form, 'cod': cod}
    return render(request, 'GestionUsuarios/updateHistoria.html', context)


def addTarea(request, hist):
    integrante = Integrante.objects.all()
    cursor = connection.cursor()
    cursor.execute('''select max(codigo) + 1 from "GestionUsuarios_tarea"''')
    row = cursor.fetchone()
    value = row[0]
    print(value)
    cursor.execute('''select "proyecto_Asociado_id" from "GestionUsuarios_historia" where codigo = ''' + str(hist))
    row2 = cursor.fetchone()
    proy = row2[0]
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro creado de manera exitosa!')
            return redirect('historias', proy)
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('historias', proy)
    else:
        form = TareaForm(initial={'historia_Asociada': hist, 'codigo': value})
    context = {'form': form, 'hist': hist, 'integrantes': integrante}
    return render(request, 'GestionUsuarios/addTarea.html', context)


def updateTarea(request, id):
    tarea = Tarea.objects.get(codigo=id)

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        cursor = connection.cursor()
        cursor.execute('''select "proyecto_Asociado_id" from "GestionUsuarios_historia" where codigo = ''' + str(
            tarea.historia_Asociada.codigo))
        row2 = cursor.fetchone()
        proy = row2[0]
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro actualizado de manera exitosa!')
            return redirect('historias', proy)
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('historias', proy)
    else:
        form = TareaForm(instance=tarea)
    context = {'form': form, 'cod': id}
    return render(request, 'GestionUsuarios/updateTarea.html', context)


def addBug(request, hist):
    cursor = connection.cursor()
    cursor.execute('''select max(codigo) + 1 from "GestionUsuarios_bug"''')
    row = cursor.fetchone()
    value = row[0]
    print(value)
    cursor.execute('''select "proyecto_Asociado_id" from "GestionUsuarios_historia" where codigo = ''' + str(hist))
    row2 = cursor.fetchone()
    proy = row2[0]
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('historias', proy)
    else:
        form = BugForm(initial={'historia_Asociada': hist, 'codigo': value})
    context = {'form': form, 'hist': hist}
    return render(request, 'GestionUsuarios/addBug.html', context)


def updateBug(request, id):
    bug = Bug.objects.get(codigo=id)
    if request.method == 'POST':
        form = BugForm(request.POST, instance=bug)
        cursor = connection.cursor()
        cursor.execute('''select "proyecto_Asociado_id" from "GestionUsuarios_historia" where codigo = ''' + str(
            bug.historia_Asociada.codigo))
        row2 = cursor.fetchone()
        proy = row2[0]
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro actualizado de manera exitosa!')
            return redirect('historias', proy)
        else:
            messages.success(request, 'Ocurrió un error, intente de nuevo!')
            return redirect('historias', proy)
    else:
        form = BugForm(instance=bug)
    context = {'form': form, 'cod': id}
    return render(request, 'GestionUsuarios/updateBug.html', context)


def start(request):
    return render(request, 'GestionUsuarios/start.html')


def addProject(request):
    cursor = connection.cursor()
    cursor.execute('''select max(codigo) + 1 from "GestionUsuarios_proyecto"''')
    row = cursor.fetchone()
    value = row[0]
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
        form = ProyectoForm(initial={'codigo': value})
    context = {'form': form}
    return render(request, 'GestionUsuarios/addProject.html', context)


def updateProject(request, proyecto_id):
    proyecto = Proyecto.objects.get(codigo=proyecto_id)
    codigo = proyecto_id
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
    context = {'form': form, 'codigo': codigo}
    return render(request, 'GestionUsuarios/updateProject.html', context)


def addMember(request):
    cursor = connection.cursor()
    cursor.execute('''select max(codigo) + 1 from "GestionUsuarios_integrante"''')
    row = cursor.fetchone()
    value = row[0]
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
        form = IntegranteForm(initial={'codigo': value})
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
            usuario = Integrante.objects.get(usuario=request.POST['correo'])
            if check_password(request.POST['pwd'], usuario.contrasena):
                request.session['Usuario'] = usuario.usuario
                return redirect('home')
            else:
                return render(request, 'GestionUsuarios/login.html')
        except:
            context = {'message': 'Fallo'}
    return render(request, 'GestionUsuarios/login.html')


def logout(request):
    try:
        del request.session['Usuario']
        print('elimina')
        return redirect('login')
    except:
        print('fallo salir sesion')
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
