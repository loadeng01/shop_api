from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    # stock = serializers.CharField(source='get_stock_display')

    class Meta:
        model = Product
        fields = '__all__'

    # def validate(self, attrs):
    #     print(attrs, '1111111111111111111111111')
    #     return attrs





