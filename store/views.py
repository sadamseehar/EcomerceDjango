from django.shortcuts import render
from .models import *
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"store/index.html")


def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request,"store/collections.html",context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products = Product.objects.filter(category__slug = slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products':products, 'category':category}
        return render(request, "store/product/index.html", context)
    else:
        messages.warning(request,"no record found")
        return redirect('collections')