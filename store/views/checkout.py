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
        cust = request.session.get('customer')
        cart = request.session.get('cart')
        print("helloo==123: ", address, phone, customer, cart)
        products = product.get_products_by_id(list(cart.keys()))

        print("helloo==arjun: ", products)

        for prod in products:
            order = Orders(customer=customer(id=cust),
                           product=prod,
                           price=prod.price,
                           address=address,
                           phone=phone,
                           quantity=cart.get(str(prod.id)))

            order.save()
            #order.placeOrder()

        request.session['cart'] = {}
        return redirect('cart')
