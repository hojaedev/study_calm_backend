from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from django.urls import path

from api.listings.views import ListingViewSet
from api.customers.views import CustomerViewSet
from api.suppliers.views import SupplierViewSet

from . import views

router = routers.DefaultRouter()

router.register(r'customers', CustomerViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'listings', ListingViewSet)

app_name = 'api_root'

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    path('', include(router.urls)),
    url(r'^docs/', get_swagger_view(title='Rest API Document')),
]