# Generated by Django 5.0 on 2024-07-12 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_product_costumer_views_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views_qty',
            field=models.IntegerField(default=0),
        ),
    ]