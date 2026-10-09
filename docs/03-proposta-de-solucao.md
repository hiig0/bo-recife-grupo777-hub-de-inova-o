
# 03 — Proposta de Solução

> **Objetivo deste documento:** apresentar a solução tecnológica proposta pela equipe e mostrar como ela se relaciona com o problema e as evidências levantadas.
>
> **Avaliação:** AV1
>
> Cada funcionalidade deve estar ligada a uma parte do problema descrito em [01-problema.md](01-problema.md) e às evidências de [02-investigacao-e-evidencias.md](02-investigacao-e-evidencias.md).

---

## Nome da solução

Rec Science

## Resumo

Plataforma pública que reúne pesquisas e projetos desenvolvidos por instituições do Recife em um único catálogo. O usuário poderá pesquisar e filtrar projetos por área, instituição, tipo de projeto e ODS. Cada projeto terá informações apresentadas de forma clara, além da opção de solicitar contato com os pesquisadores responsáveis. A plataforma busca dar mais visibilidade às pesquisas e facilitar a criação de parcerias.

## Público-alvo

Pesquisadores, instituições de ensino e pesquisa, empresas privadas, órgãos públicos, empreendedores, investidores e cidadãos interessados em inovação.

## Usuários

| Tipo de usuário | O que faz no sistema? |
|---|---|
| Usuário público / empresa / órgão público | Pesquisa projetos, consulta perfis e solicita contato. |
| Pesquisador | Cadastra e atualiza seus projetos e responde a pedidos de contato. |
| Instituição | Fornece e valida os dados dos seus projetos. |
| Curador (Comitê de inovação) | Analisa os projetos antes da publicação e ajuda a deixar as informações mais claras. |
| Gestor da plataforma | Acompanha o funcionamento da plataforma e seus resultados. |

## Proposta de valor

Hoje, as pesquisas locais estão espalhadas em diferentes lugares e muitas vezes são apresentadas com uma linguagem difícil de entender. O Hub reúne essas pesquisas em um só lugar, apresenta as informações de forma mais clara e facilita o contato entre pesquisadores e pessoas ou organizações interessadas.

## Fluxo principal

```text
Pesquisador cadastra projeto
    ↓
Curadoria valida e adapta
    ↓
Projeto é publicado
    ↓
Empresa/órgão público pesquisa e filtra
    ↓
Abre o perfil do projeto
    ↓
Solicita contato
    ↓
Sistema registra o pedido e notifica o pesquisador
    ↓
Conexão qualificada contabilizada nos indicadores
```

## Funcionalidades essenciais

| ID | Funcionalidade | Problema que ajuda a resolver | Prioridade |
|---|---|---|---|
| F01 | Catálogo público com busca por palavra-chave | Falta de centralização e visibilidade | Alta |
| F02 | Filtros por área, instituição, tipo de projeto e ODS | Dificuldade de encontrar pesquisas relevantes | Alta |
| F03 | Perfil padronizado do projeto (resumo acessível, objetivos, aplicações, instituição) | Barreira de linguagem técnica | Alta |
| F04 | Cadastro e atualização de projetos pelo pesquisador | Dados dispersos e desatualizados | Alta |
| F05 | Análise dos projetos antes da publicação | Garantir a qualidade das informações | Alta |
| F06 | Solicitação de contato com o pesquisador, com registro | Ausência de canal de conexão | Alta |
| F07 | Autenticação e perfis de acesso | Proteção das áreas restritas | Alta |
| F08 | Notificação por e-mail em segundo plano | Pesquisador não saber do pedido | Alta |

## Funcionalidades futuras

- Integração com Lattes e ORCID para importar informações dos pesquisadores.
- Recomendação de pesquisas de acordo com os interesses de empresas e órgãos públicos.
- Divulgação de eventos e hackathons, com possibilidade de inscrição.
- Painel público com informações sobre os contatos e parcerias gerados pela plataforma.
- Relatórios sobre o uso e os resultados da plataforma.
- Indicadores de conexões qualificadas.

## Diferencial

Diferente de plataformas como Lattes e ORCID, que são voltadas principalmente para informações sobre pesquisadores e suas produções, o Hub busca aproximar as pesquisas de quem pode utilizá-las. Os projetos são reunidos em um só lugar, apresentados de forma mais simples e organizados para facilitar a busca e o contato com os pesquisadores responsáveis.
