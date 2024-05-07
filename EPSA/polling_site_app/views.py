from django.shortcuts import render
from .models import PollingSite

def polling_site_list(request):
    polling_sites = PollingSite.objects.all()
    # ... implement search and filtering logic (if needed) ...
    return render(request, 'polling_site_app/polling_site_list.html', {'polling_sites': polling_sites})

def polling_site_detail(request, pk):
    polling_site = get_object_or_404(PollingSite, pk=pk)
    return render(request, 'polling_site_app/polling_site_detail.html', {'polling_site': polling_site})
