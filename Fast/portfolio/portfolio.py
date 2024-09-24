from fastapi import FastAPI,Request
from fastapi.responses import FileResponse,HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
async def Display(request: Request):
    return templates.TemplateResponse("portfolio.html",{"request": request})

@app.get("/academics",response_class=HTMLResponse)
async def get_academic(request: Request):
    return templates.TemplateResponse("academic.html",{"request": request})

@app.get("/exp",response_class=HTMLResponse)
async def get_experience(request: Request):
    return templates.TemplateResponse("experience.html",{"request": request})

@app.get("/skill",response_class=HTMLResponse)
async def get_skills(request: Request):
    return templates.TemplateResponse("skills.html",{"request": request})

#
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
