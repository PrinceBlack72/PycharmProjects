from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from MySer.models  import *

# Create your views here.

class StudentVS(viewsets.ModelViewSet):
    pass


class StudentAPIView(APIView):
    """
    处理用户的get请求
    """
    def get(self, request):
        '''
        处理业务
        跟数据库交互
        :param request:
        :return:
        '''
        stus = Student.objects.all()