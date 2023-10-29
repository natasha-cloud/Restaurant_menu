from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100 )
    image = models.ImageField(upload_to='media', blank=True, null=True)
   
    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=255, decimal_places=2)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name