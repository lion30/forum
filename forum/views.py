from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse
from blocks.models import Block


def htmltemplate(request):
	return render(request, "htmltemplate.html")


def index(request):
	block_infos = Block.objects.all().filter(status=0).order_by('-id')
	return render(request, "index.html",{'blocks':block_infos})


def register(request):
	if request.method == 'GET':
		return render(request, 'register.html')

	else:
		owner = request.POST['owner']
		email = request.POST['email']
		password = request.POST['password']
		password_check = request.POST['password_check']
		user = User.objects.create_user(owner=owner, email=email, password=password)
		user.save()
		return HttpResponse('注册成功')


def test(request):
	return HttpResponse('test')