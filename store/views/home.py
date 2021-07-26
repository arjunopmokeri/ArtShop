from django.shortcuts import render, redirect
from store.models.product import product
from store.models.category import category
from django.views import View


# Create your views here.

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1                   
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1

        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}    
        products = None        
        categories = category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = product.get_all_products_by_categoryid(categoryID)
        else:
            products = product.get_all_products()
        context = {}
        context['products'] = products
        context['categories'] = categories
        print('you are :', request.session.get('email'))
        return render(request, 'index.html', context)
