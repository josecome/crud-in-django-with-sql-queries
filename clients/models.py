from django.db import models

# Create your models here.
from django.db import models  
class Client(models.Model):  
    cid = models.CharField(max_length=40)  
    name = models.CharField(max_length=120)  
    email = models.EmailField()  
    contact = models.CharField(max_length=20)  
    class Meta:  
        db_table = "clients"