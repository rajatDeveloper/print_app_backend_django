from rest_framework import serializers
from my_app.models import PrintCart , Product , History 

# #will have all serlizers for the api here 


#Product Serializer 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        

#PrintCart Serializer 

class PrintCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintCart
        fields = '__all__'


#History Serializer 

class HistorySerializer(serializers.ModelSerializer):
    print_cart = PrintCartSerializer(many=True) 
    class Meta:
        model = History
        fields = '__all__'

#Create Histroy serlixer 

class CreateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
        
