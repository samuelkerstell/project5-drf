from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from dislikes.models import Dislike
from dislikes.serializers import DislikeSerializer


class DislikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DislikeSerializer
    queryset = Dislike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DislikeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DislikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Dislike.objects.all()