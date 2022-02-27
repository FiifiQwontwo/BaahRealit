from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreateContact
from django.core.mail import send_mail, BadHeaderError


# Create your views here.

def contactview(request):
    if request.method == 'GET':
        form = CreateContact()
    else:
        form = CreateContact(request.POST)
        if form.is_valid():

            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['ahwirengfiifi@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('contact:success_mail')
    return render(request, 'email.html', {'form': form})


def succesview(request):
    return HttpResponse('Thank you for the message ')
