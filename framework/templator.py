from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def render(template_name: str, folder='templates', **kwargs):
    """
    :param template_name: Имя шаблона
    :param folder: папка, содержащая шаблоны
    :param kwargs: именованные аргументы передаваемые в шаблон
    :return:
    """
    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)
    return template.render(**kwargs)
