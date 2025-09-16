from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from .models import Palace, Room, MemoryItem


class PalaceForm(forms.ModelForm):
    class Meta:
        model = Palace
        fields = ['name', 'description', 'palace_type', 'image', 'is_public']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-8 mb-0'),
                Column('palace_type', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'description',
            Row(
                Column('image', css_class='form-group col-md-8 mb-0'),
                Column('is_public', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save Palace', css_class='btn btn-primary')
        )


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description', 'order', 'image', 'x_coordinate', 'y_coordinate']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'x_coordinate': forms.NumberInput(attrs={'step': '0.1'}),
            'y_coordinate': forms.NumberInput(attrs={'step': '0.1'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-8 mb-0'),
                Column('order', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'description',
            'image',
            Row(
                Column('x_coordinate', css_class='form-group col-md-6 mb-0'),
                Column('y_coordinate', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save Room', css_class='btn btn-success')
        )


class MemoryItemForm(forms.ModelForm):
    class Meta:
        model = MemoryItem
        fields = ['content', 'item_type', 'mnemonic_hint', 'position_in_room', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
            'mnemonic_hint': forms.Textarea(attrs={'rows': 2}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'content',
            Row(
                Column('item_type', css_class='form-group col-md-8 mb-0'),
                Column('position_in_room', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'mnemonic_hint',
            'image',
            Submit('submit', 'Save Memory Item', css_class='btn btn-info')
        )