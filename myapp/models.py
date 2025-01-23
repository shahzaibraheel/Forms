from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

 
 
class Authenticate(models.Model):
   
    
    user_name = models.CharField(max_length=255)  
    password = models.CharField(max_length=255)  
    

    class Meta:
        db_table = 'Authenticate'    

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class ContactChangeLog(models.Model):
    username = models.CharField(max_length=150, default='unknown')  # Add a default
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255)
    old_value = models.TextField(null=True, blank=True)
    new_value = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.username} updated {self.field_name} on {self.contact}"
