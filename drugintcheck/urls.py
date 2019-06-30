from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('wechselwirkungs-check/', views.drugintcheck, name='drugintcheck'),
    path('arzneimittel-liste/', views.drug_list, name='drug_list'),
    path('hersteller-liste/', views.company_list, name='company_list'),
]