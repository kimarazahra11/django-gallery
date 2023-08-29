from django.urls import path
from .views import *



app_name = 'gallery'

urlpatterns = [
    path('gallery-single/',gallery_single,name='gallery-single'),
    path('gallery_category/',gallery,name='gallery_category'),
]