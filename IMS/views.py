from django.shortcuts import render
from .models import*

# Create your views here.
def home(request):
    all_product = product.objects.all()
    context = {
        'all_product': all_product
    }
    return render(request, 'index.html', context)