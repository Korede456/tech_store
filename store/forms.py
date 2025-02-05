from django import forms
from .models import Laptop, LaptopImages

# forms.py

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

class LaptopImagesForm(forms.ModelForm):
    class Meta:
        model = LaptopImages
        fields = ['img_1', 'img_2', 'img_3', 'img_4', 'img_5', 'img_6']

LaptopImagesFormSet = forms.inlineformset_factory(Laptop, LaptopImages, form=LaptopImagesForm, extra=1, can_delete=True)