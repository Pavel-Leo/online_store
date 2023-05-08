from django.conf import settings
from django.core.paginator import Paginator


def paginator_func(request, products):
    paginator = Paginator(products, settings.PRODUCTS_PER_PAGE)
    page_number = request.GET.get("page")
    products_list = paginator.get_page(page_number)
    return products_list
