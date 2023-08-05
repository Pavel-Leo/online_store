from django.urls import path

from posts import views

app_name: str = "posts"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<slug:post_slug>/", views.post_detail, name="post_detail"),

]
