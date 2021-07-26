from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import customer
from store.models.product import product
from store.models.orders import Orders
from django.views import View


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        product = product.get_products_by_id(list(cart.keys()))

        print(address, phone, customer, cart, product)

        for product in products:
            order=Orders(customer=customer(id=customer),
                            product=product,
                            price=product.price,
                            address=address,
                            phone=phone,
                            quantity=cart.get(str(product.id)))
                        
        request.session['cart']={}
        return redirect('cart')
