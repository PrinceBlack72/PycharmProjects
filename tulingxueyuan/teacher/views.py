from django.shortcuts import render
from django.http import HttpResponse

from django.core.urlresolvers import reverse

# Create your views here.

'''
视图函数需要一个参数，类型应该是HttpRequest
'''

def do_normalmap(request):
    return HttpResponse("This is normalmap")

def withparam(request, year, month):
    return HttpResponse("This is param {0}, {1}".format(year, month))

def do_app(request):
    return HttpResponse("这是个子路由")

def do_param2(request, pn):
    return HttpResponse("Page number is {0}".format(pn))

def extremParam(request, name):
    return HttpResponse("My name is {0}".format(name))

def revParam(r):
    return HttpResponse("Your requested URL is {0}".format(reverse("askname")))