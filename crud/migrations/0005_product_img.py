# Generated by Django 5.1.6 on 2025-02-21 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_rename_category_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='noImage.png', upload_to=''),
        ),
    ]
