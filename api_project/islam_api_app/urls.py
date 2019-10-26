from django.urls import path, include
from rest_framework import routers
from .views import FatwasView, PrayerView, HijriView

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    # path('oil-prices', OilView.as_view()),
    path('prayers/ad', PrayerView.as_view()),
    path('arabic-date', HijriView.as_view()),
    # path('fuel', UAEFuelView.as_view()),
    # path('exchange', CurrencyView.as_view()),
    path('fatwas', FatwasView.as_view())
]
