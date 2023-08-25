from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print("inside test function")
    #return HttpResponse("<h1>Hello Index</h1>")
    isActive=False   #TODO: make it true
    name="Vishank Rathore"
    list_of_programs=[
        "find prime","find odd or even"
    ]
    data={
        "isActive":isActive,
        "name":name,
        "list_of_programs":list_of_programs
    }
    return render(request, "home.html",data)

def about(request):
    #return HttpResponse("<h1>This is about page</h1>")
    return render(request, "about.html",{})

def service(request):
    #return HttpResponse("<h1>This is service page</h1>")
    return render(request, "service.html",{})