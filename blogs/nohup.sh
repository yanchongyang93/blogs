nohup gunicorn blogproject.wsgi -w 3 -k gthread -b 127.0.0.1:8000 2>&1 &
