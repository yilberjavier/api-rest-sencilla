from django.urls import path
from .views import CompanyListView, CompanyDetalView

urlpatterns = [
    path('company/', CompanyListView.as_view(), name='company_list'),
    path('company/<int:pk>', CompanyDetalView.as_view(), name='company' ),
   
]