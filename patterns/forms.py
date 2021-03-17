from django import forms

class PatternForm(forms.Form)
    pattern_name = forms.CharField((label='Pattern name', max_length=100))