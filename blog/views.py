from .models import Post, Comment, Like
from rest_framework import viewsets, filters, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer, CommentSerializer, RegisterSerializer
from .permissions import IsAdminOrReadOnly


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)

    serializer_class = PostSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ["title", "content"]

    ordering_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]

    lookup_field = "slug"

    


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all().order_by("-created_at")

    serializer_class = CommentSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RegisterView(generics.CreateAPIView):

    serializer_class = RegisterSerializer
    permission_classes = []
