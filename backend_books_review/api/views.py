from books.models import Book
from books.serializers import BookSerializer
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from users.serializers import UserSerializer


################# AUTH #################
class RegistrationApiView(CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        return Response(
            {
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "password": user.password,
            },
            status=status.HTTP_201_CREATED,
        )

    def perform_create(self, serializer):
        return serializer.save()


################# BOOKS ################
class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ("update", "destroy"):
            self.permission_classes = (IsAdminUser,)
        elif self.action == "create":
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(post_owner=self.request.user)
        else:
            raise PermissionDenied(
                "Вы должны быть зарегистрированы для того, чтобы добавлять книги."
            )
