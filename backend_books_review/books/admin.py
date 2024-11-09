from django.contrib import admin
from books.models import Book


class BookAdmin(admin.ModelAdmin):
    fields = (
        ("title",),
        ("author", "description", "release_date"),
        "cover_img",
        ("post_owner", "publicated", "is_active"),
    )
    readonly_fields = ("publicated",)


admin.site.register(Book, BookAdmin)
