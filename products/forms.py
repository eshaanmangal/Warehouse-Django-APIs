from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Product, ProductTransaction


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean(self):
        cleaned_data = self.cleaned_data
        cat_name = cleaned_data.get('name')
        qs = Category.objects.all().filter(name__contains=cat_name)
        if qs.exists():
            raise ValidationError("Category already exits")
        return cleaned_data


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    def clean(self):
        cleaned_data = self.cleaned_data
        product_name = cleaned_data.get('name')
        qs = Product.objects.all().filter(name__contains=product_name)
        if qs.exists():
            raise ValidationError("Partner already exists")
        return cleaned_data 


class ProductTranscationForm(forms.ModelForm):
    class Meta:
        model = ProductTransaction
        fields = '__all__'

    # Don't know why this is not working !!
    def clean_timestamp(self):
        timestamp = self.cleaned_data.get('timestamp')
        if not timestamp:
            return datetime.now()
        return timestamp

    # How to add feild checks in their designated fucntions ? 
    def clean(self):
        cleaned_data = super(ProductTranscationForm, self).clean()
        if not cleaned_data.get('direction'):
            raise ValidationError("Please specify the direction of transaction (IN/OUT)")
        
        if cleaned_data.get('amount') <= 0:
            raise ValidationError("Amount should be greater than equal to 0")
        
        if not cleaned_data.get('partner_id'):
            raise ValidationError("Enter a valid partner id")

        if not cleaned_data.get('product_id'):
            raise ValidationError("Enter a valid product id")
        
        return cleaned_data