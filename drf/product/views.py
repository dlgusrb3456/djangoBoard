from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializers

class ProductViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]

    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializers

    def get_queryset(self):
        qs = super().get_queryset()

        search_name = self.request.query_params.get('name',) #request.Get.get('name')

        if search_name:
            qs = qs.filter(name__contains = search_name) #name__contains로 search_name에 포함되어있는 애들 다 가져오거나(대소문자 구분) i
                                                         # 붙이면 구분 안함, 아님 name으로 딱 걔만 갖고오거나,

        return qs
    @action(detail = False, methods = ['GET'], url_path = "search/(?P<name>[^/.]+)")
    def ab_search(self,request,name=None):
        qs = self.get_queryset().filter(name__icontains=name)
        serializer = self.get_serializer(qs,many=True)

        return Response(serializer.data)
