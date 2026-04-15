import os
import sys
import django
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portfolio.models import TFC, Tecnologia

def carregar_tfcs():
    caminho_json = os.path.join(os.path.dirname(__file__), 'tfcs_final.json')

    with open(caminho_json, encoding='utf-8') as f:
        tfcs = json.load(f)

    criados = 0
    ignorados = 0

    for item in tfcs:
        titulo = item.get('titulo', '').strip()

        if TFC.objects.filter(titulo=titulo).exists():
            print(f"[IGNORADO] Já existe: {titulo}")
            ignorados += 1
            continue

        ano_str = item.get('ano', '2024')
        try:
            ano = int(ano_str.split('-')[0])
        except ValueError:
            ano = 2024

        link_pdf = item.get('link_pdf', '')
        if link_pdf == 'N/A':
            link_pdf = ''

        imagem_url = item.get('imagem', '')
        if imagem_url == 'N/A':
            imagem_url = ''

        tfc = TFC.objects.create(
            titulo=titulo,
            resumo=item.get('sumario', ''),
            autores=item.get('autor', ''),
            ano=ano,
            orientador=item.get('orientadores', ''),
            ranking=str(item.get('rating', '')),
            link_pdf=link_pdf,
            imagem_url=imagem_url,
            palavras_chave=', '.join(item.get('palavras_chave', [])),
            area=', '.join(item.get('areas', [])),
        )

        for nome_tec in item.get('tecnologias', []):
            tec, _ = Tecnologia.objects.get_or_create(nome=nome_tec)
            tfc.tecnologias.add(tec)

        print(f"[OK] Carregado: {titulo}")
        criados += 1

    print(f"\nConcluído! {criados} TFCs criados, {ignorados} ignorados (duplicados).")

if __name__ == '__main__':
    carregar_tfcs()