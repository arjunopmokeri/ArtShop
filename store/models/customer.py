from django.db import models

class customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)


    def isExists(self):
        if customer.objects.filter(email = self.email):
            return True
        
        return False

    @staticmethod
    def get_customer_by_mail(email):
        try:
            return customer.objects.get(email=email)
        except:
            return False
