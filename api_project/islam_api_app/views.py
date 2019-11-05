from rest_framework.views import APIView, Response
from rest_framework import viewsets
from .prayer_api import get_prayer, get_date
from .models import Fatwas
from .fatwas import FatwaSerializer
from django.db.models import Q
# from django_filters import rest_framework as filters


class PrayerView(APIView):

    def get(self, request):
        return Response(get_prayer())


class HijriView(APIView):

    def get(self, request):
        return Response(
            {'day': get_date()[0], 'monthArabic': get_date()[1], 'monthEnglish': get_date()[3], 'year': get_date()[2]})


# class FatwaFilter(filters.FilterSet):
#     class Meta:
#         model = Fatwas
#         fields = {
#             'title': ['icontains'],
#             'muftee': ['icontains']
#         }


class FatwasView(viewsets.ModelViewSet):
    serializer_class = FatwaSerializer
    queryset = Fatwas.objects.all()

    def get_queryset(self):
        title = self.request.GET.get('title')
        binbaz = self.request.GET.get('b')
        othaimeen = self.request.GET.get('o')
        saleh = self.request.GET.get('s')

        if title:
            fatwas = self.queryset.filter(Q(title__icontains=title))
            if othaimeen or binbaz or saleh:
                fatwas = fatwas.filter(Q(muftee__icontains=othaimeen) if othaimeen else None |
                                   Q(muftee__icontains=binbaz) if binbaz else None |
                                   Q(muftee__icontains=saleh) if saleh else None
                                   )
            else:
                pass
        else:
            fatwas = []
        return fatwas


