from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from categories.models import Category  # .models = pages.models
from categories.forms import CategoryForm
from pages.models import Product

# Create your views here.
        



def home(request):
    category = Category.get_all_categories()
    return render(request, 'categories/home.html', context={"category":category})


# def details(request, id):
#     pro = Category.get_all_categories()
#     x = { 'pro' : pro.filter(products=Product.category.products) }
#     return render(request, 'categories/details.html',x)


def details(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.products.all()  
    # print(category.products.all())
    print(products)
    return render(request, 'categories/details.html', {'category': category, 'products': products})


def createViaForm(request):
   
    form = CategoryForm()

    if request.POST:
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            id=request.POST['id']
            name = request.POST['name']
            price = request.POST['price']
            instock = request.POST['instock'] 
            description = request.POST['description']
            image = None
            if "image" in request.FILES :
                image = request.FILES['image']
            category = Category.objects.create(id=id, name=name, image=image, price=price, instock=instock, description=description)
            url = reverse('home') 
            return redirect(url)

    # return  render( request, 'pages/forms/create.html',
                    # context={"form": form})