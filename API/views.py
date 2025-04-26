from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from rest_framework import generics

# Create your views here.
class seeAPI(APIView):
    def get(self, request):
        items = Item.objects.all().order_by('-price')
        serializer = ItemSerializer(items, many = True)
        return Response(serializer.data)

class nameAPI(APIView):
    def get(self, request, name1):
        items = Item.objects.filter(name1 = name1)
        serializer = ItemSerializer(items, many = True)
        return Response(serializer.data)

class inventoryView(APIView):
    def get(self, request, pk=None):
        if pk:
            items = Item.objects.get(pk = pk)
            serializer = ItemSerializer(items)
        else:
            items = Item.objects.all()
            serializer = ItemSerializer(items, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ItemSerializer(data = request.data)
        if serializer.is_valid():
            barcode = serializer.validated_data['barcode']
            if Item.objects.filter(barcode = barcode).exists():
                return Response({'barcode':['items with this barcode already exists.']}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data
        if 'price' in data:
            item.price = data['price']
        if 'quantity' in data:
            item.quantity = data['quantity']

        item.save()
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_400_NOT_FOUND)
        else:
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

