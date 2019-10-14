
from django.shortcuts import render, HttpResponse
from django_tables2 import RequestConfig, SingleTableView
from .tables import ProduktTable, HerstellerTable
from .models import Produkt, Hersteller, Produktinteraktionsklassen, Interaktionen
from .filters import HerstellerFilter, ProduktFilter
from .forms import DrugIntCheckForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def homepage(request):
    return render(request, 'drugintcheck/homepage.html', {})

def drugintcheck(request):
    if request:
        form = DrugIntCheckForm(request.GET)
        if form.is_valid():
            query = request.GET.get('check_drug')
            #'Xeloda® 150 mg Filmtabletten'
            get_drugid = Produkt.objects.get(arzneimittel=query).id
            get_intclass1 = Produktinteraktionsklassen.objects.filter(
                productid=get_drugid).values_list('interactionclassid', flat=True)

            # Anlegen einer leeren Liste, um darin im Anschluss alle zutreffenden IntIDs2 abzulegen
            interaction_id2 = []
            for item in get_intclass1:
                get_intclass2 = Interaktionen.objects.filter(interactionclassid1=item).values_list(
                    'interactionclassid2', flat=True)
                interaction_id2.append(get_intclass2)

            # Falls notwendig, alle in dieser Liste enthaltenen Querysets zusammenführen
            if len(interaction_id2) > 1:
                interaction_id2 = [j for i in interaction_id2 for j in i]

            # Mit den Werten in der Liste wieder die ProduktID der Interaktionen erhalten
            interacting_products = []
            for item in interaction_id2:
                get_products = Produktinteraktionsklassen.objects.filter(interactionclassid=item).values_list(
                    'productid', flat=True)
                interacting_products.append(get_products)

            # Falls notwendig, alle in dieser Liste enthaltenen Querysets zusammenführen
            if len(interacting_products) > 1:
                interacting_products = [j for i in interacting_products for j in i]

            # Ausgabe aller Produkte, die mit dem gesuchten Präparat eine Wechselwirkung erzeugen
            interaktionen = []
            for item in interacting_products:
                prod = Produkt.objects.get(id=item)
                interaktionen.append(prod)

            #Anzahl der Interaktionen
            count_interactions = len(interaktionen)

            output_values = {'form': form,
                            'get_drugid': get_drugid,'get_intclass1': get_intclass1,
                            'interaction_id2': interaction_id2,
                            'interacting_products': interacting_products,
                            'count_interactions': count_interactions,
                            'interaktionen': interaktionen}

            return render(request, 'drugintcheck/drugintcheck.html', output_values)

    else:
        form = DrugIntCheckForm()

    return render(request, 'drugintcheck/drugintcheck.html', {'form': form})

    #form = DrugIntCheckForm()

def drug_list(request):
    drugs = Produkt.objects.all()
    drgs_filter = ProduktFilter(request.GET, queryset=drugs)
    drugs_tbl = ProduktTable(drgs_filter.qs)
    RequestConfig(request).configure(drugs_tbl)
    return render(request, 'drugintcheck/drug_list.html',
                    {'drugs_tbl': drugs_tbl, 'drgs_filter': drgs_filter})

def company_list(request):
    companies = Hersteller.objects.all()
    cmp_filter = HerstellerFilter(request.GET, queryset=companies)
    company_tbl = HerstellerTable(cmp_filter.qs)
    RequestConfig(request).configure(company_tbl)
    return render(request, 'drugintcheck/company_list.html',
                    {'cmp_tbl': company_tbl, 'cmp_filter': cmp_filter})
