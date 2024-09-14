from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse 
from django.shortcuts import get_object_or_404
from rest_framework import status 

from my_app.models import Product , History , PrintCart
from my_app.api.serializers import ProductSerializer , HistorySerializer ,PrintCartSerializer , CreateHistorySerializer


#get All products 
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#create product 

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

#update and delete product 

class ProductDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


#get all histroy 

class HistroyListView(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class HistoryCreateView(generics.CreateAPIView):
    serializer_class = CreateHistorySerializer
    queryset = History.objects.all()

    def perform_create(self, serializer):
        # Save the History instance first
        history = serializer.save()
        
        # Retrieve the print_cart IDs from the validated data
        print_cart_ids = self.request.data.get('print_cart', [])
        
        # Update the isInCart field of the related PrintCart instances
        PrintCart.objects.filter(id__in=print_cart_ids).update(isInCart=False)


# print cart view 


class PrintCartListView(generics.ListAPIView):
    serializer_class = PrintCartSerializer

    def get_queryset(self):
        # Return only PrintCart items where isInCart is True
        return PrintCart.objects.filter(isInCart=True)
    

class PrintCartCreateView(generics.CreateAPIView):
    serializer_class = PrintCartSerializer
    queryset = PrintCart.objects.all()    

class PrintCartDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PrintCartSerializer
    queryset = PrintCart.objects.all()






