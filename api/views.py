from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
from api.models import Lead
from api.serializers import LeadSerializer

class LeadListCreateView(ListCreateAPIView):

    queryset = Lead.objects.all()

    serializer_class = LeadSerializer




class LeadRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    queryset = Lead.objects.all()

    serializer_class = LeadSerializer