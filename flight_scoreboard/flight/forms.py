# coding=utf-8
from django import forms

from flight.models import Flight, City, Airbus


class SearchFlightsForm(forms.Form):
    city_departure = forms.ModelChoiceField(queryset=City.objects.all(), label='Город вылета', required=False)
    city_arrival = forms.ModelChoiceField(queryset=City.objects.all(), label='Город прилёта', required=False)
    status = forms.ChoiceField(choices=Flight.STATUS, label='Статус', required=False)

    class Meta:
        fields = ('city_departure', 'city_arrival', 'status')


class FlightForm(forms.ModelForm):
    departure_city = forms.ModelChoiceField(queryset=City.objects.all(), label='Город вылета')
    arrival_city = forms.ModelChoiceField(queryset=City.objects.all(), label='Город прилёта')
    plane_type = forms.ModelChoiceField(queryset=Airbus.objects.all(), label='Тип самолёта')

    class Meta:
        model = Flight
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
