from django import forms
from django.forms import ValidationError

from .models import Partner


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['id', 'name'] #, 'email', 'phone', 'address', 'contact_person_name']
    
    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name')
        qs = Partner.objects.all().filter(name__contains = name)
        print(qs, qs.exists())
        if qs.exists():
            raise ValidationError("Partner already exits")
        return cleaned_data
        
        