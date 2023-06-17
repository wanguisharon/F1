from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from app import views



urlpatterns = [
    path('', views.index, name='index'),
    path('check-weight/', views.CheckWeight, name='check-weight')
    ]

if settings.DEBUG: 
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
