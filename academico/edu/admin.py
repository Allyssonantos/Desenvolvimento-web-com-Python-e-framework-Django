from django.contrib import admin
from .models import Matricula, Curso

# Register your models here.
class AdminMatricula(admin.ModelAdmin):
    list_display = ('id', 'matricula', 'aluno')
    list_display_links = ('id', 'matricula')
    search_fields = ('aluno__user__first_name', )
    list_filter = ('curso', )
    list_per_page = 2



class AdminCursos(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'codigo', 'ativo')
    list_display_links = ('id', 'descricao', 'codigo')
    search_fields = ('descricao', 'codigo')
    list_per_page = 10
    list_editable = ('ativo',)


admin.site.register(Matricula, AdminMatricula)
admin.site.register(Curso, AdminCursos)
