import datetime
import uuid

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse
from django.utils import timezone

from blocks.models import Block
from message.models import Usermessage
from usercenter.models import ActivateCode


def htmltemplate(request):
	return render(request, "htmltemplate.html")


def index(request):
	block_infos = Block.objects.all().filter(status=0).order_by('-id')
	if request.user.is_authenticated():
		msg_cnt = Usermessage.objects.filter(status=0, owner=request.user).count()
	else:
		msg_cnt = 0
	return render(request, "index.html", {'blocks': block_infos, 'msg_cnt': msg_cnt})


def register(request):
	error = ""      # 错误信息
	if request.method == 'GET':     #GET请求返回注册页面
		return render(request, 'register.html')

	else:   # if request.method == 'POST'
		owner = request.POST['username'].strip()    # 获取页面上name = username的输入框输入内容
		email = request.POST['email'].strip()       # 获取页面上name = email的输入框输入内容
		password = request.POST['password'].strip()     # 获取页面上name = password的输入框输入内容
		password_check = request.POST['password_check'].strip()     #获取页面上name = password_check的输入内容

		if not owner or not password or not email:      #配置错误信息
			error = "任何字段都不能为空"
		if password != password_check:
			error = "两次密码不一致"
		if User.objects.filter(username=owner).count() > 0:
			error = "用户名已存在"
			
		if not error:
			user = User.objects.create_user(username=owner, email=email, password=password, is_active=False)
			user.save()

			new_code = str(uuid.uuid4()).replace('-', '')
			expire_time = timezone.now()+datetime.timedelta(days=2)
			code_record = ActivateCode(owner=user, code=new_code, expire_timestamp=expire_time)
			code_record.save()

			active_link = 'http://%s/activate/%s' % (request.get_host(), new_code)  # 用户邮件内容中注册链接
			active_email = '''点击<a href="%s">这里</a>激活''' % active_link      # 将用户注册链接嵌入用户注册邮件正文中
			send_mail(subject='测试激活邮件',     # 配置注册邮件标题，内容，发件人，
			          message='点击链接激活：%s' % active_link,
			          html_message=active_email,
			          from_email='liwang_30@126.com',
			          recipient_list=[email],
			          fail_silently=False)
		else:
			return render(request, "register.html",{"error": error})
		return render(request, 'success_hint.html', {'msg': '注册成功，请前往您的邮箱完成验证！'})


def test(request):
	return HttpResponse('test')