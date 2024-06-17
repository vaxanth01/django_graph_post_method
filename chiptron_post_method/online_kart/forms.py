from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms 
from . models import *
from django import forms
from . models import Product, Comment
class CustomUserForm(UserCreationForm):
  username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
  email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
  password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
  password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))
  class Meta:
    model=User
    fields=['username','email','password1','password2']



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'category', 'price', 'description']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'name' : 'Enter Product Name:',
            'image': 'Select an Image: ',
            'category': 'Select Category: ',
            'price': 'Enter a price: ',
            'description': 'Enter a Description: ',
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent']

 


from django import forms

class DateForm(forms.Form):
    date_field = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))




from django import forms
from .models import Sale
from datetime import datetime,timedelta

class ItemCodeForm(forms.Form):
    item_code = forms.ChoiceField(choices=[], required=False)
    start_date = forms.DateField(required=False, initial=datetime.now().date(), widget=forms.DateInput(attrs={'type': 'date'}))
    start_time = forms.TimeField(required=False, initial=(datetime.now() -  timedelta(hours=3)).time(), widget=forms.TimeInput(attrs={'type': 'time'}))

    end_date = forms.DateField(required=False,initial=datetime.now().date(), widget=forms.DateInput(attrs={'type': 'date'}))
    end_time = forms.TimeField(required=False,initial=datetime.now().time(), widget=forms.TimeInput(attrs={'type': 'time'}))

    def __init__(self, *args, **kwargs):
        super(ItemCodeForm, self).__init__(*args, **kwargs)
        item_codes = Sale.objects.values_list('item_code', flat=True).distinct()
        choices = [('', 'All Items')] + [(code, code) for code in item_codes]
        self.fields['item_code'].choices = choices

