from django.urls import path 
from . import views

app_name = 'blog'
urlpatterns = [
    # Home page
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
]