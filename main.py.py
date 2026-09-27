from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import google.generativeai as genai
import os

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/generate")
def generate_plan(request: Request, goal: str = Form(...), weight: str = Form(...)):
    prompt = f"Create a fitness plan for goal {goal}, weight {weight}kg."
    plan = f"Your plan for {goal}: Workout 5 days, Diet high protein. Weight {weight}kg"
    return templates.TemplateResponse(request, "index.html", {"plan": plan})