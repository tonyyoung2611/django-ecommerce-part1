from django.db import models
from django.conf import settings


class Store(models.Model):
    """Represent a vendor-owned store in the eCommerce application."""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """Return the store's name as a readable string."""
        return self.name


class Product(models.Model):
    """Represent a product listed for sale in a vendor's store."""

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Return the product's name as a readable string."""
        return self.name


class Profile(models.Model):
    """Store a user's profile and their buyer or vendor role."""

    ROLE_CHOICES = [
        ('vendor', 'Vendor'),
        ('buyer', 'Buyer'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='buyer'
    )

    def __str__(self):
        """Return the username and assigned user role."""
        return f"{self.user.username} - {self.role}"


class Order(models.Model):
    """Represent an order placed by a buyer."""

    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        """Return the order ID and buyer's username."""
        return f"Order #{self.id} - {self.buyer.username}"


class OrderItem(models.Model):
    """Represent a product and its quantity within a customer's order."""

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        """Return the product name and quantity ordered."""
        return f"{self.product.name} x {self.quantity}"


class Review(models.Model):
    """Represent a customer's product review and purchase verification status."""

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    rating = models.PositiveIntegerField()

    comment = models.TextField()

    verified_purchase = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        """Return the reviewer's username and reviewed product name."""
        return f"{self.user.username} - {self.product.name}"
