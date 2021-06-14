from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.HomePage.as_view(template_name="landingpage.html")),
    path('contact', views.contact, name="contact")
]