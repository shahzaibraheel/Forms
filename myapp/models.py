from django.db import models

# Create your models here.
from django.db import models

from django.db import models
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.timezone import now
import pytz

class Contact(models.Model): 
    Retailer_ID = models.CharField(max_length=100, unique=True)
    Franchise_ID = models.CharField(max_length=100)
    Retailer_Number = models.CharField(max_length=100, null=True)
    DSO_Name = models.CharField(max_length=100, null=True)
    CNIC = models.CharField(max_length=15, null=True)
    BVS_Device = models.CharField(max_length=100, null=True)
    Location = models.CharField(max_length=100)

    # Category field
    CATEGORY_CHOICES = [
        ('DSO', 'DSO'),
        ('RSO', 'RSO'),
        ('Retailer', 'Retailer'),
        ('Franchise', 'Franchise'),
    ]
    Category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='DSO')

    # Other Contact Number
    Other_Contact_Number = models.CharField(max_length=13, null=True, blank=True)

    # New Date Fields
    Date_of_Joining = models.DateField(default='2024-01-01')
    Date_of_Resignation = models.DateField(null=True, blank=True)
    
    # Get Pakistani time for Date_of_Data_Entry
    def get_pakistan_time():
        pakistan_tz = pytz.timezone('Asia/Karachi')
        return now().astimezone(pakistan_tz)

    Date_of_Data_Entry = models.DateTimeField(default=get_pakistan_time)
        # New Other_Contact_Number field
    Other_Contact_Number = models.CharField(
        max_length=13,
        null=True,
        blank=True,  # Allow the field to be left empty
    )

    def __str__(self):
        return self.Retailer_ID






 
 
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

# models.py
from django.db import models

class DataRecord(models.Model):
    second_parent_region = models.CharField(max_length=100)
    second_parent_id = models.CharField(max_length=100)
    rso_id = models.CharField(max_length=100)
    rso_msisdn = models.CharField(max_length=100)
    retailer_id = models.CharField(max_length=100)
    retailer_msisdn = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.retailer_id} - {self.retailer_msisdn}"       

   
class DataRecordBVS(models.Model):
    Device_ID = models.CharField(max_length=100)
    retailer_id = models.CharField(max_length=100)
   

    def __str__(self):
        return f"{self.retailer_id} - {self.Device_ID}"

   
class Heirarchy(models.Model):
    Franchise_ID = models.CharField(max_length=100)
    Grid = models.CharField(max_length=100)
    Cluster = models.CharField(max_length=100)

   

    def __str__(self):
        return f"{self.Franchise_ID} - {self.Grid}"



class delete_contact(models.Model): 
    Retailer_ID = models.CharField(max_length=100, unique=True)
    Franchise_ID = models.CharField(max_length=100)
    Retailer_Number = models.CharField(max_length=100, null=True)
    DSO_Name = models.CharField(max_length=100, null=True)
    CNIC = models.CharField(max_length=15, null=True)
    BVS_Device = models.CharField(max_length=100, null=True)
    Location = models.CharField(max_length=100)
    username= models.CharField(max_length=100)

    # Category field
    CATEGORY_CHOICES = [
        ('DSO', 'DSO'),
        ('RSO', 'RSO'),
        ('Retailer', 'Retailer'),
        ('Franchise', 'Franchise'),
    ]
    Category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='DSO')

    # Other Contact Number
    Other_Contact_Number = models.CharField(max_length=13, null=True, blank=True)

    # New Date Fields
    Date_of_Joining = models.DateField(default='2024-01-01')
    Date_of_Resignation = models.DateField(null=True, blank=True)
    
    # Get Pakistani time for Date_of_Data_Entry
    def get_pakistan_time():
        pakistan_tz = pytz.timezone('Asia/Karachi')
        return now().astimezone(pakistan_tz)

    Date_of_Data_Entry = models.DateTimeField(default=get_pakistan_time)
        # New Other_Contact_Number field
    Other_Contact_Number = models.CharField(
        max_length=13,
        null=True,
        blank=True,  # Allow the field to be left empty
    )

    def __str__(self):
        return self.Retailer_ID


class edit_contact(models.Model): 
    Retailer_ID = models.CharField(max_length=100)
    Franchise_ID = models.CharField(max_length=100)
    Retailer_Number = models.CharField(max_length=100, null=True)
    DSO_Name = models.CharField(max_length=100, null=True)
    CNIC = models.CharField(max_length=15, null=True)
    BVS_Device = models.CharField(max_length=100, null=True)
    Location = models.CharField(max_length=100)
    username= models.CharField(max_length=100)

    # Category field
    CATEGORY_CHOICES = [
        ('DSO', 'DSO'),
        ('RSO', 'RSO'),
        ('Retailer', 'Retailer'),
        ('Franchise', 'Franchise'),
    ]
    Category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='DSO')

    # Other Contact Number
    Other_Contact_Number = models.CharField(max_length=13, null=True, blank=True)

    # New Date Fields
    Date_of_Joining = models.DateField(default='2024-01-01')
    Date_of_Resignation = models.DateField(null=True, blank=True)
    
    # Get Pakistani time for Date_of_Data_Entry
    def get_pakistan_time():
        pakistan_tz = pytz.timezone('Asia/Karachi')
        return now().astimezone(pakistan_tz)

    Date_of_Data_Entry = models.DateTimeField(default=get_pakistan_time)
        # New Other_Contact_Number field
    Other_Contact_Number = models.CharField(
        max_length=13,
        null=True,
        blank=True,  # Allow the field to be left empty
    )

    def __str__(self):
        return self.Retailer_ID
