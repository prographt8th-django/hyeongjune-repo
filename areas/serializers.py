from rest_framework import serializers

from areas.models import Area, AreaVisitStatistic


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = (
            'id',
            'code',
            'name',
        )


class AreaVisitStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaVisitStatistic
        fields = (
            'area',
            'gender',
            'age_group',
            'companion',
            'travel_count',
            'travel_date',
        )
