from django.conf.urls import url
from flight import views

urlpatterns = [
    url(r'^flight/new/$', views.new_flight, name="new_flight"),
    url(r'^flight/(?P<flight_id>[0-9]+)/$', views.flight_view, name="flight_edit"),
    url(r'^', views.index, name="index"),
]