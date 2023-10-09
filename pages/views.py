from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

# product_details = [
#     {"id": 1, "price": 140, "name": "Half Finger Covers", "image": "1.jpg", "instock": True, "description": "text description"},
#     {"id": 2, "price": 220, "name": "1 Pair Cycling", "image": "2.jpg", "instock": False, "description": "text description"},
#     {"id": 3, "price": 300, "name": "Gym Weight cover", "image": "3.jpg", "instock": True, "description": "text description"},
# ]


def home(request):
    products = Product.objects.all()
    return render(request, 'pages/home.html', {"products": products})



# def home_details(request, product_id):
#     product = next((p for p in product_details if p['id'] == product_id), None)

#     if product:
#         return render(request, 'pages/home-details.html', {'product': product})
#     else:
#         return HttpResponse("Product not found")

# --------------------------------------------------------------

# def home_details(request, product_id):
#     product = Product.objects.get(id=product_id)
#     # product = filter(lambda x: x["id"] == product_id, product)

#     product = list(product)
#     print(product_id, product)

#     if product:
#         print(product[0])
#         return render(request, 'pages/home-details.html', {'products': product[0]})
#     else:
#         return HttpResponse("Product not found")


def home_details(request, product_id):
    product = Product.objects.get(id=product_id)

    if product:
        return render(request, 'pages/home-details.html', {'product': product})
    else:
        return HttpResponse("Product not found")

# -----------------------------------------------------------------

def delete(request, id):
     product = Product.objects.get(id=id)
     product.delete()
    #  url = reverse('pages/home-details.html')
     return HttpResponse("Product deleted")
    #  return render(request, 'pages/home-details.html')



def contact_us(request):
    return render(request, 'pages/contact-us.html') 




def about_us(request):
    return render(request, 'pages/about-us.html') 