# Generated by Django 4.0.5 on 2022-06-07 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
