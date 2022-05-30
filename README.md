# FastAPI - Blog Api

> This is a simple API for a blog. It is built with FastAPI and uses SQLAlchemy for the database with SQLite.

# Basic usage
    
## Blog endpoint

**Get:** all the posts by using the `/blog` endpoint.
<br />
**Get:** a specific post by using the `/blog/<int:id>` endpoint.
<br />
**Post:** a new blog post by using the `/blog` endpoint.
<br />
**Put:** update a specific post by using the `/blog/<int:id>` endpoint.
<br />
**Delete:** delete a specific post by using the `/blog/<int:id>` endpoint.

## User endpoint

**Get:** all the users by using the `/users` endpoint.
<br />
**Get:** specific user by using the `/users/<int:id>` endpoint.

## Auth endpoint

Genreate a token by using the `/auth` endpoint.
<br />
You will need to set the `SECRET_KEY`, `ACCESS_TOKEN_EXPIRATION_TIME` and `ALGORITHM` in .env environment variable to 
use this endpoint.

## Api Docs

just fork the project and access the docs with`localhost:8000/docs` or `localhost:8000/redoc`
to see all endpoints.
