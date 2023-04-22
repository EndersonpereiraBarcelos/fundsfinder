from rest_framework.routers import DefaultRouter
from api.views import FundoImobiliarioViewSet

app_name = 'api'
route = DefaultRouter(trailing_slash=False)
route.register(r'fundos', FundoImobiliarioViewSet)

urlpatterns = route.urls