from django import forms
from .models import Item


class ItemForm(forms.ModelForm):    # ModelForm 활용
    # name = forms.CharField()
    # desc = forms.Textarea()
    # ...
    # 이런 식으로 하나씩 작성할 수도 있지만, ModelForm 활용을 권장
    class Meta:
        model = Item
        # fields = [name, desc, ...]
        fields = '__all__'
