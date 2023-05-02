from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from .models import *
from .serializers import *

from .forms import *
# Create your views here.
    
class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class YearGroupList(generics.ListCreateAPIView):
    queryset = YearGroup.objects.all()
    serializer_class = YearGroupSerializer

class YearGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = YearGroup.objects.all()
    serializer_class = YearGroupSerializer

class MinistryList(generics.ListCreateAPIView):
    queryset = Ministry.objects.all()
    serializer_class = MinistrySerializer

class MinistryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ministry.objects.all()
    serializer_class = MinistrySerializer

class RegistrationList(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class RegistrationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer