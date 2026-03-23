from django.db import models
from django.contrib.auth.models import User

# 1. Watch Model (Products ke liye)
class Watch(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='watches/', blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # <-- Ye line add karo

    def __str__(self):
        return self.title

# 2. Order Model (Customer orders ke liye)
class Order(models.Model):
    product_name = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.customer_name} - {self.product_name}"

# 3. User Activity Model (Login/Logout track karne ke liye)
class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=50) # Login ya Logout
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"