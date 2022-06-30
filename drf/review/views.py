from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response

import review
from product.models import Product
from product.serializers import ProductSerializers
from review.models import Review
from review.serializers import ReviewSerializers

class ReviewList(APIView):
    def get(self,request,pid):
        qs = Review.objects.all()
        serializer = ReviewSerializers(qs,many=True)
        return Response(serializer.data)

    def post(self,request,pid):
        serializer = ReviewSerializers(data = request.data, many=False)
        if serializer.is_valid():
            product = Product()
            product.id = pid
            serializer.save(writer = request.user,product = product)
            return Response(serializer.data,status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):
    def get(self,request,pid,rid):
        qs = Review.objects.get(id=pid)
        serializer = ReviewSerializers(qs, many=False)
        return Response(serializer.data)

    def delete(self,request,pid,rid):
        qs = Review.objects.get(id=pid)
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self,request,pid,rid):
        qs = Review.objects.get(id=pid)
        serializer = ReviewSerializers(qs, data = request.data,partial=True) #이거 없어도 부분으로 되는것 같은뎅
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # queryset = Review.objects.all().order_by('-created_at')
    # serializer_class = ReviewSerializers
    #
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #
    #     search_score = self.request.query_params.get('score',) #request.Get.get('score')
    #
    #     if search_score:
    #         qs = qs.filter(score__contains = search_score) #name__contains로 search_name에 포함되어있는 애들 다 가져오거나(대소문자 구분) i
    #                                                      # 붙이면 구분 안함, 아님 name으로 딱 걔만 갖고오거나,
    #
    #     return qs
    # @action(detail = False, methods = ['GET'], url_path = "search/(?P<score>[^/.]+)")
    # def ab_search(self,request,score=None):
    #     qs = self.get_queryset().filter(score__icontains=score)
    #     serializer = self.get_serializer(qs,many=True)
    #
    #     return Response(serializer.data)
