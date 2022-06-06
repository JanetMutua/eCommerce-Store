import datetime
from django.db import models
import os
from django.contrib.auth.models import User

# Create your models here.


def get_file_path(request, filename):
     original_filename = filename
     now_time = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
     filename = '%s%s' % (now_time, original_filename)
     return os.path.join('uploads/', filename)



class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image= models.ImageField(upload_to= get_file_path, height_field=None, width_field=None, max_length = None)
    description = models.TextField(max_length=500, name=False, blank=False)
    status = models.BooleanField(default=False, help_text='0=default, 1=Hidden')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name




class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    product_image= models.ImageField(upload_to= get_file_path, height_field=None, width_field=None, max_length = None)
    brief_description = models.CharField(max_length=250, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=500, name=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text='0=default, 1=Hidden')
    trending = models.BooleanField(default=False, help_text='0=default, 1=Trending')
    new_arrival = models.BooleanField(default=False, help_text='0=default, 1=New Arrival')
    meta_title = models.CharField(max_length=150, null=False, blank=True)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_descripion = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name