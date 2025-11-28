from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

        
class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ["cart", "payment_completed", "order_status", "ref", "amount", "subtotal"]
       


