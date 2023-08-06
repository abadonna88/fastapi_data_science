from fastapi import FastAPI, Query, Body, Form, Header, Cookie, Request
from path_parameters import UserType
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name: str
    age: int


app = FastAPI()

@app.get("/")
async def hello_world():
    return {"hello": "world"}


@app.get("/header")
async def get_header(user_agent: str=Header(...)):
    return {"user_agent": user_agent}


@app.get("/cookie")
async def get_cookie(hello: Optional[str] = Cookie(None)):
    return {"hello": hello}


@app.get("/request")
async def get_request_object(request: Request):
    return {"path": request.url.path}


@app.get("/users")
async def get_user(page: int = Query(1, gt=0), size: int = Query(10, le=100)):
    return {"page": page, "size": size}


@app.get("/users/{type}/{id}")
async def get_users(type: UserType, id: int):
    return {"id": id}


@app.post("/users")
async def create_user(name: str=Form(...), age: int=Form(...)):
    return {"name": name, "age": age}





