from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    contact = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea)