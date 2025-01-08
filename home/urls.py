from django.urls import path
from home.views import index, contact

urlpatterns = [
    path('', index),
    path('contact/', contact)
]