from fastapi import FastAPI,Form,Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,JSONResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from modules import user_hash

app=FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
templates=Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
def login(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})

@app.get("/register",response_class=HTMLResponse)
def login(request:Request):
    return templates.TemplateResponse("register.html",{"request":request})
