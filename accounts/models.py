# accounts/models.py
from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Cart for {self.user.username}"
    @property
    def total_items(self):
        return sum(item.quantity for item in self.cartitem_set.all())
    @property
    def total_price(self):
        return sum(item.total_price for item in self.cartitem_set.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('cart', 'product')
    def __str__(self):
        return f"{self.quantity} of {self.product.name} in {self.cart.user.username}'s cart"
    @property
    def total_price(self):
        return self.quantity * self.product.price


# NEW: Represents a customer's order
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order {self.id} by {self.user.username} on {self.order_date.strftime('%Y-%m-%d')}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.PositiveIntegerField() 
    price_at_order = models.DecimalField(max_digits=10, decimal_places=2) 

    class Meta:
        unique_together = ('order', 'product')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"
    @property
    def total_price(self):
        return self.quantity * self.price_at_order
