# Generated by Django 3.1.5 on 2021-01-10 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0004_remove_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=10),
        ),
    ]
