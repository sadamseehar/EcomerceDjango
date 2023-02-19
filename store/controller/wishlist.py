from django.shortcuts import render,redirect
from django.contrib import messages

from django.http.response import JsonResponse
from store.models import Product,Cart,WhishList


# from django.contrib.auth.decorators import login_required 

# @login_required(login_url = "loginpage")

def index(request):
    wishlist = WhishList.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request,"store/wishlist.html",context)



def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(WhishList.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status':"already exits"})
                else:
                    WhishList.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status':'product added to wishlist'})
            else:
                return JsonResponse({'status':'product not found'})
        else:
            return JsonResponse({'status','login to continue'})
    return redirect("/")



def deletewishlistitem(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))

            if(WhishList.objects.filter(user=request.user, product_id=prod_id)):
                wishlistitem = WhishList.objects.filter(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':"removed"})
            else:
                return JsonResponse({'status':"not found"})
        else:
                return JsonResponse({'status':"login to continue"})

    else:
        return redirect("/")