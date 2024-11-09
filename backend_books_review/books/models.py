from django.db import models

from books.utilities import get_timestamp_path
from users.models import User


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="Название книги",
        unique=True,
        error_messages={"unique": "Такая книга уже есть в архиве."},
        verbose_name="Название",
    )
    author = models.CharField(
        max_length=200,
        default="Неизвестен",
        verbose_name="Автор книги",
    )
    description = models.TextField(
        blank=True,
        null=True,
        default="Без описания.",
        help_text="Описание книги",
        verbose_name="Описание",
    )
    release_date = models.DateField(
        blank=True,
        null=True,
        help_text="Дата издания",
        verbose_name="Издана",
    )
    cover_img = models.ImageField(
        blank=True, upload_to=get_timestamp_path, verbose_name="Обложка"
    )
    publicated = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="Опубликовано"
    )
    is_active = models.BooleanField(
        default=True, db_index=True, verbose_name="Проверено модератором?"
    )
    post_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор публикации"
    )

    def __str__(self):
        return f"{self.title} :: {self.author}"

    class Meta:
        verbose_name_plural = "Книги"
        verbose_name = "Книга"
        ordering = ["title"]
