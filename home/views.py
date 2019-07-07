from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm,ContactusForm
from twilio.rest import Client
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            contact = form.cleaned_data['contact']
            no_of_guests = form.cleaned_data['no_of_guests']
            date = form.cleaned_data['eventdate']
            email = form.cleaned_data['email']
            package= form.cleaned_data['package']
            message = form.cleaned_data['message']


            # date= "-".join(date)
            contact = str(contact)
            no_of_guests = str(no_of_guests)
            final="Name-"+name+"\n"+"Contact Number-"+contact+"\n"
            final = final + 'Email-'+email + '\n'
            final = final + 'Package-'+ package+'\n'+'No. of Guests-'+no_of_guests + '\n'+'Date:-'+date + '\n'
            final = final +'Message-' + message



            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            response = client.messages.create(
                body=final,
                to='+919919098817', from_=settings.TWILIO_PHONE_NUMBER)

            subject = 'Enquiry on Jsgardens.in'

            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['abhi24061997@gmail.com']
            send_mail(subject, final, email_from, recipient_list)

            return render(request, "success.html")

    return render(request, "index.html")

def contactus(request):
    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            contact=str(contact)

            form_query = "Name-"+name+"\n"+"Contact Number-"+contact+"\n"+'Email-'+email + '\n'+'Message-' + message

            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            response = client.messages.create(
                body=form_query,
                to='+919919098817', from_=settings.TWILIO_PHONE_NUMBER)

            subject = 'Enquiry on Jsgardens.in'

            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['abhi24061997@gmail.com']
            send_mail(subject, form_query, email_from, recipient_list)




            return render(request, "success.html")

    return render(request, "contact.html")



