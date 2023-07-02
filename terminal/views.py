from rest_framework import generics
from .serializers import *
from .models import *


class PersonCategoryView(generics.ListAPIView):
    queryset = PersonCategory.objects.all()
    serializer_class = PersonCategorySerializer


class ServiceForIndividualView(generics.ListAPIView):
    query_set = Service.objects.all()
    serializer_class = ServiceSerializer
    queryset = query_set.filter(is_for_individuals=True)


class ServiceForLegalEntityView(generics.ListAPIView):
    query_set = Service.objects.all()
    serializer_class = ServiceSerializer
    queryset = query_set.filter(is_for_legal_entities=True)