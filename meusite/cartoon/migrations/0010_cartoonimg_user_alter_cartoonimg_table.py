# Generated by Django 4.0.6 on 2022-08-05 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cartoon', '0009_alter_cartoonimg_p_cart_alter_cartoonimg_p_edge'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartoonimg',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='cartoonimg',
            table=None,
        ),
    ]
