from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def email(request):
    errors = []
    from_email=settings.EMAIL_HOST_USER
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
          try:
              
            send_mail(request.POST['subject'],request.POST['message'],from_email,request.POST('email'),fail_silently=False)
            return HttpResponse('Thank you, form has been submitted successfully')
          except Exception as err: 
            return HttpResponse(str(err))
    return render(request, 'contact.html',
        {'errors': errors})
