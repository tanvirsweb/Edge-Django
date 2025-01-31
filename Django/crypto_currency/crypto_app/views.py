from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def why(request):
    return render(request,'why.html')

def team(request):
    return render(request,'team.html')

def newpageh(request):
    return HttpResponse ("<h1> Hi </h1>")
