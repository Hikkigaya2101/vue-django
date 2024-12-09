
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from api.views import UnitViewSet,ConsumerViewSet,TreeViewsSet,UnitTypeViewSet


router = routers.DefaultRouter()
router.register('unit', TreeViewsSet)
router.register('consumer', ConsumerViewSet)

router.register('unit_type',UnitTypeViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
