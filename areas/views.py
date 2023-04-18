from datetime import datetime

from django.db.models import Sum
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from areas.models import Area, AreaVisitStatistic
from areas.serializers import AreaSerializer, AreaVisitStatisticSerializer

current_year = datetime.now().year
current_month = datetime.now().month


class AreaReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

    @action(detail=False, methods=['get'], url_path='statistics-list')
    def statistics_list(self, request):
        monthly_stats = (
            AreaVisitStatistic.objects
            .filter(travel_date__year=current_year, travel_date__month=current_month)
            .values('area__name', 'gender', 'age_group', 'companion')
            .annotate(total_count=Sum('travel_count'))
        )
        return Response({'message': monthly_stats}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='statistics-monthly')
    def statistics_monthly(self, request, pk):
        area_stats = (
            AreaVisitStatistic.objects
            .filter(id=pk, travel_date__year=current_year, travel_date__month=current_month)
            .values('area__name', 'gender', 'age_group', 'companion')
            .annotate(total_count=Sum('travel_count'))
        )
        return Response({'message': area_stats}, status=status.HTTP_200_OK)


class AreaVisitStatisticsReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AreaVisitStatistic.objects.all()
    serializer_class = AreaVisitStatisticSerializer
