from django import forms
from django.forms import PasswordInput

from comum.validations import *
from comum.models import Aluno
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password2 = forms.CharField(required=True, label='Confirme a senha', widget=PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'CPF',
            'email': 'E-mail',
            'password': 'Senha',
            }
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        lista_de_erros = {}
        username = self.cleaned_data['username']
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        possui_apenas_numeros(username, 'username', lista_de_erros)
        campo_form_vazio(first_name, 'first_name', lista_de_erros)
        campo_form_vazio(last_name, 'last_name', lista_de_erros)
        campo_form_vazio(email, 'email', lista_de_erros)
        campo_form_vazio(username, 'username', lista_de_erros)
        email_ja_cadastrado(email, lista_de_erros)
        cpf_ja_cadastrado(username, lista_de_erros)
        senhas_nao_sao_iguais(password, password2, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_de_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_de_erro)
        return self.cleaned_data


class AlunoForm(forms.ModelForm):
    '''sexo_opcoes = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outro', 'Outro')
    )
    nome = forms.CharField(max_length=100, label="Nome")
    sobrenome = forms.CharField(max_length=100, label="Sobrenome")
    email = forms.CharField(max_length=100, label="E-mail")
    data_nascimento = forms.DateTimeField(label="Data de Nascimento")#, input_formats=['%d/%m/%Y'])
    sexo = forms.ChoiceField(choices=sexo_opcoes, label="Sexo")
    telefone = forms.CharField(max_length=15, label="Telefone")'''

    '''class Meta:
        model = Aluno
        fields = ['data_nascimento', 'sexo', 'telefone']'''

    class Meta:
        model = Aluno
        fields = '__all__'
        labels = {
            'data_nascimento': 'Data de nascimento',
            'sexo': 'Sexo',
            'telefone': 'Telefone',
        }
        exclude = {'user', 'foto_aluno'}

    def clean(self):
        telefone = self.cleaned_data.get('telefone')
        lista_de_erros = {}
        possui_apenas_numeros(telefone, 'telefone', lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_de_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_de_erro)
        return self.cleaned_data


    '''def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if any(not char.isdigit() for char in telefone):
            raise forms.ValidationError('Número de telefone inválido: Inclua somente números.')
        else:
            return telefone'''


    '''data_nascimento = forms.DateField(required=True)
    #data_nascimento = forms.CharField(max_length=100, required=True, verbose_name='Data de Nascimento')
    sexo = forms.ChoiceField(choices=sexo_opcoes)
    telefone = forms.CharField(max_length=100, required=True)'''

    '''    def clean(self):
            lista_de_erros = {}
            username = self.cleaned_data['username']
            possui_apenas_numeros(username, 'username', lista_de_erros)
            if lista_de_erros is not None:
                for erro in lista_de_erros:
                    mensagem_de_erro = lista_de_erros[erro]
                    self.add_error(erro, mensagem_de_erro)
            return self.cleaned_data'''