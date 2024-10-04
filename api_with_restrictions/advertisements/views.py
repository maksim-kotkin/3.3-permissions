from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filter
from .filters import AdvertisementFilter
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import IsAdvertisementOwner


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

 
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    
    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == "create":
            return [IsAuthenticated()]
        elif self.action in ["update", "partial_update", "delete"]:
            return [IsAuthenticated(), IsAdvertisementOwner()]
        return []
