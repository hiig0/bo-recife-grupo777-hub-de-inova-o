# 06 — Arquitetura e Tecnologias


## Arquitetura

O sistema seguirá uma arquitetura de monólito modular com API REST. O frontend web responsivo se comunica com o backend por meio da API. Após a autenticação e o controle de acesso, as requisições são direcionadas aos módulos responsáveis pelas funcionalidades do sistema, que utilizam o PostgreSQL como banco de dados principal. 

```text
Interface Web Responsiva
↓
API HTTP/REST
↓
Autenticação e Controle de Acesso
↓
Módulos do Sistema
Catálogo | Projetos | Curadoria | Conexões | Indicadores
↓
PostgreSQL
```


## Frontend

A interface será uma aplicação web responsiva, acessível por navegador em computadores e celulares. O frontend será desenvolvido em JavaScript e será responsável pela exibição do catálogo de projetos, filtros, páginas dos projetos e formulários de interação com o usuário. A comunicação com o backend será feita por meio de uma API HTTP/REST

## Backend

O backend será organizado em módulos (Catálogo, Projetos, Curadoria, Conexões e Indicadores) e dividido em camadas de apresentação, aplicação e serviços, domínio e persistência. A consulta aos projetos será pública, enquanto as áreas de cadastro, curadoria e administração exigirão autenticação.

## Banco de dados

PostgreSQL: utilizado como banco de dados principal, oferecendo integridade referencial, suporte a transações e busca textual por palavras-chave. 

## APIs


- Oferecidas: API HTTP/REST utilizada para comunicação entre o frontend e o backend.
- Consumidas: Serviço de e-mail para notificações.


## Serviços externos

- Serviço de e-mail (notificações de contato e de aprovação).
- Futuro: Lattes/ORCID (importação de dados) e ferramenta de BI.


## Infraestrutura

A aplicação será executada em um ambiente de hospedagem web, com suporte ao backend, ao banco de dados PostgreSQL e aos recursos de autenticação, logs e monitoramento. A infraestrutura será definida de acordo com as necessidades do MVP e os recursos disponíveis para a equipe.

## Tecnologias

| Camada | Tecnologia | Justificativa |
|---|---|---|
| Frontend |  JavaScript, HTML E CSS | Acesso pelo navegador, no computador e no celular|
| Backend |Python | Linguagem de fácil manutenção, com ampla disponibilidade de bibliotecas e suporte ao desenvolvimento de APIs.|
| Banco de dados | PostgreSQL |Integridade, transações ACID, busca textual nativa, open source|
| Autenticação| JWT com perfis |Sessão sem estado e permissões por perfil|
| Notificações | Fila em segundo plano + e-mail | Não atrasa a solicitação de contato |
| Hospedagem |  A definir | Será escolhida considerando os recursos disponíveis e as necessidades do MVP  |

## Justificativas técnicas

- Monólito modular: equipe pequena e prazo de MVP; reduz a complexidade de operação, mantendo fronteiras claras entre módulos.
- PostgreSQL: projetos, usuários e conexões precisam de integridade e busca por texto.
- JWT com perfis: plataforma pública, mas com áreas restritas (RF11).
- Curadoria obrigatória: qualidade dos dados e conformidade com propriedade intelectual (RF10, RNF05).
- Notificações e indicadores assíncronos: e-mails e registros não devem atrasar o pedido de contato.


## Entidades principais

| Entidade | Atributos principais | Descrição |
|---|---|---|
| Usuário | id, nome, e-mail, senha_hash, perfil | Conta com perfil Pesquisador, Instituição, Curador ou Gestor |
| Instituição | id, nome, sigla | UFPE, UPE, IFPE, CESAR School, NERD |
| Pesquisador | id, usuário, instituição, área, contato | Responsável por projetos |
| Projeto | id, título, resumo acessível, objetivos, aplicações, tipo, área, status, última atualização | Pesquisa ou projeto publicado no catálogo |
| ODS | id, número, nome | Tabela de referência usada nos filtros |
| Projeto\_ODS | projeto, ods | Relação entre projetos e ODS |
| Pedido de contato | id, projeto, nome, organização, e-mail, mensagem, data | Solicitação de contato com o pesquisador |
| Indicador | id, tipo, período, valor | Contagem de conexões qualificadas |
