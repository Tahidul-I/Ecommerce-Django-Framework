# Generated by Django 4.2.5 on 2023-10-30 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_remove_product_category_feature_image_and_more'),
        ('App_order', '0002_alter_cart_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.product_images'),
        ),
    ]
