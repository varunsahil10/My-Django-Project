from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("This is Homepage!!!😎")

def contact(request):
    return HttpResponse("This is Contact page!!!📞")

def dynamic_route(request,number):
    result = f"Table of {number} is :"
    for i in range(1,11):
       result += f"\n {number} * {i} = {number * i}"
    print(result) 
    return HttpResponse(result)
