from django import forms
from .models import Contact
from .models import Authenticate

from django import forms
from django.core.exceptions import ValidationError
import re
from .models import Contact

from django import forms
from .models import Contact
from django.core.exceptions import ValidationError
import re
from django.core.validators import MinLengthValidator

class ContactForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('', 'Please select a category'),  # Default "Please select" option
        ('DSO', 'DSO'),
        ('RSO', 'RSO'),
        ('Retailer', 'Retailer'),
        ('Franchise', 'Franchise'),
    ]

    Category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    Other_Contact_Number = forms.CharField(
        max_length=12,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[MinLengthValidator(12)],  # Ensure 12-digit length
    )

    class Meta:
        model = Contact
        fields = [
            'Retailer_ID', 'Franchise_ID', 'Grid', 'Cluster', 'Region',
            'Retailer_Number', 'DSO_Name', 'CNIC', 'BVS_Device',
            'Location', 'Category', 'Other_Contact_Number'
        ]
        widgets = {
            'Retailer_ID': forms.TextInput(attrs={'class': 'form-control'}),
            'Franchise_ID': forms.TextInput(attrs={'class': 'form-control'}),
            'Grid': forms.TextInput(attrs={'class': 'form-control'}),
            'Cluster': forms.TextInput(attrs={'class': 'form-control'}),
            'Region': forms.TextInput(attrs={'class': 'form-control'}),
            'Retailer_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'DSO_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'CNIC': forms.TextInput(attrs={'class': 'form-control'}),
            'BVS_Device': forms.TextInput(attrs={'class': 'form-control'}),
            
            'Location': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_Retailer_ID(self):
        retailer_id = self.cleaned_data.get('Retailer_ID')

        # Skip validation if editing an existing contact
        if self.instance.pk:
            return retailer_id  

        # Enforce uniqueness check only when creating a new contact
        if Contact.objects.filter(Retailer_ID=retailer_id).exists():
            raise forms.ValidationError('This Retailer ID already exists in the database.')

        return retailer_id

    def clean_Other_Contact_Number(self):
        contact_number = self.cleaned_data.get('Other_Contact_Number')
        if contact_number and len(contact_number) != 12:
            raise forms.ValidationError('Other Contact Number must be exactly 12 digits.')
        return contact_number




    def clean_Grid(self):
        grid = self.cleaned_data.get('Grid')
        if not re.match(r'^[A-Za-z]{1}\d{4}$', grid):
            raise ValidationError("Grid should be in the format 'C2001'.")
        return grid

    def clean_CNIC(self):
        cnic = self.cleaned_data.get('CNIC')
        if not re.match(r'^\d{13}$', cnic):
            raise ValidationError("CNIC must be exactly 13 digits.")
        return cnic



    def clean_Retailer_Number(self):
        retailer_number = self.cleaned_data.get('Retailer_Number')
        if not re.match(r'^\d{12}$', retailer_number):
            raise ValidationError("Retailer Number must be 12 digits and in this format: 923120000000.")
        return retailer_number


from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Enter your username',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Enter your password',
        })
    )

from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField()

class BVSUploadForm(forms.Form):
    file = forms.FileField()

class HeirarchyUploadForm(forms.Form):
    file = forms.FileField()
