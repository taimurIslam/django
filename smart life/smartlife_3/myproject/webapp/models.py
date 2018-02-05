from django.db import models

# Create your models here.


class login(models.Model):
    user_Name = models.CharField(max_length=20)
    user_Password = models.CharField(max_length=20)
    user_Current_Status = models.CharField(max_length=20)

class registration(models.Model):
    user_Name = models.CharField(max_length=20)
    user_Email =  models.CharField(max_length=20)
    user_Phone_Number =  models.CharField(max_length=20)
    user_Address =  models.CharField(max_length=20)
    user_password =  models.CharField(max_length=20)

class device(models.Model):
    user_ID = models.IntegerField(null=False)
    device_ID = models.IntegerField(null=False)
    token_Number = models.CharField(max_length=20)
    time = models.DateTimeField()
    def __str__(self):
        return str(self.device_ID)

