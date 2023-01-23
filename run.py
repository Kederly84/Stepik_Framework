from wsgiref.simple_server import make_server
from framework.main import Framework
from views import routes

app = Framework(routes)

with make_server('', 8000, app) as httpd:
    print('Site available on:', 'http://127.0.0.1:8000', sep='\n')
    httpd.serve_forever()