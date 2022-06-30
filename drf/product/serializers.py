from rest_framework import serializers

from product.models import Product
from review.serializers import ReviewSerializers


class ProductSerializers(serializers.ModelSerializer):
    review_set = ReviewSerializers(many = True, read_only=True)
    review_set_count = ReviewSerializers.IntegerField(score = 'review_set.count',read_only=True)
    class Meta: #데이터에 대한 데이터
        model = Product
        fields = ['name','description','price','review_set','review_set_count'] #전체 다 넣기 , 일부분만 넣는것도 가능

    def save(self):
        name = self.validated_data['name']
        description = self.validated_data['description']
        price = self.validated_data['price']
        user = self.context['request'].user