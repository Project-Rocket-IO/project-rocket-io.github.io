from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class RocketWebsiteView(TemplateView):
    pass
    
home = RocketWebsiteView.as_view(template_name="index.html")
about = RocketWebsiteView.as_view(template_name="about.html")
pricing = RocketWebsiteView.as_view(template_name="pricing.html")
contact = RocketWebsiteView.as_view(template_name="contact.html")

##################################
##################################
# REAL TIME VIEWS IN USE #########
##################################
##################################

#########
# TICKETS

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request, 'contact/contact.html')
