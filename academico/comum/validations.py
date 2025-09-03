from django.contrib.auth.models import User

def possui_apenas_numeros(valor_campo, nome_campo, lista_de_erros):
    """Verifica se o campo possui apenas números"""
    if any(not char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Permitido apenas números neste campo.'


def campo_form_vazio(valor_campo, nome_campo, lista_de_erros):
    """Verifica se o campo do formulário  é vazio"""
    if not valor_campo.split():
        lista_de_erros[nome_campo] = 'Este campo não pode ser vazio.'

def email_ja_cadastrado(email, lista_de_erros):
    """Verifica se o email já está cadastrado no banco de dados """
    if User.objects.filter(email=email).exists():
        lista_de_erros['email'] = 'Este email já está cadastrado no sistema.'

def cpf_ja_cadastrado(cpf, lista_de_erros):
    """Verifica se o CPF (username) já está cadastrado no banco de dados """
    if User.objects.filter(username=cpf).exists():
        lista_de_erros['username'] = 'Este CPF já está cadastrado no sistema.'

def senhas_nao_sao_iguais(password, password2, lista_de_erros):
    """Verifica se o campo é vazio"""
    if password != password2:
        lista_de_erros['password2'] = 'Este campo não pode ser vazio.'