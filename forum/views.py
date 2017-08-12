import uuid
import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.utils import timezone
from blocks.models import Block
from usercenter.models import ActivateCode
from message.models import Usermessage


def htmltemplate(request):
	return render(request, "htmltemplate.html")


def index(request):
	block_infos = Block.objects.all().filter(status=0).order_by('-id')
	if request.user.is_authenticated():
		msg_cnt = Usermessage.objects.filter(status=0, owner=request.user).count()
	else:
		msg_cnt = 0
	return render(request, "index.html",{'blocks':block_infos, 'msg_cnt': msg_cnt})


def register(request):
	error = ""
	if request.method == 'GET':
		return render(request, 'register.html')

	else:
		owner = request.POST['username'].strip()
		email = request.POST['email'].strip()
		password = request.POST['password'].strip()
		password_check = request.POST['password_check'].strip()

		if not owner or not password or not email:
			error = "任何字段都不能为空"
		if password != password_check:
			error = "两次密码不一致"
		if User.objects.filter(username=owner).count() > 0:
			error="用户名已存在"
		if not error:
			user = User.objects.create_user(username=owner, email=email, password=password, is_active=False)
			user.save()

			new_code = str(uuid.uuid4()).replace('-', '')
			expire_time = timezone.now()+datetime.timedelta(days=2)
			code_record = ActivateCode(owner=user, code=new_code, expire_timestamp=expire_time)
			code_record.save()

			active_link = 'http://%s/activate/%s' % (request.get_host(), new_code)
			active_email = '''点击<a href="%s">这里</a>激活''' % active_link
			send_mail(subject='测试激活邮件',
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