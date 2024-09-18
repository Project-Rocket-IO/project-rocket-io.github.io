from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Blog

##################################
##################################
# REAL TIME VIEWS IN USE #########
##################################
##################################

########
# MAIN #
########

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def blog_list(request):
    blogs = Blog.objects.all()
    context = {"blogs":blogs}
    return render(request, 'blog-list.html', context=context)

def blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {"blog":blog}
    return render(request, 'blog.html', context=context)

def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request, 'contact/contact.html')
