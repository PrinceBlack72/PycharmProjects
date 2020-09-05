from rest_framework import serializers
from Myser.model import *

# class StudentSerializer(serializers.Serializer):
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    '''
    里面写的是每一个需要序列化反序列化的字段
    和模型定义基本一致
    '''
    # name = serializers.CharField(label="姓名", max_length=20)
    # age = serializers.IntegerField()
    # score = serializers.IntegerField()

    class Meta:
        model = Student
        # fields = ('name', 'age', 'score')
        fields = '__all__'
