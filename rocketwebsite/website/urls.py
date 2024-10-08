# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blogs/', views.blog_list, name='blogs'),
    path('blog/<int:pk>', views.blog, name='blog'),
    path('pricing/', views.pricing, name='pricing'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
