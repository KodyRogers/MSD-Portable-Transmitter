from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
import json

from fastapi.templating import Jinja2Templates
from backend.load_files import load_files
from backend.settings import load_settings, save_settings
from httpcore import request

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GUI_DIR = os.path.join(BASE_DIR, "gui")
CSS_DIR = os.path.join(BASE_DIR, "css")

templates = Jinja2Templates(directory=GUI_DIR)

# Serve static files (CSS, JS, images, etc.)
#app.mount("/static", StaticFiles(directory=GUI_DIR), name="static")
app.mount("/css", StaticFiles(directory=CSS_DIR), name="css")

@app.get("/")
async def serve_index():
    return FileResponse(os.path.join(GUI_DIR, "index.html"))

@app.get("/program")
async def program(request: Request):
    return templates.TemplateResponse("program.html", {
        "request": request,
        "success": False
    })

@app.get("/control")
async def control():
    return FileResponse(os.path.join(GUI_DIR, "control.html"))

@app.get("/select")
async def select(request: Request):
    
    files = load_files()
    return templates.TemplateResponse("select.html", {
        "request": request,
        "files": files
    })

@app.get("/recordings")
async def recordings():
    return FileResponse(os.path.join(GUI_DIR, "recordings.html"))

@app.get("/status")
async def status():
    return FileResponse(os.path.join(GUI_DIR, "status.html"))


@app.post("/save-program")
async def save_program(
    request: Request,
    delay: int = Form(...),
    start_delay: int = Form(...),
    iterations: int = Form(...)
):
    
    data = load_settings()
    
    data["program"] = {
        "delay": delay,
        "start_delay": start_delay,
        "iterations": iterations
    }

    save_settings(data)

    return templates.TemplateResponse("program.html", {
        "request": request,
        "success": True
    })


@app.post("/create_sequence")
async def create_sequence(request: Request):

    payload = await request.json()
    order = payload["order"]

    data = load_settings()
    data["sequence"] = order
    save_settings(data)

    return {"status":"ok", "success": True}