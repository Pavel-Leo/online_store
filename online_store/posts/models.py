from audioop import reverse
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name="Заголовок", help_text="Введите заголовок")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    text = models.TextField(verbose_name="Текст", help_text="Введите текст")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")
    image = models.ImageField(upload_to="posts/%Y/%m/%d", blank=True, verbose_name="Изображение",)
    description = models.TextField(blank=True, verbose_name="Описание")
    available = models.BooleanField(default=True, verbose_name="Доступность")

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_slug': self.slug})