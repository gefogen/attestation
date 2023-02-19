from django.urls import path, include
from rest_framework.routers import SimpleRouter

from network.views import LinkViewSet


link_router = SimpleRouter()
link_router.register('link', LinkViewSet, basename='link')


urlpatterns = [
    path('', include(link_router.urls)),
]