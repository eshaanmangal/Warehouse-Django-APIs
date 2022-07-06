from rest_framework import serializers

from .models import Category, Product, ProductTransaction


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductTranscationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductTransaction
        fields = '__all__'
    
    # This doesn't return error gracefully
    def validate_amount(self, amount):
        if amount <= 0:
            return serializers.ValidationError("Amount should be greater than 0")
        return amount
    
    # have to complete it
    def validate(self, attrs):
        if attrs['direction'] == 'OUT':
            name = attrs['name'].strip()
            qs = ProductTransaction.objects.all().filter(direction__exact='IN', name__exact=name, product_id=attrs['product_id'])
            if qs.exists():
                if qs[0].amount < attrs['amount']:
                    return serializers.ValidationError("OUT amount cannot be greater than IN amount")
        return super().validate(attrs)