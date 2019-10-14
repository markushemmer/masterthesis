# filters.py
from .models import Hersteller, Produkt
import django_filters
from dal import autocomplete

class HerstellerFilter(django_filters.FilterSet):
    class Meta:
        model = Hersteller
        fields = ['hersteller', 'stadt']

class ProduktFilter(django_filters.FilterSet):
    markteintrittsdatum = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Produkt
        fields = ['arzneimittel', 'markteintrittsdatum', 'hersteller']
