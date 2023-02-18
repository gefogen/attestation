# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.viewsets import ModelViewSet
#
# from network.models import BaseSupplier
# from serializers import SupplierSerializer


# class SupplierViewSet(ModelViewSet):
#     def get(self, request):
#         queryset = BaseSupplier.objects.all()
#         serializer_class = SupplierSerializer(queryset, many=True)
#
#         return Response(serializer_class.data)