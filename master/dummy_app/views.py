# master/dummy_app/views.py
from django.http import HttpResponse

def dummy_view(request):
    return HttpResponse("Dummy page for 'live' namespace.")
