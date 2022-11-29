from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement, AdvertisementStatusChoices
from advertisements.permissions import IsOwnerOrAdmin
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filterset_class = AdvertisementFilter
    search_fields = ['title', 'description', ]
    ordering_fields = ['created_at', ]
    permission_classes = [AllowAny, IsAuthenticated, IsOwnerOrAdmin, ]

    def get_queryset(self):
        """Удаление из выдачи DRAFT объявлений"""
        if self.request.user.is_superuser:
            return self.queryset
        exclude_draft = self.queryset.exclude(status=AdvertisementStatusChoices.DRAFT)
        if str(self.request.user) == "AnonymousUser":
            return exclude_draft
        return exclude_draft | self.queryset.filter(status=AdvertisementStatusChoices.DRAFT, creator=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]
        return []
