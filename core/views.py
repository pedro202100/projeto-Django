from django.shortcuts import render,redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

# Create your views here.

#def index(request):
 #   return redirect('/agenda')

def login_user(request):
    return render(request,'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:
            messages.error(request,"Usuario e/ou senha invalidos")

    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def listaEventos(request):
    user = request.user
    dataAtual = datetime.now() - timedelta(hours=1)
    evento = Evento.objects.filter(usuario=user)
    dados = {'eventos':evento}

    return render(request,'agenda.html',dados)

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request,'evento.html',dados)

@login_required(login_url='/login/')
def submitEvento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        dataEvento = request.POST.get('data')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            Evento.objects.filter(id=id_evento).update(titulo=titulo,
                                 dataEvemto = dataEvento,
                                 descricao = descricao,
                                 )
            return redirect('/')
        else:
            Evento.objects.create(titulo=titulo,
                                 dataEvemto = dataEvento,
                                 descricao = descricao,
                                 usuario = usuario)

    return redirect('/')

@login_required(login_url='/login/')
def deleteEvento(requeste, id_evento):
    usuario = requeste.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception :
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')
@login_required(login_url='/login/')
def jsonListaEvento(request):
    user = request.user
    evento = Evento.objects.filter(usuario=user).values('id','titulo')

    return JsonResponse(list(evento), safe=False)






