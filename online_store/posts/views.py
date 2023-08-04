from django.shortcuts import get_object_or_404, redirect, render

from posts.models import Post
from shop.common import post_pagination_func


def post_list(request):
    title = "Статьи блога"
    posts = Post.objects.filter(available=True).all()
    page_obj = post_pagination_func(request, posts)
    context = {
        "page_obj": page_obj,
        "title": title,
    }
    return render(request, "post_list.html", context)


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {
        "post": post,
        "title": post.title,
    }
    return render(request, "post_detail.html", context)

