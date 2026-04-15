import os
import sys
import django
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portfolio.models import Licenciatura, UnidadeCurricular

# Limpa dados anteriores para não duplicar
UnidadeCurricular.objects.all().delete()
Licenciatura.objects.all().delete()

# Cria a licenciatura com os teus campos
lei = Licenciatura.objects.create(
    nome='Engenharia Informática',
    instituicao='Universidade Lusófona',
    grau='Licenciatura',
    ects=180,
    website='https://www.ulusofona.pt/licenciatura/engenharia-informatica',
)

# Abre o ficheiro principal do curso
pasta_files = os.path.join(os.path.dirname(__file__), 'files')

with open(os.path.join(pasta_files, 'ULHT260-PT.json'), encoding='utf-8') as f:
    curso = json.load(f)

# Para cada UC do curso, carrega os detalhes
for uc_info in curso['courseFlatPlan']:
    codigo = uc_info['curricularIUnitReadableCode']
    ficheiro = os.path.join(pasta_files, f"{codigo}-PT.json")

    if not os.path.exists(ficheiro):
        print(f"Ficheiro não encontrado: {ficheiro}")
        continue

    with open(ficheiro, encoding='utf-8') as f:
        uc = json.load(f)

    UnidadeCurricular.objects.create(
        licenciatura=lei,
        nome=uc.get('curricularUnitName', ''),
        sigla=codigo,                          # usa o código como sigla
        ects=uc.get('ects', 0),
        semestre=uc_info.get('semester', 1),   # vem do ficheiro principal do curso
    )
    print(f"[OK] UC carregada: {uc.get('curricularUnitName', codigo)}")

print("\nConcluído!")