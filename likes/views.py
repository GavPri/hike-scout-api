from django.shortcuts import render
from rest_framework import generics, permissions
from hike_scout.permissions import IsOwnerOrReadOnly 
from likes.serializers import LikeSerializer
from .models import Like

class LikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
