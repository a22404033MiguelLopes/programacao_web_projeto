from django.contrib import admin
from .models import Professor, Curso, Aluno

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display  = ('nome', 'email')
    search_fields = ('nome',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display      = ('nome', 'professor')
    list_filter       = ('professor',)
    search_fields     = ('nome',)
    filter_horizontal = ('alunos',)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display  = ('numero', 'nome')
    search_fields = ('nome',)