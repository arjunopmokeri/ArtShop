from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import customer
from django.views import View



class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # validation
        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }
        error_message = None

        customers = customer(first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)

        if(not first_name):
            error_message = "First Name Required!!!"
        elif len(first_name) < 4:
            error_message = "first name must be 4 charecter"

        elif(not last_name):
            error_message = "Last Name Required!!!"
        elif len(last_name) < 4:
            error_message = "Last name must be 4 charecter"

        elif(not phone):
            error_message = "Phone Number Required!!!"
        elif len(phone) < 10:
            error_message = "Phone Number must be 10 digits"

        elif len(password) < 6:
            error_message = "Password must be 10 charecters"
        elif len(email) < 5:
            error_message = "Email must be 5 charecter"

        elif customers.isExists():
            error_message = "Email Address Alredy Registered"

        # insert into models
        if not error_message:
            customers.password = make_password(customers.password)
            customers.save()
            return redirect('homepage')
        else:
            context = {
                'error': error_message,
                'values': values,
            }
            return render(request, 'signup.html', context)


