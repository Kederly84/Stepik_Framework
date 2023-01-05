Для запуска используется команда uwsgi --http :8080 --wsgi-file run.py,
можно так же запускать через gunicorn с командой gunicorn --bind=127.0.0.1:8080 run:application
