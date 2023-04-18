from django.urls import include, path
from rest_framework.routers import DefaultRouter

from areas.views import AreaReadViewSet, AreaVisitStatisticsReadViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'areas', AreaReadViewSet, basename='areas')
router.register(r'area-statistics', AreaVisitStatisticsReadViewSet, basename='statistics')

urlpatterns = [
    path('', include(router.urls)),
]
