# Klassenmodelle für die gerenderten Datentabellen
import django_tables2 as tables
from .models import Hersteller, Produkt

class ProduktTable(tables.Table):

    class Meta:
        model = Produkt
        exclude = ('id', )
        template_name = 'django_tables2/bootstrap4.html'

class HerstellerTable(tables.Table):

    class Meta:
        model = Hersteller
        exclude = ('id', )
        template_name = 'django_tables2/bootstrap4.html'
