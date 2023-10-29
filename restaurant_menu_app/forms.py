from django import forms
from django.forms import FileInput
from .models import MenuItem

class MenuItemForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
    
    class Meta:
        model = MenuItem
        fields = ['name', 'image', 'description', 'price', 'category']

        widgets = {
            'image': FileInput(attrs={'style': 'z-index:-1; position: absolute;', 'onchange': "changeTick('id_frontimg' ,'frontimg', 'frontimgicon', 'frontimg_error')"}),
        }