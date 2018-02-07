from django.db import models

# Create your models here.


class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.ImageField(null=False)
    email_address = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_address = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name+' '+self.last_name


