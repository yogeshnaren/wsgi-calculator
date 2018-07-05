# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    a,b,result = 0,0,0    	    
    if(request.GET.get('add')): 
        if(request.GET.get('num1') == ""):
                result = "Invalid Input"
        else:
                a = int(request.GET.get('num1'))
        if(request.GET.get('num2') == ""):
                result = "Invalid Input"
        else:
                b = int(request.GET.get('num2'))
        result = (a+b)
    elif (request.GET.get('subtract')):
        if(request.GET.get('num1') == ""):
                result = "Invalid Input"
        else:
                a = int(request.GET.get('num1'))
        if(request.GET.get('num2') == ""):
                result = "Invalid Input"
        else:
                b = int(request.GET.get('num2'))
        result = (a-b)
    elif (request.GET.get('multiply')):
        if(request.GET.get('num1') == ""):
            result = "Invalid Input"
        else:
            a = int(request.GET.get('num1'))
        if(request.GET.get('num2') == ""):
            result = "Invalid Input"
        else:
            b = int(request.GET.get('num2'))
        result = (a*b)
    elif(request.GET.get('divide')):
        if(request.GET.get('num1') == ""):
            result = "Invalid Input"
        else:
            a = int(request.GET.get('num1'))
        if(request.GET.get('num2') == ""):
            result = "Invalid Input"
        else:
            b = int(request.GET.get('num2'))
        if (b!=0):
            result = (a/b)
        else:
            result = "Exception: Divide by Zero!"
    if request.GET.get('clear'):
        result = ""
    return render(
        request,
        'calculator.html',
        {
            'result': result,
        })