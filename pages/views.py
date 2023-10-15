from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from .models import Product  # .models = pages.models
from .forms import ProductForm
from django.views.generic import ListView

# Create your views here.

# product_details = [
#     {"id": 1, "price": 140, "name": "Half Finger Covers", "image": "1.jpg", "instock": True, "description": "text description"},
#     {"id": 2, "price": 220, "name": "1 Pair Cycling", "image": "2.jpg", "instock": False, "description": "text description"},
#     {"id": 3, "price": 300, "name": "Gym Weight cover", "image": "3.jpg", "instock": True, "description": "text description"},
# ]


def home(request):
# request.GET --> dictionary obj in django that contains all GET parameters sent with the request
# .get('p') --> get the value of 'q' parameter 
    query = request.GET.get('q')
    products = Product.objects.all()
#.filter() --> method provided by Django's QuerySet API to filter results of DB query
# icontains --> case sensitive contains 
    if query:
          products = products.filter(name__icontains=query)

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


class ProductListView(ListView):
    model = Product
    template_name = 'pages/home.html'
    context_object_name = 'products'
    




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
    #  return HttpResponse("Product deleted")
     return redirect('home')
    #  return render(request, 'pages/home-details.html')



def contact_us(request):
    return render(request, 'pages/contact-us.html') 




def about_us(request):
    return render(request, 'pages/about-us.html') 

# ---------------------------------------------------------

# -------- forms --------------------------------

# def createViaForm(request):
#     form = ProductForm()
#     if request.method == 'POST':
#         print(request.POST)
#         form = ProductForm(request.POST, request.FILES)
#         # product = None 
#         # if request.POST['product']:
#         #     product = Product.objects.get(id=request.POST['product'])
#         if form.is_valid():
#             product = Product.objects.create(
#                                 id=request.POST['id'], 
#                                 name = request.POST['name'], 
#                                 description = request.POST['description'],
#                                 price = request.POST['price'],
#                                 instock = request.POST['instock'] )
#             image = None
#             if "image" in request.FILES :
#                 image = request.FILES['image']
#             # product = Product.objects.create(id=id, name=name, image=image, price=price, instock=instock, description=description)
#             url = reverse('tracks.index')  # /tracks/
#             return redirect(url)

#     return  render( request, 'pages/forms/create.html',
#                     context={"form": form})
            

def createViaForm(request):
   
    form = ProductForm()

    if request.POST:
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            id=request.POST['id']
            name = request.POST['name']
            price = request.POST['price']
            instock = request.POST['instock'] 
            description = request.POST['description']
            image = None
            if "image" in request.FILES :
                image = request.FILES['image']
            product = Product.objects.create(id=id, name=name, image=image, price=price, instock=instock, description=description)
            url = reverse('home') 
            return redirect(url)

    return  render( request, 'pages/forms/create.html',
                    context={"form": form})