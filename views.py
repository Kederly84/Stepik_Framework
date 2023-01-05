from framework.templator import render


class Index:

    def __call__(self, requests):
        return '200 OK', render('index.html')


class About:

    def __call__(self, requests):
        return '200 OK', render('about.html')


class InputForm:

    def __call__(self, requests):
        return '200 OK', render('input.html')
