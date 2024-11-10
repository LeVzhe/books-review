from books.models import Book
from rest_framework import serializers
from users.models import User


class BookSerializer(serializers.ModelSerializer):
    post_owner = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all(), required=False
    )
    # comments_count = serializers.IntegerField(source="comments.count", read_only=True)
    # recent_comments = serializers.SerializerMethodField()
    # likes_count = serializers.IntegerField(source="likes.count", read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "description",
            "release_date",
            "cover_img",
            "publicated",
            "post_owner",
            "is_active",
        ]
        read_only_fields = (
            "publicated",
            # "comments_count",
            # "likes_count",
        )
