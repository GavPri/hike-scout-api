from rest_framework import generics, permissions 
from hike_scout.permissions import IsOwnerOrReadOnly
from .models import Followers
from .serializers import FollowersSerializer

class FollowersList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowersSerializer
    queryset = Followers.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowersDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowersSerializer
    queryset = Followers.objects.all()
