from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Новая любимая сладость")
    
