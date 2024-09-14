from django.contrib import admin
from .models import Product, PrintCart, History

# Register your models here.


admin.site.register(Product , list_display=['id','name' , 'stock' ,'category'  , 'price'])

admin.site.register(PrintCart , list_display=['id' , 'product' ,'quantity' , 'isInCart'])

admin.site.register(History , list_display=['id','date' , 'payment_mode'])



