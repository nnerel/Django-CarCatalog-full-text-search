from django.shortcuts import render
from catalog.forms import CarSearchForm
from .models import Car

def car_search(request):
    form = CarSearchForm

    results = []

    if 'q' in request.GET:
        form = CarSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            results = Car.objects.filter(name__contains=q)

    return render(request, 'index.html', {'form':form, 'results': results})