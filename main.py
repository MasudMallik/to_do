from fastapi import FastAPI,Form,Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,JSONResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from modules.user_hash import new_user
from pydantic import ValidationError

app=FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
templates=Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
def login(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})

@app.get("/register",response_class=HTMLResponse)
def login(request:Request):
    return templates.TemplateResponse("register.html",{"request":request})


@app.post("/",response_class=HTMLResponse)
def login(request:Request,email:str=Form(...,description="email of the user"),password:str=Form(...,description="password of thr user")):
    print(email,password)
    return templates.TemplateResponse("login.html",{"request":request})


@app.post("/register",response_class=HTMLResponse)
async def register(request:Request,
          name:str=Form(...,description="name"),
          email:str=Form(...,description="abc@gmail.com"),
          password:str=Form(...,description="atleast one lower,upper and special characet should be there"),
          confirm_password:str=Form(...)
          ):
    if name and email and password and confirm_password:
        try:
            user=new_user(
                name=name,
                email=email,
                password=password,
                confirm_password=confirm_password
            )
        except ValidationError as e:
            print(e.errors())  # list of dicts

            t = []
            for err in e.errors():
                loc = err.get("loc", [])
                if "name" in loc:
                    t.append("Name must contain alphabets only")
                elif "email" in loc:
                    t.append("Give correct email")
                elif "password" in loc:
                    t.append("Give strong password")

            return templates.TemplateResponse(
                "register.html",
                {"request": request, "confirm": t,}
            )