from django import forms
from django.core.exceptions import ValidationError

from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['id', 'name']

    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name')
        qs = Category.objects.all().filter(name__contains=name)
        print('all_data', name, qs)
        if qs.exists():
            print("Here   HEHEHEHEHEHEHEHEHEHEH")
            raise ValidationError("Category already exits")
        return cleaned_data
