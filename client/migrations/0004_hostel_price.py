# Generated by Django 5.0.6 on 2024-05-25 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_hostel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Price'),
            preserve_default=False,
        ),
    ]