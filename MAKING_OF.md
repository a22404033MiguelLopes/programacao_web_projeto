# Making Of - Projeto de Portfólio Académico (Django)

Este documento detalha o processo de conceção, modelação e implementação do meu portfólio. Este projeto foi desenvolvido para a unidade curricular de Programação Web e serve como um diário de bordo das decisões técnicas tomadas.

---

## 1. Diário de Bordo e Processo de Decisão

### Fase 1: Análise e Modelação Inicial
O processo começou com a leitura do enunciado e a identificação das entidades principais. Utilizei papel e caneta para esboçar o Diagrama Entidade-Relação (DER), focando-me na forma como as unidades curriculares (UCs) ligam os projetos às competências.

* **Registo Visual:** As fotos do planeamento inicial encontram-se em `media/makingof/` (`der_papel_v1.jpg` e `der_final.jpg`).

---

## 2. Justificações de Modelação

Abaixo encontram-se as decisões tomadas para cada entidade, justificando a sua estrutura e relações.

### Licenciatura
* **Justificação 1:** Inclusão do atributo `website` para permitir ao utilizador validar o plano de estudos oficial no site da universidade.
* **Justificação 2:** O campo `logo` foi incluído para garantir que a identidade visual da instituição seja preservada no portfólio.

### Unidades Curriculares (UC)
* **Justificação 1:** Relação `Many-to-Many` com a entidade **Professor**, pois uma cadeira pode ter vários docentes (Teórica/Prática) e o mesmo docente pode lecionar várias UCs.
* **Justificação 2:** Atributo `semestre` e `ano_letivo` para permitir uma filtragem e ordenação lógica no frontend.

### Projetos
* **Justificação 1:** Relação `Many-to-One` com a **UC**. Cada projeto nasce num contexto académico específico, permitindo ao recrutador entender em que cadeira a competência foi adquirida.
* **Justificação 2:** Campo `github_link` e `video_link` definidos como essenciais para demonstrar transparência de código e o funcionamento real do projeto.

### Tecnologias
* **Justificação 1:** Relação `Many-to-Many` com **Projetos**. Um projeto raramente usa apenas uma tecnologia, e esta modelação permite listar todos os projetos feitos em, por exemplo, "Python".
* **Justificação 2:** Atributo `nivel_interesse` para destacar áreas de especialização e preferência de carreira.

### TFC (Trabalho Final de Curso)
* **Justificação 1:** Entidade separada de "Projetos" devido à sua maior complexidade e peso académico, incluindo atributos como `orientador`.
* **Justificação 2:** Atributo `ranking` para destacar trabalhos de excelência ou prémios recebidos.

### Competências & Formações
* **Justificação 1:** As **Competências** são alimentadas pelas **Tecnologias** dominadas, criando uma coerência entre o que digo saber e o que os meus projetos provam.
* **Justificação 2:** As **Formações** incluem datas de início e fim para permitir a geração de uma linha do tempo (timeline) automática.

### Língua (Entidade Adicional)
* **Justificação 1:** Decidi incluir esta entidade por ser um fator diferenciador em currículos de TI, permitindo separar as "Hard Skills" técnicas das competências comunicativas.
* **Justificação 2:** Campo `certificado` (FileField) para prova documental de proficiência.

### MakingOf (Entidade Obrigatória)
* **Justificação 1:** Modelação centralizada para permitir que o processo de desenvolvimento seja parte integrante da base de dados, facilitando a manutenção da página "Making Of".
* **Justificação 2:** Atributo `uso_ia` para manter o registo de como ferramentas externas auxiliaram na produtividade.

---

## 3. Evolução do Modelo e Erros

| Versão | Alteração | Motivo / Erro Corrigido |
| :--- | :--- | :--- |
| **v1.0** | Tecnologias como CharField no Projeto | **Erro:** Impossível filtrar ou associar logos a cada tecnologia. |
| **v1.1** | Criação da Entidade Tecnologia | Permite reutilizar a tecnologia em vários projetos e UCs. |
| **v1.2** | Relação Professor/UC alterada | De FK para Many-to-Many para permitir múltiplos docentes por UC. |

---

## 4. Uso de Inteligência Artificial

Neste projeto, utilizei o modelo **Gemini** como assistente de modelação.
* **Contribuição Positiva:** Auxiliou na estruturação da lógica de relações `Many-to-Many` e na redação técnica das justificações. Ajudou na conversão do raciocínio em papel para o formato `models.py` do Django.
* **Validação Humana:** Todas as sugestões da IA foram revistas face ao enunciado da Ficha 6, garantindo que os requisitos mínimos de atributos por entidade fossem cumpridos.

---
