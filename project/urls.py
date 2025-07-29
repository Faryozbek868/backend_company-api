from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ServiceViewSet, PortfolioItemViewSet,
    NewsViewSet, TeamMemberViewSet, StatisticViewSet
)

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'portfolio', PortfolioItemViewSet)
router.register(r'news', NewsViewSet)
router.register(r'team', TeamMemberViewSet)
router.register(r'statistics', StatisticViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
