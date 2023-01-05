from os.path import join
from jinja2 import Template


def render(template_name: str, folder='templates', **kwargs):
    """
    :param template_name: Имя шаблона
    :param folder: папка, содержащая шаблоны
    :param kwargs: именованные аргументы передаваемые в шаблон
    :return:
    """
    # Получаем путь к шаблону
    file_path = join(folder, template_name)
    # Открывааем шаблон
    with open(file_path, encoding='utf-8') as file:
        # Читаем
        template = Template(file.read())
    # Рендерим шаблон с полученными параметрами
    return template.render(**kwargs)
