from fastapi import FastAPI

from schemas import Blog

app = FastAPI()




@app.post("/blog")
async def create_blog(request: Blog):
    return request
