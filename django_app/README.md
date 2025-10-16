# Django Docker App

Local development commands (if Docker is unavailable):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

With Docker:

```bash
docker compose build
docker compose up
```
