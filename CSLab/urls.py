"""CSLab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.static import serve

import xadmin
from django.urls import path, include, re_path

from django.contrib import admin
from django.views.generic import TemplateView

from organization.views import DepView
from users.views import LoginView, user_login, RegisterView, ActiveUserView, ForgetPwdView, ModifyPwdView, ResetView, \
    IndexView, LogoutView
from CSLab.settings import MEDIA_ROOT

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name='index'),
    # 登录
    path('login/', LoginView.as_view(), name='login'),
    # 登出
    path('logout/', LogoutView.as_view(), name='logout'),
    # 注册
    path('register/', RegisterView.as_view(), name='register'),
    # 验证码
    path('captcha/', include('captcha.urls')),
    # 邮箱注册激活链接处理
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    # 忘记密码
    path('forget_pwd/', ForgetPwdView.as_view(), name='forget_pwd'),
    # 邮箱重置密码链接处理
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    # 配置上传文件的访问处理函数
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    # 课程部门相关URL配置
    path('dep/', include('organization.urls', namespace='dep')),
    # 课程相关URL配置
    path('course/', include('courses.urls', namespace='course')),
    # 用户相关URL配置
    path('users/', include('users.urls', namespace='users')),

    # re_path('r^static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),

    # path('ueditor/', include('DjangoUeditor.urls')),

]

# 全局404页面配置
handler404 = 'users.views.pag_not_found'
# 全局500页面配置
handler500 = 'users.views.page_error'
