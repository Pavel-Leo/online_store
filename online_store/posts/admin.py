from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "pub_date",
        "title",
        "text",
        "description",
    ]
    list_filter = ["id", "pub_date", "text"]
    search_fields = ["id", "pub_date", "text"]
    empty_value_display = "-пусто-"
    prepopulated_fields = {"slug": ("title",)}
