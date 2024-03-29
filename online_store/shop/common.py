from django.conf import settings
from django.core.paginator import Page, Paginator


def paginator_func(request, products) -> Page:
    """Функция для отображения страницы с товарами с пагинацией."""
    paginator = Paginator(products, settings.PRODUCTS_PER_PAGE)
    page_number = request.GET.get("page")
    products_list = paginator.get_page(page_number)
    return products_list


def post_pagination_func(request, posts) -> Page:
    """Функция для отображения страницы с постами с пагинацией."""
    paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    posts_list: Page = paginator.get_page(page_number)
    return posts_list
