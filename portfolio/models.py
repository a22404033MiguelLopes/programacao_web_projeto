from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    grau = models.CharField(max_length=50, default='Licenciatura')
    ects = models.IntegerField()
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='licenciatura/', blank=True, null=True)

    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
    ects = models.IntegerField()
    semestre = models.IntegerField()
    icone = models.ImageField(upload_to='ucs/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.sigla


class Professor(models.Model):
    ucs = models.ManyToManyField(UnidadeCurricular, related_name='professores', blank=True)
    nome = models.CharField(max_length=100)
    link_pagina = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    NIVEL_CHOICES = [(i, str(i)) for i in range(1, 6)]
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    nivel_interesse = models.IntegerField(choices=NIVEL_CHOICES, default=3)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.SET_NULL, null=True, related_name='projetos')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos', blank=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ano = models.IntegerField()
    github_link = models.URLField(blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    conceitos_aplicados = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo


class TFC(models.Model):
    tecnologias = models.ManyToManyField(Tecnologia, related_name='tfcs', blank=True)
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    autores = models.CharField(max_length=200)
    ano = models.IntegerField()
    orientador = models.CharField(max_length=100)
    ranking = models.CharField(max_length=50, blank=True, null=True)
    link_pdf = models.URLField(blank=True, null=True)
    imagem_url = models.URLField(blank=True, null=True)
    palavras_chave = models.CharField(max_length=300, blank=True, null=True)
    area = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.titulo


class Competencia(models.Model):
    CATEGORIA_CHOICES = [('hard', 'Hard Skill'), ('soft', 'Soft Skill')]
    NIVEL_CHOICES = [('iniciante', 'Iniciante'), ('intermedio', 'Intermédio'), ('avancado', 'Avançado'), ('expert', 'Expert')]
    tecnologias = models.ManyToManyField(Tecnologia, related_name='competencias', blank=True)
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    tecnologias = models.ManyToManyField(Tecnologia, related_name='formacoes', blank=True)
    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    certificado = models.FileField(upload_to='certificados/', blank=True, null=True)

    def __str__(self):
        return self.nome


class Lingua(models.Model):
    NIVEL_CHOICES = [('A1','A1'),('A2','A2'),('B1','B1'),('B2','B2'),('C1','C1'),('C2','C2'),('Nativo','Nativo')]
    idioma = models.CharField(max_length=50)
    nivel = models.CharField(max_length=10, choices=NIVEL_CHOICES)
    certificado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.idioma} ({self.nivel})"


class MakingOf(models.Model):
    etapa = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    foto = models.ImageField(upload_to='makingof/', blank=True, null=True)
    erros_encontrados = models.TextField(blank=True, null=True)
    uso_ia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.etapa