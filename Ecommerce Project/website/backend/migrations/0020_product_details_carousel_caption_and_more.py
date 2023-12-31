# Generated by Django 4.2.5 on 2023-11-03 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_dicounted_carousel_rel_with_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='carousel_caption',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product_details',
            name='carousel_fiture_ima',
            field=models.ImageField(blank=True, null=True, upload_to='carousel_fiture_image/'),
        ),
        migrations.AddField(
            model_name='product_details',
            name='carousel_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product_details',
            name='disount_percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='dicounted_carousel',
        ),
    ]
