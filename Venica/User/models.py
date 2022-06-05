from django.db import models
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
import datetime


def get_file_image_path(request, filename):
     original_filename = filename
     now_time = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
     filename = '%s%s' % (now_time, original_filename)
     return os.path.join('profile_pics/', filename)




class Profile(models.Model):
    # create a one to many relationship with each user and profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( upload_to= get_file_image_path)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

