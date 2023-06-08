from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ml import FaceDetect
app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse, name="home")
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/camera", response_class=HTMLResponse)
async def camera(request: Request):
    fd = FaceDetect()
    fd.start_detect()
    return templates.TemplateResponse("smile-detected.html", {"request": request})
