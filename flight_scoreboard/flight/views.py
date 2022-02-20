# coding=utf-8
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods

from flight.models import Flight
from flight.forms import SearchFlightsForm, FlightForm


@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        search_form = SearchFlightsForm(request.POST)
        if search_form.is_valid():
            search_data = {}
            if search_form.cleaned_data['city_departure']:
                search_data['departure_city'] = search_form.cleaned_data['city_departure'].id
            if search_form.cleaned_data['city_arrival']:
                search_data['arrival_city'] = search_form.cleaned_data['city_arrival'].id
            if search_form.cleaned_data['status']:
                search_data['status'] = search_form.cleaned_data['status']
            flights = Flight.objects.filter(**search_data)
        else:
            flights = Flight.objects.all()
    else:
        search_form = SearchFlightsForm()
        flights = Flight.objects.all()

    data = {
        'search_form': search_form,
        'flights': flights
    }
    return render(request, 'index.html', context=data, status=200)


@require_http_methods(['GET', 'POST'])
def flight_view(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    flight_form = FlightForm(request.POST or None, instance=flight)
    if request.method == 'POST':
        if flight_form.is_valid():
            flight_form.save()
            return redirect("flight:index")
    return render(request, "flight.html", {'flight_form': flight_form, 'flight': flight})


@require_http_methods(['GET', 'POST'])
def new_flight(request):
    if request.method == 'POST':
        flight_form = FlightForm(request.POST)
        if flight_form.is_valid():
            flight_form.save()
            return redirect('flight:index')
        return render(request, 'flight.html', {'flight_form': flight_form, 'flight': None})
    flight_form = FlightForm()
    return render(request, 'flight.html', {'flight_form': flight_form, 'flight': None})


@require_http_methods(['POST', 'GET'])
def delete_flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    if request.method == 'POST':
        flight.delete()
        messages.add_message(request, messages.SUCCESS, 'Рейс удален')
        return redirect('flight:index')
    else:
        return render(request, 'flight_delete_confirm.html', {'flight_id': flight_id})