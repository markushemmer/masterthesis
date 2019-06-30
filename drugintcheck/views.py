from django.shortcuts import render

def homepage(request):
    return render(request, 'drugintcheck/homepage.html', {})

def drugintcheck(request):
	return render(request, 'drugintcheck/drugintcheck.html', {})

def drug_list(request):
	return render(request, 'drugintcheck/drug_list.html', {})

def company_list(request):
	return render(request, 'drugintcheck/company_list.html', {})