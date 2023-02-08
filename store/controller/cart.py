from django.shortcuts import render,redirect
from django.contrib import messages

from django.http.response import JsonResponse
from store.models import Product,Cart

def addtocart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        product_check = Product.objects.get(id=prod_id)
        if(product_check):
            if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                return JsonResponse({'status':"Product already in car"})
            else:
                prod_qty = int(request.POST.get('product_qty'))

                if product_check.quantity >= prod_qty:
                    Cart.objects.create(user=request.user, product_id=prod_id ,product_qty=prod_qty)
                    return JsonResponse({'status':"Product added "})
                else:
                    return JsonResponse({'status':"Only"+ str(product_check.quantity)+"quantity avaiable"})
        else:
            return JsonResponse({'status':"no such product"})
    else:
        return JsonResponse({'status':"Login to continue"})
    
    return redirect("/")

            

                    
                