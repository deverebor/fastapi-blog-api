from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "data": {
            "message": "Hello World"
        }
    }


@app.get("/blog")
async def blog_list(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {
            "data": {
                f"{limit} published blog list from db"
            }
        }
    else:
        return {
            "data": {
                f"{limit} blog list from db"
            }
        }


@app.get('/blog/unpublished')
async def unpublished():
    return {
        "data": {
            "message": "Unpublished Blog"
        }
    }


@app.get('/blog/{id}')
async def blog(id: int):
    return {
        "data": {
            id: "Blog Post"
        }
    }


@app.get('/blog/{id}/comments')
async def comments(id: int, limit: int = 10):
    return {
        "data": {
            id: {
                f"comments {limit}": [
                    "Comment 1",
                    "Comment 2"
                ]
            }
        }
    }
