"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin

from forum.views import htmltemplate, index, register, test
from usercenter.views import activate

urlpatterns = [
	url(r'^admin/', admin.site.urls),  # admin后台
	url(r'^htmltemplate/$', htmltemplate),  # 自己设置的template样式页面
	url(r'^$', index),  # 论坛首页
	url(r'^article/', include('article.urls')),  # 文章子URL
	url(r'^comment/', include('comment.urls')),  # 文章评论子URL
	url(r'^message/', include('message.urls')),  # 消息系统子URL
	url(r'^register/$', register),  # 注册系统
	url(r'^test/$', test),  # 测试连接
	url(r'^activate/(?P<code>\w+)$', activate),  # 注册时带有激活码的激活连接页面
	url(r'^accounts/', include('django.contrib.auth.urls')),  # 用户登录页面URL
	url(r'^usercenter/', include('usercenter.urls')),  # 用户中心子URL
	url(r'^ueditor/', include('DjangoUeditor.urls'))  # 富文本编辑器子URL
]

admin.site.disable_action('delete_selected')  # 禁用删除功能
