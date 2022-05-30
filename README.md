# FastAPI Blog API 

![GitHub language count](https://img.shields.io/github/languages/count/deverebor/fastapi-blog-api?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/deverebor/fastapi-blog-api?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/deverebor/fastapi-blog-api?style=for-the-badge)
![GitHub pull requests](https://img.shields.io/github/issues-pr/deverebor/fastapi-blog-api?style=for-the-badge)

---

> This is a simple API for a blog. It is built with FastAPI and uses SQLAlchemy for the database with SQLite.

## Sobre o projeto

Essa API foi desenvolvida com o FastAPI, um framework de desenvolvimento de APIs.

A api conta com um CRUD completo além de autenticação com JWT para a rota `/blog`, utilizando oauth2.

## Lista de Funcionalidades

Gophish returns the following status codes in its API:

| Funcionalidade                                    | Verbo    | Descrição                           | Autenticação |
|:--------------------------------------------------|:---------|:------------------------------------|:-------------|
| https://api-fastapi-blog.herokuapp.com/blog       | `GET`    | Lista todos os posts.               | `TRUE`       |
| https://api-fastapi-blog.herokuapp.com/blog       | `POST`   | Cria um novo post.                  | `TRUE`       |
| https://api-fastapi-blog.herokuapp.com/blog/{id}  | `GET`    | Lista um post específico.           | `TRUE`       |
| https://api-fastapi-blog.herokuapp.com/blog/{id}  | `PUT`    | Atualiza um post.                   | `TRUE`       |
| https://api-fastapi-blog.herokuapp.com/blog/{id}  | `DELETE` | Deleta um post.                     | `TRUE`       |
| https://api-fastapi-blog.herokuapp.com/users      | `POST`   | Cria um usuário.                    | `FALSE`      |
| https://api-fastapi-blog.herokuapp.com/users/{id} | `GET`    | Lista um usuário específico.        | `TRUE`       |
| https://api-fastapi-blog.herokuapp.com/auth       | `POST`   | Gera um JWT para acesso do usuário. | `FALSE`      |

### Ajustes e melhorias

O projeto está concluido porem restam alguns pontos de melhoria:

- [ ] Migra a estrutura para postgresql
- [ ] Adicionar testes unitários para as rotas
- [x] Fazer deploy no HEROKU.

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
* Você instalou a versão mais recente de `python & pip`.
* Você possui instalado Postman ou Insomnia para testar a API.
* Você tem uma máquina `Windows / Linux / Mac`.

## 🚀 Instalando FastAPI - Blog API

Para instalar o FastAPI - Blog API, siga estas etapas:

> Clone o repositório do projeto.

```zsh
git clone git@github.com:deverebor/fastapi-blog-api.git
```

> Entre no projeto

```zsh
cd fastapi-blog-api
```

> Crie um ambiente virtual

```zsh
python3 -m venv .venv
```

> Entre no ambiente virtual

```zsh
. .venv/bin/activate
```

> Instale as dependências

```zsh
pip install -r requirements.txt
```

> Inicie o servidor

```zsh
uvicorn api.main:app --reload
```

> Acesse a porta da API

```zsh
http://localhost:8000/docs
```

## ☕ Usando FastAPI - Blog API

Para usar FastAPI - Blog API, siga estas etapas:

> Crie um usuário na aplicação.

```web
POST: localhost:8000/users
```

> Logo após, faça o login.

```web
POST: localhost:8000/auth
```

Caso opte por fazer via interface, siga as seguintes etapas:

acesse a doc:

```web
http://localhost:8000/docs
```

E replique os passos ateriores.

Assim todas as rotas serão liberadas.

## 📫 Contribuindo para FastAPI - Blog API
Para contribuir com FastAPI - Blog API, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b feat: <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m 'feat: <commit>'`.
4. Envie para o branch original: `git push deverebor/fastapi-blog-api`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

[⬆ Voltar ao topo](#fastapi-blog-api)