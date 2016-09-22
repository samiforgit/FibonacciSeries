import json
import requests
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from fibonacci.models import *

@csrf_exempt
def fibonacci_home(request):
    return_data = {}
    return render (request,'home.html',return_data)

@csrf_exempt
def fibonacci(request):
    nterms = None
    fibo_data = Fibonacci()

    if request.POST.get('nterms') !="":
        nterms = request.POST.get('nterms')

    result_list = []
    i = 0
    if nterms is not None:
        nterms = nterms
        if nterms <= 0:
            print("Plese enter a positive integer")
        else:
            print("Fibonacci sequence:")
            for i in range(0 , int(nterms)):
                print(recur_fibo(i))
                result_list.append(recur_fibo(i))
    
    fibo_data.terms = int(nterms)
    fibo_data.result = result_list
    fibo_data.save()
    return_data = result_list
    return HttpResponse(json.dumps(return_data),content_type="application/json" )

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))