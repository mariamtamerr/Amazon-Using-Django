# Generated by Django 4.2.6 on 2023-10-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
