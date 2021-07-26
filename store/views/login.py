from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import customer
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customers = customer.get_customer_by_mail(email)
        error_message = None

        if customers:
            flag = check_password(password, customers.password)
            if flag:
                request.session['customer'] = customers.id
                return redirect('homepage')
            else:
                error_message = 'Email or Password Invalid !!'
        else:
            error_message = 'Email or Password Invalid !!'

        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')
