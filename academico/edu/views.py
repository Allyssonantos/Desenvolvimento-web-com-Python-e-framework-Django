from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Matricula, Curso
from comum.models import Aluno
import datetime

from django.utils import timezone


# Create your views here.
'''def index(request):
    matriculas = Matricula.objects.all()
    cursos = Curso.objects.order_by('codigo').filter(ativo=True)

    dados = {
        'matriculas': matriculas,
        'cursos': cursos,
    }
    return render(request, 'index.html', dados)'''

def index(request):
    cursos = Curso.objects.filter(ativo=True)
    dados = {
        'cursos': cursos,
    }
    return render(request, 'index.html', dados)

'''def curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    dados = {
        'curso': curso,
    }
    return render(request, 'edu/curso.html', dados)'''

def curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    matriculado = 0
    if request.user.is_authenticated:
        matriculado = 1
        if Aluno.objects.filter(user_id=request.user.id):
            matriculado = 2
            if Matricula.objects.filter(aluno_id=request.user.aluno.id, curso_id=curso_id).exists():
                matriculado = 3
    dados = {
        'curso': curso,
        'matriculado': matriculado,
    }
    return render(request, 'edu/curso.html', dados)

def matricular_aluno(request, curso_id):
    if request.user.is_authenticated:
        user_id = request.user.id
        aluno = get_object_or_404(Aluno, user_id=user_id)
        curso = get_object_or_404(Curso, pk=curso_id)
        if request.method == 'POST':
            observacao = request.POST['observacao']
            currentDateTime = datetime.datetime.now()
            year = currentDateTime.date().strftime("%Y")
            numero = '0000000000{}{}'.format(user_id, curso_id)
            num_matricula = '{}{}'.format(year, numero[-6:])
            matricula = Matricula.objects.create(aluno=aluno, curso=curso, matricula=num_matricula, observacao=observacao)
            matricula.save()
            print('Matrícula efetuada com sucesso')
            return redirect('dashboard')
        else:
            dados = {
                'aluno': aluno,
                'curso': curso,
            }
            return render(request, 'edu/matricular_aluno.html', dados)
    else:
        print('Primeiro, realize o login.')
        return redirect('login')

def desmatricular_aluno(request, curso_id):
    matricula = Matricula.objects.filter(curso_id=curso_id,aluno_id=request.user.aluno.id)
    matricula.delete()
    print('Matrícula deletada com sucesso')
    return redirect('dashboard')

def buscar(request):
    lista_cursos = Curso.objects.order_by('codigo').filter(ativo=True)
    if 'busca' in request.GET: #se buscar tem um valor nesta request
        dado_a_buscar = request.GET['busca'] #recebe o texto buscado
        print(dado_a_buscar)
        if buscar:

            lista_cursos = lista_cursos.filter(descricao__icontains=dado_a_buscar)
    print(lista_cursos)
    dados = {
        'cursos': lista_cursos,
    }
    return render(request, 'edu/buscar.html', dados)


'''def edu(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    data_acesso = timezone.now()
    curso_a_exibir = {
        'curso': curso,
        'data_acesso': data_acesso
    }
    return render(request, 'curso.html', curso_a_exibir)'''

