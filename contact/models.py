from django.db import models

# Create your models here.
class Contact(models.Model):  
    cid = models.CharField(max_length=20)  
    cname = models.CharField(max_length=100)
    clastname = models.CharField(max_length=100) 
    cemail = models.EmailField()  
    cphone = models.CharField(max_length=8)
    

    class Meta:  
        db_table = "contact"