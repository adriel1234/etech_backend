from rest_framework import routers

from teste import viewsets

router = routers.DefaultRouter()

router.register('client', viewsets.ClientViewSet)

router.register('product', viewsets.ProductViewSet)

router.register('employee', viewsets.EmployeeViewSet)

router.register('sale', viewsets.SaleViewSet)

urlpatterns = router.urls
