from django.db.models import Count
from rest_framework import generics
from rest_framework import permissions, filters
from hike_scout.permissions import IsOwnerOrReadOnly
from .models import Posts
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Posts.objects.annotate (
        like_count=Count('like', distinct=True), 
        comments_count=Count('comments', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
        ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'like__owner__profile',
        'owner__profile',
    ]
    search_fields=[
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'like_count',
        'comments_count',
        'like__created_at',
        ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Posts.objects.annotate (
        like_count=Count('like', distinct=True), 
        comments_count=Count('comments', distinct=True),
    ).order_by('-created_at')