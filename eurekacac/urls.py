from django.urls import path
from .views import (
    ConsultationContactsList, 
    ConsultationContactsDetails, 
    ConsultationDateRangeList, 
    ConsultationDateRangeDetails,
)

urlpatterns = [
    path('contactforms/', ConsultationContactsList.as_view(), name='consultation_contacts_list'),
    path('contactforms/<int:pk>/', ConsultationContactsDetails.as_view(), name='consultation_contacts_details'),
    path('date/', ConsultationDateRangeList.as_view(), name='consultation_date_list'),
    path('date/<int:pk>/', ConsultationDateRangeDetails.as_view(), name='consultation_date_details'),
]