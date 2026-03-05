from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
import json

from fastapi.templating import Jinja2Templates
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
async def select():
    return FileResponse(os.path.join(GUI_DIR, "select.html"))

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
    data = {
        "delay": delay,
        "start_delay": start_delay,
        "iterations": iterations
    }

    # Save to JSON file
    with open("program_settings.json", "w") as f:
        json.dump(data, f, indent=4)

    return templates.TemplateResponse("program.html", {
        "request": request,
        "success": True
    })
