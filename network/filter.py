import django_filters

from network.models import Link


class LinkFilter(django_filters.FilterSet):
    """ Фильтр по Городу """
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Link
        fields = ['city']
