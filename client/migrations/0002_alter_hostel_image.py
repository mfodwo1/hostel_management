# Generated by Django 5.0.6 on 2024-05-24 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hostel_images/', verbose_name='Hostel Image'),
        ),
    ]
