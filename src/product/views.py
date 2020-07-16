from django.shortcuts import render
from models import Product
# Create your views here.


def productDetailView(request):
    myProduct = Product.objects.get(id=1)
    context = {
        'title': myProduct.title,
        'description': myProduct.description
    }
    return render(request, "product/detail.html", context)
