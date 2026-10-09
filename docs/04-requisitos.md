> **Objetivo deste documento:** transformar a proposta de solução em requisitos claros e verificáveis.
>
> **Avaliação:** AV1 (revisar na AV2, se necessário)

---

## Requisitos funcionais

| ID | Requisito |
|---|---|
| RF01 | O sistema deve disponibilizar uma plataforma pública para consulta de pesquisas e projetos. |
| RF02 | O sistema deve permitir cadastrar e atualizar projetos e pesquisas. |
| RF03 | O sistema deve permitir pesquisar por palavras-chave. |
| RF04 | O sistema deve permitir filtrar por área do conhecimento, instituição, tipo de projeto e ODS relacionado. |
| RF05 | O sistema deve apresentar uma página com as informações de cada projeto. |
| RF06 | A página do projeto deve apresentar um resumo em linguagem simples, seus objetivos e possíveis aplicações. |
| RF07 | O sistema deve permitir solicitar contato com os pesquisadores responsáveis. |
| RF08 | O sistema deve permitir identificar a instituição responsável por cada projeto. |
| RF09 | O sistema deve registrar as solicitações de contato realizadas pelos usuários. |
| RF10 | O sistema deve permitir que o curador analise e aprove ou devolva projetos antes da publicação. |
| RF11 | O sistema deve permitir autenticação de usuários e controlar o acesso de acordo com o perfil cadastrado. |

## Requisitos não funcionais

| ID | Categoria | Requisito |
|---|---|---|
| RNF01 | Segurança | As áreas restritas, como cadastro, curadoria e administração, devem exigir login e permissão adequada. |
| RNF02 | Usabilidade | O projeto deve ser encontrado e consultado em no máximo 3 cliques a partir da página inicial. |
| RNF03 | Desempenho | 95% das buscas com filtros devem apresentar os resultados em até 2 segundos. |
| RNF04 | Clareza do conteúdo | Todos os projetos publicados devem apresentar resumo em linguagem simples, objetivos e possíveis aplicações. |
| RNF05 | Integridade | Todos os projetos devem passar por análise e aprovação antes de serem publicados. |
| RNF06 | Compatibilidade | A aplicação deve ser web responsiva, utilizável em navegador de computador e de celular. |
| RNF07 | Arquitetura | Frontend e backend devem se comunicar por API HTTP/REST, com PostgreSQL como banco principal. |
| RNF08 | Segurança | A comunicação deve usar HTTPS. |

## Critérios de aceite do MVP

- [ ] **Busca:** dado que o usuário está na página inicial, quando digita uma palavra-chave e aplica filtros, então vê somente projetos publicados que atendem aos critérios, em até 2 s em 95% das buscas.
- [ ] **Perfil:** dado que o usuário abriu um projeto publicado, então vê resumo acessível, objetivos, aplicações e instituição responsável.
- [ ] **Acesso restrito:** dado que um usuário sem login ou sem perfil adequado, quando tenta acessar a área de curadoria ou administração, então o sistema bloqueia o acesso.
- [ ] **Curadoria:** dado que um pesquisador cadastra ou altera um projeto, então o projeto fica "Em curadoria" e só aparece no catálogo público após aprovação do curador.
- [ ] **Contato:** dado que o usuário está no perfil de um projeto, quando envia um pedido de contato, então o pedido é registrado no sistema e fica disponível ao pesquisador responsável.
- [ ] **Usabilidade:** dado um projeto publicado, então ele é alcançado em no máximo 3 cliques a partir da página inicial.