# Generated by Django 4.2.5 on 2023-11-02 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_alter_dicounted_carousel_rel_with_pro_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dicounted_carousel',
            name='rel_with_pro_img',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carousel', to='backend.product_images'),
        ),
    ]
