from django.conf import settings
from django.core.paginator import Paginator

POST_PER_PAGE = getattr(settings, "POST_PER_PAGE", None)


def paginations(data_list, page_number):
    """Пагинация данных по страницам.
    Принимает на вход list с элементами данных, номер страницы.
    Возвращает объект страницы."""

    paginator = Paginator(data_list, POST_PER_PAGE)
    page_obj = paginator.get_page(page_number)

    return page_obj
