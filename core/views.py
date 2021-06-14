from django.shortcuts import get_list_or_404,redirect,get_object_or_404,render,HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,TemplateView
from .forms import ContactForm
from django.core.mail import send_mail,BadHeaderError

'''
Displaying the landing page.
'''
class HomePage(TemplateView):
    template_name = "templates/landingpage.html"

'''
Depending on the request method either the form is displayed or it is being submitted.
+The email is sent to the company email address.
'''
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['content']
            try:
                send_mail(subject, message, from_email, ['guildsystemsbw@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "contactSuccess.html")
    return render(request, "contact.html", {'form': form})