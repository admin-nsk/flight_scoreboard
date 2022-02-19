from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('flight', views.ApiFlightViewSet, base_name='flight')

urlpatterns = router.urls

