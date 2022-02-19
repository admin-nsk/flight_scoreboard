# coding=utf-8
from django.contrib import admin
from models import Flight, City, Airbus


class FlightAdmin(admin.ModelAdmin):
    fields = (
        'number',
        'departure_city',
        'arrival_city',
        'status',
        'plane_type',
        'planned_departure_time',
        'planned_arrival_time',
        'actual_departure_time',
        'actual_arrival_time',
    )
    list_display = (
        'number',
        'departure_city',
        'arrival_city',
        'status',
        'plane_type',
        'planned_departure_time',
        'planned_arrival_time',
        'actual_departure_time',
        'actual_arrival_time',
    )


admin.site.register(Flight, FlightAdmin)


class CityAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


admin.site.register(City, CityAdmin)


class AirbusAdmin(admin.ModelAdmin):
    fields = ('type_plane',)


admin.site.register(Airbus, AirbusAdmin)
