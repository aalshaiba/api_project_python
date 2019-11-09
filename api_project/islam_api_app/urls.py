from django.urls import path, include
from rest_framework import routers
from .views import FatwasView, PrayerView, HijriView, DroosView
from rest_framework import routers

router = routers.DefaultRouter()
hala = routers.DefaultRouter()
router.register('', FatwasView)
hala.register('', DroosView)

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    # path('oil-prices', OilView.as_view()),
    path('prayers/ad', PrayerView.as_view()),
    path('arabic-date', HijriView.as_view()),
    # path('fuel', UAEFuelView.as_view()),
    # path('exchange', CurrencyView.as_view()),
    path('fatwas', include(router.urls)),
    path('droos', include(hala.urls))

]
