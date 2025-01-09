from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    names = ['John', 'Doe', 'Jane']
    context = {
        'names': names
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def dynamic_route(request,number):
    result = f"Table of {number} is :"
    for i in range(1,11):
       result += f"\n {number} * {i} = {number * i}"
    print(result) 
    return HttpResponse(result)
