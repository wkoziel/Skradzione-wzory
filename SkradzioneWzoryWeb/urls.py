from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_project, name='about'),
    path('run/', views.run_algorithms, name='run'),
    path('upload/', views.upload_page, name='upload'),
]