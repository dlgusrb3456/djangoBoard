from rest_framework import serializers

from product.models import Product
from review.models import Review


class ReviewSerializers(serializers.ModelSerializer):
    class Meta: #데이터에 대한 데이터
        model = Review
        fields = ['score','contents',] #전체 다 넣기 , 일부분만 넣는것도 가능