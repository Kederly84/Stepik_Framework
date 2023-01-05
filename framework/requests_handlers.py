class GetRequests:
    """
    Класс для парсинга параметров GET запроса
    """

    @staticmethod
    def parse_input_data(data: str) -> dict:
        result = {}
        if data:
            # Получаем все параметры GET запроса
            params = data.split('&')
            # Получаем имя и значение каждого параметра
            for item in params:
                key, value = item.split('=')
                result[key] = value
        return result

    @staticmethod
    def get_request_params(environ) -> dict:
        # Получаем параметры запроса
        query_string = environ['QUERY_STRING']
        # Преобразовываем параметры из строки в словарь
        request_params = GetRequests.parse_input_data(query_string)
        return request_params


class PostRequests:
    """
    Класс для парсинга данных POST запроса
    """

    @staticmethod
    def parse_input_data(data: str) -> dict:
        result = {}
        if data:
            # Получаем все параметры GET запроса
            params = data.split('&')
            # Получаем значение имя и значение каждого параметра
            for item in params:
                key, value = item.split('=')
                result[key] = value
        return result

    @staticmethod
    def get_wsgi_input_data(environ) -> bytes:
        # Получаем длину контента
        content_length_data = environ.get('CONTENT_LENGTH')
        # content_length_data = int(content_length_data) if content_length_data else 0
        if content_length_data:
            content_length_data = int(content_length_data)
        else:
            content_length_data = 0
        # data = environ['wsgi.input'].read(content_length_data) if content_length_data > 0 else b''
        if content_length_data > 0:
            data = environ['wsgi.input'].read(content_length_data)
        else:
            data = b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ) -> dict:
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data
