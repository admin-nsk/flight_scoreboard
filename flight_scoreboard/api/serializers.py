# coding=utf-8
from rest_framework import serializers
from flight.models import Flight


class FlightSerializer(serializers.ModelSerializer):
    departure_city = serializers.StringRelatedField(source='departure_city.name')
    arrival_city = serializers.StringRelatedField(source='arrival_city.name')
    plane_type = serializers.StringRelatedField(source='plane_type.type_plane')
    status = serializers.CharField(source='get_status_display')


    class Meta:
        model = Flight
        fields = [
            'id',
            'number',
            'departure_city',
            'arrival_city',
            'plane_type',
            'planned_departure_time',
            'planned_arrival_time',
            'actual_departure_time',
            'actual_arrival_time',
            'status',
        ]
