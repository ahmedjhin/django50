from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
 return HttpResponse('hello, world!')



def brain(request):
    return render(request, 'hello/index.html')


def aliu(request):
   return HttpResponse('hello, aliu')


def greet(request, name):
   return render(request, 'hello/index.html',{'name':name})

