from django import forms
from .models import cartoonImg


class ImageFileUploadForm(forms.ModelForm):
    class Meta:
        model = cartoonImg
        fields = ('photo', 'p_edge', 'p_cart') 