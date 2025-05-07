from django.http import HttpResponse
from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')


def transaction_add(request):
    return render(request, 'transaction_add.html')

def transaction_view(request):
    return HttpResponse("Hello")

