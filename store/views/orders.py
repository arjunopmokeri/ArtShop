from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import customer
from store.models.product import product
from store.models.orders import Orders
from django.views import View


class OrderView(View):
    def get(self, request):
        cust = request.session.get('customer')
        ord = Orders.get_orders_by_customer(cust)
        print(ord)
        ord = ord.reverse()
        return render(request, 'orders.html', {'orders' : ord})
