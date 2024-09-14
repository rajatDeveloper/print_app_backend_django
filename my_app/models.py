from django.db import models
from django.utils import timezone

# Product model
class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# PrintCart model
class PrintCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    isInCart = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} - {self.isInCart}"

# History model
class History(models.Model):
    PAYMENT_MODES = [
        ('CASH', 'Cash'),
        ('ONLINE', 'Online'),
    ]

    print_cart = models.ManyToManyField(PrintCart, related_name="history_cart")
    date = models.DateTimeField(default=timezone.now)
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODES)

    def __str__(self):
        return f"Order on {self.date} - {self.get_payment_mode_display()}"

    
     
