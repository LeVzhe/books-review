from django.contrib import admin
from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    fields = (
        ("book", "post_owner"),
        "content",
        "publicated",
        "rating",
    )
    readonly_fields = ("publicated",)


admin.site.register(Review, ReviewAdmin)
