from django.urls import include, path
from rest_framework import routers
from .views import AdViewSet, ExchangeProposalViewSet

router = routers.DefaultRouter()
router.register(r'ads', AdViewSet)
router.register(r'exchanges', ExchangeProposalViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]