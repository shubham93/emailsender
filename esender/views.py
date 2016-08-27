from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from esender.models import email_data
def email(request):
    errors = []
    email_list=[]
    from_email=settings.EMAIL_HOST_USER
    if request.method == 'POST':
        if request.POST['subject'] =='':
            errors.append('Enter a subject.')
        if request.POST['message'] =='':
            errors.append('Enter a message.')
        if request.POST['email'] and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        email_list=request.POST['email'].split(",")
        # save info in db
        p=email_data()
        p.subject=request.POST['subject']
        p.email=request.POST['email']
        p.message=request.POST['message']
        p.save()
        # #######################
        #print email_list
        if not errors:
          try:
            send_mail(request.POST['subject'],request.POST['message'],from_email, email_list,fail_silently=False)
            return HttpResponse('Thank you, form has been submitted successfully')
          except Exception as err:
            return HttpResponse(str(err))
    return render(request, 'contact.html',{'errors': errors})
