from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, RegisterView

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
]

urlpatterns += router.urls
