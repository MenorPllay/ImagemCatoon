# Generated by Django 4.0.6 on 2022-07-26 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartoon', '0002_alter_cartoonimg_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartoonimg',
            old_name='photo',
            new_name='photo_cart',
        ),
    ]
