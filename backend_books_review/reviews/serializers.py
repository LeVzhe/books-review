from books.models import Book
from reviews.models import Review
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    post_owner = serializers.SlugRelatedField(
        slug_field="username",
        required=False,
        read_only=True,
    )

    book = serializers.SlugRelatedField(
        slug_field="title", queryset=Book.objects.all(), required=False
    )

    class Meta:
        model = Review
        fields = [
            "id",
            "book",
            "post_owner",
            "content",
            "publicated",
            "rating",
        ]
        read_only_fields = ("publicated",)