from rest_framework.views import APIView, Response
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
# from .adnoc import prices_uae
# from .exchange_rate import get_currency
from .prayer_api import get_prayer, get_date
# from .support import get_data
from .models import Fatwas
from .fatwas import FatwaSerializer


# class OilView(APIView):
#
#     def get(self, request):
#         return Response(get_data())
#
#


class PrayerView(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request):
        return Response(get_prayer())


class HijriView(APIView):

    def get(self, request):
        return Response(
            {'day': get_date()[0], 'monthArabic': get_date()[1], 'monthEnglish': get_date()[3], 'year': get_date()[2]})


#
# class UAEFuelView(APIView):
#
#     def get(self, request):
#         return Response(prices_uae(1))
#
#
# class CurrencyView(APIView):
#
#     def get(self, request):
#         return Response(get_currency())


class FatwasView(viewsets.ModelViewSet):
    queryset = Fatwas.objects.all()
    serializer_class = FatwaSerializer
