# Generated by Django 4.0.6 on 2022-07-26 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartoon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartoonimg',
            name='photo',
            field=models.ImageField(upload_to='cartoon'),
        ),
    ]