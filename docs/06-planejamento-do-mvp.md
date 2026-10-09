# 07 — Planejamento do MVP

> **Objetivo deste documento:** definir com precisão o que será entregue como MVP na AV2.
>
> **Avaliação:** AV1 (é um dos documentos mais importantes da AV1)

---

## O que é um MVP?

> **MVP significa Produto Mínimo Viável.** Não é o sistema completo. É a **menor versão da solução capaz de demonstrar que a proposta central funciona**.

Um bom MVP:
- resolve **uma parte clara** do problema;
- possui **pelo menos um fluxo principal funcionando de ponta a ponta**;
- é **viável** de ser construído pela equipe no prazo da disciplina;
- pode ser **testado** e **validado**.

## O que obrigatoriamente estará no MVP?

Funcionalidades F01 a F07:

- Catálogo público com busca por palavra-chave e filtros (área, instituição, tipo de projeto e ODS).
- Perfil padronizado do projeto, com resumo acessível, objetivos, aplicações e instituição.
- Login com perfis de acesso (Pesquisador, Curador e Gestor).
- Cadastro e atualização de projetos, com status "Em curadoria".
- Aprovação dos projetos pelo curador antes da publicação.
- Solicitação de contato com registro no banco de dados.

Se o prazo permitir, serão incluídos indicadores básicos (F08) e notificações por e-mail (F09), conforme o planejamento do MVP.

## O que NÃO estará no MVP?

- Integração com Lattes/ORCID (os dados serão carregados manualmente).
- Recomendação automática de pesquisas.
- Hackathons e eventos com inscrição.
- Painel público de indicadores e BI.
- CI/CD avançado e testes de resiliência.
- Perfil de Instituição com tela própria (as instituições serão cadastradas pela equipe).


## Fluxo mínimo que deverá funcionar

```text
Pesquisador cadastra projeto
    ↓
Curador aprova e publica
    ↓
Empresa/órgão público busca, filtra e abre o perfil
    ↓
Solicita contato
    ↓
Pedido gravado no PostgreSQL
    ↓
Pedido registrado e disponível para o pesquisador responsável
```


## Funcionalidades por avaliação

| Funcionalidade | AV1 | AV2 | Prioridade |
|---|---|---|---|
| F01 - Catálogo e busca | Em desenvolvimento | Implementar | Alta |
| F02 - Filtros | Em desenvolvimento | Implementar | Alta |
| F03 - Perfil padronizado | Em desenvolvimento | Implementar | Alta |
| F04 - Cadastro e atualização | Em desenvolvimento | Implementar | Alta |
| F05 - Curadoria | Em desenvolvimento | Implementar | Alta |
| F06 - Solicitar contato | Em desenvolvimento | Implementar | Alta |
| F07 - Autenticação e perfis | Em desenvolvimento | Implementar | Alta |
| F08 - Indicadores | Planejada | Implementar se houver prazo | Média |
| F09 - Notificação por e-mail | Planejada | Implementar se houver prazo | Média |

## Riscos

| Risco | Plano de ação |
|---|---|
| Baixa adesão das instituições e dados desatualizados | Carregar manualmente um conjunto inicial de projetos para demonstração e exibir a última atualização no perfil. |
| Conteúdo técnico difícil de entender | Utilizar campos obrigatórios no cadastro e adaptar os textos durante a curadoria. |
| Violação de propriedade intelectual ou de política de divulgação | Exigir termo de autorização no cadastro e validar os projetos antes da publicação. |
| Acesso indevido a áreas restritas | Utilizar JWT, autorização por perfil, HTTPS e testes de acesso. |
| Lentidão nas buscas com o crescimento do catálogo | Utilizar índices no PostgreSQL, paginação e testes de carga. |
| Falta de recursos para manter a plataforma | Começar com uma estrutura simples, utilizar componentes open source e acompanhar o uso. |
| Escopo maior que o prazo da AV2 | Priorizar o fluxo mínimo e retirar F08 e F09, se necessário. |

## Cronograma


| Etapa | Responsável | Situação |
|---|---|---|
| Escolha do BO e investigação | Arnaldo Reis | Concluído |
| Proposta e requisitos | Higor Ricardo | Concluído |
| Protótipo navegável | Gustavo Lopes | Concluído |
| Arquitetura e planejamento | Carla Rayanne | Concluído |
| Entrega da AV1 | Higor Ricardo | Não iniciado |
| Modelagem do banco e API | Arnaldo Reis | Não iniciado |
| Frontend e fluxo mínimo | Emilly Mayra | Não iniciado |
| Testes e validação | Arnaldo Reis | Não iniciado |
| Entrega da AV2 | Higor Ricardo | Não iniciado |
