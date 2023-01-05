from quopri import decodestring
from framework.requests_handlers import PostRequests, GetRequests


class PageNotFound:
    """Класс для обработки путей, не представленных в urls"""

    def __call__(self, requests):
        return '404 NOT FOUND', '404 Page not Found'


class Framework:
    """Основной класс фреймворка"""

    def __init__(self, routes: list, requests=None):
        if requests is None:
            requests = {}
        self.routes = routes
        self.requests = requests

    def __call__(self, environ: dict, start_response):
        # Получаем адрес по которому хотел перейти пользователь
        url_path = environ['PATH_INFO']

        # Проверяем, корректность указания пути, если в пути не указан слеш - добавляем его
        if not url_path.endswith('/'):
            url_path = f'{url_path}/'

        # Получаем данные запроса
        method = environ['REQUEST_METHOD']
        self.requests['method'] = method

        # Обработка, если метод POST
        if method == 'POST':
            # Получаем данные из запроса
            data = PostRequests().get_request_params(environ)
            # Сохраняем в словарь
            self.requests['data'] = Framework.decode_data(data)
            # Вывод в терминал содержимого POST запроса
            print(f'We have POST data {Framework.decode_data(data)}')

        # Обработка, если метод GET
        if method == 'GET':
            # Получаем данные из запроса
            request_params = GetRequests().get_request_params(environ)
            # Сохраняем в словарь
            self.requests['request_params'] = request_params
            # Вывод в терминал содержимого POST запроса
            print(f'We have GET params {request_params}')

        # Находим нужный контроллер или PageNotFound если нет нужного
        if url_path in self.routes:
            view = self.routes[url_path]
        else:
            view = PageNotFound()

        # Запускаем нужный контроллер
        code, body = view(self.requests)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_data(data: dict) -> dict:
        """
        Функция для корректного декодирования кириллических символов
        :param data: Словарь, с закодированными символами
        :return: Словарь с корректным отображением кириллических символов
        """
        new_data = {}
        for key, value in data.items():
            val = bytes(value.replace('%', '=').replace('+', ' '), 'UTF-8')
            val_decode = decodestring(val).decode("utf-8")
            new_data[key] = val_decode
        return new_data
