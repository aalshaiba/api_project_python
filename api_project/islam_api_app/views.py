from rest_framework.views import APIView, Response
from rest_framework import viewsets
from .prayer_api import get_prayer, get_date
from .models import Fatwas, Droosuae
from .fatwas import FatwaSerializer, DroosUAESerializer
from django.db.models import Q


class PrayerView(APIView):
    def get(self, request):
        return Response(get_prayer())


class HijriView(APIView):

    def get(self, request):
        return Response(
            {'day': get_date()[0], 'monthArabic': get_date()[1], 'monthEnglish': get_date()[3], 'year': get_date()[2]})


class FatwasView(viewsets.ModelViewSet):
    serializer_class = FatwaSerializer
    queryset = Fatwas.objects.all()

    def get_queryset(self):
        title = self.request.GET.get('title')
        muftee = self.request.GET.get('muftee')
        fatwas = Fatwas.objects.all()
        if title:
            listFatwas = fatwas.filter(Q(title__icontains=title))
            if muftee:
                listFatwas = listFatwas.filter(Q(muftee__icontains=muftee))
            return listFatwas
        else:
            return []


class DroosView(viewsets.ModelViewSet):
    serializer_class = DroosUAESerializer
    queryset = Droosuae.objects.all()

    def get_queryset(self):
        title = self.request.GET.get('title')
        shaikh = self.request.GET.get('shaikh')
        droos = Droosuae.objects.all()

        if title:
            listDroos = droos.filter(Q(title__icontains=title))
            if shaikh:
                listDroos = listDroos.filter(Q(shaikh__icontains=shaikh))
            return listDroos
        else:
            return []
