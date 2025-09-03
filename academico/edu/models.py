from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Matricula(models.Model):
    matricula = models.IntegerField()
    #nome_aluno = models.CharField(max_length=200)
    aluno = models.ForeignKey('comum.Aluno', verbose_name='Aluno', related_name='comum_aluno', on_delete=models.CASCADE)
    #curso = models.CharField(max_length=100)
    curso = models.ForeignKey('edu.Curso', verbose_name='Curso', related_name='edu_curso', on_delete=models.CASCADE)
    observacao = models.TextField()
    data_matricula = models.DateTimeField(verbose_name='Data da matrícula', blank=True, auto_now_add=True)

    class Meta:
        verbose_name = 'Matrícula de Aluno'
        verbose_name_plural = 'Matrículas de Aluno'




class Curso(models.Model):

    PERIODICIDADE_CHOICES = [

        [1, 'Anual'],

        [2, 'Semestral'],

        [3, 'Livre']]

    TIPO_HORA_AULA_CHOICES = [

        [45, '45 min'],

        [60, '60 min']

    ]

    codigo = models.CharField(verbose_name='Código do Curso', help_text='Código usado para composição de turmas e matrículas', unique=True, max_length=10)

    descricao = models.CharField(verbose_name='Descrição', max_length=500, null=True, blank=True)

    ativo = models.BooleanField('Ativo', default=True)

    ppc = models.FileField(upload_to='static/', null=True, blank=True, verbose_name='PPC', default=None)

    ch_total = models.PositiveIntegerField('Carga Horária Total do Curso', blank=True, null=True, default=None)

    tipo_hora_aula = models.PositiveIntegerField('Tipo Hora Aula', blank=True, null=True, choices=TIPO_HORA_AULA_CHOICES)

    periodicidade = models.PositiveIntegerField('Periodicidade', choices=PERIODICIDADE_CHOICES, null=True)

    media_aprovacao = models.DecimalField('Média para aprovação', null=True, blank=True, help_text='Valor entre 0 e 10.', decimal_places=2, max_digits=5, validators=[MinValueValidator(Decimal(0)), MaxValueValidator(Decimal(10))])

    conteudo = models.TextField(verbose_name='Conteúdo')

    class Meta:

        verbose_name = 'Curso'

        verbose_name_plural = 'Cursos'

        ordering =('id', 'ativo',)

    def __str__(self):

        codigo = self.codigo.replace('-', '')

        return '{} - {}'.format(codigo, self.descricao)


