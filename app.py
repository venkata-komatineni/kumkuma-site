from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
import datetime as dt

BASE = Path(__file__).parent
templates = Environment(
    loader=FileSystemLoader(str(BASE / "templates")),
    autoescape=select_autoescape(["html", "xml"]),
)

app = FastAPI(title="Kumkuma — Biryani Kitchen", version="0.1.0")
app.mount("/static", StaticFiles(directory=str(BASE / "static")), name="static")

BRAND = {
    "name": "Kumkuma",
    "tagline": "Biryani-only cloud kitchen",
    "phone": "+44 20 7123 4567",
    "address": "123 Spice Lane, London",
    "hours": "Mon–Sun 11:00–23:00",
    "colors": {"saffron":"#FF6F00","maroon":"#7B1F2A","beige":"#F5E6C8","charcoal":"#2C2C2C"},
}

MENU = [
    {"name": "Chicken Biryani", "desc": "Fragrant basmati, tender chicken, saffron.", "price": "£7.99 / £12.99 / £19.99"},
    {"name": "Mutton Biryani", "desc": "Slow-cooked mutton, layered rice, whole spices.", "price": "£9.99 / £15.99 / £23.99"},
    {"name": "Veg Biryani", "desc": "Seasonal veg, mint & fried onions.", "price": "£6.99 / £11.99 / £18.99"},
    {"name": "Raita", "desc": "Cool yoghurt with cucumber & mint.", "price": "£1.99"},
    {"name": "Gulab Jamun", "desc": "Warm syrupy dumplings.", "price": "£3.49"},
    {"name": "Soft Drinks", "desc": "Assorted cans.", "price": "£1.50"},
]

def render(tpl_name: str, request: Request, **ctx) -> HTMLResponse:
    t = templates.get_template(tpl_name)
    html = t.render(request=request, BRAND=BRAND, year=dt.date.today().year, **ctx)
    return HTMLResponse(html)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return render("index.html", request, title="Home")

@app.get("/menu", response_class=HTMLResponse)
async def menu(request: Request):
    return render("menu.html", request, title="Menu", items=MENU)

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return render("about.html", request, title="About")

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return render("contact.html", request, title="Contact")
