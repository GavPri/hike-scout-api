from rest_framework import generics, permissions
from .models import Comments
from .serializers import CommentsSerializer
from hike_scout.permissions import IsOwnerOrReadOnly

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Comments.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.use)