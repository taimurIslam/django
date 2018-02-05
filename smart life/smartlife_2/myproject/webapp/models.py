from django.db import models

# Create your models here.


class device(models.Model):

    device_ID = models.IntegerField(max_length=20)
    token_Number = models.CharField(max_length=20)
    time = models.DateTimeField()

    def __str__(self):
        return str(self.device_ID)
