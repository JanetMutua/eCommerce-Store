# Generated by Django 4.0.5 on 2022-06-07 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0009_product_clearance_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
    ]
