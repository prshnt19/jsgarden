from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    contact = forms.IntegerField()
    no_of_guests = forms.IntegerField()
    eventdate = forms.CharField()
    email=forms.EmailField(required=False)
    package = forms.CharField()
    message = forms.CharField(widget=forms.Textarea,required=False)