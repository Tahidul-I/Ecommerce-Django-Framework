# Generated by Django 4.2.5 on 2023-11-01 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_alter_dicounted_carousel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_images',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
