from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):

    return render (request,'index.html')
def mail(request):
    if request.method=='POST':
        subject='Greeting'
        msg='Welcome to Mail server IN DJANGO'
        to=request.POST.get('email')
        res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
        if (res==1):
            msg='mail sent sucessfully'
        else:
            msg='mail Could not sent'
        return HttpResponse(msg)
    return render(request,'index.html')

