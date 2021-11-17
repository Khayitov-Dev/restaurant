from enum import unique
from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200,unique=True)


    class Meta:
        verbose_name_plural = 'Category'

    
    def __str__(self):
        return self.title


class Food(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,unique=True)
    photo = models.ImageField(upload_to='food/',unique=True)


    class Meta:
        verbose_name_plural = 'Restaurant'

    
    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=25,unique=True)
    body = models.TextField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ("created",)


    def __str__(self):
        return f"Comment by {self.name} on {self.post}"


class Cook(models.Model):
    name = models.CharField(max_length=50,null=True)
    surname = models.CharField(max_length=50,null=True)
    photo = models.ImageField(upload_to='cook/',unique=True)



    class Meta:
        verbose_name_plural = 'Cook'

    
    def __str__(self):
        return self.name