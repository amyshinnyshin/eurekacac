from rest_framework import generics

from .models import ConsultationContact, ConsultationDateRange
from .serializer import ConsultationContactsSerializer, ConsultationDateSerializer

# Create your views here.
class ConsultationContactsList(generics.ListCreateAPIView): 
    queryset = ConsultationContact.objects.all()
    serializer_class= ConsultationContactsSerializer

class ConsultationContactsDetails(generics.RetrieveUpdateDestroyAPIView): 
    queryset = ConsultationContact.objects.all()
    serializer_class= ConsultationContactsSerializer



class ConsultationDateRangeList(generics.ListCreateAPIView): 
    queryset = ConsultationDateRange.objects.all()
    serializer_class= ConsultationDateSerializer

class ConsultationDateRangeDetails(generics.RetrieveUpdateDestroyAPIView): 
    queryset = ConsultationDateRange.objects.all()
    serializer_class= ConsultationDateSerializer