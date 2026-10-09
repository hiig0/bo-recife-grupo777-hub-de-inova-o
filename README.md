# Hub de Inovação e Pesquisa de Recife

Projeto Integrador do curso de **Análise e Desenvolvimento de Sistemas**, desenvolvido a partir de um desafio do [Banco de Oportunidades da Prefeitura do Recife](https://bancodeoportunidades.recife.pe.gov.br/).

> **Situação do projeto:** AV1 em andamento; AV2 não iniciada. O desenvolvimento do MVP será realizado na segunda avaliação.

## Identificação da equipe

- **Turma:** 5NA
- **Grupo:** REC SCIENCE
- **Nome do projeto:** REC SCIENCE
- **BO escolhido:** Hub de Inovação e Pesquisa de Recife
- **Link do BO:** https://bancodeoportunidades.recife.pe.gov.br/

### Integrantes

| Nome | GitHub |
|---|---|
| Arnaldo Reis Leal Neto | [Arnaldoreisl](https://github.com/Arnaldoreisl) |
| Carla Rayanne da Silva | [CarlaSilva](https://github.com/CarlaSilva-Dev) |
| Gustavo Lopes de Lima | [gustavolopeslima](https://github.com/gustavolopeslima) |
| Higor Ricardo da Silva | [hiig0](https://github.com/hiig0) |
| Emilly Mayra do Santos Silva | A informar |

## Visão geral

Recife reúne universidades, institutos federais e centros de inovação que produzem pesquisas e projetos relevantes. Entretanto, essas informações ficam distribuídas entre diferentes sites e instituições, dificultando que gestores públicos, empresas, empreendedores e cidadãos encontrem e compreendam possíveis soluções.

O **Hub de Inovação e Pesquisa de Recife** propõe uma plataforma pública para reunir pesquisas e projetos em um catálogo pesquisável, com filtros por área do conhecimento, instituição, tipo de projeto e Objetivos de Desenvolvimento Sustentável (ODS). Cada projeto terá uma apresentação padronizada e acessível, além de um mecanismo para solicitar contato com os pesquisadores responsáveis.

## Problema e proposta de solução

**Problema:** a produção científica e tecnológica local tem pouca centralização e visibilidade fora do meio acadêmico. A linguagem técnica e a ausência de um canal organizado de contato dificultam possíveis parcerias e aplicações práticas.

**Solução:** disponibilizar um catálogo público de pesquisas e projetos das instituições participantes, com informações padronizadas, curadoria antes da publicação e registro das solicitações de contato.

**Público-alvo:** pesquisadores, instituições de ensino e pesquisa, empresas, órgãos públicos, empreendedores, investidores e cidadãos interessados em inovação.

### Fluxo principal previsto

```text
Pesquisador cadastra um projeto
        ↓
Curador analisa e aprova a publicação
        ↓
Interessado pesquisa e filtra os projetos
        ↓
Interessado consulta o perfil do projeto
        ↓
Interessado solicita contato
        ↓
Sistema registra a solicitação para o pesquisador responsável
```

## Funcionalidades do MVP

- Catálogo público com pesquisa por palavras-chave.
- Filtros por área do conhecimento, instituição, tipo de projeto e ODS.
- Perfil padronizado dos projetos, com resumo acessível, objetivos, aplicações e instituição responsável.
- Cadastro e atualização de projetos por pesquisadores.
- Análise e aprovação dos projetos antes da publicação (curadoria).
- Solicitação de contato com o pesquisador, com registro no sistema.
- Autenticação e controle de acesso conforme o perfil do usuário.

**Fora do escopo inicial:** importação automática de dados do Lattes/ORCID, recomendação automática de pesquisas, negociação ou financiamento pela plataforma e painel público de BI. Notificações por e-mail e indicadores básicos poderão ser incluídos se houver tempo.

## Arquitetura e tecnologias previstas

A solução foi planejada como um **monólito modular**, com uma interface web responsiva, comunicação por **API HTTP/REST** e persistência em **PostgreSQL**.

| Camada | Tecnologia ou abordagem |
|---|---|
| Frontend | HTML, CSS e JavaScript |
| Backend | Python |
| Banco de dados | PostgreSQL |
| Autenticação | JWT com controle de acesso por perfil |
| Comunicação | API HTTP/REST |
| Notificações | Serviço de e-mail e processamento em segundo plano, se incluído |
| Hospedagem | A definir conforme os recursos do MVP |

> As tecnologias acima descrevem o planejamento arquitetural da equipe, não uma implementação já concluída.

## Protótipo

[**Acessar o protótipo no Figma**](https://www.figma.com/design/3QOYNbl0Jwc72Y3NQvX92X/Untitled?node-id=0-1&t=af7AH4OgNlfhMWEu-1)

O fluxo navegável mínimo previsto é: **página inicial → busca com filtros → perfil do projeto → solicitação de contato → confirmação**.

## Documentação

Os arquivos disponíveis no repositório organizam as entregas e o planejamento do projeto:

| Arquivo | Conteúdo |
|---|---|
| [01-problema.md](docs/01-problema.md) | Definição e delimitação do problema |
| [02-investigacao-e-evidencias.md](docs/02-investigacao-e-evidencias.md) | Investigação e evidências |
| [03-proposta-de-solucao.md](docs/03-proposta-de-solucao.md) | Proposta de solução e funcionalidades |
| [04-requisitos.md](docs/04-requisitos.md) | Requisitos funcionais, não funcionais e critérios de aceite |
| [05-arquitetura-e-tecnologias.md](docs/05-arquitetura-e-tecnologias.md) | Arquitetura e tecnologias previstas |
| [06-planejamento-do-mvp.md](docs/06-planejamento-do-mvp.md) | Escopo e planejamento do MVP |
| [checklist-av1.md](docs/checklist-av1.md) | Conferência da entrega AV1 |
| [checklist-av2.md](docs/checklist-av2.md) | Conferência da entrega AV2 |

Outros arquivos importantes: [ENTREGA.md](ENTREGA.md), para identificação das versões entregues, e [CONTRIBUTING.md](CONTRIBUTING.md), para as regras de colaboração.

## Avaliações e entregas

### AV1 — Projeto da solução

A primeira avaliação contempla a investigação do problema, a proposta de solução, os requisitos, o protótipo, a arquitetura e o planejamento do MVP.

- **Status no documento acadêmico:** em andamento.
- **Tag prevista para a entrega:** `v1.0-av1`.
- **Checklist:** [docs/checklist-av1.md](docs/checklist-av1.md).

### AV2 — MVP funcional

Na segunda avaliação, a equipe deverá implementar e validar pelo menos um fluxo principal funcional de ponta a ponta, incluindo o registro de solicitações de contato no banco de dados.

- **Status no documento acadêmico:** não iniciada.
- **Tag prevista para a entrega:** `v2.0-av2`.
- **Checklist:** [docs/checklist-av2.md](docs/checklist-av2.md).

### Como executar

As instruções de instalação, variáveis de ambiente e execução serão adicionadas quando a implementação do MVP estiver definida e disponível na AV2. **O protótipo e a documentação não substituem a aplicação funcional.**

### Versionamento das avaliações

A equipe deverá registrar em [ENTREGA.md](ENTREGA.md) a tag/release correspondente a cada avaliação. As tags só devem ser criadas após a revisão e consolidação das alterações na branch principal, seguindo o procedimento do professor.

## Colaboração e segurança

Todos os integrantes devem contribuir para o repositório utilizando suas próprias contas. As mudanças devem ser registradas em commits descritivos, preferencialmente em branches, com Pull Requests revisados pela equipe. Consulte [CONTRIBUTING.md](CONTRIBUTING.md).

Não devem ser publicados senhas, tokens, chaves de API, credenciais, arquivos `.env` com valores reais nem dados pessoais sensíveis.

## Licença

Este projeto está distribuído sob a licença MIT. Consulte [LICENSE](LICENSE).
