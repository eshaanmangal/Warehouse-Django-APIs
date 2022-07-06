from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CategorySerializer, ProductSerializer, ProductTranscationSerializer
from .models import Category, Product, ProductTransaction

class CategoryViews(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request, id=None):
        item = Category.objects.get(id=id)
        serializer = CategorySerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
    
    def delete(self, request, id=None):
        item = get_object_or_404(Category, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class ProductViews(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            category = Product.objects.get(id=id)
            serializer = ProductSerializer(category)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        categories = Product.objects.all()
        serializer = ProductSerializer(categories, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request, id=None):
        item = Product.objects.get(id=id)
        serializer = ProductSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
    
    def delete(self, request, id=None):
        item = get_object_or_404(Product, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class ProductTranscationViews(APIView):
    def post(self, request):
        serializer = ProductTranscationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            productTrans = ProductTransaction.objects.get(id=id)
            serializer = ProductTranscationSerializer(productTrans)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        categories = ProductTransaction.objects.all()
        serializer = ProductTranscationSerializer(categories, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request, id=None):
        item = ProductTransaction.objects.get(id=id)
        serializer = ProductTranscationSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
    
    def delete(self, request, id=None):
        item = get_object_or_404(ProductTransaction, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})