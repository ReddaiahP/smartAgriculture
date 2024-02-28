from django.shortcuts import render
from . models import Agriculture


def home(request):
    last_agriculture_data = Agriculture.objects.order_by('-id').first()
    return render(request, 'home.html', {'last_agriculture_data':last_agriculture_data})