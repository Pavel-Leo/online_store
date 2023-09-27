from typing import Dict

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from posts.models import Post
from shop.common import post_pagination_func
from shop.models import Category


def post_list(request) -> HttpResponse:
    """Функция для отображения списка статей блога."""
    title: str = "Статьи блога"
    posts: Post = Post.objects.filter(available=True).all()
    categories: Category = Category.objects.all()
    page_obj = post_pagination_func(request, posts)
    context: Dict[str, any] = {
        "page_obj": page_obj,
        "title": title,
        "categories": categories,
    }
    return render(request, "post_list.html", context)


def post_detail(request, post_slug) -> HttpResponse:
    """Функция для отображения отдельной статьи блога."""
    post: Post = get_object_or_404(Post, slug=post_slug)
    categories: Category = Category.objects.all()
    context: Dict[str, any] = {
        "post": post,
        "title": post.title,
        "categories": categories,
    }
    return render(request, "post_detail.html", context)
