from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=300, null=True, blank=True)  
    book_price = models.DecimalField(max_digits=10, decimal_places=2) 
    book_desciption = models.TextField()   
    sku = models.CharField(max_length=13, unique=True)

    book_image = models.ImageField(upload_to='about/', null=True, blank=True)
    book_slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.book_name}"
    
class Contact(models.Model):
    contact_name = models.CharField(max_length=200, null=True, blank=True)
    contact_surname = models.CharField(max_length=200, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.contact_name} {self.contact_surname}"    