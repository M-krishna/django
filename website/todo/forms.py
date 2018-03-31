from django import forms

class TodoApp(forms.Form):
    text = forms.CharField(max_length=50,
    widget = forms.TextInput(attrs={
        'class': 'form-control mr-3',
        'placeholder': 'A Django TODO'
    }))