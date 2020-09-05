from django.db import models
import time
# Create your models here.

class ClassRoom(models.Model):
    roomID = models.IntegerField()
    loc = models.CharField(max_length=20)
    roomName = models.CharField(max_length=20)

    def __str__(self):
        return self.roomName


class Teacher(models.Model):
    name = models.CharField(max_length=5)
    course = models.CharField(max_length=20)

    def getRoomName(self):
        return self.room.roomName

    getRoomName.short_description = "教室"

    def curTime(self):
        return time.ctime()

    curTime.short_description = "当前时间"
    curTime.admin_order_field = "name"
    def __str__(self):
        return self.name

    room = models.OneToOneField(ClassRoom)



class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    room = models.ForeignKey(ClassRoom)