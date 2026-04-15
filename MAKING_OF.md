# Making Of - Portfólio Académico (Django)

Diário de bordo do desenvolvimento do meu portfólio para a cadeira de Programação Web.

---

## Fase 1: Planeamento e Modelação

Comecei por ler o enunciado e perceber que entidades ia precisar. Fiz rascunhos em papel para desenhar o Diagrama Entidade-Relação antes de começar a programar, o que me ajudou a visualizar as ligações entre as entidades.

As fotos do planeamento estão guardadas em `media/makingof/`.

---

## Fase 2: Decisões de Modelação

### Licenciatura
- Adicionei o campo `website` para ter o link direto para o site oficial do curso.
- O campo `logo` permite mostrar a identidade visual da instituição no portfólio.

### Unidades Curriculares
- Cada UC pertence a uma Licenciatura (relação Many-to-One).
- A relação com Professor é Many-to-Many porque uma cadeira pode ter vários docentes e um docente pode dar várias cadeiras.

### Professor
- Optei por guardar o `email` e o `link_pagina` para facilitar o contacto e a consulta do perfil do docente.

### Tecnologias
- Criei uma entidade separada para as tecnologias em vez de usar um simples campo de texto. Assim consigo reutilizá-las em várias entidades (Projetos, TFCs, Competências, Formações) e filtrar projetos por tecnologia.
- O campo `nivel_interesse` (1 a 5) permite destacar as tecnologias que mais me interessam.

### Projetos
- Cada projeto está ligado a uma UC (Many-to-One) para mostrar em que contexto académico foi feito.
- Os campos `github_link` e `video_link` servem para demonstrar o código e o funcionamento real.

### TFC (Trabalho Final de Curso)
- Separei os TFCs dos Projetos normais porque têm mais peso académico e atributos próprios como `orientador` e `ranking`.

### Competências
- Divididas entre Hard Skills e Soft Skills com níveis (Iniciante a Expert).
- Ligadas às Tecnologias para manter coerência entre o que digo saber e o que os projetos provam.

### Formações
- Incluem datas de início e fim para eventualmente criar uma timeline.
- O campo `certificado` (FileField) permite guardar o comprovativo.

### Línguas
- Entidade adicional com níveis do QECR (A1 a C2 + Nativo), relevante para o currículo.

### MakingOf
- Guarda o registo de cada etapa do desenvolvimento, incluindo erros encontrados e uso de IA.

---

## Fase 3: Carregamento de Dados

### Dados do Curso (API da Lusófona)
Usei a API pública da Universidade Lusófona para descarregar os JSONs com a informação do curso LEI e de cada UC. O script `data/descarregar_api.py` faz o download e guarda tudo na pasta `data/files/`.

Depois de explorar a estrutura dos JSONs, vi que existem campos como `objectives`, `programme`, `bibliography` e `methodology`, mas decidi **não adicionar esses campos ao modelo**. A informação essencial da UC (nome, sigla, ECTS e semestre) já está contemplada, e esses campos de texto longo não fazem sentido no contexto de um portfólio pessoal — o foco deve ser nos projetos e competências, não em reproduzir a ficha da cadeira.

O script `data/carregar_curso.py` carrega as UCs para a base de dados usando os JSONs descarregados.

### Dados dos TFCs
O script `data/carregar_tfcs.py` carrega os Trabalhos Finais de Curso a partir do ficheiro `data/tfcs_final.json`, criando automaticamente as Tecnologias associadas a cada TFC.

---

## Evolução do Modelo

| Versão | O que mudou | Porquê |
| :--- | :--- | :--- |
| v1.0 | Tecnologias como texto no Projeto | Impossível filtrar ou associar logos |
| v1.1 | Criação da entidade Tecnologia | Reutilizável em vários modelos |
| v1.2 | Professor/UC passou a Many-to-Many | Permitir vários docentes por UC |
| v1.3 | Adicionado `tipo` à Tecnologia | Ao inserir dados, percebi que "Python" é uma linguagem mas "Django" é um framework — sem esta distinção ficava tudo misturado |
| v1.4 | Adicionado `ano_letivo` à UC | O semestre sozinho não chega — preciso saber se é o semestre 1 de 2023-2024 ou de 2024-2025 |
| v1.5 | Adicionado `participantes` ao Projeto | Alguns projetos foram feitos em grupo e faz sentido registar com quem trabalhei |

---

## Fase 4: Carregamento Manual de Dados

Ao tentar inserir os meus dados reais no Django Admin, reparei em algumas limitações do modelo original:

- **Tecnologia sem tipo:** Ao adicionar Python, Django, Git, Bootstrap, etc., ficava tudo numa lista genérica sem distinção. Adicionei o campo `tipo` com categorias (Linguagem, Framework, Ferramenta, Biblioteca, Outro) para organizar melhor.
- **UC sem ano letivo:** Só tinha o número do semestre, mas isso não me dizia em que ano letivo frequentei a cadeira. Adicionei `ano_letivo` como CharField (ex: "2024-2025").
- **Projeto sem participantes:** Vários projetos foram feitos em grupo e queria registar isso. Adicionei o campo `participantes`.

Estas alterações surgiram naturalmente ao recolher informação sobre os meus projetos e experiências — é o tipo de coisa que só se percebe quando se tenta usar o modelo com dados reais.

---

## Uso de IA

Usei o **Gemini** como assistente durante a modelação. Ajudou-me a estruturar as relações Many-to-Many e a converter o raciocínio que fiz em papel para o `models.py` do Django. Todas as sugestões foram verificadas contra o enunciado da ficha.

---