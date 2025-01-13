from django.urls import path
from home.views import *

urlpatterns = [
    path('', index,name='home'),
    path('contact/', contact,name='contact'),
    path('dynamic_route/<int:number>', dynamic_route),
    path('search/', search),
]