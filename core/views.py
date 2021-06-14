from django.shortcuts import get_list_or_404,redirect,get_object_or_404
from django.views.generic import ListView,TemplateView
from .forms import ContactForm
from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q, Case, Value, When
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class HomePage(TemplateView):
    template_name = "templates/landingpage.html"

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)  
            print(contact)   
            #post.save()
            return redirect('')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

