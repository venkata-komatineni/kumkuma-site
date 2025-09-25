# Kumkuma Simple Site (No Ordering)

FastAPI website with static pages (Home, Menu, About, Contact). Customers call to order.

## Quick start
```bash
# 1) Create & activate a virtualenv (optional but recommended)
python -m venv .venv && . .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install deps
pip install -r requirements.txt

# 3) Run
uvicorn app:app --reload --port 8000

# Open the site
# http://localhost:8000
```
Pages:
- `/` Home
- `/menu`
- `/about`
- `/contact` (shows phone, address, hours)

## Edit your business info
Open `app.py` and update the `BRAND` dict (phone, address, hours).
Update menu items in `MENU` list.

## Deploy tips
- Railway / Render: deploy as a Python web service running `uvicorn app:app --host 0.0.0.0 --port $PORT`
- Dockerfile (optional) can be added easily if you need it.
