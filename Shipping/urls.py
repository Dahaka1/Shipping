from django.urls import path
from machines.views import MachineViewSet
from cargo.views import CargoViewSet
from rest_framework import routers
from django.urls import include


router = routers.DefaultRouter()
router.register(r'machine', MachineViewSet)
router.register(r'cargo', CargoViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls))
]
