from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from edu.models import Matricula
from django.contrib import auth, messages
from .forms import AlunoForm, UserForm
from .models import Aluno

def cadastro(request):
    form_user = UserForm()
    form_aluno = AlunoForm()
    contexto = {
        'form_user': form_user,
        'form_aluno': form_aluno,
    }
    '''if form_aluno.is_valid() and form_user.is_valid():
        messages.error(request, 'Ocorreu um problema no formulário. Recarre a página e tente novamente.')'''
    return render(request, 'comum/cadastro.html', contexto)

def confirma_cadastro(request):
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_aluno = AlunoForm(request.POST)
        contexto = {
            'form_user': form_user,
            'form_aluno': form_aluno,
        }
        if form_aluno.is_valid() and form_user.is_valid():
            # Buscando os fields
            username = form_user.cleaned_data.get('username')
            email = form_user.cleaned_data.get('email')
            password = form_user.cleaned_data.get('password')
            first_name = form_user.cleaned_data.get('first_name')
            last_name = form_user.cleaned_data.get('last_name')
            data_nascimento = form_aluno.cleaned_data.get('data_nascimento')
            sexo = form_aluno.cleaned_data.get('sexo')
            telefone = form_aluno.cleaned_data.get('telefone')

            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name)
            aluno = Aluno.objects.create(data_nascimento=data_nascimento,
                                         sexo=sexo,
                                         telefone=telefone,
                                         user=user)
            user.save()
            aluno.save()
            messages.success(request, 'Usuário cadastrado com sucesso.')
            return render(request, 'comum/confirma_cadastro.html', contexto)
        else:
            return render(request, 'comum/cadastro.html', contexto)
    else:
        return redirect('index')

def confirma_cadastro22(request):
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_aluno = AlunoForm(request.POST)
        contexto = {
            'form_user': form_user,
            'form_aluno': form_aluno,
        }
        if form_aluno.is_valid() and form_user.is_valid():
            username = form_user.cleaned_data.get('username')
            email = form_user.cleaned_data.get('email')
            password = form_user.cleaned_data.get('password')
            first_name = form_user.cleaned_data.get('first_name')
            last_name = form_user.cleaned_data.get('last_name')
            data_nascimento = form_aluno.cleaned_data.get('data_nascimento')
            sexo = form_aluno.cleaned_data.get('sexo')
            telefone = form_aluno.cleaned_data.get('telefone')

            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name)
            aluno = Aluno.objects.create(data_nascimento=data_nascimento,
                                         sexo=sexo,
                                         telefone=telefone,
                                         user=user)
            user.save()
            aluno.save()
            messages.success(request, 'Usuário cadastrado com sucesso.')
            return render(request, 'comum/confirma_cadastro.html', contexto)
        else:
            print('Form inválido')
            return render(request, 'comum/cadastro.html', contexto)
    else:
        return redirect('index')

'''def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'comum/dashboard.html')
    else:
        return redirect('index')'''

def dashboard(request):
    if request.user.is_authenticated:
        matriculas = Matricula.objects.order_by('-data_matricula').filter(aluno_id=request.user.aluno.id)
        dados = {
            'matriculas': matriculas,
        }
        return render(request, 'comum/dashboard.html', dados)
    else:
        return redirect('index')

def login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        senha = request.POST["senha"]
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.error(request, 'Login realizado com sucesso')
                return redirect('dashboard')
            else:
                messages.error(request, 'Falha na autenticação')
                return redirect('login')
        else:
            messages.error(request, 'E-mail não cadastrado.')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'comum/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def perfil(request):
    return render(request, 'comum/perfil.html')