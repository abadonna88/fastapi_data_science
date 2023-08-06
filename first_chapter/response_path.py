from fastapi import FastAPI, status, Response, Body, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse


class Post(BaseModel):
    title: str


# Dummy database
posts = {
    1: Post(title="hello", nb_views=100),
}


app = FastAPI()


@app.get("/")
async def custom_header(response: Response):
    response.headers["Custom-Header"] = "Custom-Header-Value"
    return {"hello": "world"}


@app.get("/cookie")
async def custom_cookie(response: Response):
    response.set_cookie("cookie-name", "cookie-value", max_age=86400)
    return {"hello": "world"}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    return post


@app.put("/posts/{id}")
async def update_or_create_post(id: int, post: Post, response: Response):
    if id not in posts:
        response.status_code = status.HTTP_201_CREATED
    posts[id] = post
    return posts[id]


@app.post("/password")
async def check_password(password: str=Body(...), password_confirm: str=Body(...)):
    if password != password_confirm:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Passwords don't match.",)
    return {"message": "Password match"}


@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return """
        <html>
            <head>
                <title>Hello</title>
            </head>
            <body>
                <h1>Hello World!</h1>
            </body>
        </html>
    """


@app.get("/text", response_class=PlainTextResponse)
async def text():
    return "Hello world!"


@app.get("/redirect")
async def redirect():
    return RedirectResponse("/new-url", status_code=status.HTTP_301_MOVED_PERMANENTLY)

