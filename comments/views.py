from rest_framework import generics, permissions
from .models import Comments
from .serializers import CommentsSerializer
from hike_scout.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Comments.objects.all()

    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        'post'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.use)