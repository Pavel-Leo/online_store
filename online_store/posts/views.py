from django.shortcuts import get_object_or_404, render

from posts.models import Post
from shop.models import Category
from shop.common import post_pagination_func


def post_list(request):
    title = "Статьи блога"
    posts = Post.objects.filter(available=True).all()
    categories = Category.objects.all()
    page_obj = post_pagination_func(request, posts)
    context = {
        "page_obj": page_obj,
        "title": title,
        "categories": categories,
    }
    return render(request, "post_list.html", context)


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    categories = Category.objects.all()
    context = {
        "post": post,
        "title": post.title,
        "categories": categories,
    }
    return render(request, "post_detail.html", context)

