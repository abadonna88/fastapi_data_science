from typing import Tuple

from fastapi import FastAPI, Depends, Query, status
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse


class Post(BaseModel):
    title: str


class PostUpdate(BaseModel):
    title: str

# Dummy database
posts = {
    1: Post(title="hello", nb_views=100),
}


class Pagination:
    def __init__(self, maximum_limit: int=100):
        self.maximum_limit = maximum_limit
    
    
    async def skip_limit(self, skip: int=Query(0, ge=0), limit: int=Query(10, ge=0)) -> Tuple[int, int]:
        capped_limit = min(self.maximum_limit, limit)
        return (skip, capped_limit)

    async def page_size(self, page: int=Query(1, ge=1), size: int=Query(10, ge=0)) -> Tuple[int, int]:
        capped_size = min(self.maximum_limit, size)
        return (page, capped_size)


app = FastAPI()


async def pagination(skip: int=Query(0, ge=0), limit: int=Query(10, ge=0)) -> Tuple[int, int]:
    return (skip, limit)


async def get_post_or_404(id: int) -> Post:
    try:
        return db.posts[id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


pagination = Pagination(maximum_limit=50)


@app.get("/items")
async def list_items(p: Tuple[int, int]=Depends(pagination.skip_limit)):
    skip, limit = p
    return {"skip": skip, "limit": limit}


@app.get("/things")
async def list_things(p: Tuple[int, int]=Depends(pagination.page_size)):
    skip, limit = p
    return {"skip": skip, "limit": limit}


@app.get("/posts/{id}")
async def get(post: Post=Depends(get_post_or_404)):
    return post


@app.patch("/posts/{id}")
async def update(post_update: PostUpdate, post: Post=Depends(get_post_or_404)):
    updated_post = post.copy(update=post_update.dict())
    db.posts[post.id] = updated_post
    return updated_post


@app.delete("posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(post: Post=Depends(get_post_or_404)):
    db.posts.pop(post.id)


