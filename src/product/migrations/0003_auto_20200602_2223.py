# Generated by Django 3.0.6 on 2020-06-03 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(blank=True, default='this is a default value', max_length=128),
        ),
    ]
