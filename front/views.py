from django.shortcuts import render

def login_page(request):
    return render(request,'login.html')

def request_page(request):
    return render(request,'req.html')

def dashboard_page(request):
    return render(request,'dashboard.html')

def detail_page(request,id):
    return render(request,'detail.html')