from django.conf.urls import url
from flight import views


app_name = 'flight'
urlpatterns = [
    url(r'^flight/new/$', views.new_flight, name="new_flight"),
    url(r'^flight/(?P<flight_id>[0-9]+)/$', views.flight_view, name="flight_edit"),
    url(r'^flight/delete/(?P<flight_id>[0-9]+)/$', views.delete_flight, name="delete_flight"),
    url(r'^', views.index, name="index"),
]