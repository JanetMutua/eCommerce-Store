# Generated by Django 4.0.5 on 2022-06-07 13:51

import Store.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0010_remove_product_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(height_field=500, upload_to=Store.models.get_file_path),
        ),
    ]
