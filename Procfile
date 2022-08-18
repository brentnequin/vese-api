release: flask db upgrade --directory app/migrations
web: gunicorn app.wsgi:app