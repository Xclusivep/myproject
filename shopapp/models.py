from django.db import models

class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

# Create your models here.
class product(models.Model):
    name = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_id = models.IntegerField(default= None, null=True, blank=True)
    price = models.DecimalField(null=True, decimal_places=2, max_digits= 4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product_id

class customer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.title}{self.content}'
        



# primary key is the unique key identifier of a product in the database
# foreign keybis a primary key, but in seperate table pointin to the main table

