from books.models import Book
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models
from users.models import User


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="Книга",
    )
    post_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор публикации",
    )
    content = models.CharField(
        max_length=256,
        verbose_name="Отзыв",
    )
    publicated = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Опубликовано",
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="Оценка книги от 0 до 5",
        blank=True,
        null=True,
        verbose_name="Оценка",
    )

    def __str__(self):
        return f"{self.book.title} ({self.book.author})  :: {self.post_owner}"

    class Meta:
        verbose_name_plural = "Отзывы"
        verbose_name = "Отзыв"
        ordering = ["-publicated"]
