from django import forms

class FormContacto(forms.Form):
    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()