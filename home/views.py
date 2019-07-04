from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm
from twilio.rest import Client
from django.conf import settings
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            contact = form.cleaned_data['contact']
            message = form.cleaned_data['message']

            contact = str(contact)
            final="Name-"+name+"\n"+"Contact Number-"+contact+"\n"+"Message-"+message

            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            response = client.messages.create(
                body=final,
                to='+919919098817', from_=settings.TWILIO_PHONE_NUMBER)
            # print (form)
            return render(request, "success.html")

    return render(request, "index.html")