# products/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        help_text="Name of the category (e.g., 'Electronics', 'Books')",
        verbose_name="Category Name"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(
        max_length=255,
        help_text="Name of the product",
        verbose_name="Product Name"
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Detailed description of the product",
        verbose_name="Description"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Price of the product",
        verbose_name="Price"
    )
    stock_quantity = models.IntegerField(
        default=0,
        help_text="Current stock level of the product",
        verbose_name="Stock Quantity"
    )

    image = models.ImageField(
        upload_to='products/', 
        blank=True,
        null=True,
        help_text="Upload a product image file",
        verbose_name="Product Image"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.RESTRICT,
        related_name='products',
        help_text="The category this product belongs to",
        verbose_name="Category"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Products"
