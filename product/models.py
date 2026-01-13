from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.



class Category(models.Model):
    
    name=models.CharField(max_length=250)
    description=models.TextField(blank=True,null=True)
    
    
    
    def __str__(self):
        return self.name



class Product(models.Model):
    
    name=models.CharField(max_length=250)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveBigIntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    


class ProductImage(models.Model):
    
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='products/images',)
    
    
    def __str__(self):
        return f"Image of {self.product.name}"
    
 
 
class Review(models.Model):
    
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    rating=models.PositiveBigIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
     
    
    
    
        
    
    
    