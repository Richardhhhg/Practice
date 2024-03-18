from django import forms

class InputForm(forms.Form):
    input = forms.CharField(max_length = 100)
    