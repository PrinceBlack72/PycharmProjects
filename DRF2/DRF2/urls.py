from django.conf.urls import include, url
from django.contrib import admin
# 导入视图
from MySer import views
# 导入drf的路由
from rest_framework import routers


# 定义DRF的一个简单路由
router = routers.DefaultRouter()

# router.register(r'student/', views.StudentVS, base_name="stu")
router.register(r'myview/', views.StudentAPIView.as_view(), base_name="stu")

urlpatterns = [
    # Examples:
    # url(r'^$', 'DRF2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', views.StudentAPIView.as_view()),
]
