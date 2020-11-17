# pages/views.py
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello, World!, This is not my first Project.')
