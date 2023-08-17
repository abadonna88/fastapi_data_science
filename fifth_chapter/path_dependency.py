from typing import Optional

from fastapi import FastAPI, status, Response, Body, Header, HTTPException, Depends
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse


def secret_header(secret_header: Optional[str]=Header(None)) -> None:
    if not secret_header or secret_header != "SECRET VALUE":
        raise HTTPException(status.HTTP_403_FORBIDDEN)


app = FastAPI(dependencies=[Depends(secret_header)])



@app.get("/protected-route")
async def protected_route():
    return {"hello": "world"}

