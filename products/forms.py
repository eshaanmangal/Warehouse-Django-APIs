from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Product


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