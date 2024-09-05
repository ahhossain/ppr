from django.shortcuts import render
from django.core.paginator import Paginator
from django.utils.dateparse import parse_date
from .models import entry


# Create your views here.
def index(request):
    query = request.GET.get('q', None)
    county = request.GET.get('county', None)
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)
    
    entries = entry.objects.all()
    entries_filtered = entries
    
    if query:
        entries_filtered = entries.filter(Address__icontains=query)

    if county:
        entries_filtered = entries_filtered.filter(County__icontains=county)
    
    # Filter by price range
    if min_price:
        entries_filtered = entries_filtered.filter(Price__gte=min_price)
    if max_price:
        entries_filtered = entries_filtered.filter(Price__lte=max_price)

    # Filter by date range
    if start_date:
        entries_filtered = entries_filtered.filter(Date__gte=start_date)

    if end_date:
        entries_filtered = entries_filtered.filter(Date__lte=end_date)
      
    paginator = Paginator(entries_filtered, 50)  # Show 10 listings per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'index.html', context)