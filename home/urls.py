from django.urls import path
from home.views import *

urlpatterns = [
    path('', index,name='home'),
    path('contact/', contact,name='contact'),
    path('dynamic_route/<int:number>', dynamic_route),
    path('search_student/', search_student,name='search_student'),
    path('search_teacher/', search_teacher,name='search_teacher'),
]