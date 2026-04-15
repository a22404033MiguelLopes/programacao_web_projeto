from django.contrib import admin
from .models import (
    Licenciatura, UnidadeCurricular, Professor, Tecnologia,
    Projeto, TFC, Competencia, Formacao, Lingua, MakingOf
)

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'grau', 'ects')
    search_fields = ('nome', 'instituicao')

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'ects', 'semestre', 'licenciatura')
    list_filter = ('semestre', 'licenciatura')
    search_fields = ('nome', 'sigla')

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    filter_horizontal = ('ucs',)

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel_interesse')
    list_filter = ('nivel_interesse',)
    search_fields = ('nome',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'uc', 'ano')
    list_filter = ('ano', 'uc')
    search_fields = ('titulo',)
    filter_horizontal = ('tecnologias',)

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autores', 'ano', 'orientador', 'ranking')
    list_filter = ('ano',)
    search_fields = ('titulo', 'autores', 'orientador')
    filter_horizontal = ('tecnologias',)

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'nivel')
    list_filter = ('categoria', 'nivel')
    search_fields = ('nome',)
    filter_horizontal = ('tecnologias',)

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'data_inicio', 'data_fim')
    search_fields = ('nome', 'instituicao')
    filter_horizontal = ('tecnologias',)

@admin.register(Lingua)
class LinguaAdmin(admin.ModelAdmin):
    list_display = ('idioma', 'nivel', 'certificado')
    list_filter = ('nivel',)

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('etapa', 'data')
    search_fields = ('etapa',)