from rest_framework.views import APIView, Response
from rest_framework import viewsets, generics, renderers
# from .adnoc import prices_uae
# from .exchange_rate import get_currency
from .prayer_api import get_prayer, get_date
# from .support import get_data
from .models import Fatwas
from rest_framework import filters
from .fatwas import FatwaSerializer
from django.utils.encoding import smart_unicode


# class OilView(APIView):
#
#     def get(self, request):
#         return Response(get_data())
#
#


class PlainTextRenderer(renderers.BaseRenderer):
    media_type = 'text/plain'
    format = 'text'
    charset = 'windows-1256'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data.encode(self.charset)


class PrayerView(APIView):

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


class FatwasView(generics.ListCreateAPIView):
    queryset = Fatwas.objects.all()
    serializer_class = FatwaSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title']
