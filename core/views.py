from django.shortcuts import get_list_or_404,redirect,get_object_or_404,render,HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,TemplateView
from .forms import ContactForm
from django.core.mail import send_mail,BadHeaderError

class HomePage(TemplateView):
    template_name = "templates/landingpage.html"

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            fromEmail = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            send_mail(subject, content, fromEmail, ['guildsystemsbw@gmail.com'])
            return redirect('')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact1(request):
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