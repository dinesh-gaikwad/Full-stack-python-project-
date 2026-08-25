from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=120,unique=True)
    slug=models.SlugField(unique=True)
    description=models.TextField(blank=True)
    def __str__(self): return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    name=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField(default=0)
    image=models.ImageField(upload_to='products/',blank=True)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self): return self.name

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    phone=models.CharField(max_length=30,blank=True)
    address=models.TextField(blank=True)
    city=models.CharField(max_length=100,blank=True)
    postal_code=models.CharField(max_length=20,blank=True)
    def __str__(self): return self.user.username

class Order(models.Model):
    STATUS=[('pending','Pending'),('paid','Paid'),('shipped','Shipped'),('delivered','Delivered'),('cancelled','Cancelled')]
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='orders')
    full_name=models.CharField(max_length=160)
    email=models.EmailField()
    address=models.TextField()
    city=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=20)
    total=models.DecimalField(max_digits=12,decimal_places=2,default=0)
    status=models.CharField(max_length=20,choices=STATUS,default='pending')
    stripe_session_id=models.CharField(max_length=255,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'Order #{self.id}'

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    product_name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField()
    @property
    def subtotal(self): return self.price*self.quantity

class CartItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='cart_items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    class Meta:
        unique_together=('user','product')
