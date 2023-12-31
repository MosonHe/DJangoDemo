"""
URL configuration for djangodemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#  从创建的App中导入视图模块
from app01 import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    # 绑定路由index/和视图中函数index
    path('index/', views.index),
    path('test/', views.test),
    path('tmp/', views.tmp),
    path('req_resp/', views.req_resp),
    path('login/', views.login),
    path('orm/',  views.orm),

    # 用户管理案例
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('user/delete/', views.user_delete)

]
