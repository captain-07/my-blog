from django.urls import path
from .views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)

urlpatterns = router.urls