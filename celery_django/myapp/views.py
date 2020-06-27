from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .tasks import add

class IndexView(View):
    def get(self,request):
        res=add.delay(10,20)
        print(res)
        return HttpResponse('Home page')

