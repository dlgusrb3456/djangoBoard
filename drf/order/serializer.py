from rest_framework import serializers
from rest_framework.authtoken.admin import User

from order.models import Order
from product.serializers import ProductSerializers

class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation()
        response['product'] = ProductSerializers(instance.product).data
        response['user'] = OrderUserSerializer(instance.user).data