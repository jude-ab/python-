# Generated by Django 4.2.5 on 2023-12-06 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restnearme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='michelinrestaurants',
            name='latitude',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='michelinrestaurants',
            name='longitude',
            field=models.CharField(max_length=100),
        ),
    ]