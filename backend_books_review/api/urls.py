from api.views import BooksViewSet, RegistrationApiView, ReviewsViewSet
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

app_name = "api"

router = routers.DefaultRouter()

router.register(r"", BooksViewSet)
router.register(r"(?P<book_id>[^/.]+)/reviews", ReviewsViewSet, basename="reviews")

urlpatterns = [
    ################# AUTH #################
    path("registration/", RegistrationApiView.as_view(), name="registration"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    ################# BOOKS ################
    path("books/", include(router.urls)),
]
