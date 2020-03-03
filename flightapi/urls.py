from django.urls import include, path
from rest_framework import routers
from flightapi import views

router = routers.SimpleRouter()
router.register('airport', views.AirportViewSet)
router.register('ausairport', views.AusAirportViewSet)
router.register('map', views.MapViewSet)
router.register('maparea', views.MapAreaViewSet, 'map')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls