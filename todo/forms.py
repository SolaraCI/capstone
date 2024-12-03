from django import forms
from .models import List, Item

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name', 'description', 'creator']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'parent_list', 'complete']