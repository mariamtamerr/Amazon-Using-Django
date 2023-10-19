from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from .models import Product  # .models = pages.models
from .forms import ProductForm
import os
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
    print("Query:", query)
    products = Product.objects.all()
    print("All products:", products)
#.filter() --> method provided by Django's QuerySet API to filter results of DB query
# icontains --> case sensitive contains 
    if query:
          products = products.filter(name__icontains=query)
          print("Filtered products:", products)

    # return render(request, 'pages/home.html', {"products": products})
    return render(request, 'pages/home.html', {"products": products, 'query':query})


def home_details(request, product_id):
    product = Product.objects.get(id=product_id)

    if product:
        return render(request, 'pages/home-details.html', {'product': product})
    else:
        return HttpResponse("Product not found")
    

# --------- edit --------------

@login_required
def edit(request, id):
    product = get_object_or_404(Product, id=id)
    
#  check if the user is the product owner 3shan y-delete/edit wlla mynf3sh
    if product.owner != request.user:
        return HttpResponse("You are not allowed to edit this product.")

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product.id = form.cleaned_data['id']
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.instock = form.cleaned_data['instock']
            product.category = form.cleaned_data['category']

            if 'image' in request.FILES:
                product.image = form.cleaned_data['image']
            

            product.save()
            return redirect('home')
    else:
        form = ProductForm({
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'instock': product.instock,
            'category': product.category,
            }
        )

    context = {
        'form': form
    }
    return render(request, 'pages/edit.html', context)




# -----------------------------------------------------------------

@login_required
def delete(request, id):
     product = Product.objects.get(id=id)
     if product.owner != request.user:
         return HttpResponse("</div class='container'><h1>You're not allowed to delete this product</h1> </div>")
     if product:
        product_instance = product[0]
        image_path = product_instance.image.path

        if os.path.exists(image_path):
            os.remove(image_path)
        
        product_instance.delete()
        print(request.user,'deleting .. ')
        return redirect('home')
     else:
        return HttpResponse("Product not found")    
    


def contact_us(request):
    return render(request, 'pages/contact-us.html') 




def about_us(request):
    return render(request, 'pages/about-us.html') 

# ---------------------------------------------------------

# -------- forms --------------------------------
         
        #  this is the add new product functionnnnnnn 


# @login_required
# def createViaForm(request):
   
#     form = ProductForm()

#     if request.POST:
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             id=request.POST['id']
#             name = request.POST['name']
#             price = request.POST['price']
#             instock = request.POST['instock'] 
#             description = request.POST['description']
#             image = None
#             if "image" in request.FILES :
#                 image = request.FILES['image']
#             product = Product.objects.create(id=id, name=name, image=image, price=price, instock=instock, description=description)
#             url = reverse('home') 
#             return redirect(url)

#     return  render( request, 'pages/forms/create.html',
#                     context={"form": form})




@login_required
def createViaForm(request):
   
 
    if request.POST:
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            if Product.objects.filter(name=form.cleaned_data['name']).exists():
                form.add_error('name', 'A Product with this name already exists.')
            else:
                product = Product(
                    id=form.cleaned_data['id'],
                    name=form.cleaned_data['name'],
                    image=form.cleaned_data['image'],
                    price=form.cleaned_data['price'],
                    description=form.cleaned_data['description'],
                    instock=form.cleaned_data['instock'],
                    category=form.cleaned_data['category'],
                    owner=request.user
                )
                product.save()
                return redirect('home')
    else:
           form = ProductForm()


    return  render( request, 'pages/forms/create.html',
                    context={"form": form})

