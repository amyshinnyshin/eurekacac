from rest_framework import serializers
from .models import ConsultationContact, ConsultationDateRange

class ConsultationContactsSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = ConsultationContact
        fields = '__all__'

class ConsultationDateSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = ConsultationDateRange
        fields = '__all__'