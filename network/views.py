from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from network.filter import LinkFilter
from network.models import Link
from network.permissions import PermissionsUsers
from network.serializers import LinkSerializer


class LinkViewSet(ModelViewSet):
    queryset = Link.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = LinkFilter
    permission_classes = PermissionsUsers

    serializer_class = LinkSerializer(queryset, many=True)
