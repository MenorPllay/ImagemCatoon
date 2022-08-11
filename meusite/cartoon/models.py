from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class cartoonImg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='photo', null=True)
    p_edge = models.ImageField(upload_to='photo', null=True)
    p_cart = models.ImageField(upload_to='photo', null=True)

    def __str__(self):
        return str(self.id)

    # class Meta:
    #     db_table = 'cartoonimg'