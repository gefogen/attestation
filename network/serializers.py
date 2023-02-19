from rest_framework import serializers

from network.models import Link


class LinkSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True, read_only=True)
    debt = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Link
        fields = '__all__'
