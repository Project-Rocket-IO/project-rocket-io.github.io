from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class RocketWebsiteView(TemplateView):
    pass
    
home = RocketWebsiteView.as_view(template_name="pages/index5.html")
dashboard_analytics_view = RocketWebsiteView.as_view(template_name="dashboards/dashboard-analytics.html")
dashboard_crm_view = RocketWebsiteView.as_view(template_name="dashboards/dashboard-crm.html")
dashboard_crypto_view = RocketWebsiteView.as_view(template_name="dashboards/dashboard-crypto.html")
dashboard_projects_view = RocketWebsiteView.as_view(template_name="dashboards/dashboard-projects.html")
dashboard_nft_view = RocketWebsiteView.as_view(template_name="dashboards/dashboard-nft.html")
dashboard_job_view = RocketWebsiteView.as_view(template_name="dashboards/dashboard-job.html")


##################################
##################################
# REAL TIME VIEWS IN USE #########
##################################
##################################

#########
# TICKETS

def home(request):
    context = {}
    return render(request,'index.html',context)

def home2(request):
    return render(request, 'example.html')
def home3(request):
    return render(request, 'example.html')
def home4(request):
    return render(request, 'example.html')
